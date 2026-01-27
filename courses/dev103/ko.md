---
name: 자바스크립트 및 NodeJS 기초
goal: 자바스크립트 프로그래밍의 기초와 NodeJS 개발을 배워 실용적인 애플리케이션과 도구를 구축하세요.
objectives: 

  - 기본 자바스크립트 구문, 유형 및 제어 흐름 마스터하기
  - JavaScript의 함수, 객체, 클래스 이해하기
  - 오류 처리 및 디버깅 기술 배우기
  - NodeJS와 그 생태계에 대해 알아보기

---

# 개발 여정 시작하기


JavaScript와 NodeJS에 대한 이 강좌에 오신 것을 환영합니다.


JavaScript는 최신 브라우저의 스크립팅 언어이므로 기본적으로 *일부* JavaScript를 작성하지 않고는 최신 웹 애플리케이션을 구축하는 것이 불가능하며, NodeJS 런타임을 사용하면 브라우저 외부에서도 사용하여 컴퓨터에서 직접 실행되는 스크립트 및 애플리케이션을 만들 수 있습니다.


이 과정은 프로그래밍을 전혀 처음 접하거나 다른 언어를 사용해 본 적이 있지만 특히 NodeJS의 맥락에서 JavaScript가 어떻게 작동하는지 이해하고자 하는 사람들을 위해 설계되었습니다.


과정을 마치면 자바스크립트로 직접 프로그램을 작성하고, NodeJS 표준 라이브러리를 사용하고, 타사 패키지를 설치 및 사용하여 유용한 도구를 구축할 수 있어야 합니다.


+++
# 기본 자바스크립트

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## 설정

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>


이 섹션에서는 첫 번째 자바스크립트 프로그램을 작성하고 실행하도록 컴퓨터를 설정해 보겠습니다.


자바스크립트 프로그램은 자바스크립트 런타임에서 실행할 명령어를 포함하는 (하나 이상의) 텍스트 파일 모음입니다.


이러한 텍스트 파일의 이름은 일반적으로 `my_script.js`, `my_program.js` 등과 같이 파일 확장자가 `.js`로 끝납니다.


여기에 포함된 명령은 자바스크립트 프로그래밍 언어로 작성되었습니다.


자바스크립트 런타임은 이러한 파일을 실행하는 특수 프로그램입니다.


![](assets/en/001.webp)


### NodeJS 설치


가장 일반적인 자바스크립트 런타임은 NodeJS입니다.


공식 지침](https://nodejs.org/en/download)에 따라 설치할 수 있습니다.


다운로드 페이지에서는 세 가지 주요 OS(운영 체제) 모두에 대한 지침을 제공합니다: Windows, Linux 및 MacOS. OS에서 터미널을 여는 방법을 알고 있다고 가정합니다.


NodeJS는 세 가지 OS 모두에서 사용할 수 있으므로 작성하는 프로그램은 모든 OS에서 실행할 수 있습니다(일부 예외적인 경우를 제외).


예를 들어, Windows PC에서 자바스크립트로 간단한 비디오게임을 작성하여 친구에게 전달하면 친구의 Mac에서 실행할 수 있습니다.


![](assets/en/002.webp)


### 텍스트 편집


프로그래밍의 멋진 점 중 하나는 모든 텍스트 편집기, 심지어 OS의 기본 메모장을 사용하여 코드를 작성할 수 있다는 것입니다.


하지만 코드 작성에 특화된 텍스트 편집기 중에는 무료로 제공되는 것도 있고 라이선스 비용을 지불해야 하는 것도 있습니다.


코드 편집기의 선택은 이 강좌의 범위를 넘어서는 거대한 토끼굴이므로 여기서는 다루지 않겠습니다. 무엇을 사용해야 할지 모르겠다면 가장 많이 사용되는 무료 편집기는 [VSCode](https://code.visualstudio.com/)입니다.


Interface은 약간 부풀려져 있지만 파일 편집기, 파일 탐색기(작업 중인 디렉터리의 파일과 하위 디렉터리를 시각화), 코드 실행을 위한 터미널 등 필요한 기능을 모두 갖추고 있습니다. 또한 많은 플러그인을 지원하며 기본적으로 JavaScript 구문 강조 표시 기능이 제공됩니다.


좀 더 Cypherpunk을 원한다면 [VSCodium](https://vscodium.com/)을 대신 사용할 수 있습니다.


### 첫 번째 프로그램(헬로 월드)


일반적으로 프로그래밍 언어를 공부할 때 가장 먼저 작성하는 프로그램은 콘솔에 "hello world!"를 출력하는 것으로 구성됩니다.


'my_js_code/'라는 디렉터리를 만들고 그 안에 'main.js'라는 파일을 만듭니다(이 이름은 임의적임).


VSCode로 디렉토리를 엽니다.


이 코드를 파일에 작성합니다:


```javascript
console.log("hello world!")
```


터미널을 열고 다음 명령을 실행하여 프로그램을 실행합니다:


```
node main.js
```


결과는 다음과 같아야 합니다


```
hello world!
```


### 일어난 일


자바스크립트에서는 모든 것이 '객체'입니다.


콘솔`은 프로그램을 디버깅하는 데 사용되는 객체입니다.


콘솔`에서 가장 많이 사용되는 메서드는 `console.log`입니다. 이 메서드는 사용자가 전달한 인수를 모두 출력합니다.


둥근 괄호 '()`를 사용하여 `console.log`에 인수를 전달합니다.


예를 들어 '1000'이라는 숫자를 인쇄하려면 다음과 같이 작성하면 됩니다


```javascript
console.log(1000)
```


그런 다음 다음을 실행하여 실행합니다


```
node main.js
```


를 입력합니다(지금부터 이 과정에서는 프로그램을 실행하는 방법을 알고 있다고 가정합니다).


다음과 같이 인쇄됩니다


```
1000
```


다음과 같이 여러 가지를 전달할 수 있습니다


```javascript
console.log(16, 8, 1993)
```


이렇게 인쇄됩니다


```
16 8 1993
```


## 변수 및 댓글

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


프로그램은 일반적으로 데이터에 대한 연산을 실행합니다.


변수는 데이터를 저장하는 데 사용하는 네임드 박스와 같습니다. 변수를 사용하면 데이터를 특정 이름과 연결할 수 있으므로 나중에 해당 이름을 사용하여 데이터를 검색할 수 있습니다.


### let 선언


자바스크립트에서 변수를 선언하려면 `let` 키워드를 사용할 수 있습니다.


Let`이라고 쓴 다음 변수에 붙일 이름, `=` 기호, 저장할 값을 차례로 작성합니다.


예를 들어


```javascript
let age = 25

console.log(age)
```


변수 이름(기술적으로는 "식별자"라고 함)에는 일반적으로 문자, 밑줄(`_`), 달러 기호(`$`) 및 숫자를 포함할 수 있지만 첫 번째 문자는 숫자가 될 수 없습니다.


위 코드에서는 'age'라는 변수를 선언하고 그 안에 '25'라는 값을 저장했습니다.


그런 다음 `console.log(age)`를 사용하여 값을 출력했습니다.


이 코드를 `node main.js`와 함께 실행하면 다음과 같이 출력됩니다:


```
25
```


식별자는 대소문자를 구분하므로 소문자와 대문자는 식별자의 차이로 계산되므로 예를 들면 다음과 같습니다


```javascript
let age = 25

let Age = 20

console.log(age)
```


는 완전히 별개의 두 변수로 간주되므로 25를 출력합니다!


문자열(텍스트)을 변수에 저장할 수도 있습니다:


```javascript
let message = "hello again"

console.log(message)
```


인쇄됩니다:


```
hello again
```


이전과 마찬가지로 `console.log()`를 사용하여 변수에 저장된 값을 출력했습니다.


이제 두 가지를 함께 해보겠습니다:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


실행하면 인쇄됩니다:


```
25
hello again
```

### 재할당


Let`으로 선언된 변수는 생성된 후에 변경할 수 있습니다.


이를 재할당이라고 합니다.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


먼저 `10`을 `점수`에 할당하고 이를 출력합니다.


그런 다음 `score` 값을 `15`로 변경하고 다시 인쇄합니다.


출력은 다음과 같습니다:


```
10
15
```


이 기능은 점수가 증가하는 게임처럼 시간이 지남에 따라 값이 변할 때 매우 유용합니다.


여기에 또 다른 변수를 추가해 보겠습니다:


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


인쇄됩니다:


```
10
Alice
20
Bob
```


보시다시피 `점수`와 `플레이어`가 모두 변경되었습니다.


### const 선언


하지만 대부분의 경우 변수가 생성된 후 변경되는 것을 원하지 않습니다. 이를 위해 `const`를 사용합니다.


const`는 "상수"의 줄임말입니다. Const` 변수에 값을 할당하고 나면 변경할 수 없습니다.


```javascript
const pi = 3.14
console.log(pi)
```


인쇄됩니다:


```
3.14
```


하지만 이렇게 해보세요:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript는 다음과 같은 오류를 표시합니다:


```
TypeError: Assignment to constant variable.
```


이는 `pi`가 `const`를 사용하여 선언되었기 때문이며, 그 이후에는 값을 변경할 수 없습니다. 자바스크립트 인터프리터에게 해당 변수를 변경하지 않겠다는 의사를 전달하고 있는 것입니다.


이는 실수로 변경할 가능성을 줄여주기 때문에 유용합니다. 프로그램이 수천 줄의 코드로 매우 커지면 한 번에 일어나는 모든 일을 따라잡는 것이 불가능하므로(우리가 컴퓨터를 사용하는 주된 이유는 두뇌로는 계산할 수 없는 복잡한 프로세스를 실행하기 위해서입니다), 이와 같은 제한을 두어 프로그램을 보다 결정적으로 만드는 것이 유용해집니다.


나중에 값을 수정할 것이 확실하지 않다면 항상 값을 `const`로 선언하는 것이 가장 좋은 방법이라고 생각합니다.


### 자바스크립트 댓글


가끔 코드에 실행되지 않는 메모를 작성하고 싶을 때가 있습니다. 이를 주석이라고 합니다.


댓글은 프로그램이 실행될 때 무시되지만, 자신이나 다른 사람에게 설명하는 데 유용합니다.


한 줄 댓글을 작성하려면 `//`를 사용합니다


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


그래도 인쇄됩니다:


```
10
```


댓글은 사람이 읽기 위한 것입니다.


또한 `/*` 및 `*/`를 사용하여 여러 줄의 댓글을 작성할 수도 있습니다


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


이렇게 인쇄됩니다


```
20
```


댓글은 무시됩니다.


주석을 사용하여 코드에 작은 주석을 추가하면 코드가 어떤 기능을 하는지, 왜 특정 방식으로 작성되었는지 기억할 수 있습니다. 또한 다른 프로그래머가 코드를 이해하는 데 도움이 될 수도 있습니다.


## 기본 유형: 숫자, 문자열, 부울

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


자바스크립트에서 '타입'은 값이 어떤 종류의 데이터인지 알려줍니다.


자바스크립트에는 몇 가지 기본 유형이 있으며, 이 섹션에서는 그 중 몇 가지를 살펴보겠습니다.


### 숫자 및 산술 연산


첫 번째로 소개할 유형은 '숫자'입니다.


자바스크립트에서 숫자는 정수(예: `5`) 또는 소수(예: `3.14`)일 수 있습니다.


덧셈, 뺄셈, 곱셈, 나눗셈과 같은 산수를 할 수 있습니다.


다음은 기본적인 예입니다:


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


인쇄됩니다:


```
15
5
50
2
```


괄호 `()`를 사용하여 연산 순서를 제어할 수도 있습니다:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


인쇄됩니다:


```
20
```


괄호가 없으면 '2 + 3 * 4'가 됩니다:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


인쇄됩니다:


```
14
```


일반 수학에서는 곱셈이 덧셈보다 먼저 일어나기 때문입니다.


### 문자열 및 보간


두 번째로 소개할 자바스크립트 유형은 `string`입니다.


문자열은 텍스트 조각입니다. 작은따옴표 ''...'` 또는 큰따옴표 '"..."`를 사용하여 문자열을 만들 수 있습니다.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


인쇄됩니다:


```
hello
Bob
```


문자열을 결합하려면 `+` 연산자를 사용하면 됩니다:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


인쇄됩니다:


```
hello Bob
```


하지만 **스트링 보간**이라는 문자열을 결합하는 더 좋은 방법이 있습니다. 백틱을 사용하여 문자열 `` `...` ``를 선언하고 문자열 안에 `${...}`를 사용하여 변수를 작성합니다:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


이것도 인쇄됩니다:


```
hello Bob
```


'${...}` 안에 어떤 표현식이라도 포함할 수 있습니다:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


인쇄됩니다:


```
Next year, I will be 31 years old.
```


보간은 최신 자바스크립트에서 매우 일반적입니다.


### 부울, 비교 및 논리 연산


세 번째로 소개할 유형은 '부울'입니다. 부울 논리를 발명한 수학자 조지 불의 이름을 따서 명명되었습니다.


부울은 '참'과 '거짓'이라는 두 가지 값만 가능합니다.


변수에 저장할 수 있습니다:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


인쇄됩니다:


```
true
false
```


논리 연산자를 사용하여 부울을 결합할 수 있습니다:



- '&&'는 "그리고"를 의미하며, **두** 값이 모두 `참`인 경우에만 `참`을 반환하고, 그렇지 않으면 `거짓`을 반환합니다
- '`||`'는 "또는"을 의미하며, 값 중 **하나 이상**이 `참`이면 `참`을 반환하고, 그렇지 않으면 (둘 다 거짓인 경우) `거짓`을 반환합니다
- '!`는 "아니다"를 의미하며, 부울 앞에 적용되어 부울이 `참`이면 `거짓`을 반환하고 그 반대의 경우 `거짓`을 반환합니다.


![](assets/en/003.webp)


예시:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


자바스크립트에서는 `>`, `<`, `===`, `!==`와 같은 연산자를 사용하여 값을 비교할 수 있습니다. 이러한 비교의 결과는 항상 부울입니다.


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


자바스크립트에는 '더 크거나 같음'을 의미하는 `>=`와 '더 작거나 같음'을 의미하는 `<=`도 있습니다.


"이메일이 도착했고 필요한 이미지가 포함되어 있거나 이메일의 길이가 10000자보다 길다"와 같이 복잡한 조건을 선언하기 위해 프로그램에서 부울, 비교 및 논리 연산자를 결합하는 경우가 많습니다. 나중에 이러한 연산자들이 프로그램의 논리를 구성하는 데 필수적인 구성 요소라는 것을 알게 될 것입니다.


## 배열, 널, 정의되지 않음

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


이 섹션에서는 자바스크립트 프로그램에서 매우 일반적인 세 가지 유형을 더 다뤄보겠습니다:



- **배열**: 값의 시퀀스
- **정의되지 않음**: "아무것도 할당되지 않음"을 의미하는 특수 값입니다
- **null**: "의도적으로 비어 있음"을 의미하는 또 다른 특수 값입니다


### 배열 및 인덱스 액세스


배열**은 목록에 여러 값을 담을 수 있는 유형입니다.**


대괄호 `[]`를 사용하고 쉼표로 항목을 구분하여 배열을 만듭니다.


다음은 기본적인 예입니다:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


인쇄됩니다:


```
[ 10, 2, 88 ]
```


숫자뿐만 아니라 무엇이든 배열에 저장할 수 있습니다:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


인쇄됩니다:


```
[ 'apple', 42, true ]
```


배열의 특정 항목에 액세스하려면 **인덱스**를 사용합니다. 인덱스는 **0**부터 시작하는 항목의 위치입니다.


이 배열에서


```javascript
const colors = ["red", "green", "blue"]
```



- colors[0]`은 `"빨간색"`입니다
- colors[1]`은 `"Green"`입니다
- colors[2]`는 `"blue"`입니다


해보겠습니다:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


인쇄됩니다:


```
red
green
blue
```


배열의 특정 인덱스에 값을 할당할 수 있습니다


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


인쇄됩니다:


```
[ 'red', 'yellow', 'blue' ]
```


변수에 저장된 자연수를 포함한 모든 자연수를 인덱스로 사용할 수 있습니다


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


인쇄됩니다:


```
green
```


그러나 존재하지 않는 인덱스에 액세스하려고 하면 '정의되지 않음'이라는 메시지가 표시됩니다:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


인쇄됩니다:


```
undefined
```


저게 뭐죠?


### '정의되지 않음'


특수 값 '정의되지 않음'은 "값이 할당되지 않음"을 의미합니다.


변수를 만들었지만 값을 지정하지 않으면 '정의되지 않음'이 됩니다:


```javascript
const name
console.log(name)
```


인쇄됩니다:


```
undefined
```


이름`에 아무 것도 할당하지 않았기 때문에 자바스크립트는 기본적으로 `정의되지 않음`으로 설정합니다.


앞서 살펴본 것처럼 존재하지 않는 배열 인덱스에 액세스하면 '정의되지 않음'이 반환될 수도 있습니다:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


인쇄됩니다:


```
undefined
```


### 'null'과 이를 처리하는 방법


null`도 특별한 값입니다. "여기에는 아무것도 없으며 일부러 그렇게 했습니다."라는 뜻입니다


자동인 '정의되지 않음'과 달리 'null'은 사용자가 직접 설정하는 항목입니다.


예를 들어


```javascript
const currentUser = null
console.log(currentUser)
```


인쇄됩니다:


```
null
```


왜 `null`을 사용하나요? 나중에 값을 기대할 수 있지만 아직 준비가 되지 않았을 수 있습니다:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


인쇄됩니다:


```
Alice
```


따라서 `null`은 예를 들어 "나중에 여기에 무언가가 있어야 하지만 지금은 비어 있습니다."라고 말하고 싶을 때 유용합니다


## 블록 및 제어 흐름

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


지금까지는 대부분 차례로 실행되는 코드 줄을 작성했습니다.


하지만 코딩을 할 때는 실행 순서를 제어할 수 있습니다.


이를 **흐름 제어**라고 합니다.


블록과 범위를 이해하는 것부터 시작하겠습니다.


### 글로벌 범위


우리가 선언하는 모든 변수는 **범위**에 존재하며, 이는 변수가 알려진 코드의 영역을 의미합니다.


블록 외부에 변수를 선언하면 해당 변수는 **글로벌 범위**에 존재합니다.


```javascript
const color = "blue"
console.log(color)
```


이 변수 'color'는 전역 범위에 있으므로 파일 내 어디에서나 액세스할 수 있습니다.


줄을 더 추가하는 경우


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


색상`과 `크기`는 모두 전역 변수입니다. 파일의 모든 곳에서 사용할 수 있습니다.


하지만 블록 내부에서는 어떤 일이 일어날까요?


### 블록 및 로컬 범위


블록**은 중괄호 `{}`로 둘러싸인 코드 조각입니다.**


블록 내부에 `let` 또는 `const`로 선언된 변수는 해당 블록 내부에만 존재합니다.


```javascript
{
const message = "inside block"
console.log(message)
}
```


인쇄됩니다:


```
inside block
```


하지만 이렇게 해보세요:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript는 다음과 같은 오류를 표시합니다:


```
ReferenceError: message is not defined
```


이는 `메시지`가 블록 내부에서 선언되었고 블록 외부에 존재하지 않기 때문입니다.


즉, 블록을 사용하여 코드의 일부를 격리하고 "블록에서 일어나는 일은 블록에 남아있게"(라스베가스처럼) 할 수 있습니다.


블록으로 코드를 구성하면 `if`와 같은 제어 흐름 구문을 사용하여 프로그램 실행을 구조화할 수도 있습니다


### if, else


때때로 우리는 어떤 것이 참일 때만 코드를 실행하고 싶을 때가 있습니다. 이것이 바로 `if` 문입니다.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


인쇄됩니다:


```
Am I an adult?
Yes I am!
```


아래 코드에서 `myAge`와 `18`을 비교하는 것을 확인할 수 있습니다.

이 경우 `>=` 연산자는 `true`를 반환하므로 블록이 실행됩니다.

조건이 'true'가 아닌 경우 블록이 실행되지 않습니다.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


인쇄됩니다:


```
Am I an adult?
```


'else' 블록을 추가하여 반대의 경우를 처리할 수 있습니다:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


인쇄됩니다:


```
Am I an adult?
No, I am not.
```


If` 및 `else` 블록은 모두 여전히 블록이므로 내부에 선언된 변수는 외부에 존재하지 않습니다.


어떤 것이 사실이 아닌지 확인하려면 어떻게 해야 할까요?


앞서 설명한 것처럼 자바스크립트에는 부울을 뒤집는 'not' 연산자가 있습니다. 따라서 다음을 수행할 수 있습니다


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

여전히 인쇄됩니다:


```
Am I an adult?
No, I am not.
```

왜냐하면 `!` 연산자를 사용하여 `adult` 변수를 반전시켰기 때문입니다.


`if (!adult) {...}`는 "어른이 아니라면..."으로 읽어야 합니다


블록, 논리 및 비교 연산자를 사용하여 어떤 일이 일어나기 위해 '참'(또는 '거짓')이어야 하는 변수를 정의함으로써 프로그램 실행을 구조화할 수 있습니다.


### 동안, 브레이크, 계속


동안` 루프는 조건이 참인 한 *동안* 코드를 반복합니다.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


인쇄됩니다:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


카운트`가 3이 되면 루프가 중지됩니다.


Break`를 사용하여 루프를 일찍 중지할 수 있습니다:


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


인쇄됩니다:


```
0
1
2
```


숫자가 `3`이 되면 `if` 블록이 실행되어 루프가 중지되기 때문입니다.


'계속'을 사용하여 나머지 루프를 건너뛸 수 있습니다:


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


인쇄됩니다:


```
1
2
4
5
```


숫자가 `3`일 때 `계속`은 프로그램이 숫자를 인쇄하는 줄을 건너뛰게 만들었기 때문입니다.


### for ... of ...


배열이 있고 그 안의 모든 항목에 대해 무언가를 수행하려는 경우 `for ... of ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


인쇄됩니다:


```
apple
banana
cherry
```

블록은 배열의 각 요소에 대해 한 번씩 실행됩니다.


여기서 `fruit`는 배열의 각 항목의 값을 가져와 블록 내에서 연산하는 새 변수입니다.


### for ... in ...


For ... in`을 사용하여 배열의 키(인덱스)를 반복할 수 있습니다:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


인쇄됩니다:


```
0
1
2
```


인덱스를 사용하여 값을 가져올 수도 있습니다:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


이것은 '...에 대해'와 동일하게 인쇄됩니다:


```
apple
banana
cherry
```


실제로 배열의 경우 '...의'를 사용하는 것이 더 간단하고 깔끔하므로 이를 선호해야 합니다.


### 바운드 루프


특정 횟수를 반복하거나 일반적으로 무언가를 추적하면서 블록을 반복하는 코드를 작성하고 싶을 때가 있습니다.

바인딩된 `for` 루프는 바로 이런 용도로 유용합니다.

바운드 루프는 일반적으로 `(... ; ... ; ....)`와 같이 세미콜론 `;`으로 구분된 세 가지 조건을 사용합니다.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


인쇄됩니다:


```
0
1
2
```


설명해 드리겠습니다:



- 'let i = 0`: 블록에서 사용할 변수를 선언합니다(이 경우 0에서 시작하는 카운터)
- i < 3`: 블록을 실행하기 위한 조건을 `true`로 선언합니다(이 경우 "`i`가 3보다 작은 동안 반복")
- `i = i + 1`: 블록을 실행할 때마다 실행할 코드를 선언합니다(이 경우 "`i`를 1씩 증가")


보시다시피 바운디드 루프는 코드의 반복 실행을 위해 더 복잡한 조건을 선언해야 하지만 대부분의 경우 필요하지 않습니다.


### 블록 레이블


좀 더 복잡한 제어 흐름을 작성해야 하는 경우, 자바스크립트를 사용하면 `브레이크` 또는 `계속`을 사용하여 블록의 이름을 지정하고 뒤로 이동할 `위치`를 지정할 수 있습니다.


예시:


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


인쇄됩니다:


```
Inside outer block
Inside inner block
Done
```


외부` 블록을 완전히 종료하려면 `브레이크 아웃`을 사용했습니다.


루프에 레이블을 지정할 수도 있습니다. 이 예를 들어 보겠습니다:


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

이것은 매우 지루한 예시이지만 라벨의 (가끔씩) 필요성을 명확하게 설명해 주었기를 바랍니다.


## 기능 소개

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


프로그램이 성장함에 따라 코드 조각을 **재사용**하고 싶을 때가 많습니다.


함수는 코드를 그룹화하여 이름을 지정하고 원할 때마다 실행할 수 있도록 해주는 기능입니다.


### 함수 선언


함수를 선언하려면 `function` 키워드를 사용하면 됩니다. 그런 다음 이름과 괄호 `()` 한 쌍과 인수를 지정하고 실행할 코드 블록 `{}`을 지정합니다. 인수를 받지 않는 함수부터 시작해 보겠습니다:


```javascript
function sayHello () {console.log(`Hello!`) }
```


이 코드는 함수를 **선언**하지만 아직 **실행하지** 않습니다.


### 함수 호출


함수를 실행(또는 "호출")하려면 괄호 안에 함수 이름을 적습니다:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


인쇄됩니다:


```
Hello!
```


원하는 횟수만큼 함수를 호출할 수 있습니다:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


인쇄됩니다:


```
Hello!
Hello!
```


함수 내부의 코드는 사용자가 함수를 호출할 때만 실행됩니다.


### 함수 인수(함수에 대한 입력)


때로는 함수가 일부 입력과 함께 작동하기를 원할 때가 있습니다. 괄호 안에 **인수**를 추가하면 됩니다.


예를 들어


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


이제 이 함수는 '친구'라는 **하나의 인수**를 받습니다.


함수를 호출할 때 값을 전달할 수 있습니다:


```javascript
sayHelloTo("Tommy")
```


인쇄됩니다:


```
Hello Tommy!
```


다른 이름으로 함수를 다시 호출할 수 있습니다:


```javascript
sayHelloTo("Sam")
```


인쇄됩니다:


```
Hello Sam!
```


전달한 값은 함수 내부의 `친구` 변수를 대체합니다.


인수를 두 개 이상 사용할 수도 있습니다:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


인쇄됩니다:


```
Hello Lina and Marco!
```


### 반환(함수에서 출력)


함수는 값을 **반환**할 수도 있습니다. 즉, 함수가 호출된 곳으로 값을 다시 전송합니다.


다음은 간단한 예입니다:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


인쇄됩니다:


```
42
```


GetNumber()` 함수는 `42`를 반환하고 이를 `result`에 저장한 다음 인쇄합니다.


계산한 내용을 반환할 수도 있습니다:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


인쇄됩니다:


```
5
```


값이 '반환'되면 함수가 중지됩니다. 해당 블록의 `return` 이후에는 아무 일도 일어나지 않습니다.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


인쇄만 가능합니다:


```
hi
```


"hi"`만 반환되기 때문입니다. 콘솔 로그("this never runs")` 줄은 건너뜁니다.


함수는 작은 하위 프로그램이라고 생각하면 됩니다. 각 함수는 약간의 입력을 받아 작업한 후 약간의 출력을 반환할 수 있습니다.


함수의 반환값을 사용하려고 하는데 해당 함수가 아무것도 반환하지 않으면 어떻게 될까요?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

그러면 `undefined`가 출력됩니다. 아무것도 반환하지 않는 함수의 반환 값은 `undefined`입니다.


## 객체 및 클래스

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


자바스크립트는 흔히 객체 지향 언어라고 불립니다.


즉, 값과 함수를 **객체**로 그룹화하여 코드를 정리하는 데 도움이 됩니다.


### '객체'란 무엇인가요?


객체에는 데이터와 해당 데이터에서 작동하는 함수가 포함될 수 있습니다. 객체에 함수를 넣을 때 우리는 이를 '메서드'라고 부릅니다.


첫 번째로 살펴본 객체는 '콘솔' 객체입니다. 이 객체는 화면에 무언가를 출력하고 프로그램을 디버깅하는 여러 메서드를 포함하는 객체입니다.


자체 인쇄도 가능합니다


```javascript
console.log(console)
```


를 입력하면 포함된 메서드 목록이 인쇄됩니다. 예를 들어, 제 컴퓨터에서는 다음과 같이 인쇄되었습니다


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


보시다시피 디버깅에 사용할 수 있는 많은 메서드가 있습니다!


자바스크립트는 우리가 원하는 모든 작업을 수행할 수 있는 새로운 객체를 만드는 다양한 방법을 제공합니다.


### 객체 만들기


중괄호 `{}`를 사용하여 데이터와 함수를 그룹화하는 것이 객체를 만드는 가장 쉬운 방법입니다.


이렇게 하면 **익명 객체**가 생성됩니다


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


이렇게 하면 객체가 생성되고 'cat'이라는 변수에 저장됩니다.


객체에는 두 개의 **프로퍼티**가 있습니다:



- 이름`을 `"수염"` 값으로 설정합니다
- 나이`를 `3` 값으로 설정합니다


인쇄해 보겠습니다:


```javascript
console.log(cat)
```


인쇄됩니다:


```
{ name: 'Whiskers', age: 3 }
```


ObjectName.propertyName`에서와 같이 점을 사용하여 객체에서 속성을 가져올 수 있습니다:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


숙소를 **변경**할 수도 있습니다:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


보시다시피 객체가 `const`로 정의되어 있어도 객체에 포함된 데이터를 수정할 수 있습니다.


객체의 경우 `const`를 사용하면 전체 객체를 재정의할 수 없습니다:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


앞서 언급했듯이 객체는 **함수**를 보유할 수도 있으며, 함수가 객체의 일부인 경우 이를 **메소드**라고 부릅니다.


다음은 한 가지 예입니다:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


이 객체에는



- 이름` 속성
- Speak()` 메서드


메서드를 호출해 보겠습니다:


```javascript
cat.speak()
```


인쇄됩니다:


```
Meow!
```


메서드는 `this` 키워드를 통해 객체에 포함된 데이터를 사용할 수 있습니다.

이`는 현재 객체를 나타냅니다. 이 예제에서는 고양이의 이름을 인쇄하는 데 사용됩니다:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


인쇄됩니다:


```
Whiskers says meow!
```


'this`라는 단어는 "이 객체"를 의미합니다...이 경우 '고양이'라는 객체입니다.



이러한 종류의 객체는 빠르고 간단한 것을 원할 때 유용합니다. 하지만 동일한 구조의 **다수의 객체**를 만들어야 한다면 더 좋은 방법이 있는데, 바로 **클래스**가 바로 그것입니다.


### 클래스 및 생성자


클래스는 청사진과 같습니다. 자바스크립트에 특정 종류의 객체를 생성하는 방법을 알려줍니다.


클래스` 키워드 뒤에 클래스 이름과 중괄호 `{}` 블록을 사용하여 클래스를 정의합니다.


```javascript
class Dog {}
```


클래스는 일반적으로 관례에 따라 대문자로 시작합니다.


New`를 사용하여 클래스의 새 객체를 만들 수 있습니다:


```javascript
const hachiko = new Dog()
```


개체를 인쇄해 보세요:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


다음을 얻을 수 있습니다


```
Dog {}
```


보시다시피 Dog 클래스가 비어 있으므로 `myDog` 객체도 비어 있습니다.


생성자`를 추가하여 Dog 객체가 포함해야 하는 프로퍼티를 정의할 수 있습니다.


생성자는 새 객체를 생성(또는 "생성")할 때 실행되는 특수 함수입니다.


```javascript
class Dog {
constructor() { }
}
```


각 Dog에 이름을 지정하고 싶으므로 함수에 `name` 매개 변수를 추가합니다:


```javascript
class Dog {
constructor(name) { }
}
```


그리고 `이것`을 사용하여 `name`이 우리가 빌드 중인 `Dog` 객체의 `이름`임을 선언합니다


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


지금 사용해 보겠습니다:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


다음과 같은 내용이 인쇄됩니다:


```
Dog { name: 'hachiko' }
```


보시다시피 '생성자' 메서드는 'new Dog()'를 실행할 때 클래스에 전달한 인수를 받아 이를 사용해 객체를 생성합니다.


자세히 살펴보겠습니다:



- 'class Dog'는 Dog 클래스를 정의합니다.
- 생성자(이름)`는 객체가 생성될 때 객체를 설정합니다.
- this.name = name`은 새 객체에 값을 저장합니다.
- new Dog("hachiko")`는 클래스에서 `name` 속성이 `"hachiko"`로 설정된 새 객체를 생성합니다.


이제 클래스에 메서드를 추가해 보겠습니다:


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


이렇게 인쇄됩니다


```javascript
hachiko says barf!
```


두 개의 서로 다른 Dog 인스턴스에 대해 동일한 작업을 수행하면



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


우리는 얻는다


```
hachiko says barf!
bobby says barf!
```


에서 `speak()` 메서드는 호출되는 `Dog`의 `name` 속성을 사용합니다.


클래스를 사용하면 데이터에서 작동하는 메서드 집합을 정의한 다음 동일한 데이터 '모양'을 공유하는 여러 개체를 만들 수 있기 때문입니다.


이러한 객체 중 하나에서 메서드를 호출하면 해당 메서드는 *특정 객체가 보유한 데이터에 대해 작동합니다.*


### 개체 모양 변경하기


자바스크립트의 객체는 유연합니다. 객체를 생성한 후에도 새 속성을 추가하거나 기존 속성을 제거할 수 있습니다.


허용되지만 신중하게 사용해야 하는 기능입니다.


간단한 '강아지' 클래스부터 시작하겠습니다:


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


이 시점에서 `myDog`에는 하나의 속성만 있습니다: 이름`입니다. 생성된 후에도 새 프로퍼티를 추가할 수 있습니다:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


새로운 방법을 추가할 수도 있습니다:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


또한 `삭제` 키워드를 사용하여 속성도 제거할 수 있습니다.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


이 방법은 효과가 있지만 한 가지 알아두어야 할 중요한 사항이 있습니다: V8(Node.js 및 Chrome 브라우저에서 사용)과 같은 JavaScript 엔진은 객체가 항상 동일한 프로퍼티를 유지할 때 더 빠르게 실행됩니다. 객체가 생성된 후에 속성을 추가하거나 제거하면 속도가 느려질 수 있습니다.


소규모 프로그램에서는 크게 중요하지 않습니다. 하지만 게임과 같은 대규모 프로젝트에서는 당장 사용하지 않더라도 처음부터 생성자에 모든 프로퍼티를 나열하는 것이 좋습니다. 이렇게 하면 객체 모양이 안정적으로 유지되고 코드가 더 빠르게 실행됩니다.


예를 들어, 이렇게 대신할 수 있습니다:


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


다음을 수행할 수 있습니다


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


두 버전 모두 작동하지만 두 번째 버전이 성능 면에서 더 좋습니다. 각 객체가 어떤 속성을 가질지 엔진에 미리 알려주면 엔진이 그에 따라 최적화할 수 있습니다.


자바스크립트를 사용하면 객체의 모양을 자유롭게 변경할 수 있지만 클래스를 사용할 때는 객체의 모양을 미리 계획하는 것이 가장 좋습니다.



### Extends 및 super()를 사용한 상속


때로는 다른 클래스와 '거의' 동일하지만 몇 가지 추가 기능이 있는 클래스를 만들고 싶을 때가 있습니다.


앞서 언급한 것처럼 객체의 모양을 수정하거나(성능에 최적이 아닌) 새 클래스를 처음부터 다시 작성해야 하는 대신 JavaScript를 사용하면 **상속**이라는 것을 사용할 수 있습니다.


상속은 한 클래스가 다른 클래스를 **확장**할 수 있음을 의미합니다. 새 클래스는 이전 클래스의 모든 프로퍼티와 메서드를 가져와서 필요한 것을 추가하거나 변경할 수 있습니다.


'Vehicle'이라는 베이스 클래스가 있다고 가정해 보겠습니다:


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


이제 '자동차' 클래스를 만들고 싶습니다. 자동차는 일종의 차량이지만 시동을 걸 때 몇 가지 추가 기능이나 다른 메시지를 표시하고 싶을 수 있습니다. 모든 것을 다시 작성하는 대신 `extends`를 사용할 수 있습니다:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Car` 클래스는 이제 `Vehicle`의 모든 것을 **상속**합니다. 브랜드` 속성을 가져오고 `start()` 메서드를 자체 버전으로 대체했습니다.


![](assets/en/004.webp)


한번 사용해 보세요:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


인쇄됩니다:


```
Toyota car is ready to drive!
```


Car`에는 자체 생성자가 없지만 여전히 `Vehicle`의 생성자를 사용합니다. 하지만 `Car`에 사용자 정의 생성자를 작성하려면 `super()`를 사용하여 부모 생성자에 대한 호출을 포함하기만 하면 됩니다.


방법은 다음과 같습니다:


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


![](assets/en/005.webp)



인쇄됩니다:


```
Toyota Corolla is ready to drive!
```


요약하면 다음과 같습니다



- '확장'은 한 클래스가 다른 클래스를 기반으로 한다는 의미입니다.
- super()`는 확장하려는 클래스의 생성자를 호출하는 데 사용됩니다.
- 새 클래스는 원래 클래스의 모든 프로퍼티와 메서드를 가져옵니다.
- 메서드(예: `start()`)를 **재정의**하여 다른 작업을 수행하도록 할 수 있습니다.


자동차, 트럭, 자전거처럼 비슷한 사물이 여러 개 있고 코드를 공유하되 각 사물이 고유한 방식으로 동작하도록 하려는 경우에 유용합니다.


### 인스턴스 오브


인스턴스 오브` 키워드는 객체가 특정 클래스에서 생성되었는지 확인합니다.


'사용자'라는 클래스가 있다고 가정해 보겠습니다:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


인쇄됩니다:


```
true
```


일반 사용자`가 `사용자`인지 확인합니다. 일반 사용자`가 `사용자` 클래스를 사용하여 생성되었기 때문입니다.


상속된 클래스에서도 작동합니다. 예를 들어, 다음은 `User`를 확장하는 `Admin` 클래스입니다:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


두 줄 모두 `true`를 반환합니다. 이는 `Admin`이 `User`의 서브클래스이므로 `ourAdmin`이 `Admin`이자 `User`이기 때문입니다


# 중급 자바스크립트

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## 오류 처리

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


복잡한 자바스크립트 프로그램을 작성하다 보면 **오류**가 발생하게 됩니다. 이는 무언가 잘못되는 예기치 않은 상황입니다. 변수가 '정의되지 않은' 상태인데 이를 사용하려고 하거나 일부 코드가 잘못된 유형의 입력을 수신할 수 있습니다.


이러한 오류를 제대로 처리하지 않으면 프로그램이 충돌하거나 예기치 않은 방식으로 작동할 수 있습니다. 자바스크립트는 이러한 오류를 감지하고 관리할 수 있는 도구를 제공하여 오류를 보다 원활하게 처리할 수 있도록 합니다.


### 일반적인 오류: '정의되지 않음'의 값 액세스


다음은 오류를 일으키는 일반적인 상황입니다:


```javascript
const user = undefined
console.log(user.name)
```


이 코드를 실행하면 다음과 같은 오류가 발생합니다:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


자바스크립트가 이렇게 말합니다: "이봐요, 당신은 '정의되지 않은' 것에서 '이름' 속성을 가져오려고 했는데, 그건 말이 안 됩니다." 보시다시피 이런 종류의 오류가 발생하면 이를 포착하고 처리하는 코드를 특별히 작성하지 않는 한 프로그램 실행이 중지됩니다.


### 오류 '던지기'


코드에서 오류를 수동으로 **발생**하고 싶을 때가 있습니다. 이 경우 `throw` 키워드를 사용합니다.


```javascript
throw new Error("This is a custom error message")
```


그러면 프로그램이 즉시 중지되고 인쇄됩니다:


```
Uncaught Error: This is a custom error message
```


프로그램에서 `throw`를 사용하여 규칙을 적용할 수 있습니다. 예를 들어


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


이 예제에서는 0으로 나누는 것이 허용되지 않기 때문에 두 번째 호출은 오류를 발생시킵니다.


### Try...catch로 오류 잡기


오류가 발생했을 때 프로그램이 충돌하는 것을 원하지 않는다면 `try...catch` 블록을 사용하여 오류를 잡을 수 있습니다. 이는 프로그램이 실패하더라도 계속 진행되도록 하고 싶을 때 유용합니다.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


출력:


```
Oops! Something went wrong.
```


작동 방식은 다음과 같습니다:



- 시도` 블록 안에 있는 코드가 먼저 시도됩니다.
- 오류가 발생하면 자바스크립트는 나머지 'try' 블록을 건너뛰고 'catch' 블록으로 **점프**합니다.
- Catch` 블록은 오류를 수신하므로 오류를 인쇄하거나 다음과 같은 다른 방식으로 처리할 수 있습니다


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


출력:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### '마지막으로' 블록


'마지막으로' 블록을 추가할 수도 있습니다. 이는 오류 발생 여부와 관계없이 **항상 실행**되는 코드입니다.


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


출력:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## 버그 방지

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


이 장에서는 자바스크립트에서 가장 흔한 함정 몇 가지와 이를 피하는 방법을 설명합니다.


### 선언 없는 var 및 Assignment


이전 자바스크립트 코드에서 변수는 종종 `var` 키워드를 사용하여 선언되었습니다. 이미 학습한 `let` 및 `const`와 달리 `var`는 혼란스러운 방식으로 작동할 수 있습니다.


예를 들어


```javascript
{
var message = "hello"
}
console.log(message)
```


메시지`는 블록 내부에만 존재할 것으로 예상할 수 있지만 그렇지 않습니다. var`는 블록 범위를 무시하고 전체 함수 또는 파일에서 변수를 사용할 수 있게 합니다.


특히 대규모 프로그램에서는 예기치 않은 동작이 발생할 수 있습니다. 따라서 최신 자바스크립트 코드에서는 항상 `var` 대신 `let` 또는 `const`를 사용해야 합니다.


더 나쁜 것은 자바스크립트를 사용하면 **변수를 전혀 선언하지 않고도** 변수에 값을 할당할 수 있다는 것입니다:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


이렇게 하면 선언 없이 새로운 전역 변수 'name'이 생성됩니다. 이는 조용히 발생할 수 있으며 특히 단순한 오타일 경우 추적하기 어려운 Hard 수준의 버그로 이어질 수 있습니다. 항상 `let` 또는 `const`를 사용하여 변수를 선언하세요.


### 약한 유형 시스템


자바스크립트는 약한 타입이므로 필요한 경우 값을 한 타입에서 다른 타입으로 자동 변환합니다. 이를 유형 강제라고 하며, 편리할 수는 있지만 종종 혼란스러운 결과를 초래합니다.


예를 들어


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


이 예제에서 자바스크립트는 사용자가 무엇을 의미하는지 추측하려고 합니다. 때로는 문자열을 숫자로, 부울을 숫자로, 문자열을 문자열로 바꾸기도 합니다. 이로 인해 코드가 예상치 못한 방식으로 동작할 수 있습니다.


자바스크립트의 취약한 타이핑 시스템을 인식하는 것이 중요합니다. 자바스크립트가 이상하게 동작하기 시작하면 예기치 않은 유형 강제로 인한 것일 수 있습니다.


### "사용 엄격"


일부 무음 오류를 실제 오류로 전환하고 언어의 일부 위험한 기능을 사용하지 못하도록 하는 더 엄격한 모드를 활성화할 수 있습니다.


이 더 엄격한 모드를 사용하려면 파일 또는 함수 상단에 이 줄을 추가하세요:


```javascript
"use strict"
```


예를 들어


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


엄격 모드가 없으면 자바스크립트는 `name`이라는 전역 변수를 조용히 생성합니다. 하지만 엄격 모드를 사용하면 이것이 실제 오류가 되어 버그를 더 일찍 발견할 수 있습니다.


또한 엄격한 모드는 자바스크립트의 일부 오래된 기능을 비활성화하여 코드를 더 쉽게 최적화하고 유지 관리할 수 있게 해줍니다.


## 가치 대 참조

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


자바스크립트는 다양한 종류의 값을 다양한 방식으로 처리합니다.


일부 값은 변수에 할당할 때 **복사**됩니다.


다른 변수는 새 변수에 할당할 때 **공유**되므로 하나를 변경하면 다른 변수도 변경됩니다.


### 값으로 전달


값이 **값으로** 전달되면 자바스크립트는 이를 **복사**합니다.


따라서 하나를 변경해도 다른 하나에는 영향을 미치지 않습니다.


이는 다음과 같은 원시 유형에서 발생합니다:



- 숫자
- 문자열
- 부울(`참` 및 `거짓`)
- `null`
- '정의되지 않음'


예를 들어 보겠습니다:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


B`에 `a`의 값을 부여했지만 `b`를 `10`으로 변경했습니다.


숫자는 값으로 전달되기 때문에 자바스크립트는 `5`를 `b`로 복사했습니다. B`의 `5`는 `a`의 원래 `5`와 독립적이므로 `b`의 값을 변경해도 `a`에는 아무런 영향을 미치지 않습니다.


문자열로 해보겠습니다:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


다시 말하지만, 문자열도 값으로 전달되기 때문에 `name2`를 변경해도 `name1`에는 영향을 미치지 않습니다.


프리미티브를 함수에 전달할 때도 같은 일이 발생합니다. 따라서 함수는 원본을 변경할 수 없습니다.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


함수 내부에서 `1`이 `x`에 추가되었지만 원래의 `수`는 변경되지 않았습니다.


함수에 **copy**만 전달되었기 때문입니다.


### 참조로 전달


객체는 **참조**로 전달됩니다.


즉, 자바스크립트는 변수를 복사하는 대신 **참조**를 전달하고, 이를 수정하면 이를 가리키는 다른 모든 변수에도 변경 사항이 적용됩니다.


예를 들어


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


사람1`과 `사람2`는 모두 메모리에서 동일한 객체를 가리킵니다.


그래서 `person2.name`을 변경할 때 `person1.name`도 변경했는데, 둘 다 같은 것을 보고 있기 때문입니다.


배열은 객체이므로 배열로 동일한 작업을 해보겠습니다:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


4`를 `list2`에 밀어 넣었지만 `list1`도 같은 배열을 참조하기 때문에 영향을 받았습니다.


함수에 객체를 전달하면 어떤 일이 발생하는지 살펴보겠습니다:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


함수가 객체를 변경했습니다! 원래 '사람' 객체에 대한 **참조**를 받았기 때문입니다.


복사본을 얻지 못했습니다. 원본 개체에 액세스하여 이를 수정할 수 있는 기능을 얻었습니다.


그렇지 않으면 코드가 예상과 다르게 동작할 수 있으므로 이 구분을 기억하는 것이 중요합니다. 예를 들어, 수신하는 인수를 수정하지 않을 것으로 예상하고 함수를 작성했다가 나중에 실제로 인수를 수정하고 있다는 사실을 알게 될 수 있습니다(객체이므로 참조로 전달되었기 때문).


## 함수 작업

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


이미 자바스크립트에서 함수를 선언하고 사용하는 방법을 배웠습니다. 하지만 자바스크립트는 강력한 방식으로 함수를 사용할 수 있는 더 많은 도구를 제공합니다.


### 화살표 기능


화살표 함수는 함수를 짧게 작성하는 방법입니다. 함수` 키워드를 사용하는 대신 화살표(`=>`)를 사용합니다.


다음은 정상적인 기능입니다:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


화살표 버전은 다음과 같습니다:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


함수에 **한 줄만 있는 경우** 중괄호를 건너뛰고 '반환'할 수 있습니다:


```javascript
const greet = (name) => `Hello, ${name}!`
```


함수에 매개변수가 하나만 있는 경우 매개변수 주위의 괄호를 생략할 수도 있습니다:


```javascript
const greet = name => `Hello, ${name}!`
```


화살표 함수는 훨씬 적은 상용구로 간단한 함수를 표현할 수 있기 때문에 최신 자바스크립트에서 매우 일반적입니다.


### 기본 매개 변수


인수가 전달되지 않은 경우 함수가 **기본값**을 갖도록 하고 싶을 때가 있습니다.


이렇게 하면 됩니다:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


아무것도 전달되지 않으면 기본값 ``친구``가 사용됩니다.


### 스프레드 매개변수 (...)


함수가 유연한 수의 인수를 받는다면 어떨까요?


스프레드 연산자(`...`)를 사용하여 배열로 모을 수 있습니다:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


그런 다음 루프를 사용하여 각 항목을 처리할 수 있습니다:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


스프레드 연산자는 전달되는 인수의 개수를 알 수 없을 때 유용합니다.


### 고차 함수


고차 함수는 **고차 함수**를 말합니다:



- 는 다른 함수를 입력으로 받습니다
- 및/또는 함수를 출력으로 반환합니다


다음은 간단한 예입니다:


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


인쇄됩니다:


```
Hello, friend!
Hello, friend!
```


화살표 함수를 전달할 수 있습니다:


```javascript
runTwice(
() => console.log("Hello!")
)
```


인쇄됩니다:


```
Hello!
Hello!
```


다른 함수를 **반환**하는 함수를 작성할 수도 있습니다:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


MakeGreeter` 함수는 다른 함수를 빌드하는 함수입니다. 이 함수는 문자열을 받은 후 `console.log` 호출에서 해당 문자열을 사용하는 새 함수를 반환합니다.


이러한 종류의 패턴은 함수에 '구멍'을 남겨두었다가 나중에 필요한 동작으로 채울 수 있기 때문에 매우 강력합니다.


### 맵(), 필터(), 감소()


자바스크립트는 배열에 사용할 수 있는 몇 가지 유용한 내장 메서드를 제공합니다.


이러한 메서드는 함수를 인수로 사용하므로 고차 함수이기도 합니다.


map()`은 배열의 각 항목을 다른 항목으로 변환합니다.


예시:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


각 숫자는 두 배가 되고 결과는 새로운 배열이 됩니다.


필터()`는 테스트를 통과하지 못하면 배열에서 항목을 제거합니다.


예시:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


X > 2` 조건이 `true`를 반환하는 배열 항목만 유지됩니다.


reduce()`는 배열의 모든 항목을 단일 값으로 결합하는 데 사용됩니다.


예시:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


reduce`는 배열을 통과하며, 이 예에서는 `1`과 `2` 사이에 `+` 연산자를 적용한 다음, 결과인 `3`과 `3` 사이에, 결과인 `6`과 `4` 사이에 모든 배열 항목의 합(10)이 될 때까지 `+` 연산자를 적용합니다.


합계, 평균, 단계별 새 값 만들기 등 다양한 작업에 `reduce()`를 사용할 수 있습니다.


이러한 메서드('map', 'filter', 'reduce')는 수동 루프를 작성하지 않고도 데이터를 처리할 수 있는 강력한 도구입니다.


다음과 같이 일련의 작업으로 결합할 수도 있습니다:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## 개체 작업

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


이 장에서는 자바스크립트에서 객체 작업을 위한 강력하고 조금 더 고급스러운 도구에 대해 알아보겠습니다.


### 개인 속성


객체 외부에서 변경하거나 접근할 수 없도록 객체의 속성을 숨기고 싶을 때가 있습니다. 자바스크립트에서는 속성 이름 앞에 `#`를 사용하여 이를 수행하는 방법을 제공합니다. 이렇게 하면 클래스 내부에서만 액세스할 수 있는 **private** 프로퍼티가 생성됩니다.


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


비공개 속성은 실수로 변경하는 것을 방지하고자 할 때 유용합니다.


### 정적 속성


때로는 프로퍼티가 해당 클래스에서 생성하는 각 객체가 아닌 클래스 자체에 속하기를 원할 때가 있습니다. 이것이 바로 `정적` 프로퍼티입니다. 정적` 프로퍼티는 클래스에 포함되며 해당 클래스의 모든 객체가 이를 참조합니다.


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


이는 하나의 객체가 아닌 전체 객체 그룹에 적용되는 공유 데이터 및 메서드를 저장하는 데 유용합니다.


### get 및 set


자바스크립트에서 `get`과 `set`을 사용하면 일반 변수처럼 보이지만 실제로는 백그라운드에서 특수 코드를 실행하는 프로퍼티를 만들 수 있습니다.


Get`ter 메서드는 프로퍼티를 *읽으려고 할 때* 실행됩니다. 메서드 앞에 프로퍼티 이름이 있는 `get`을 써서 선언합니다.


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


전체 이름`은 일반 프로퍼티가 아니지만 프로퍼티처럼 사용할 수 있으며, 백그라운드에서는 `get` 함수를 실행하여 전체 이름을 작성합니다.


'설정' 메서드는 프로퍼티에 값을 '할당'할 때 실행됩니다. 이를 통해 누군가 해당 값을 변경하려고 할 때 어떤 일이 발생하는지 제어할 수 있습니다. 메서드 앞에 프로퍼티 이름과 함께 `set`을 쓰면 선언됩니다.


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


User.fullName = "John Smith"`를 수행하면 `set` 메서드가 실행되고 `firstName` 및 `lastName` 값이 업데이트됩니다.


따라서 단순한 변수를 설정하는 것처럼 보이지만 실제로는 다른 프로퍼티를 업데이트하는 로직을 트리거하고 있습니다.


## 키 및 값

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


자바스크립트 객체의 모든 프로퍼티에는 **키**(프로퍼티 이름이라고도 함)와 **값**이 있습니다.


예를 들어


```javascript
const user = {
name: "Alice",
age: 30
}
```


이 객체에서 ``이름``과 ``나이``는 키이고, ``Alice``와 ``30``은 그 값입니다.


### 동적 액세스


사용자 입력에서 프로퍼티 이름을 얻거나 변수에서 프로퍼티 이름을 읽는 등 프로퍼티 이름을 미리 알지 못하는 경우가 있습니다. 그래도 `myObject["keyName"]`과 같은 **대괄호 표기법**을 사용하여 액세스할 수 있습니다.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


해당 값을 가져오기 위해 객체에 문자열 `name`을 전달했습니다.


키를 변수에 저장하고 나중에 다음과 같이 해당 값에 액세스하는 데 사용할 수 있습니다


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### 동적 Assignment


변수를 키로 사용하여 객체 속성을 만들거나 업데이트할 수도 있습니다.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


이 기능은 단계별로 개체를 빌드할 때 유용합니다. 예를 들어


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


대괄호를 사용하여 객체를 생성하는 동안 동적 키를 *사용*할 수도 있습니다:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


이를 **계산된 속성**이라고 합니다. 대괄호 안의 값이 평가되고 그 결과가 키로 사용됩니다.


### 기호 유형


문자열 외에도 자바스크립트에서는 `심볼`이라는 특수 유형을 객체 키로 사용할 수 있습니다.


간단한 예부터 시작하겠습니다:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


이 예에서 `id`는 심볼입니다. 문자열은 아니지만 여전히 키로 작동합니다. 콘솔에 `user`를 로그하려고 하면 다음과 같이 표시됩니다:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


또 한 가지 중요한 점은 동일한 문자열을 사용하여 생성하더라도 생성하는 모든 심볼은 고유하다는 것입니다.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


기호를 사용하면 일반 키와 충돌하지 않는 키를 정의할 수 있습니다. 예를 들어 `name` 속성이 있는 개체가 있지만 향후 사용자가 예측할 수 없는 방식으로 개체를 사용자 지정할 수 있고 그 사용자가 `name` 속성도 추가할 수 있다고 가정해 봅시다. 원래 `name` 속성이 문자열로 정의된 경우 다음과 같이 새 속성으로 덮어쓰게 됩니다:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


대신 기호를 사용하는 경우:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


보시다시피 원래의 `name` 속성은 이런 식으로 보존됩니다. 이는 특정 에지 케이스에서 유용할 수 있습니다.


## 유틸리티 개체

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


자바스크립트는 디버깅 및 수학 연산과 같은 작업을 수행하는 데 도움이 되는 몇 가지 유용한 내장 객체를 제공합니다.


### 기타 '콘솔' 메서드


이미 화면에 값을 출력하는 `console.log`를 보셨을 것입니다.


콘솔` 객체에는 프로그램 디버깅에 도움이 되는 몇 가지 유용한 메서드가 있습니다.


#### `console.warn`


노란색(또는 일부 환경에서는 경고 아이콘과 함께)으로 메시지를 인쇄합니다:


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


오류와 같은 메시지를 빨간색으로 인쇄합니다:


```javascript
console.error("Something went wrong!")
```


#### `console.table`


배열 또는 개체를 테이블로 표시합니다:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


다음과 같은 표가 인쇄됩니다:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


이는 구조화된 데이터를 시각화하는 데 유용할 수 있습니다.


#### 콘솔 시간` 및 `콘솔 시간 종료`


작업에 걸리는 시간을 측정할 수 있습니다:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


다음과 같은 내용이 인쇄됩니다:


```
timer: 2.379ms
```


간단한 성능 테스트에 유용합니다.


### 수학 개체


자바스크립트는 계산을 수행하는 데 유용한 메서드가 포함된 `Math` 객체를 제공합니다.


#### `Math.random()`


0(포함)과 1(제외) 사이의 임의의 숫자를 반환합니다:


```javascript
const r = Math.random()
console.log(r)
```


출력 예시:


```
0.4387429859
```


#### math.floor()` 및 `Math.ceil()`



- 수학 바닥(n)`은 **내림**하여 가장 가까운 정수로 반올림합니다
- `Math.ceil(n)`은 가장 가까운 정수로 **반올림**합니다


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


가장 가까운 정수로 반올림합니다:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### math.max()` 및 `Math.min()`


숫자 목록에서 가장 크거나 가장 작은 값을 반환합니다:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### math.pow()` 및 `Math.sqrt()`



- '수학.pow(a, b)`는 `a`를 `b`의 거듭제곱으로 반환합니다
- `Math.sqrt(n)`은 `n`의 제곱근을 제공합니다


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# 고급 자바스크립트

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## 기타 컬렉션

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


자바스크립트는 일반 배열과 객체를 뛰어넘는 몇 가지 특별한 컬렉션 유형을 제공합니다. 여기에는 `Map`과 `Set`이 포함됩니다.


값 그룹을 저장하고 관리하는 데 도움이 되지만 지금까지 본 것과는 다른 방식으로 작동합니다.


'맵'은 객체와 마찬가지로 **키-값 쌍**의 모음입니다. 하지만 몇 가지 중요한 차이점이 있습니다:



- 키는 문자열뿐만 아니라 **모든 값**이 될 수 있습니다.
- 항목의 순서는 그대로 유지됩니다.
- 더 쉽게 작업할 수 있는 메서드가 내장되어 있습니다.


다음과 같이 새 맵을 만듭니다:


```javascript
const myMap = new Map()
```


그러면 빈 맵이 생성됩니다. 여기에 항목을 추가하려면 `myMap.set(키, 값)`을 사용합니다:


```javascript
myMap.set("name", "Alice")
```


이렇게 하면 `"name"` 키에 `"Alice"` 값이 추가됩니다.


숫자를 키로 사용할 수도 있습니다:


```javascript
myMap.set(42, "The answer")
```


심지어 객체를 키로 사용할 수도 있습니다:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


이는 문자열 키만 허용하는 일반 객체에서는 작동하지 않습니다.


값을 가져오려면 `myMap.get(key)`를 사용합니다:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


키가 존재하는지 확인하려면 `myMap.has(key)`를 사용합니다:


```javascript
console.log(myMap.has("name")) // true
```


키를 **제거**하려면 `myMap.delete(key)`를 사용합니다:


```javascript
myMap.delete("name")
```


전체 지도를 **지우려면** `myMap.clear()`를 사용합니다:


```javascript
myMap.clear()
```


큰 맵에서 값에 액세스하면 일반적으로 큰 개체보다 훨씬 더 나은 성능을 얻을 수 있기 때문에 맵은 대규모 값 컬렉션을 관리하는 데 유용합니다.


### 설정


Set`은 **값만 있는**(키가 없는) 컬렉션으로, 각 값은 **유일한** 값이어야 합니다. 즉



- 동일한 값을 두 번 사용할 수 없습니다
- 값은 추가한 순서대로 저장됩니다


다음과 같이 세트를 만듭니다:


```javascript
const mySet = new Set()
```


값을 **추가**하려면 `mySet.add(value)`를 사용합니다:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


2`를 두 번 추가하려고 시도했지만 세트는 하나의 복사본만 유지합니다.


값이 집합에 있는지 **확인**하려면 `mySet.has(value)`를 사용합니다:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


값을 **제거**하려면 `mySet.delete(value)`를 사용합니다:


```javascript
mySet.delete(2)
```


모든 것을 지우려면 `mySet.clear()`를 사용합니다:


```javascript
mySet.clear()
```


'설정'은 중복 여부를 수동으로 확인할 필요 없이 고유한 값 모음을 유지하려는 경우에 유용합니다:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


'세트'는 중복을 방지합니다.


## 이터레이터

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


배열, 문자열, 맵, 집합 등 자바스크립트에서 반복할 수 있는 대부분의 객체는 **이터러블**로, 해당 내용에 대한 반복자를 제공할 수 있습니다.


이터레이터는 항목 목록을 **한 번에 하나씩** 살펴볼 수 있도록 도와주는 자바스크립트의 특수 객체입니다.


### 객체 이터레이터


배열이나 맵과 달리 일반 객체는 `for...of`로 **이터러블**하지 않습니다. 이렇게 해보세요:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


오류가 발생합니다:


```
TypeError: user is not iterable
```


일반 객체에는 이터레이터가 내장되어 있지 않기 때문입니다. 하지만 자바스크립트에는 반복할 수 있는 다른 도구가 있습니다.


#### `Object.keys()`


객체의 **키** 배열을 가져온 다음 `Object.keys(obj)`를 사용하여 반복할 수 있습니다:


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


인쇄됩니다:


```
name
age
```


#### `Object.values()`


값**을 반복하려면 `Object.values()`를 사용합니다:


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


인쇄됩니다:


```
Alice
30
```


#### `Object.entries()`


키와 값을 모두 원한다면 `Object.entries()`를 사용하세요:


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


인쇄됩니다:


```
name is Alice
age is 30
```


객체를 직접 이터러블할 수는 없지만 이러한 메서드를 사용하면 `for...of`와 잘 작동하는 방식으로 객체의 콘텐츠에 완전히 액세스할 수 있습니다.


그렇다면 반복기는 어떻게 작동할까요?


### 심볼.이터레이터


모든 이터러블의 비밀은 'Symbol.iterator'라는 특별한 **심볼**입니다.


이 기호는 자바스크립트에 알려주는 내장 키입니다: "이 객체를 반복할 수 있습니다."


MyIterable[Symbol.iterator]()`를 호출하면 자바스크립트는 '.next()` 메서드가 있는 **이터레이터 객체**를 반환합니다.


어떤 모습인지 살펴보겠습니다:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


.next()`를 호출할 때마다 다음 값을 반환합니다. 완료되면 반환됩니다:


```javascript
{ value: undefined, done: true }
```


### next()


.next()` 메서드는 시퀀스에서 다음 항목을 가져오는 데 사용됩니다.


.next()`를 호출할 때마다 두 개의 키가 있는 객체를 얻습니다:



- `값`: 현재 항목
- done`: 반복이 끝났는지 여부를 알려주는 부울입니다


전체 예시를 살펴보겠습니다:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


인쇄됩니다:


```
Lina
Tom
Eva
```


이것이 `for...of` 루프가 내부적으로 작동하는 방식입니다. 이 패턴은 '.next()`와 함께 사용됩니다.


다음에서도 동일한 결과를 얻을 수 있습니다


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### 클래스 이터러블 만들기


'[Symbol.iterator]()` 메서드를 추가하여 자신만의 **이터러블 클래스**를 정의할 수도 있습니다.


1에서 5까지의 숫자 **범위를** 나타내는 클래스가 필요하다고 가정해 보겠습니다.


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


인쇄됩니다:


```
1
2
3
4
5
```


현재 상황은 다음과 같습니다:



- 범위` 클래스를 정의했습니다
- 클래스 내부에 '[Symbol.iterator]()`를 구현하여 자바스크립트가 이를 반복하는 방법을 알고 있습니다
- 다음()` 메서드는 각 숫자를 하나씩 반환합니다
- 끝`에 도달하면 `{ done: true }`를 반환합니다


이제 `Range` 클래스는 배열처럼 작동하며, 이터러블을 기대하는 모든 루프에서 사용할 수 있습니다.


### 생성기 함수 및 수율


반복자를 쉽게 생성할 수 있도록 자바스크립트는 `function*` 키워드(끝에 `*`가 붙은 `함수`)와 `yield` 키워드를 사용하여 **제너레이터 함수**를 제공합니다.


해보겠습니다:


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


각 `yield`는 값을 반환하고 다음 '.next()`가 호출될 때까지 함수를 **일시 정지**합니다.


'...의'를 사용하여 생성기를 반복할 수도 있습니다:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


인쇄됩니다:


```
1
2
3
```


## 콜백을 사용한 동시성

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


지금까지의 코드는 한 번에 한 줄씩 순서대로 실행되는 **동기식** 코드였습니다. 하지만 현실에서는 시간이 걸리는 일도 있고, 기다리는 동안 프로그램 전체가 멈추는 것도 원하지 않습니다.


이 장에서는 새로운 개념을 소개하겠습니다: **동시성**이라는 새로운 개념을 소개합니다. 이 개념을 사용하면 작업이 완료되는 순서를 조작할 수 있습니다. 이는 타이머, 사용자 입력, 디스크에서 파일 읽기 등을 처리할 때 유용합니다. 자바스크립트는 동시성을 수행하기 위한 다양한 도구를 제공합니다.


### setTimeout


설정타임아웃` 함수를 사용하면 일정 시간이 경과한 후 **나중에 함수를 실행**할 수 있습니다.


예시:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


인쇄됩니다:


```
Start
End
This runs after 2 seconds
```


설정타임아웃`이 코드 중간에 나타나지만 나머지는 차단하지 않습니다. 대신 함수가 **나중에** 실행되도록 예약하고 즉시 계속 진행합니다.


'2000'은 2000밀리초(2초)를 의미합니다.

다음은 데이터 조작과 명확한 주석을 사용하여 **콜백** 및 **프로미스** 섹션을 보다 상세하고 초보자 친화적으로 재작성한 예시입니다:


### 콜백


콜백**은 다른 함수가 나중에 **호출할 수 있도록 다른 함수에 부여하는 함수에 불과합니다.


숫자를 사용한 실제 예시를 살펴보겠습니다. 숫자 목록이 있고 각 숫자를 두 배로 늘린 다음 그 결과 "두 배가 된" 배열에 함수(콜백)를 적용하고 싶지만 마치 인터넷에서 데이터를 로드하는 것처럼 느린 것을 기다리는 것처럼 약간의 지연 후에 이 작업을 수행하고 싶다고 상상해 보겠습니다.


다음은 **콜백**을 사용하여 이를 수행하는 함수입니다:


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


이 기능을 사용해 보겠습니다:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


1초 후에 인쇄됩니다:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**여기서 무슨 일이 일어나고 있나요?**


1. 두 배로 늘리려는 숫자 목록으로 '입력'을 전달합니다.

2. 또한 두 배로 늘린 후 수행할 작업을 프로그램에 알려주는 **콜백 함수**도 전달합니다.

3. DoubleNumbers` 내부에서 `setTimeout`을 사용하여 지연을 시뮬레이션한 다음 두 배로 늘리기를 수행합니다.

4. 이 작업이 완료되면 결과 "두 배가 된" 배열에서 콜백을 호출합니다.


이 기법은 효과가 있지만 그 후에 작은 숫자를 필터링한 다음 합산하는 등 **더 많은 단계**를 수행한다고 가정해 보세요. 이런 식으로 더 많은 콜백을 **중첩**해야 할 것입니다:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


이것은 읽기에 Hard이고 지저분합니다. 이 스타일을 **콜백 지옥**이라고 하며, 바로 이 문제를 해결하기 위해 `Promise`가 만들어졌습니다.


## 약속을 통한 동시성

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


'약속'은 **향후에 준비될** 값을 나타내는 내장 자바스크립트 객체입니다.


다음과 같이 약속을 만들 수 있습니다:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


새 프로미스()` 부분은 프로미스를 생성합니다.


그 안에 두 개의 매개 변수가 있는 함수를 제공합니다:



- 'resolve'는 모든 것이 성공했을 때 호출하는 함수입니다
- '거부'는 문제가 발생하면 호출하는 함수입니다


위의 예에서는 "성공했습니다!"라는 메시지와 함께 즉시 해결합니다.


### .then()


약속이 완료된 **후**에 무언가를 하려면 '.then()`을 사용합니다:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


인쇄됩니다:


```
The result is: 100
```


해결()`에 전달한 값은 `.then()` 내부의 함수에 `result`로 전송됩니다.


설정타임아웃`을 사용하여 2초가 걸리는 작업을 시뮬레이션해 보겠습니다:


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


2초간 기다린 후 인쇄됩니다:


```
Done waiting!
```


### reject()


실패하는 약속을 만들어 봅시다:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


이제 여기에 '.then()`을 사용하면 `.then()`은 성공만 처리하기 때문에 아무 일도 일어나지 않습니다.


오류를 처리하기 위해 `.catch()`를 사용합니다:


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


다음 항목만 인쇄됩니다


```
Caught an error: Something went wrong
```


Reject()`에 전달된 값은 `.catch()` 함수로 전송됩니다.


어떤 조건에 따라 **때로는 작동하고 때때로 실패하는** 약속을 만들어 보겠습니다.


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


이제 이 기능을 호출하여 두 가지 경우를 모두 처리할 수 있습니다:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


인쇄됩니다:


```
Success: Positive number
```


다른 번호로 시도해 보세요:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


인쇄됩니다:


```
Failure: Not a positive number
```


### Promise를 사용한 연쇄 연산



앞의 예제를 '약속'을 사용하여 다시 작성하면 훨씬 깔끔하게 보입니다.


먼저 두 배 함수의 새 버전을 작성해 보겠습니다. 이번에는 **약속**을 반환합니다:


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


이제 `.then()`을 사용하여 자바스크립트에게 결과를 어떻게 처리할지 지시할 수 있습니다:


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


인쇄됩니다:


```
Doubled numbers: [ 2, 4, 6 ]
```


지금까지는 콜백 버전과 동일하게 작동하지만 이제 코드를 더 쉽게 확장하고 읽을 수 있습니다.


단계를 더 추가하고 싶다고 가정해 보겠습니다:


1. 먼저, 모든 숫자를 두 배로 늘립니다

2. 그런 다음 4보다 작은 숫자를 제거합니다

3. 마지막으로, 모두 합산합니다


각 단계마다 하나의 함수를 작성할 수 있으며, 모두 프로미스를 사용합니다:


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


이제 이렇게 **연결**할 수 있습니다:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


인쇄됩니다:


```
Final result after all steps: 10
```


어떤 기능을 하는지 살펴보겠습니다:


1. doubleNumbers`는 배열을 두 배로 늘립니다: `[2, 4, 6]`

2. 필터 빅넘버`는 3 이하인 `[4, 6]`을 제거합니다

3. sumNumbers`는 나머지 숫자를 더합니다: `4 + 6 = 10`

4. 마지막으로 결과를 인쇄합니다.


각 '.then()`은 단계가 완료될 때까지 기다립니다. 따라서 중첩 없이 **작업 체인**을 구축할 수 있습니다. 이렇게 하면 코드가 더 읽기 쉽고 디버깅하기 쉬워집니다.


## 동기화/대기를 사용한 동시성

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


'약속' 체인이 콜백 지옥을 피하는 데 어떻게 도움이 되는지 살펴봤지만, 단계가 많을 때는 여전히 약간의 Hard가 발생할 수 있습니다.


이것이 바로 `async`와 `await`의 역할입니다. 이를 통해 동기식 코드처럼 보이는 비동기식 코드를 작성할 수 있으므로 이해하기 쉽습니다.


### '비동기'란 무엇인가요?


함수 앞에 `async` 키워드를 작성하면 JavaScript는 자동으로 함수의 반환값을 Promise로 래핑합니다.


기본적인 예를 살펴보겠습니다:


```javascript
async function greet() {
return "hello"
}
```


이 함수를 호출하면


```javascript
const result = greet()
console.log(result)
```


이걸 보실 수 있습니다:


```
Promise { 'hello' }
```


방금 문자열을 반환했지만 자바스크립트는 이를 프로미스로 변환합니다. 다음과 같이 '.then()`을 사용하여 실제 값을 얻을 수 있습니다:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


또는 `대기`를 사용할 수 있습니다...


### '대기'란 무엇인가요?


키워드 `await`은 자바스크립트에게 말합니다: "이 약속이 완료될 때까지 기다렸다가 결과를 알려주세요."라고 말합니다


하지만 '대기'는 비동기 함수 내에서만 사용할 수 있습니다.


Await`을 사용하여 예제를 다시 작성해 보겠습니다:


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


이제 결과를 일반 값처럼 사용할 수 있습니다.


이제 좀 더 유용한 작업을 해보겠습니다.


### 대기로 지연 시뮬레이션하기


밀리초를 인수로 받아 다른 작업을 수행하지 않고 해당 밀리초가 지나면 해결되는 간단한 'wait' 함수를 만들어 보겠습니다:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


사용해 보겠습니다:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


인쇄됩니다:


```
waiting 2 seconds...
done waiting
```


'기다림'은 "약속이 완료될 때까지 여기서 잠시 멈춘 다음 계속합니다."라고 생각할 수 있습니다


이를 통해 '.then()` 호출을 연쇄하지 않고 비동기적으로 동작하는 **탑-투-하향** 방식으로 코드를 작성할 수 있습니다.


### 데이터 대기 중


숫자를 두 배로 늘린 다음 필터링하고 합산하는 이전 예제를 다시 사용하겠습니다. 하지만 이번에는 `async`/`await`을 사용하겠습니다.


대기를 시뮬레이션하는 3개의 함수를 생성하고 Promise를 반환하겠습니다:


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


이제 이 둘을 결합하는 `async` 함수를 작성해 보겠습니다:


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


인쇄됩니다:


```
Final result: 10
```


이는 `.then()`을 연결하거나 콜백을 중첩하는 것보다 훨씬 읽기 쉽습니다.


일반적인 단계별 프로그램처럼 보이지만 여전히 비동기적으로 작동합니다.


## 비동기 이터레이터

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


이미 **이터레이터**와 배열 및 기타 이터러블 객체를 반복하기 위해 `for...of`를 사용하는 방법에 대해 배웠습니다.


하지만 반복하려는 데이터가 도착하는 데 시간이 걸린다면 어떻게 해야 할까요?


채팅의 메시지, 파일의 줄, 느린 소스의 숫자 등 **비동기적으로** 도착하는 항목에 대해 반복 작업을 하고 싶을 때가 있습니다.


이를 위해 자바스크립트는 **동기화 반복자**를 제공합니다.


### 비동기 생성기 기능


비동기 반복기를 만드는 가장 쉬운 방법은 **비동기 생성기 함수**를 사용하는 것입니다.


이렇게 작성합니다:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


일반 제너레이터와 비슷해 보이지만 그 앞에 '동기화'가 붙습니다.


이제 `for await...of`를 사용하여 값을 소비할 수 있습니다:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


인쇄됩니다:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


그렇다면 일반 발전기와의 차이점은 무엇일까요?


차이점은 이제 생성기 내부에서 'await'을 사용할 수 있다는 것입니다.


지연 도우미를 다시 만들어 보겠습니다:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


이제 **느리게** 숫자를 산출해 봅시다:


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


사용해 보세요:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### 비동기 반복기를 사용하는 이유는 무엇인가요?


비동기 반복기는 다음과 같은 경우에 유용합니다:



- 모든 값이 한꺼번에 도착하는 것은 아닙니다.
- 한 번에 하나씩, '올 때' 처리하고 싶을 것입니다.
- 약속을 사용하여 작업하고 있으며 깔끔한 방식으로 반복하고 싶습니다.


예를 들어 채팅 서버에서 메시지를 하나씩 로드하거나 대용량 파일을 한꺼번에 다운로드하려는 경우 비동기 반복기를 사용하면 지연된 데이터로 작동하는 `for` 루프를 작성할 수 있습니다.


### Symbol.asyncIterator


커스텀 클래스에서 비동기 반복기를 사용할 수도 있습니다.


다음은 지연이 있는 숫자를 생성하는 예제입니다:


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


이제 이전과 마찬가지로 `for await...of`를 사용할 수 있습니다:


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


이를 통해 비동기적으로 반복할 수 있는 오브젝트를 만들 수 있습니다


## Assignment 구문 설탕

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"구문 설탕"이란 어떤 내용을 변경하지 않고 더 짧거나 쉬운 방식으로 작성하는 것을 의미합니다. 같은 말을 더 멋지게 표현한 것입니다.


자바스크립트에는 더 깔끔하고 짧은 선언을 작성할 수 있는 몇 가지 내장된 구문 설탕이 있습니다. 이 장에서는 조건에 따라 값을 할당하고, 수학을 사용하여 변수를 업데이트하고, 배열이나 객체에서 값을 가져오고, 더 간단한 구문으로 복사하거나 결합하는 방법을 살펴봅니다.


### 삼항 연산자


자바스크립트에서는 `if...else`를 짧게 쓰는 방법인 **보조 연산자**를 사용하여 조건에 따라 값을 할당할 수 있습니다.


하는 대신:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


글을 쓸 수 있습니다:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


즉,



- IsMorning`이 참이면 `굿모닝`을 사용합니다
- 그렇지 않으면 ``안녕하세요``를 사용합니다


일반적인 형식은 다음과 같습니다:


```javascript
condition ? valueIfTrue : valueIfFalse
```


다른 표현식에서도 사용할 수 있습니다:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


간단한 의사 결정에만 사용하세요. 논리가 복잡하다면 `if...else`를 사용하세요.


### 대체 Assignment 운영자


자바스크립트에는 연산과 결합된 과제를 수행하기 위한 **바로 가기 연산자**가 있습니다.


일반적인 방법을 살펴봅시다:


```javascript
let counter = 1
counter = counter + 1
```


단축할 수 있습니다:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


가장 일반적인 것은 다음과 같습니다:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

예시:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


자체 값을 사용하여 변수를 업데이트하려는 경우에 유용합니다.


### 디스트럭처링


**구조화**를 사용하면 배열이나 객체에서 값을 꺼내 변수에 쉽게 저장할 수 있습니다.


#### 배열


있다고 가정해 보겠습니다:


```javascript
const colors = ["red", "green", "blue"]
```


하는 대신:


```javascript
const first = colors[0]
const second = colors[1]
```


할 수 있습니다:


```javascript
const [first, second] = colors
```


이렇게 할당합니다:



- 첫 번째`를 `빨간색`으로 변경
- '초'를 'Green'로 변경합니다


값을 건너뛸 수도 있습니다:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### 개체


개체에서 값을 추출할 수도 있습니다:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


프로퍼티의 이름이 원하는 변수와 다른 경우 이름을 바꿀 수 있습니다:


```javascript
const { name: username } = user
console.log(username) // Alice
```


디스트럭처링은 객체 및 배열로 작업할 때 코드를 더 깔끔하게 만듭니다.


### 구문 확산


**스프레드 구문**은 '...'을 사용하여 값을 풀거나 복사합니다.


#### 배열


배열을 복사하거나 병합할 수 있습니다:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


배열을 복제할 수도 있습니다:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### 개체


객체에서도 동일한 작업을 수행할 수 있습니다:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


값을 재정의할 수도 있습니다:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


이 기능은 원본을 변경하지 않고 개체를 업데이트할 때 매우 유용합니다.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## 노드에 도달한 방법

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


이 장에서는 JavaScript와 NodeJS에 대한 역사적 배경에 대해 알아볼 것입니다.


소프트웨어에서 역사적 맥락은 매우 중요한데, 다른 사람이 만든 도구를 사용하는 경우가 많기 때문에 과거에 다른 사람이 내린 결정에 영향을 받기 때문입니다.


이러한 결정의 이유와 우리가 사용하는 도구가 어떻게 현재와 같이 되었는지 이해하면 우리가 하고 있는 일에 대한 혼란을 조금 덜 느낄 수 있습니다.


### 자바스크립트의 기원


자바스크립트는 웹 페이지를 대화형으로 만들기 위해 고안된 간단한 언어로 시작되었습니다.


1990년대에 넷스케이프 네비게이터와 같은 웹 브라우저는 개발자가 브라우저에서 직접 실행되는 코드를 작성할 수 있도록 자바스크립트를 추가했습니다.


원래의 아이디어는 웹사이트를 만드는 핵심 언어(소위 '자바 애플릿'이라고 불리는)로 Java를 사용하고, 자바스크립트는 사소한 작업에만 사용하는 것이었습니다.


핵심 디자인은 당시 넷스케이프의 직원이었던 브렌단 아이히(Brendan Eich)가 2주도 채 안 되는 기간에 완성했습니다.


하지만 대부분의 사람들이 자바보다 자바스크립트 사용을 선호했고, 당시 자바 애플릿에는 보안 문제가 있었기 때문에 결국 자바는 옵션에서 제외되었고 자바스크립트가 웹 개발의 사실상 표준이 되었습니다.


### V8 엔진


자바스크립트는 C와 같은 컴파일된 언어와 달리 해석된 언어입니다.


컴파일된 언어로 작성된 코드는 바이너리로 변환되고, 이 바이너리는 컴퓨터의 CPU에 직접 공급됩니다.


![](assets/en/006.webp)


반면에 인터프리드 언어는 사용자 친화적인 경향이 있으며, 기계의 작동 방식('로우 레벨')보다는 인간의 사고 방식('하이 레벨')에 더 가깝기 때문에 일반적으로 코드를 실행하기 위해 가상 머신이 구축되어 있습니다.


가상 머신은 사용자가 작성한 코드와 CPU 사이에 위치하여 코드를 실행하는 특수 프로그램입니다(CPU는 코드를 이해할 수 없으므로).


이렇게 하면 기본 머신에 대해 잘 몰라도 프로그래밍할 수 있지만 컴퓨터가 사용자 프로그램만 실행하는 것이 아니라 프로그램을 실행하는 프로그램(가상 머신)을 실행하기 때문에 성능 측면에서 비용이 발생합니다.


웹 애플리케이션이 점점 더 복잡해짐에 따라 자바스크립트의 성능을 개선해야 한다는 요구가 있었습니다. V8 엔진은 구글 크롬에서 자바스크립트를 구동하는 인터프리터입니다. Google에서 개발되어 2008년에 출시되었습니다.


이전 자바스크립트 엔진은 대부분 전통적인 가상 머신이었던 반면, V8 엔진은 JIT(Just-In-Time) 컴파일러입니다.


자바스크립트 코드는 V8 엔진에 공급되고 엔진은 그 일부를 네이티브 바이너리로 즉시 컴파일하려고 시도합니다. 이를 통해 로우레벨 언어에 조금 더 가까운 성능으로 하이레벨 언어의 경험을 할 수 있습니다. 이 덕분에 자바스크립트는 세계에서 가장 빠른 하이레벨 언어가 되었으며, '두 마리 토끼'를 모두 잡은 셈이죠.


### NodeJS 런타임


사용하기 쉽고 실행 속도가 매우 빠르지만, V8 자바스크립트는 출시 이후 브라우저 내에서만 실행할 수 있다는 큰 한계를 안고 있었습니다.


그게 왜 문제인가요?


브라우저는 인터넷의 수백만 가지 소스에서 가져온 코드를 실행하기 때문에 멀웨어에 쉽게 감염될 수 있으므로 나머지 운영 체제로부터 '샌드박스'됩니다.


![](assets/en/007.webp)


자바스크립트는 컴퓨터의 파일 시스템과 기타 로컬 리소스에 액세스할 수 없었기 때문에(적어도 다른 언어처럼 쉽게 액세스할 수 있는 것은 아니었습니다), 자바스크립트로 만들 수 있는 애플리케이션의 종류에 상당한 제한이 있었습니다.


2009년 Ryan Dahl은 브라우저 외부에서 컴퓨터의 기본 운영체제에서 직접 V8 엔진을 사용할 수 있는 런타임인 NodeJS를 발표했습니다. 또한 서버 측 및 명령줄 프로그램을 작성하는 데 유용한 많은 기능을 추가했습니다. 예를 들어 NodeJS를 사용하여 웹 서버를 만들고, 파일을 읽고 쓰거나, 작업을 자동화하는 도구를 만들 수 있습니다.


![](assets/en/008.webp)


지금까지 이 강좌에서는 브라우저와 NodeJS에 모두 존재하는 자바스크립트 기능을 살펴보았습니다. 이러한 기능을 통해 데이터를 정의하고 추상적인 방식으로 데이터를 조작할 수 있었습니다. 다음 몇 개의 강의에서는 운영 체제와 상호 작용할 수 있는 NodeJS 전용 기능을 살펴보겠습니다.


## 명령줄 인수

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS를 사용하면 무엇보다도 CLI(명령줄 인터페이스)를 구축할 수 있습니다.


이를 위해서는 명령줄 인수를 받는 방법이 필요한데, Node에서는 내장된 `process` 객체를 사용하여 이를 수행합니다.


### 프로세스


NodeJS는 현재 실행 중인 프로그램을 나타내는 '프로세스'라는 특수 객체를 제공합니다.


이를 사용하여 환경과 현재 작업 디렉터리를 검사하고 필요한 경우 프로그램을 종료할 수도 있습니다.


예를 들어


```javascript
console.log(process.platform)
```


이것은 `win32`, `linux` 또는 `darwin`(Mac)과 같은 운영 체제 플랫폼을 인쇄합니다.


### process.argv


터미널에서 NodeJS 프로그램을 실행할 때 스크립트 이름 뒤에 추가 단어(인수)를 전달할 수 있습니다. 이러한 인수는 `process.argv`에 저장됩니다.


예를 들어 다음 명령을 실행하면 됩니다:


```
node my_script.js alpha beta
```


인수를 다음과 같이 인쇄할 수 있습니다:


```javascript
console.log(process.argv)
```


출력은 다음과 같이 표시될 수 있습니다:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


처음 두 항목은 항상 노드 경로와 스크립트 경로입니다. 스크립트에 전달한 모든 추가 단어는 그 뒤에옵니다.


Process.argv` 배열은 '.slice()` 메서드를 사용하여 다른 배열처럼 잘라낼 수 있으므로 전달된 인자만 가져오려면 다음을 수행하면 됩니다


```javascript
const args = process.argv.slice(2)

console.log(args)
```


사용자가 전달하는 인수에 액세스하는 것은 명령줄 애플리케이션을 개발하는 데 있어 기본입니다.


## 모듈

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


NodeJS와 같은 자바스크립트 런타임은 일반적으로 각 자바스크립트 파일을 별도의 모듈로 취급합니다.


모듈을 상자로 생각하세요. 상자에는 고유한 개인 공간이 있으므로 그 안에 선언한 변수와 함수는 다른 상자에 있는 코드를 방해하지 않습니다. 기본적으로 각 모듈에는 고유한 범위가 있습니다.


모듈은 콘텐츠의 일부를 내보내 다른 모듈에서 사용할 수 있도록 하고, 다른 모듈이 내보낸 콘텐츠를 가져올 수 있습니다. JavaScript를 사용하면 모듈 간에 콘텐츠를 내보내고 가져와서 서로 다른 파일을 연결할 수 있습니다.


자바스크립트 프로그램은 서로 연결된 여러 모듈로 구성되는 경우가 많습니다.


모듈을 사용하는 이유는 무엇인가요? 코드를 모듈로 나누면 프로그램을 더 작고 명확하며 재사용 가능한 부분으로 구성할 수 있습니다. 각 모듈은 수학 계산 처리, 파일 작업, 텍스트 서식 지정 등 한 가지 유형의 작업에만 집중할 수 있습니다.


### CommonJS 모듈


NodeJS에서 모듈을 관리하는 가장 일반적인 시스템은 **CommonJS**라고 합니다.


이 시스템에서는 `module.exports`를 사용하여 모듈에서 코드를 공유(내보내기)하고 `require()`를 사용하여 다른 파일에서 로드(가져오기)할 수 있습니다.


모듈 외부에서 무언가를 사용할 수 있게 하려면 `module.exports`에 할당하면 됩니다:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


여기서 `"Hello!"` 문자열은 이 모듈이 내보내는 문자열입니다.


다른 파일에서 내보낸 코드를 사용하려면 해당 파일의 경로와 함께 `require()` 함수를 사용합니다:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


인쇄됩니다:


```
Hello!
```


다음과 같이 익명 개체에 여러 개를 함께 묶어 내보낼 수 있습니다


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS는 NodeJS에서 처음 채택한 모듈 시스템입니다. 나중에 ES 모듈도 추가되었습니다.


### ES 모듈


NodeJS는 웹 개발에서 널리 사용되는 **ES 모듈**이라는 또 다른 유형의 모듈도 지원합니다. 이 모듈은 'export'와 'import'라는 키워드를 사용합니다.


ES 모듈은 브라우저용으로 개발되었으며 나중에 Node에 추가되었습니다. 이 모듈을 사용하려면 사용 중인 Node 버전에 따라 파일 확장자로 '.js' 대신 '.mjs'를 사용해야 할 수도 있습니다.


Greeting.mjs`라는 파일 하나에 다음과 같이 작성합니다


```javascript
export const greeting = "Hello!"
```

보시다시피, 상수가 정의되는 곳에서 직접 상수를 내보내고 있습니다


'index.mjs'라는 다른 파일에서 이 파일을 가져옵니다:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


다음과 같이 파일의 다른 부분에 다른 선언을 내보낼 수 있습니다


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### NodeJS 표준 라이브러리


NodeJS에는 많은 기본 제공 모듈도 포함되어 있습니다. 이러한 모듈은 파일 읽기, 운영 체제 작업 또는 네트워크 연결과 같은 일반적인 작업에 도움이 되는 NodeJS에서 제공하는 기성품 모듈입니다.


예를 들어 `os` 모듈은 운영 체제에 대한 정보를 제공합니다:


```javascript
const os = require("os")

console.log(os.platform())
```


이러한 내장 모듈을 설치할 필요는 없으며, NodeJS와 함께 제공됩니다. 이러한 모듈은 런타임의 '표준 라이브러리'를 구성하며 대부분의 Node 애플리케이션에서 파일 읽기나 인터넷을 통한 통신과 같은 작업을 수행하는 데 사용됩니다.


다음 장에서는 몇 가지 유용한 사용 예시를 보여드리겠습니다.


## F 모듈

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


F` 모듈(**파일 시스템**의 줄임말)은 NodeJS 표준 라이브러리의 일부입니다. 이를 통해 컴퓨터의 파일 및 디렉터리로 파일 읽기, 파일 쓰기, 삭제, 이름 바꾸기 등의 작업을 할 수 있습니다.


이 기능을 사용하려면 먼저 파일 상단에서 파일을 가져와야 합니다:


```javascript
const fs = require("fs")
```


### 동기화 API


F`를 사용하는 가장 간단한 방법은 **sync** 메서드를 사용하는 것입니다.


이러한 메서드는 프로그램이 완료될 때까지 프로그램을 차단합니다(따라서 다음 코드 줄은 작업이 완료될 때까지 실행되지 않습니다).


다음은 파일을 동기식으로 읽는 예제입니다:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


스크립트와 같은 디렉터리에 'example.txt'라는 파일이 있으면 그 내용을 인쇄합니다.


파일에 동기식으로 쓸 수도 있습니다:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


그러면 텍스트가 포함된 'output.txt'라는 파일이 생성(또는 덮어쓰기)됩니다.


다음은 이 API로 수행할 수 있는 몇 가지 일반적인 작업입니다:


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


동기화 API는 간단하고 작은 스크립트에는 좋지만, 완료될 때까지 프로그램을 차단하기 때문에 대용량 파일이나 서버로 작업하는 경우 속도가 느려질 수 있습니다.


### 콜백 비동기 API


콜백 API는 비차단 방식으로, 파일 작업이 진행되는 동안 NodeJS가 다른 작업을 계속할 수 있게 해줍니다.


결과를 직접 반환하는 대신 연산이 완료되면 호출되는 함수(**콜백**)를 사용합니다.


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


이렇게 진행됩니다:



- fs.readFile`이 `example.txt`를 읽기 시작합니다.
- NodeJS는 기다리지 않고 사용자가 작성한 다른 코드를 실행하기 위해 이동합니다.
- 파일 읽기가 완료되면 콜백이 실행됩니다:



  - 오류가 발생하면 `err`에 오류가 포함됩니다.
  - 그렇지 않으면 `데이터`에 내용이 포함됩니다.


파일에 쓰는 방법은 다음과 같습니다:


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


같은 아이디어: 파일을 쓰는 동안 프로그램이 멈추지 않습니다.


이 API로 수행할 수 있는 작업의 몇 가지 예입니다:


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


콜백 API는 프로그램을 차단하지 않기 때문에 서버나 대규모 작업에 더 적합하지만, 중첩된 콜백은 많은 작업을 연결하면 지저분해질 수 있습니다. 그래서 프로미스 기반 비동기 API가 추가되었습니다.


### 프로미스 비동기 API


약속 기반 API는 최신이며 '.then()` 및 `async/await`과 함께 잘 작동합니다. 이는 `fs.promises`로 사용할 수 있습니다.


'약속' 속성을 가져와야 합니다:


```javascript
const fs = require("fs").promises
```


.then()`을 사용합니다:


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


또는 `async/await`을 사용하는 것이 더 좋습니다:


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


파일에 쓰기:


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


API의 일반적인 예제 목록입니다:


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


코드를 작성할 때 다른 사람이 작성한 코드, 예를 들어 날짜, 색상, 서버 또는 거의 모든 작업을 도와주는 라이브러리를 사용해야 하는 경우가 많습니다.


파일을 수동으로 다운로드하고 복사하는 대신 **패키지 관리자**를 사용할 수 있습니다.


패키지 관리자는 도구입니다:



- 패키지 다운로드
- 프로젝트에 필요한 패키지를 추적합니다
- 팀원 모두가 동일한 버전의 패키지를 가지고 있는지 확인합니다


### NPM이란?


NodeJS 세계에서 가장 많이 사용되는 패키지 관리자는 *Node Package Manager*의 약자인 **NPM**입니다.


NodeJS를 설치하면 자동으로 NPM이 제공됩니다.


터미널에서 실행하여 NPM이 있는지 확인할 수 있습니다:


```
npm -v
```


현재 사용 중인 NPM 버전이 인쇄됩니다:


```
10.2.1
```


### 패키지 만들기


NodeJS에서 **패키지**는 `package.json` 파일이 있는 디렉터리일 뿐입니다.


단계별로 하나씩 만들어 보겠습니다.


1. 프로젝트를 위한 새 폴더를 만듭니다:


```
mkdir my_project
cd my_project
```


2. 이 명령을 실행합니다:


```
npm init
```


그러면 프로젝트 이름, 버전, 설명 등과 같은 질문을 묻는 대화형 설정이 시작됩니다.


모든 항목에 답변하고 싶지 않고 기본값만 수락하고 싶다면 다음을 사용할 수 있습니다:


```
npm init -y
```


실행하면 폴더에 새 파일이 표시됩니다:


```
package.json
```


### package.json


Package.json` 파일은 프로젝트에 대한 메타데이터를 저장하는 JSON 파일일 뿐입니다.


다음은 한 가지 예입니다:


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


몇 가지 중요한 필드입니다:



- 이름`: 패키지 이름
- 버전`: 현재 버전
- 메인`: 엔트리 포인트 파일(예: `index.js`)
- 스크립트`: 실행할 수 있는 명령(예: `npm start`)
- 의존성`: 프로젝트가 의존하는 모든 패키지를 나열합니다


### 패키지 설치하기


터미널 출력에 색상을 추가하기 위해 `picocolors`라는 특정 패키지를 사용한다고 가정해 보겠습니다.


실행하여 설치할 수 있습니다:


```
npm install picocolors
```


이제 프로젝트에서 사용할 수 있습니다. 다음을 사용하여 `index.js` 파일을 만듭니다


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


를 클릭하고 실행해 보세요. 터미널에서 컬러 버전의 텍스트가 인쇄되어야 합니다.


NPM은 무엇을 했나요?



- 패키지를 다운로드하여 `node_modules/`라는 하위 폴더에 저장했습니다
- package.json`의 `dependencies` 아래에 항목을 추가했습니다
- 패키지 잠금` 파일을 업데이트했습니다


Package-lock.json`이란 무엇인가요?


### package-lock.json


이 파일은 NPM에 의해 자동으로 생성됩니다.


이미 `package.json`이 있는데 왜 또 다른 파일이 필요한지 궁금할 수 있습니다

그 이유는 다음과 같습니다:



- package.json`은 프로젝트에 필요한 패키지의 **범위** 버전만 알려줍니다.

예시:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


1.1.0`은 "1.1.x와 호환되는 모든 버전"을 의미하므로 유연하게 사용할 수 있습니다.



- package-lock.json`은 모든 단일 패키지와 그 하위 종속 요소의 정확한 버전을 **동결**하여 프로젝트를 설치하는 모든 사람이 정확히 동일한 작업 설정을 갖도록 합니다.


이것이 왜 중요한가요?


팀에서 작업하거나 프로젝트를 서버에 배포하거나 나중에 다시 돌아와서 작업하는 경우에도 동일한 방식으로 작동하는지 확인하고 싶을 것입니다.

패키지가 업데이트되었는데 잠금 파일 없이 다시 설치하면 약간 다른 버전이 나타나서 다르게 작동할 수 있습니다.


프로젝트에 `package-lock.json`을 유지하면 NPM은 항상 여기에 나열된 정확한 버전을 설치하여 모든 사람이 동일한 환경을 갖도록 합니다.


package-lock.json`은 모든 것을 매우 특정한 버전으로 잠가 다른 컴퓨터에서 프로젝트를 더 쉽게 재현할 수 있도록 합니다.


그러나 많은 사람이 패키지를 사용해야 하는 경우, 대신 커밋하지 않도록 선택하여 NPM이 `package.json` 파일만 찾고 해당 파일에 허용된 최신 버전을 자동으로 설치하도록 할 수 있습니다.


하지만 이러한 부분은 나중에 코드를 직접 게시하기 시작하면 걱정해야 할 부분입니다. 지금은 프로젝트에서 다른 개발자가 게시한 라이브러리를 찾아서 사용할 수 있도록 NPM의 기본 사항만 소개했습니다.



## NodeJS의 네트워킹

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


스크립트를 서버로 전환하고 다른 서버에 요청하는 데도 사용할 수 있는 백엔드 언어로 NodeJS가 자주 사용됩니다.


이 장에서는 이를 가능하게 하는 몇 가지 기본적인 네트워킹 기능을 소개합니다.


### fetch()


프로그램에서 웹사이트나 API에서 데이터를 다운로드하려면 **HTTP 요청**을 해야 합니다.


최신 버전의 NodeJS에서는 내장된 `fetch()` 함수를 사용할 수 있습니다.


다음은 API에 GET 요청을 하는 예제입니다:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


이를 실행하면 다음과 같은 내용이 표시됩니다:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


다음과 같은 일이 발생합니다:


1. fetch()`는 URL을 받아 요청을 합니다.

2. '응답' 객체로 해석되는 **Promise**를 반환합니다.

3. response.text()`는 응답 본문을 문자열로 읽습니다.


하지만 실제로 반환되는 문자열은 JSON입니다. 그게 뭔가요?


### JSON


웹 API로 작업할 때 데이터는 JavaScript 객체 표기법을 의미하는 **JSON**으로 송수신되는 경우가 많습니다.


JSON은 JavaScript 객체와 매우 유사한 텍스트 형식입니다. 예를 들어


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


JSON` 객체는 이 데이터 형식으로 작업하는 데 사용할 수 있는 JavaScript의 내장 유틸리티입니다.


JSON.stringify()`를 사용하여 JavaScript 객체를 JSON 문자열로 변환할 수 있습니다:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


인쇄됩니다:


```
{"name":"Alice","age":30}
```


JSON.parse()`를 사용하여 JSON 텍스트를 자바스크립트 객체로 다시 변환할 수도 있습니다:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


인쇄됩니다:


```
{ name: 'Bob', age: 25 }
```


주의하세요: 문자열이 유효한 JSON이 아닌 경우 `JSON.parse()`는 오류를 발생시킵니다.


```javascript
JSON.parse("not json") // ❌ Error!
```


따라서 문자열의 형식이 올바른지 확인하세요.


### http 서버


NodeJS를 사용하면 다른 것을 설치하지 않고도 웹 서버를 만들 수 있습니다.


기본 제공 `http` 모듈을 사용하여 클라이언트의 요청을 처리하고 응답을 다시 보낼 수 있습니다.


다음은 아주 기본적인 예입니다:


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


이 스크립트를 실행하고 브라우저에서 `http://localhost:3000`을 열면 다음과 같은 내용을 확인할 수 있습니다:


```
Hello from NodeJS server!
```


이것이 코드에서 일어나는 일입니다:


1. 노드 표준 라이브러리에서 `http` 서버를 가져왔습니다.

2. http.createServer()`는 서버를 생성합니다. 누군가 연결할 때마다 실행되도록 콜백 `(req, res) => {...}`을 `http.createServer()`에 전달했습니다.

3. 응답에 상태 코드 200(성공적인 작업을 나타냄)을 할당했습니다. Http 상태 코드에 대한 자세한 내용은 [여기](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)에서 확인할 수 있습니다

3. res.end()`는 응답을 전송하고 연결을 종료합니다.

4. server.listen(3000)`은 포트 3000에서 서버를 시작합니다.


요청에서 `req.url` 및 `req.method`를 확인하여 다른 경로 또는 요청 유형을 처리할 수도 있습니다.


라우팅의 예입니다:


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


이는 매우 기본적인 예시입니다. 더 고급 서버를 구축하려면 대부분의 개발자는 [express](https://www.npmjs.com/package/express)와 같은 기성 백엔드 라이브러리를 다운로드할 것입니다.


## 데이터 처리: 버퍼, 이벤트, 스트림

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


이 장에서는 주로 세 가지 클래스의 오브젝트를 소개합니다:



- 작은 바이너리 데이터 청크를 나타내는 '버퍼'
- "이벤트"라는 신호를 방출하여 비동기 프로세스로 썸스텝을 추적하는 데 사용할 수 있는 '이벤트이미터'입니다
- 한 번에 하나의 '버퍼'로 대량의 데이터를 처리할 수 있고 이벤트를 발생시켜 프로세스를 추적하는 '스트림'입니다


이들은 전문 NodeJS 코드에서 매우 일반적이므로 첫 번째 프로젝트에서 사용하지 않더라도 언제 상호 작용해야 하는지에 대한 기본적인 이해를 하는 것이 좋습니다


### 버퍼


NodeJS에서 **버퍼**는 이진 데이터로 작업하는 데 사용되는 객체 유형입니다.


버퍼는 원시 바이트를 저장하는 고정 크기 컨테이너라고 생각하면 됩니다.


문자열로 버퍼를 만드는 방법은 다음과 같습니다:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


다음과 같은 내용이 인쇄됩니다:


```
<Buffer 68 65 6c 6c 6f>
```


이러한 숫자(`68`, `65`, `6c` 등)는 `"hello"`의 문자를 16진수로 표현한 것입니다.


다음과 같이 문자열로 다시 변환할 수 있습니다:


```javascript
console.log(buf.toString())
```


인쇄됩니다:


```
hello
```


0으로 채워진 특정 크기의 버퍼를 만들 수도 있습니다:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


다음과 같은 내용이 인쇄됩니다:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


버퍼에 쓸 수 있습니다:


```javascript
buf.write("abc")
console.log(buf)
```


그리고 개별 바이트에 액세스할 수 있습니다:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


버퍼는 매우 낮은 수준에서 데이터를 조작해야 할 때 특히 유용합니다.


### 이벤트


자바스크립트에서 **이벤트**는 프로그램에서 반응할 수 있는 어떤 일을 의미합니다.


예를 들어



- 파일 로딩이 완료됩니다
- 타이머가 울립니다
- 사용자가 버튼을 클릭하는 경우
- 네트워크 요청이 데이터를 반환합니다


이벤트**는 어떤 일이 발생했다는 신호이며, 이러한 이벤트를 수신하고 이에 반응하는 코드를 작성할 수 있습니다.


NodeJS에서는 많은 객체가 이벤트를 방출할 수 있습니다. 이러한 객체를 **EventEmitters**라고 합니다.


다음은 한 가지 예입니다:


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


인쇄됩니다:


```
Hello! An event happened.
```


자세한 내용은 다음과 같습니다:


1. 이벤트 이미터` 객체를 생성합니다.

2. .on("greet")`을 사용하여 `"greet"` 이벤트가 발생할 때마다 콜백을 실행하도록 지시합니다.

3. 나중에 `.emit()`을 사용하여 `"greet"` 이벤트를 트리거합니다.

4. 콜백이 실행됩니다


이벤트와 함께 데이터를 전달할 수 있습니다:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


인쇄됩니다:


```
Hello, Alice!
```


다른 이벤트에도 청취자를 등록할 수 있습니다:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


이벤트 유형에 원하는 만큼 많은 리스너를 연결할 수 있으며, 동일한 이미터에서 다양한 유형의 이벤트를 실행할 수 있습니다.


NodeJS의 많은 객체는 이벤트를 방출하여 프로그램의 나머지 부분에 어떤 일이 발생하고 있음을 알립니다.



### 스트림이란 무엇인가요?


스트림은 버퍼와 이벤트를 결합하여 데이터를 처리하는 데 도움을 줍니다.


파일, 네트워크의 데이터, 심지어 긴 텍스트로 작업할 때 모든 것을 한꺼번에 메모리에 로드할 필요는 없습니다(또는 원하지도 않습니다). 그러면 속도가 느려지거나 데이터가 너무 크면 프로그램이 충돌할 수도 있습니다.


대신, 한 번에 잔 전체를 마시지 않고 빨대를 통해 물을 마시는 것처럼 데이터가 도착하거나 읽혀질 때마다 **조금씩** 처리할 수 있습니다. 이를 **스트림**이라고 합니다.


NodeJS에서 스트림은 소스에서 데이터를 읽거나 대상에 데이터를 **한 번에 하나씩** 쓸 수 있는 객체입니다.


NodeJS에는 네 가지 주요 스트림 유형이 있습니다:



- **읽기 가능**: 데이터를 읽을 수 있는 스트림(예: 파일 읽기)
- **쓰기 가능**: 데이터를 쓸 수 있는 스트림(예: 파일에 쓰기)
- **이중화**: 읽기 및 쓰기가 모두 가능한 스트림
- **변환**: 양방향 스트림과 비슷하지만 데이터가 흐르면서 데이터를 변경(변환)할 수 있습니다


### 읽을 수 있는 스트림


처리해야 할 `bigfile.txt`가 있다고 가정해 봅시다. F` 모듈로 읽을 수 있는 스트림을 생성하여 파일을 하나씩 읽을 수 있습니다.


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


여기서 무슨 일이 일어나나요?


1. fs.createReadStream()`은 읽기 가능한 스트림을 생성합니다.

2. 파일의 일부가 준비될 때마다 스트림은 `데이터` 이벤트를 발생시키고 데이터의 "청크"('버퍼')를 제공합니다. 청크를 인쇄합니다.

3. 전체 파일을 읽으면 '종료' 이벤트가 트리거됩니다.

4. 파일이 존재하지 않는 등의 오류가 발생하면 '오류' 이벤트가 트리거됩니다.


이렇게 하면 대용량 파일을 한 번에 모두 메모리에 로드하지 않고도 읽을 수 있습니다.


데이터가 바이너리가 아닌 사람이 읽을 수 있는 형태로 도착하도록 하려면 스트림의 인코딩을 지정하면 됩니다:


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


이제 코드가 사람이 읽을 수 있는 형식으로 파일을 인쇄합니다.


### 쓰기 가능한 스트림


쓰기 가능한 스트림을 사용하면 데이터를 청크 단위로 어딘가로 전송할 수 있습니다.


다음은 스트림을 사용하여 `target.txt` 파일에 쓰는 예제입니다:


```javascript
const fs = require("fs");

const stream = fs.createWriteStream("target.txt");

stream.on("error", (err) => {
  console.error("Error:", err);
});

stream.on("finish", () => {
  console.log("All data written.");
});

stream.write("First line\n");
stream.write("Second line\n");
stream.end("Finished writing\n");
```


이렇게 진행됩니다:


1. `fs.createWriteStream()`은 쓰기 가능한 스트림을 생성합니다.

2. `error` 및 `finish` 이벤트에 대한 핸들러를 등록합니다.

3. `.write()`를 사용하여 텍스트를 작성합니다.

4. 작업이 끝나면 `.end()`를 호출하여 스트림을 닫습니다.

5. 버퍼링된 모든 데이터가 플러시되고 기록되면 `finish` 이벤트가 발생합니다. 문제가 발생하면 `error` 이벤트가 발생합니다.


읽기 가능한 스트림과 마찬가지로 쓰기 가능한 스트림은 모든 것을 한꺼번에 메모리에 저장할 필요가 없기 때문에 빅데이터에 적합합니다.


### 파이핑 스트림


스트림의 가장 멋진 점 중 하나는 읽기 가능한 스트림을 쓰기 가능한 스트림에 직접 연결하여 서로 '파이프'할 수 있다는 점입니다.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


여기:



- 읽을 수 있는 스트림은 `bigfile.txt`에서 읽습니다.
- 쓰기 가능한 스트림은 `copy.txt`에 씁니다.
- .pipe()`는 읽기 가능한 스트림에서 쓰기 가능한 스트림으로 데이터를 직접 전송합니다.


### 이중 스트림


듀플렉스 스트림은 읽기 및 쓰기가 모두 가능합니다. 한 가지 예로 네트워크 소켓을 들 수 있는데, 이 소켓으로 데이터를 보내고 데이터를 받을 수 있습니다.


다음은 `net` 모듈을 사용하는 매우 간단한 예제입니다:


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


이 예제에서는



- 소켓` 객체는 이중 스트림입니다.
- 여기에 `쓰기()`를 할 수 있고 `데이터` 이벤트를 수신할 수도 있습니다.


### 스트림 변환


트랜스폼 스트림은 양방향 스트림으로, 이를 통과하는 데이터도 수정합니다.


예를 들어 내장된 `zlib` 모듈을 사용하여 데이터를 압축하거나 압축 해제할 수 있습니다.


트랜스폼 스트림을 사용하여 파일을 압축하는 방법은 다음과 같습니다:


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


그리고 다시 압축을 해제합니다:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


트랜스폼 스트림은 스트리밍 중 압축, 암호화 또는 파일 형식 변경과 같은 작업에 매우 유용합니다.


### 역압


쓰기 가능한 스트림이 데이터를 처리하는 속도가 느릴 때가 있습니다. 쓰기 가능한 스트림이 처리할 수 있는 속도보다 빠르게 데이터를 계속 밀어 넣으면 문제가 발생할 수 있습니다. 이를 **백프레셔**라고 합니다.


쓰기 가능한 스트림에서 `.write()` 메서드를 호출하면 스트림에 일시 중지가 필요한지 여부를 알려주는 부울을 반환하므로 다음과 같이 반환값을 확인해야 할 수 있습니다:


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


이것은 데이터를 읽기 가능에서 쓰기 가능으로 수동으로 파이핑하고 배압을 수동으로 관리하는 예시입니다.


일반적으로는 자동으로 역압을 처리하는 `.pipe()` 메서드를 사용하여 데이터를 파이프합니다.


따라서 어떤 이유로 `.write()`를 수동으로 호출할 때만 역압에 대해 걱정할 필요가 있습니다.


## 최종 참고 사항

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


지금까지 수업을 잘 따라가셨다면 이제 NodeJS로 간단한 프로그램을 작성할 수 있을 것입니다.


기본을 배운 후 몇 가지 개인 프로젝트를 만들어보는 것이 연습을 통해 더 나은 프로그래머가 될 수 있는 가장 좋은 방법입니다.


무엇을 만들지는 중요하지 않으며, 중요한 것은 코드로 문제를 해결하기 위해 도전하는 것입니다.


최신 프로그래밍 언어는 놀라울 정도로 강력하며, NodeJS는 이 단계에서 실험하기에 가장 좋은 툴박스일 것입니다.


행운을 빕니다!


# 마지막 섹션


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## 리뷰 및 평가


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## 결론


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>