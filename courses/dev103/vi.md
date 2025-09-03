---
name: Cơ bản về JavaScript và NodeJS
goal: Tìm hiểu những kiến thức cơ bản về lập trình JavaScript và phát triển NodeJS để xây dựng các ứng dụng và công cụ thực tế.
objectives: 

  - Nắm vững cú pháp JavaScript cơ bản, các kiểu dữ liệu và luồng điều khiển
  - Hiểu các hàm, đối tượng và lớp trong JavaScript
  - Học các kỹ thuật xử lý lỗi và gỡ lỗi
  - Làm quen với NodeJS và hệ sinh thái của nó

---

# Bắt đầu hành trình phát triển của bạn


Chào mừng bạn đến với khóa học về JavaScript và NodeJS.


JavaScript là ngôn ngữ lập trình phổ biến nhất trên thế giới: đây là ngôn ngữ kịch bản của các trình duyệt hiện đại, do đó về cơ bản không thể xây dựng một ứng dụng web hiện đại mà không viết *một số* JavaScript; và với NodeJS runtime, nó cũng có thể được sử dụng bên ngoài trình duyệt để tạo các kịch bản và ứng dụng chạy trực tiếp trên máy tính của bạn.


Khóa học này được thiết kế dành cho những người hoàn toàn mới làm quen với lập trình hoặc đã sử dụng ngôn ngữ khác nhưng muốn hiểu cách JavaScript hoạt động, đặc biệt là trong bối cảnh của NodeJS.


Đến cuối khóa học, bạn sẽ có thể viết chương trình của riêng mình bằng JavaScript, sử dụng thư viện chuẩn NodeJS và cài đặt cũng như sử dụng các gói của bên thứ ba để xây dựng các công cụ hữu ích.


+++
# JavaScript cơ bản

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Cài đặt

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>


Trong phần này, chúng ta sẽ thiết lập máy để viết và thực thi chương trình JavaScript đầu tiên.


Một chương trình JavaScript chỉ là một tập hợp (một hoặc nhiều) tệp văn bản chứa các lệnh được thực thi bởi thời gian chạy JavaScript.


Tên của các tệp văn bản này thường kết thúc bằng phần mở rộng tệp `.js`, như `my_script.js`, `my_program.js`, v.v.


Các lệnh chứa trong đó được viết bằng ngôn ngữ lập trình JavaScript.


Thời gian chạy JavaScript là một chương trình đặc biệt thực thi các tệp này.


![](assets/en/1.webp)


### Cài đặt NodeJS


Môi trường chạy JavaScript phổ biến nhất là NodeJS.


Bạn có thể cài đặt bằng cách làm theo [hướng dẫn chính thức](https://nodejs.org/en/download).


Trang tải xuống sẽ cung cấp cho bạn hướng dẫn cho cả ba hệ điều hành chính: Windows, Linux và MacOS. Trang này giả định rằng bạn đã biết cách mở terminal trên hệ điều hành của mình.


Vì NodeJS có sẵn cho cả ba hệ điều hành nên các chương trình bạn viết sẽ có thể chạy trên tất cả các hệ điều hành đó (trừ một số trường hợp ngoại lệ).


Điều này có nghĩa là bạn có thể viết một trò chơi điện tử đơn giản bằng JavaScript trên máy tính Windows của mình và chuyển cho bạn bè chạy trên máy Mac của họ.


![](assets/en/2.webp)


### Chỉnh sửa văn bản


Một trong những điều thú vị về lập trình là bạn có thể viết mã bằng bất kỳ trình soạn thảo văn bản nào, thậm chí là notepad mặc định của hệ điều hành bạn đang sử dụng.


Tuy nhiên, có một số trình soạn thảo văn bản chuyên dùng để viết mã, một số miễn phí, một số khác yêu cầu bạn phải trả phí cấp phép.


Việc lựa chọn trình soạn thảo mã là một vấn đề nan giải vượt quá phạm vi của khóa học này, vì vậy chúng ta sẽ không bàn về nó ở đây. Nếu bạn không biết nên dùng trình soạn thảo nào, trình soạn thảo miễn phí được sử dụng nhiều nhất là [VSCode](https://code.visualstudio.com/).


Interface của nó hơi cồng kềnh, nhưng nó có những gì bạn cần: trình soạn thảo tệp, trình duyệt tệp (để trực quan hóa các tệp và thư mục con trong thư mục bạn đang làm việc) và một thiết bị đầu cuối để chạy mã. Nó cũng hỗ trợ rất nhiều plugin và mặc định có tính năng tô sáng cú pháp JavaScript.


Nếu bạn muốn có nhiều Cypherpunk hơn một chút, bạn có thể sử dụng [VSCodium](https://vscodium.com/) thay thế.


### Chương trình đầu tiên (xin chào thế giới)


Theo truyền thống, khi học một ngôn ngữ lập trình, chương trình đầu tiên mà người ta viết là in dòng chữ "hello world!" ra màn hình điều khiển.


Tạo một thư mục có tên `my_js_code/`, bên trong có một tệp có tên `main.js` (những tên này là tùy ý).


Mở thư mục bằng VSCode.


Viết mã này vào tệp của bạn:


```javascript
console.log("hello world!")
```


Mở terminal và thực hiện lệnh này để chạy chương trình:


```
node main.js
```


Kết quả phải là


```
hello world!
```


### Chuyện gì đã xảy ra thế


Trong JavaScript, mọi thứ đều là "đối tượng".


`console` là một đối tượng được sử dụng để gỡ lỗi chương trình.


`console.log` là phương thức được sử dụng nhiều nhất của `console`. Nó chỉ in ra bất kỳ đối số nào bạn truyền vào.


Bạn truyền đối số cho `console.log` bằng cách sử dụng dấu ngoặc tròn `()`.


Vì vậy, ví dụ, nếu bạn muốn in số `1000`, bạn chỉ cần viết


```javascript
console.log(1000)
```


Sau đó thực hiện nó bằng cách chạy


```
node main.js
```


trong thiết bị đầu cuối của bạn (từ bây giờ, khóa học này sẽ mặc định rằng bạn biết cách thực thi chương trình).


Điều này sẽ in


```
1000
```


Bạn có thể truyền nhiều thứ, như


```javascript
console.log(16, 8, 1993)
```


Điều này sẽ in


```
16 8 1993
```


## Biến và chú thích

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Các chương trình thường thực hiện các thao tác trên dữ liệu.


Biến giống như các hộp được đặt tên mà chúng ta sử dụng để lưu trữ dữ liệu. Chúng cho phép chúng ta liên kết một phần dữ liệu với một tên cụ thể, để sau này có thể truy xuất dữ liệu bằng tên đó.


### khai báo `let`


Để khai báo một biến trong JavaScript, chúng ta có thể sử dụng từ khóa `let`.


Sau khi viết `let`, chúng ta viết tên muốn đặt cho biến, sau đó là dấu `=` và cuối cùng là giá trị muốn lưu trữ.


Ví dụ:


```javascript
let age = 25

console.log(age)
```


Tên của một biến (về mặt kỹ thuật được gọi là "mã định danh") thường có thể chứa các chữ cái, dấu gạch dưới (`_`), dấu đô la (`$`) và số, mặc dù ký tự đầu tiên không thể là số.


Trong đoạn mã trên, chúng ta đã khai báo một biến có tên là `age` và lưu trữ giá trị `25` trong đó.


Sau đó, chúng tôi in giá trị bằng cách sử dụng `console.log(age)`.


Nếu bạn chạy mã này với `node main.js`, đầu ra sẽ là:


```
25
```


Mã định danh phân biệt chữ hoa và chữ thường, nghĩa là chữ thường và chữ hoa đều được tính là sự khác biệt trong mã định danh, ví dụ


```javascript
let age = 25

let Age = 20

console.log(age)
```


sẽ in ra 25, vì chúng được coi là hai biến hoàn toàn riêng biệt!


Bạn cũng có thể lưu trữ chuỗi (văn bản) trong một biến:


```javascript
let message = "hello again"

console.log(message)
```


Lệnh này sẽ in ra:


```
hello again
```


Giống như trước, chúng ta sử dụng `console.log()` để in giá trị được lưu trữ trong biến.


Bây giờ chúng ta hãy thực hiện cả hai cùng lúc:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


Chạy lệnh này sẽ in ra:


```
25
hello again
```

### Phân công lại


Các biến được khai báo bằng `let` có thể được thay đổi sau khi chúng được tạo.


Đây được gọi là sự phân công lại.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Đầu tiên, chúng ta gán `10` cho `score`, sau đó in ra.


Sau đó, chúng ta thay đổi giá trị của `score` thành `15` và in lại.


Đầu ra sẽ là:


```
10
15
```


Điều này rất hữu ích khi giá trị thay đổi theo thời gian, chẳng hạn như trong trò chơi mà điểm số tăng dần.


Chúng ta hãy thêm một biến nữa vào hỗn hợp:


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


Lệnh này sẽ in ra:


```
10
Alice
20
Bob
```


Như bạn có thể thấy, cả `score` và `player` đều đã thay đổi.


### khai báo `const`


Tuy nhiên, hầu hết chúng ta không muốn một biến thay đổi sau khi nó được tạo. Vì vậy, chúng ta sử dụng `const`.


`const` là viết tắt của “constant” (hằng số). Một khi bạn đã gán giá trị cho biến `const`, bạn không thể thay đổi nó.


```javascript
const pi = 3.14
console.log(pi)
```


Bản in này:


```
3.14
```


Nhưng nếu bạn thử làm thế này:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript sẽ đưa ra lỗi như sau:


```
TypeError: Assignment to constant variable.
```


Điều này là do `pi` được khai báo bằng `const` và bạn không thể thay đổi giá trị của nó sau đó. Bạn đang thông báo với trình thông dịch JavaScript rằng bạn không muốn biến đó thay đổi.


Điều này hữu ích vì nó giảm thiểu khả năng thay đổi chương trình do nhầm lẫn. Khi chương trình trở nên rất lớn, với hàng ngàn dòng mã, việc theo dõi mọi thứ diễn ra cùng một lúc là không thể (đó là lý do chính khiến chúng ta sử dụng máy tính để thực hiện các quy trình phức tạp mà não bộ không thể tính toán được), vì vậy việc đặt ra những hạn chế như thế này sẽ rất hữu ích, giúp chương trình mang tính quyết định hơn.


Người ta cho rằng cách tốt nhất là luôn khai báo các giá trị của chúng ta là `const`, trừ khi chúng ta chắc chắn muốn sửa đổi chúng sau này.


### Bình luận trong JavaScript


Đôi khi chúng ta muốn viết ghi chú vào mã nhưng không được thực thi. Những ghi chú này được gọi là chú thích.


Chương trình sẽ bỏ qua các bình luận khi chạy, nhưng lại hữu ích khi giải thích mọi thứ cho chính chúng ta hoặc người khác.


Để viết chú thích một dòng, hãy sử dụng `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


Lệnh này vẫn sẽ in ra:


```
10
```


Những bình luận này chỉ dành cho con người đọc.


Bạn cũng có thể viết chú thích nhiều dòng bằng cách sử dụng `/*` và `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


Điều này sẽ in


```
20
```


Và bình luận sẽ bị bỏ qua.


Bạn có thể sử dụng chú thích để thêm các chú thích nhỏ vào mã của mình, giúp bạn nhớ mã đó làm gì và tại sao nó được viết theo cách nhất định. Nó cũng có thể giúp các lập trình viên khác hiểu mã đó.


## Các kiểu cơ bản: số, chuỗi, boolean

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


Trong JavaScript, "kiểu" cho bạn biết giá trị đó thuộc loại dữ liệu nào.


Javascript có một số loại cơ bản và trong phần này chúng ta sẽ khám phá một số loại trong số đó.


### Số và phép tính số học


Kiểu đầu tiên chúng ta sẽ giới thiệu là `số`.


Số trong JavaScript có thể là số nguyên (như `5`) hoặc số thập phân (như `3,14`).


Bạn có thể thực hiện các phép tính số học với chúng: cộng, trừ, nhân và chia.


Sau đây là một ví dụ cơ bản:


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


Lệnh này sẽ in ra:


```
15
5
50
2
```


Bạn cũng có thể sử dụng dấu ngoặc đơn `()` để kiểm soát thứ tự các phép tính:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Bản in này:


```
20
```


Nếu không có dấu ngoặc đơn, kết quả sẽ là `2 + 3 * 4`, tức là:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


Điều đó sẽ in ra:


```
14
```


Bởi vì trong toán học thông thường, phép nhân diễn ra trước phép cộng.


### Chuỗi và nội suy


Kiểu JavaScript thứ hai mà chúng ta sẽ giới thiệu là `string`.


Chuỗi là các đoạn văn bản. Bạn có thể sử dụng dấu ngoặc đơn `'...'` hoặc dấu ngoặc kép `"..."` để tạo chuỗi.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Bản in này:


```
hello
Bob
```


Để kết hợp các chuỗi, bạn có thể sử dụng toán tử `+`:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Lệnh này sẽ in ra:


```
hello Bob
```


Nhưng có một cách hay hơn để kết hợp các chuỗi được gọi là **nội suy chuỗi**. Bạn sử dụng dấu ngoặc ngược để khai báo chuỗi `` `...` `` và viết các biến bằng `${...}` bên trong chuỗi:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


Điều này cũng in ra:


```
hello Bob
```


Bạn có thể đưa bất kỳ biểu thức nào vào bên trong `${...}`:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Bản in này:


```
Next year, I will be 31 years old.
```


Nội suy rất phổ biến trong JavaScript hiện đại.


### Boolean, so sánh và các phép toán logic


Kiểu thứ ba chúng ta sẽ giới thiệu là `boolean`. Kiểu này được đặt theo tên nhà toán học George Boole, người đã phát minh ra logic boolean.


Boolean rất đơn giản: chỉ có hai giá trị có thể là `true` và `false`.


Bạn có thể lưu trữ chúng trong các biến:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Bản in này:


```
true
false
```


Bạn có thể kết hợp các giá trị boolean bằng cách sử dụng các toán tử logic:



- `&&` có nghĩa là “và”, và nó sẽ trả về `true` chỉ khi **cả hai** giá trị đều `true`, nếu không nó sẽ trả về `false`
- `||` có nghĩa là "hoặc", và nó sẽ trả về `true` nếu **ít nhất một** giá trị là `true`, nếu không (nếu cả hai đều sai) thì nó sẽ trả về `false`
- `!` nghĩa là “không”, được áp dụng trước một giá trị boolean và sẽ đảo ngược giá trị đó: nếu giá trị boolean là `true` thì sẽ trả về `false` và ngược lại.


![](assets/en/3.webp)


Ví dụ:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


Bạn có thể so sánh các giá trị trong JavaScript bằng các toán tử như `>`, `<`, `===` và `!==`. Kết quả của những phép so sánh này luôn là một giá trị boolean.


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


Javascript cũng có `>=` nghĩa là "lớn hơn hoặc bằng" và `<=` nghĩa là "nhỏ hơn hoặc bằng".


Boolean, toán tử so sánh và toán tử logic thường được kết hợp trong chương trình để khai báo các điều kiện phức tạp, chẳng hạn như để đảm bảo "email đã đến VÀ chứa hình ảnh tôi cần HOẶC độ dài của email dài hơn 10.000 ký tự". Sau này bạn sẽ thấy rằng đây là những khối xây dựng thiết yếu để xây dựng logic của chương trình.


## Mảng, null, không xác định

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


Trong phần này, chúng ta sẽ tìm hiểu thêm ba loại rất phổ biến trong các chương trình JavaScript:



- Mảng**: chuỗi giá trị
- undefined**: một giá trị đặc biệt có nghĩa là “không có gì được gán”
- null**: một giá trị đặc biệt khác có nghĩa là "có chủ ý để trống"


### Mảng và truy cập chỉ mục


**Mảng** là một kiểu dữ liệu có thể chứa nhiều giá trị trong một danh sách.


Bạn tạo một mảng bằng cách sử dụng dấu ngoặc vuông `[]` và phân tách các mục bằng dấu phẩy.


Sau đây là một ví dụ cơ bản:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Bản in này:


```
[ 10, 2, 88 ]
```


Bạn có thể lưu trữ bất cứ thứ gì trong một mảng, không chỉ số:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Bản in này:


```
[ 'apple', 42, true ]
```


Để truy cập một mục cụ thể trong mảng, chúng ta sử dụng **chỉ mục**. Chỉ mục là vị trí của mục, bắt đầu từ **0**.


Vì vậy, trong mảng này:


```javascript
const colors = ["red", "green", "blue"]
```



- `colors[0]` là `"đỏ"`
- `colors[1]` là `"Green"`
- `colors[2]` là `"xanh lam"`


Chúng ta hãy thử nhé:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Lệnh này sẽ in ra:


```
red
green
blue
```


Bạn có thể gán một giá trị cho một chỉ mục cụ thể của một mảng


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Lệnh này sẽ in ra:


```
[ 'red', 'yellow', 'blue' ]
```


Bạn có thể sử dụng bất kỳ số tự nhiên nào làm chỉ mục, thậm chí là số được lưu trữ trong một biến


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Lệnh này sẽ in ra:


```
green
```


Nhưng nếu bạn cố truy cập vào một chỉ mục không tồn tại, bạn sẽ nhận được `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Bản in này:


```
undefined
```


Cái gì thế kia??


### `không xác định`


Giá trị đặc biệt `undefined` có nghĩa là “không có giá trị nào được gán”.


Nếu bạn tạo một biến nhưng không gán giá trị cho nó, biến đó sẽ là `undefined`:


```javascript
const name
console.log(name)
```


Bản in này:


```
undefined
```


Vì chúng ta không gán bất cứ thứ gì cho `name` nên JavaScript mặc định đặt nó thành `undefined`.


Như đã thấy trước đó, bạn cũng có thể nhận được `undefined` khi bạn truy cập vào chỉ mục mảng không tồn tại:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Bản in này:


```
undefined
```


### `null` và cách xử lý nó


`null` cũng là một giá trị đặc biệt. Nó có nghĩa là "không có gì ở đây, và tôi cố tình làm vậy".


Không giống như `undefined` là giá trị tự động, `null` là giá trị bạn tự đặt.


Ví dụ:


```javascript
const currentUser = null
console.log(currentUser)
```


Bản in này:


```
null
```


Tại sao lại dùng `null`? Có thể bạn mong đợi một giá trị sau này, nhưng nó vẫn chưa sẵn sàng:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Bản in này:


```
Alice
```


Vì vậy, `null` hữu ích khi bạn muốn nói, ví dụ, "Sẽ có thứ gì đó ở đây sau này, nhưng hiện tại nó trống rỗng".


## Khối và kiểm soát luồng

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Cho đến nay, chúng ta chủ yếu viết các dòng mã chạy lần lượt.


Nhưng khi chúng ta viết mã, chúng ta có thể kiểm soát thứ tự thực thi của mã đó.


Đây được gọi là **luồng điều khiển**.


Chúng ta hãy bắt đầu bằng việc tìm hiểu về khối và phạm vi.


### Phạm vi toàn cầu


Mỗi biến chúng ta khai báo đều tồn tại trong một **phạm vi**, nghĩa là vùng mã mà biến đó được biết đến.


Nếu bạn khai báo một biến bên ngoài bất kỳ khối nào, biến đó sẽ tồn tại trong **phạm vi toàn cục**.


```javascript
const color = "blue"
console.log(color)
```


Biến `color` này nằm trong phạm vi toàn cục, do đó có thể truy cập từ bất kỳ đâu trong tệp.


Nếu bạn thêm nhiều dòng hơn:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


Cả `color` và `size` đều là biến toàn cục. Chúng có mặt ở mọi nơi trong tệp.


Nhưng điều gì xảy ra bên trong một khối?


### Khối và phạm vi cục bộ


**Khối** là một đoạn mã được bao quanh bởi dấu ngoặc nhọn `{}`.


Các biến được khai báo bằng `let` hoặc `const` bên trong một khối chỉ tồn tại bên trong khối đó.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Bản in này:


```
inside block
```


Nhưng nếu bạn thử cách này:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript sẽ đưa ra lỗi như sau:


```
ReferenceError: message is not defined
```


Đó là vì `message` được khai báo bên trong khối và không tồn tại bên ngoài khối đó.


Điều này có nghĩa là chúng ta có thể sử dụng các khối để cô lập các phần mã của mình và đảm bảo rằng "những gì xảy ra trong khối sẽ chỉ nằm trong khối" (giống như Las Vegas).


Việc tổ chức mã của chúng ta thành các khối cũng cho phép chúng ta cấu trúc việc thực thi chương trình, với các cấu trúc luồng điều khiển như `if`


### `nếu`, `nếu không`


Đôi khi chúng ta muốn chạy mã **chỉ khi** điều gì đó là đúng. Đó chính là mục đích của câu lệnh `if`.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Bản in này:


```
Am I an adult?
Yes I am!
```


Như bạn có thể thấy, đoạn mã so sánh `myAge` và `18`.

Trong trường hợp này, toán tử `>=` trả về `true`, do đó khối được thực thi.

Nếu điều kiện không `đúng`, khối sẽ không được thực thi.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Bản in này:


```
Am I an adult?
```


Bạn có thể thêm khối `else` để xử lý trường hợp ngược lại:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Bản in này:


```
Am I an adult?
No, I am not.
```


Cả khối `if` và `else` vẫn là khối - do đó các biến được khai báo bên trong chúng không tồn tại bên ngoài.


Nếu chúng ta muốn chắc chắn rằng điều gì đó **không** đúng, chúng ta có thể làm gì?


Vâng, như đã thảo luận trước đó, JavaScript có toán tử "not", dùng để đảo ngược các giá trị boolean. Vì vậy, chúng ta có thể làm


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

Vẫn in được:


```
Am I an adult?
No, I am not.
```

Bởi vì chúng ta đã sử dụng toán tử `!` để đảo ngược biến `adult`.


`if (!adult) {...}` nên được đọc là "nếu không phải là người lớn..."


Bằng cách sử dụng các khối, toán tử logic và so sánh, chúng ta có thể cấu trúc quá trình thực thi chương trình bằng cách định nghĩa các biến phải `true` (hoặc `false`) để một điều gì đó xảy ra.


### `trong khi`, `nghỉ`, `tiếp tục`


Vòng lặp `while` lặp lại mã *miễn là* điều kiện vẫn đúng.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Bản in này:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Khi `count` trở thành 3, vòng lặp dừng lại.


Bạn có thể dừng vòng lặp sớm bằng cách sử dụng `break`:


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


Bản in này:


```
0
1
2
```


Bởi vì khi số trở thành `3`, khối `if` sẽ được thực thi và dừng vòng lặp.


Bạn có thể bỏ qua phần còn lại của vòng lặp bằng cách sử dụng `continue`:


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


Bản in này:


```
1
2
4
5
```


Bởi vì khi số là `3`, `continue` khiến chương trình bỏ qua dòng in ra số đó.


### `cho ... của ...`


Nếu bạn có một mảng và muốn thực hiện hành động nào đó với mọi mục trong mảng đó, bạn có thể sử dụng `for ... of ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Bản in này:


```
apple
banana
cherry
```

Khối này sẽ được thực thi một lần cho mỗi phần tử của mảng.


`fruit` ở đây là một biến mới lấy giá trị của từng mục trong mảng để thao tác bên trong khối.


### `vì ... trong ...`


Bạn có thể sử dụng `for ... in` để lặp qua các khóa (chỉ mục) của một mảng:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Bản in này:


```
0
1
2
```


Bạn cũng có thể sử dụng chỉ mục để lấy giá trị:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Điều này in ra kết quả giống như `for ... of`:


```
apple
banana
cherry
```


Trên thực tế, đối với mảng, bạn nên sử dụng `for ... of` vì nó đơn giản và rõ ràng hơn.


### Vòng lặp giới hạn


Đôi khi chúng ta muốn lặp lại một số lần cụ thể hoặc nói chung là viết một đoạn mã lặp lại một khối trong khi vẫn theo dõi một điều gì đó.

Đó chính là tác dụng của vòng lặp `for` bị chặn.

Một vòng lặp giới hạn thường có ba điều kiện, được phân tách bằng dấu chấm phẩy `;`, như trong `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Bản in này:


```
0
1
2
```


Chúng ta hãy giải thích nhé:



- `let i = 0`: khai báo một biến được sử dụng trong khối (trong trường hợp này là một bộ đếm bắt đầu từ 0)
- `i < 3`: khai báo một điều kiện là `đúng` để khối được thực thi (trong trường hợp này là "lặp lại khi `i` nhỏ hơn 3")
- `i = i + 1`: khai báo một số mã sẽ được chạy sau mỗi lần thực thi khối (trong trường hợp này là "tăng `i` lên 1")


Như bạn có thể thấy, vòng lặp giới hạn cho phép chúng ta khai báo các điều kiện phức tạp hơn để thực thi lặp lại một đoạn mã, nhưng hầu hết thời gian điều này là không cần thiết.


### Nhãn khối


Nếu bạn phải viết luồng điều khiển phức tạp hơn, JavaScript cho phép bạn đặt tên khối bằng **nhãn** có thể được sử dụng bởi `break` hoặc `continue` để chỉ định *nơi* quay lại.


Ví dụ:


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


Bản in này:


```
Inside outer block
Inside inner block
Done
```


Chúng tôi sử dụng `break outer` để thoát hoàn toàn khỏi khối `outer`.


Bạn cũng có thể dán nhãn cho các vòng lặp. Hãy xem ví dụ sau:


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

Đây là một ví dụ rất nhàm chán nhưng hy vọng nó có thể làm rõ nhu cầu (thỉnh thoảng) về nhãn.


## Giới thiệu các chức năng

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


Khi chương trình của bạn phát triển, bạn thường muốn **tái sử dụng** các đoạn mã.


Đó chính là mục đích của **hàm**: chúng cho phép bạn nhóm một số mã lại với nhau, đặt tên và chạy bất cứ khi nào bạn muốn.


### Khai báo hàm


Để khai báo một hàm, chúng ta có thể sử dụng từ khóa `function`. Sau đó, chúng ta đặt tên cho hàm, một cặp dấu ngoặc đơn `()` với các đối số mà hàm nhận vào, và một khối mã `{}` để thực thi. Hãy bắt đầu với một hàm không có đối số:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Đoạn mã này **khai báo** hàm, nhưng **chưa** chạy hàm đó.


### Gọi hàm


Để chạy (hoặc "gọi") hàm, bạn viết tên hàm theo sau là dấu ngoặc đơn:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Bản in này:


```
Hello!
```


Bạn có thể gọi hàm này nhiều lần tùy ý:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Bản in này:


```
Hello!
Hello!
```


Mã bên trong hàm chỉ chạy khi bạn gọi nó.


### Đối số hàm (đầu vào cho hàm)


Đôi khi, bạn muốn một hàm hoạt động với một số dữ liệu đầu vào. Bạn có thể làm điều đó bằng cách thêm **đối số** vào trong dấu ngoặc đơn.


Ví dụ:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Bây giờ hàm này có **một đối số** được gọi là `friend`.


Khi bạn gọi hàm, bạn có thể truyền một giá trị:


```javascript
sayHelloTo("Tommy")
```


Bản in này:


```
Hello Tommy!
```


Bạn có thể gọi lại hàm này với tên khác:


```javascript
sayHelloTo("Sam")
```


Bản in này:


```
Hello Sam!
```


Giá trị bạn truyền vào sẽ thay thế biến `friend` bên trong hàm.


Bạn cũng có thể sử dụng nhiều hơn một đối số:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Bản in này:


```
Hello Lina and Marco!
```


### `return` (đầu ra từ các hàm)


Các hàm cũng có thể **trả về** giá trị. Điều này có nghĩa là chúng gửi một giá trị trở lại nơi hàm được gọi.


Đây là một ví dụ đơn giản:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Bản in này:


```
42
```


Hàm `getNumber()` trả về `42`, và chúng ta lưu trữ nó trong `result`, sau đó in ra.


Bạn cũng có thể trả về kết quả bạn tính toán:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Bản in này:


```
5
```


Khi một giá trị được `return`, hàm sẽ dừng lại. Bất cứ điều gì sau `return` trong khối đó đều không xảy ra.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


Chỉ in ra:


```
hi
```


vì chỉ có `"hi"` được trả về. Dòng `console.log("this never runs")` bị bỏ qua.


Bạn có thể coi hàm như những chương trình con nhỏ. Mỗi hàm có thể tiếp nhận một số dữ liệu đầu vào, xử lý chúng và trả về cho bạn một số dữ liệu đầu ra.


Điều gì xảy ra nếu chúng ta thử sử dụng giá trị trả về của một hàm nhưng hàm đó không trả về bất cứ giá trị nào?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Câu lệnh này sẽ in ra `undefined`. Giá trị trả về của một hàm không trả về bất kỳ giá trị nào là `undefined`.


## Đối tượng và lớp

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript thường được gọi là ngôn ngữ hướng đối tượng.


Điều đó có nghĩa là nó giúp bạn sắp xếp mã của mình bằng cách nhóm các giá trị và hàm lại với nhau thành **đối tượng**.


### `Đối tượng` là gì?


Một đối tượng có thể chứa dữ liệu và các hàm hoạt động trên dữ liệu đó. Khi một hàm được đưa vào một đối tượng, chúng ta gọi đó là một `phương thức`.


Đối tượng đầu tiên chúng ta thấy là đối tượng `console`. Đây là một đối tượng chứa nhiều phương thức để in nội dung ra màn hình và gỡ lỗi chương trình.


Nó thậm chí có thể tự in; bạn có thể làm


```javascript
console.log(console)
```


và nó sẽ in ra danh sách các phương thức mà nó chứa. Ví dụ, trên máy của tôi, nó in ra


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


Như bạn thấy, nó có rất nhiều phương pháp mà bạn có thể sử dụng để gỡ lỗi!


Javascript cung cấp cho chúng ta nhiều cách khác nhau để tạo ra các đối tượng mới có thể thực hiện bất kỳ chức năng nào chúng ta muốn.


### Tạo một đối tượng


Cách dễ nhất để tạo một đối tượng chỉ là nhóm dữ liệu và hàm bằng cách sử dụng **dấu ngoặc nhọn** `{}`.


Điều này tạo ra thứ mà chúng ta gọi là **đối tượng ẩn danh**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Thao tác này tạo ra một đối tượng và lưu trữ nó trong một biến có tên là `cat`.


Đối tượng có hai **thuộc tính**:



- `name` với giá trị `"Whiskers"`
- `tuổi` có giá trị `3`


Chúng ta hãy in nó ra:


```javascript
console.log(cat)
```


Bản in này:


```
{ name: 'Whiskers', age: 3 }
```


Bạn có thể lấy các thuộc tính ra khỏi đối tượng bằng cách sử dụng dấu chấm, như trong `objectName.propertyName`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Bạn cũng có thể **thay đổi** một thuộc tính:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Như bạn thấy, ngay cả khi một đối tượng được định nghĩa là `const`, bạn vẫn có thể sửa đổi dữ liệu mà nó chứa.


Trong trường hợp đối tượng, `const` sẽ chỉ ngăn bạn ghi đè toàn bộ đối tượng:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Như đã đề cập trước đó, các đối tượng cũng có thể chứa **hàm** và khi một hàm là một phần của đối tượng, chúng ta gọi đó là **phương thức**.


Sau đây là một ví dụ:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Đối tượng này có:



- Thuộc tính `tên`
- Phương thức `speak()`


Chúng ta hãy gọi phương thức này là:


```javascript
cat.speak()
```


Nó in ra:


```
Meow!
```


Phương pháp có thể sử dụng dữ liệu mà đối tượng chứa thông qua từ khóa `this`.

`this` tham chiếu đến đối tượng hiện tại. Trong ví dụ này, nó sẽ được dùng để in tên của con mèo:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Bản in này:


```
Whiskers says meow!
```


Từ `this` có nghĩa là "đối tượng này"...trong trường hợp này là đối tượng `cat`.



Những loại đối tượng này rất hữu ích khi bạn chỉ cần thứ gì đó nhanh chóng và đơn giản. Nhưng nếu bạn cần tạo **nhiều đối tượng** có cùng cấu trúc, thì có một cách tốt hơn, và đó chính là lúc **lớp** xuất hiện.


### Các lớp và hàm tạo


**Lớp** giống như một bản thiết kế. Nó cho JavaScript biết cách tạo ra một loại đối tượng nhất định.


Bạn định nghĩa một lớp bằng cách sử dụng từ khóa `class`, theo sau là tên của lớp và khối dấu ngoặc nhọn `{}`.


```javascript
class Dog {}
```


Theo thông lệ, các lớp học thường bắt đầu bằng chữ cái in hoa.


Bạn có thể tạo một đối tượng mới của một lớp bằng cách sử dụng `new`:


```javascript
const hachiko = new Dog()
```


Hãy thử in đối tượng:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Bạn sẽ nhận được


```
Dog {}
```


Như bạn có thể thấy, lớp Dog trống, vì vậy đối tượng `myDog` cũng trống.


Chúng ta có thể xác định các thuộc tính mà đối tượng Dog nên chứa bằng cách thêm `constructor`.


Hàm tạo là một hàm đặc biệt chạy khi bạn tạo (hoặc "xây dựng") một đối tượng mới.


```javascript
class Dog {
constructor() { }
}
```


Chúng tôi muốn mỗi chú chó có một cái tên, vì vậy chúng tôi thêm tham số `name` vào hàm:


```javascript
class Dog {
constructor(name) { }
}
```


Và sau đó chúng ta sử dụng `this` để khai báo rằng `name` là `tên` của đối tượng `Dog` mà chúng ta đang xây dựng


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Chúng ta hãy thử sử dụng nó ngay bây giờ:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


Điều này in ra nội dung tương tự như sau:


```
Dog { name: 'hachiko' }
```


Như bạn có thể thấy, phương thức `constructor` lấy các đối số mà bạn truyền cho lớp khi bạn thực hiện `new Dog()` và sử dụng chúng để xây dựng đối tượng.


Chúng ta hãy phân tích nó như sau:



- `class Dog` định nghĩa lớp Dog.
- `constructor(name)` thiết lập đối tượng khi nó được tạo.
- `this.name = name` lưu trữ giá trị trong đối tượng mới.
- `new Dog("hachiko")` tạo một đối tượng mới từ lớp, với thuộc tính `name` được đặt thành `"hachiko"`.


Bây giờ chúng ta hãy thêm một phương thức vào lớp của chúng ta:


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


Điều này sẽ in


```javascript
hachiko says barf!
```


Nếu chúng ta làm tương tự cho hai trường hợp khác nhau của Dog



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


chúng ta nhận được


```
hachiko says barf!
bobby says barf!
```


phương thức `speak()` sử dụng thuộc tính `name` của `Dog` mà nó được gọi.


Đây là lý do chính khiến các lớp tồn tại: chúng cho phép chúng ta xác định một tập hợp các phương thức hoạt động trên dữ liệu, sau đó tạo nhiều đối tượng có cùng "hình dạng" dữ liệu.


Khi chúng ta gọi một phương thức trên một trong những đối tượng này, nó sẽ hoạt động trên dữ liệu mà *đối tượng cụ thể đó* nắm giữ.


### Thay đổi hình dạng của một vật thể


Đối tượng trong JavaScript rất linh hoạt. Ngay cả sau khi đã tạo đối tượng, bạn vẫn có thể thêm thuộc tính mới hoặc xóa thuộc tính hiện có.


Bạn được phép làm vậy, nhưng bạn nên cẩn thận khi sử dụng.


Chúng ta hãy bắt đầu với lớp `Dog` đơn giản của chúng ta:


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


Lúc này, `myDog` chỉ có một thuộc tính: `name`. Chúng ta vẫn có thể thêm các thuộc tính mới sau khi nó được tạo:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


Chúng ta cũng có thể thêm một phương pháp mới:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


Và chúng ta cũng có thể xóa các thuộc tính bằng cách sử dụng từ khóa `delete`.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


Cách này hiệu quả, nhưng có một điều quan trọng cần lưu ý: Các công cụ JavaScript như V8 (được sử dụng trong Node.js và trình duyệt Chrome) chạy nhanh hơn khi đối tượng của bạn luôn duy trì cùng một thuộc tính. Việc thêm hoặc xóa thuộc tính sau khi đối tượng được tạo có thể làm chậm tốc độ.


Trong các chương trình nhỏ, điều này không quan trọng lắm. Nhưng trong các dự án lớn hơn (như trò chơi), tốt hơn hết là nên liệt kê tất cả các thuộc tính trong hàm khởi tạo ngay từ đầu, ngay cả khi bạn không sử dụng chúng ngay lập tức. Điều này giúp giữ hình dạng đối tượng ổn định và giúp mã của bạn chạy nhanh hơn.


Ví dụ, thay vì thế này:


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


Bạn có thể làm


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


Cả hai phiên bản đều hoạt động, nhưng phiên bản thứ hai hiệu suất tốt hơn. Bạn đang cho công cụ biết trước các thuộc tính mà mỗi đối tượng sẽ có, và nó có thể tối ưu hóa cho phù hợp.


JavaScript cho phép bạn định hình lại các đối tượng một cách thoải mái, nhưng khi sử dụng các lớp, tốt nhất là bạn nên lập kế hoạch cho hình dạng của đối tượng trước.



### Kế thừa với `extends` và `super()`


Đôi khi bạn muốn tạo một lớp *gần như* giống với một lớp khác, nhưng có thêm một vài tính năng.


Thay vì phải sửa đổi hình dạng của các đối tượng (như đã đề cập trước đó, điều này không tối ưu cho hiệu suất) hoặc phải viết lại một lớp mới từ đầu, JavaScript cho phép bạn sử dụng thứ gọi là **thừa kế**.


Kế thừa nghĩa là một lớp có thể **mở rộng** lớp khác. Lớp mới sẽ nhận được tất cả các thuộc tính và phương thức của lớp cũ, và bạn có thể thêm hoặc thay đổi những gì bạn cần.


Giả sử chúng ta có một lớp cơ sở có tên là `Vehicle`:


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


Bây giờ chúng ta muốn tạo một lớp `Car`. Car là một loại phương tiện, nhưng chúng ta có thể muốn nó có thêm một số tính năng hoặc một thông báo khác khi khởi động. Thay vì viết lại mọi thứ, chúng ta có thể sử dụng `extends`:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Lớp `Car` hiện **thừa hưởng** mọi thứ từ `Vehicle`. Nó có thuộc tính `brand`, và chúng tôi đã thay thế phương thức `start()` bằng phiên bản riêng của mình.


![](assets/en/4.webp)


Chúng ta hãy thử xem nhé:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Bản in này:


```
Toyota car is ready to drive!
```


Mặc dù `Car` không có hàm dựng riêng, nó vẫn sử dụng hàm dựng từ `Vehicle`. Tuy nhiên, nếu chúng ta muốn viết một hàm dựng tùy chỉnh trong `Car`, chúng ta có thể, chỉ cần thêm lệnh gọi đến hàm dựng của lớp cha bằng `super()`.


Sau đây là cách thực hiện:


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



Bản in này:


```
Toyota Corolla is ready to drive!
```


Vì vậy, để tóm tắt



- `extends` có nghĩa là một lớp dựa trên một lớp khác.
- `super()` được sử dụng để gọi hàm tạo của lớp mà bạn đang mở rộng.
- Lớp mới sẽ có tất cả các thuộc tính và phương thức của lớp gốc.
- Bạn có thể **ghi đè** các phương thức (như `start()`) để khiến chúng thực hiện hành động khác.


Điều này hữu ích khi bạn có nhiều thứ tương tự nhau (như ô tô, xe tải và xe đạp) và bạn muốn chúng chia sẻ mã nhưng vẫn hoạt động theo cách riêng của chúng.


### `thể hiện của`


Từ khóa `instanceof` kiểm tra xem một đối tượng có được tạo từ một lớp nhất định hay không.


Giả sử chúng ta có một lớp có tên là `User`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Bản in này:


```
true
```


Xác nhận rằng `regularUser` là một `User`. Điều này là do `regularUser` được tạo bằng lớp `User`.


Nó cũng hoạt động với các lớp **được kế thừa**. Ví dụ, đây là lớp `Admin` mở rộng `User`:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Cả hai dòng đều trả về `true`. Bởi vì `Admin` là một lớp con của `User`, do đó `ourAdmin` vừa là `Admin` vừa là `User`.


# JavaScript trung cấp

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Xử lý lỗi

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


Khi viết các chương trình JavaScript phức tạp hơn, bạn sẽ gặp phải **lỗi**. Đây là những tình huống bất ngờ khi có sự cố xảy ra. Có thể một biến `undefined` nhưng bạn cố gắng sử dụng nó, hoặc một số mã nhận được kiểu dữ liệu đầu vào không đúng.


Nếu chúng ta không xử lý đúng các lỗi này, chương trình của chúng ta có thể bị sập hoặc hoạt động không như mong đợi. JavaScript cung cấp các công cụ để phát hiện và quản lý các lỗi này, giúp chúng ta xử lý chúng một cách nhẹ nhàng hơn.


### Lỗi thường gặp: truy cập giá trị trên `undefined`


Sau đây là tình huống thường gặp gây ra lỗi:


```javascript
const user = undefined
console.log(user.name)
```


Nếu bạn chạy mã này, bạn sẽ nhận được lỗi như sau:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


Đó là JavaScript đang nói với bạn rằng: "Này, bạn đã cố lấy thuộc tính `name` từ một thứ `không xác định` và điều đó không có ý nghĩa gì cả." Và như bạn thấy, khi loại lỗi này xảy ra, chương trình sẽ ngừng chạy trừ khi bạn đã viết mã cụ thể để phát hiện và xử lý lỗi đó.


### `ném` một lỗi


Đôi khi bạn muốn tự tay **gây lỗi** trong mã của mình. Trong trường hợp đó, bạn sử dụng từ khóa `throw`.


```javascript
throw new Error("This is a custom error message")
```


Lệnh này sẽ dừng chương trình ngay lập tức và in ra:


```
Uncaught Error: This is a custom error message
```


Bạn có thể sử dụng `throw` để thực thi các quy tắc trong chương trình của mình. Ví dụ:


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


Cuộc gọi thứ hai gây ra lỗi vì không được phép chia cho số không trong ví dụ này.


### Bắt lỗi bằng `try...catch`


Nếu bạn không muốn chương trình bị sập khi xảy ra lỗi, bạn có thể xử lý lỗi bằng khối `try...catch`. Điều này hữu ích khi bạn muốn chương trình **tiếp tục chạy** ngay cả khi có lỗi xảy ra.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Đầu ra:


```
Oops! Something went wrong.
```


Sau đây là cách thức hoạt động:



- Mã bên trong khối `try` sẽ được thử trước.
- Nếu xảy ra lỗi, JavaScript **sẽ nhảy tới khối `catch`**, bỏ qua phần còn lại của khối `try`.
- Khối `catch` nhận lỗi, do đó bạn có thể in lỗi hoặc xử lý lỗi theo cách khác, ví dụ như


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Đầu ra:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### Khối `cuối cùng`


Bạn cũng có thể thêm khối `finally`. Đây là mã **luôn chạy**, bất kể có lỗi hay không.


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


Đầu ra:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Tránh lỗi

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


Chương này sẽ chỉ ra một số lỗi thường gặp nhất trong JavaScript và cách tránh chúng.


### `var` và Assignment không cần khai báo


Trong mã JavaScript cũ, các biến thường được khai báo bằng từ khóa `var`. Không giống như `let` và `const` mà bạn đã tìm hiểu, `var` có thể hoạt động theo những cách khó hiểu.


Ví dụ:


```javascript
{
var message = "hello"
}
console.log(message)
```


Bạn có thể mong đợi `message` chỉ tồn tại bên trong khối, nhưng không phải vậy. `var` bỏ qua phạm vi khối và khiến biến có sẵn trong toàn bộ hàm hoặc tệp.


Điều này có thể dẫn đến những hành vi không mong muốn, đặc biệt là trong các chương trình lớn. Vì lý do này, mã JavaScript hiện đại nên luôn sử dụng `let` hoặc `const` thay vì `var`.


Tệ hơn nữa, JavaScript cho phép bạn gán giá trị cho các biến **mà không cần khai báo chúng**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Thao tác này sẽ tạo ra một biến toàn cục mới `name` mà không cần khai báo. Điều này có thể diễn ra âm thầm và dẫn đến các lỗi cần được theo dõi ở mức Hard, đặc biệt nếu đó chỉ là lỗi đánh máy. Luôn khai báo biến bằng `let` hoặc `const`.


### Hệ thống loại yếu


JavaScript có kiểu dữ liệu yếu, nghĩa là nó tự động chuyển đổi giá trị từ kiểu này sang kiểu khác nếu cần. Điều này được gọi là ép kiểu (type coercion), và mặc dù có thể tiện lợi, nhưng nó thường dẫn đến kết quả khó hiểu.


Ví dụ:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


Trong các ví dụ này, JavaScript cố gắng đoán ý bạn. Đôi khi, nó biến chuỗi thành số, hoặc boolean thành số, hoặc chuỗi thành chuỗi. Điều này có thể khiến mã của bạn hoạt động theo những cách không mong muốn.


Việc nhận thức được hệ thống kiểu dữ liệu yếu của JavaScript là rất quan trọng. Khi mọi thứ bắt đầu hoạt động kỳ lạ, có thể là do sự ép kiểu dữ liệu không mong muốn.


### `"sử dụng nghiêm ngặt"`


Bạn có thể kích hoạt chế độ nghiêm ngặt hơn để biến một số lỗi im lặng thành lỗi thực sự và ngăn bạn sử dụng một số tính năng nguy hiểm hơn của ngôn ngữ.


Để kích hoạt chế độ nghiêm ngặt hơn này, hãy thêm dòng này vào đầu tệp hoặc hàm của bạn:


```javascript
"use strict"
```


Ví dụ:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Nếu không có chế độ nghiêm ngặt, JavaScript sẽ tự động tạo một biến toàn cục có tên là `name`. Nhưng với chế độ nghiêm ngặt, biến này sẽ trở thành một lỗi thực sự, giúp bạn phát hiện lỗi sớm hơn.


Chế độ nghiêm ngặt cũng vô hiệu hóa một số tính năng lỗi thời của JavaScript và giúp mã của bạn dễ tối ưu hóa và bảo trì hơn.


## Giá trị so với Tham chiếu

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript xử lý các loại giá trị khác nhau theo nhiều cách khác nhau.


Một số giá trị được **sao chép** khi bạn gán chúng cho một biến.


Những biến khác được **chia sẻ** khi bạn gán chúng cho một biến mới, vì vậy nếu bạn thay đổi biến này, biến kia cũng sẽ thay đổi theo.


### Truyền theo giá trị


Khi một giá trị được truyền **theo giá trị**, JavaScript sẽ tạo một **bản sao** của giá trị đó.


Vì vậy, nếu bạn thay đổi cái này thì sẽ không ảnh hưởng đến cái kia.


Điều này xảy ra với các kiểu dữ liệu nguyên thủy như:



- số
- dây đàn
- boolean (`true` và `false`)
- `null`
- `không xác định`


Chúng ta hãy xem một ví dụ:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


Chúng ta đã gán giá trị của `a` cho `b`, nhưng sau đó chúng ta đã đổi `b` thành `10`.


Vì số được truyền theo giá trị, JavaScript đã sao chép `5` vào `b`. `5` trong `b` độc lập với `5` ban đầu trong `a`, nên việc thay đổi giá trị của `b` không ảnh hưởng đến `a`.


Chúng ta hãy thử với một chuỗi:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Một lần nữa, việc thay đổi `name2` không ảnh hưởng đến `name1`, vì chuỗi cũng được truyền theo giá trị.


Điều tương tự cũng xảy ra khi bạn truyền một giá trị nguyên thủy vào một hàm: nó được sao chép. Vì vậy, hàm không thể thay đổi giá trị gốc.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Mặc dù bên trong hàm `1` đã được thêm vào `x`, `số` ban đầu vẫn không thay đổi.


Đó là vì chỉ có một **bản sao** được truyền vào hàm.


### Truyền theo tham chiếu


Các đối tượng được truyền **bằng tham chiếu**.


Điều đó có nghĩa là thay vì sao chép chúng, JavaScript chỉ truyền một **tham chiếu** đến nó và nếu bạn sửa đổi nó, tất cả các biến khác trỏ tới nó cũng sẽ thấy sự thay đổi.


Ví dụ:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Cả `person1` và `person2` đều trỏ tới cùng một đối tượng trong bộ nhớ.


Vì vậy, khi chúng tôi thay đổi `person2.name`, chúng tôi cũng thay đổi `person1.name`, vì cả hai đều đang xem cùng một thứ.


Mảng là đối tượng, vì vậy chúng ta hãy thử làm điều tương tự với một mảng:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


Chúng tôi đã đẩy `4` vào `list2`, nhưng `list1` cũng bị ảnh hưởng vì cả hai đều tham chiếu đến cùng một mảng.


Hãy xem điều gì xảy ra khi chúng ta truyền một đối tượng vào một hàm:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


Hàm này đã thay đổi đối tượng! Đó là vì nó nhận được **tham chiếu** đến đối tượng `person` ban đầu.


Nó không có bản sao. Nó có quyền truy cập vào đối tượng gốc và nhờ đó có khả năng chỉnh sửa đối tượng đó.


Điều quan trọng là phải nhớ sự khác biệt này, vì nếu không, mã của chúng ta có thể hoạt động khác với những gì chúng ta mong đợi. Ví dụ, chúng ta có thể viết một hàm với kỳ vọng rằng nó sẽ không sửa đổi các đối số nhận được, nhưng sau đó phát hiện ra rằng nó thực sự đã sửa đổi chúng (vì chúng là đối tượng, nên được truyền theo tham chiếu).


## Làm việc với các hàm

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Bạn đã học cách khai báo và sử dụng hàm trong JavaScript. Nhưng JavaScript cung cấp cho bạn nhiều công cụ hơn để làm việc với hàm một cách hiệu quả.


### Các hàm mũi tên


Hàm mũi tên là một cách viết hàm ngắn gọn hơn. Thay vì sử dụng từ khóa `function`, chúng ta sử dụng mũi tên (`=>`).


Sau đây là một hàm bình thường:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


Phiên bản mũi tên trông như thế này:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Nếu hàm **chỉ có một dòng**, bạn có thể bỏ qua dấu ngoặc nhọn và `return`:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Nếu hàm chỉ có **một tham số**, bạn thậm chí có thể bỏ qua dấu ngoặc đơn xung quanh các tham số:


```javascript
const greet = name => `Hello, ${name}!`
```


Các hàm mũi tên rất phổ biến trong JavaScript hiện đại vì chúng cho phép thể hiện các hàm đơn giản với ít mã lệnh mẫu hơn đáng kể.


### Các tham số mặc định


Đôi khi bạn muốn một hàm có **giá trị mặc định** nếu không có đối số nào được truyền vào.


Bạn có thể làm như thế này:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


Giá trị mặc định `"friend"` được sử dụng khi không có dữ liệu nào được truyền vào.


### Tham số lan truyền (`...`)


Nếu hàm của bạn có số lượng đối số linh hoạt thì sao?


Bạn có thể sử dụng **toán tử trải rộng** (`...`) để tập hợp chúng thành một mảng:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Sau đó, bạn có thể sử dụng vòng lặp để xử lý từng mục:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


Toán tử spread hữu ích khi bạn không biết có bao nhiêu đối số sẽ được truyền.


### Các hàm bậc cao


**Hàm bậc cao** là hàm:



- lấy một hàm khác làm đầu vào
- và/hoặc trả về một hàm như đầu ra


Sau đây là một ví dụ đơn giản:


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


Bản in này:


```
Hello, friend!
Hello, friend!
```


Chúng ta có thể truyền một hàm mũi tên cho nó:


```javascript
runTwice(
() => console.log("Hello!")
)
```


Bản in này:


```
Hello!
Hello!
```


Bạn cũng có thể viết các hàm **trả về** các hàm khác:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


Hàm `makeGreeter` là một hàm xây dựng các hàm khác. Nó nhận một chuỗi và trả về một hàm mới sử dụng chuỗi đó trong lệnh gọi `console.log`.


Kiểu mẫu này rất hiệu quả vì nó cho phép bạn để lại "lỗ hổng" trong các hàm mà sau này bạn có thể lấp đầy bằng hành vi bạn cần.


### `map()`, `filter()`, `reduce()`


JavaScript cung cấp cho bạn một số phương thức tích hợp hữu ích để sử dụng với mảng.


Các phương pháp này lấy hàm làm đối số nên chúng cũng là hàm bậc cao.


`map()` chuyển đổi từng mục trong mảng thành một mục khác.


Ví dụ:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Mỗi số được nhân đôi và kết quả là một mảng mới.


`filter()` xóa các mục khỏi mảng nếu chúng không vượt qua bài kiểm tra.


Ví dụ:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Chỉ các mục mảng có điều kiện `x > 2` trả về `true` mới được giữ lại.


`reduce()` được sử dụng để kết hợp tất cả các mục trong một mảng thành một giá trị duy nhất.


Ví dụ:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` duyệt qua mảng và, trong ví dụ này, áp dụng toán tử `+` giữa `1` và `2`, sau đó giữa `3` và `3` kết quả, sau đó giữa `6` và `4` kết quả, cho đến khi có tổng của tất cả các mục trong mảng (là 10).


Bạn có thể sử dụng `reduce()` cho nhiều mục đích như tính tổng, tính trung bình hoặc xây dựng các giá trị mới theo từng bước.


Các phương pháp này (`map`, `filter`, `reduce`) là những công cụ mạnh mẽ để xử lý dữ liệu mà không cần phải viết vòng lặp thủ công.


Bạn thậm chí có thể kết hợp chúng thành một chuỗi hoạt động như thế này:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Làm việc với các đối tượng

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


Trong chương này, chúng ta sẽ tìm hiểu một số công cụ mạnh mẽ và nâng cao hơn một chút để làm việc với các đối tượng trong JavaScript.


### Bất động sản tư nhân


Đôi khi, chúng ta muốn ẩn một thuộc tính của một đối tượng để nó không thể bị thay đổi hoặc truy cập từ bên ngoài đối tượng. JavaScript cung cấp cho chúng ta một cách để làm điều này bằng cách sử dụng ký tự `#` trước tên thuộc tính. Thao tác này tạo ra một thuộc tính **riêng tư**, chỉ có thể truy cập từ bên trong lớp.


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


Tài sản riêng tư hữu ích khi bạn muốn ngăn chặn những thay đổi ngoài ý muốn.


### Thuộc tính `static`


Đôi khi, bạn muốn một thuộc tính thuộc về chính lớp đó, chứ không phải thuộc về từng đối tượng bạn tạo ra từ lớp đó. Đó chính là mục đích của `static`. Một thuộc tính `static` được chứa trong lớp và tất cả các đối tượng của lớp đó sẽ tham chiếu đến nó.


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


Điều này hữu ích khi lưu trữ dữ liệu và phương pháp chia sẻ áp dụng cho toàn bộ nhóm đối tượng, không chỉ một đối tượng.


### `get` và `set`


Trong JavaScript, `get` và `set` cho phép bạn tạo các thuộc tính *trông* giống như các biến bình thường, nhưng thực chất lại chạy mã đặc biệt ở chế độ nền.


Phương thức `get`ter chạy khi bạn cố gắng *đọc* một thuộc tính. Nó được khai báo bằng cách viết `get` trước một phương thức có tên thuộc tính.


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


Mặc dù `fullName` không phải là một thuộc tính thông thường, chúng ta có thể sử dụng nó như một thuộc tính thông thường và chạy hàm `get` để xây dựng tên đầy đủ.


Phương thức `set`ter chạy khi bạn *gán* một giá trị cho một thuộc tính. Nó cho phép bạn kiểm soát những gì xảy ra khi ai đó cố gắng thay đổi giá trị đó. Nó được khai báo bằng cách viết `set` trước một phương thức có tên thuộc tính.


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


Khi chúng ta thực hiện `user.fullName = "John Smith"`, phương thức `set` sẽ chạy và cập nhật các giá trị `firstName` và `lastName`.


Vì vậy, mặc dù có vẻ như chúng ta chỉ đang thiết lập một biến đơn giản, nhưng thực ra chúng ta đang kích hoạt logic cập nhật các thuộc tính khác.


## Khóa và Giá trị

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Mỗi thuộc tính trong đối tượng JavaScript đều có **khóa** (còn gọi là tên thuộc tính) và **giá trị**.


Ví dụ:


```javascript
const user = {
name: "Alice",
age: 30
}
```


Trong đối tượng này, `"name"` và `"age"` là các khóa, còn "Alice" và `30` là giá trị của chúng.


### Truy cập động


Đôi khi, bạn không biết trước tên của một thuộc tính... có thể bạn lấy nó từ dữ liệu người dùng nhập vào, hoặc đọc nó từ một biến. Bạn vẫn có thể truy cập nó bằng cách sử dụng **ký hiệu ngoặc vuông**, chẳng hạn như `myObject["keyName"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


Chúng tôi đã truyền chuỗi `name` cho đối tượng để lấy giá trị tương ứng.


Chúng ta có thể lưu khóa vào một biến và sử dụng nó để truy cập giá trị tương ứng sau này, như


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Assignment động


Bạn cũng có thể tạo hoặc cập nhật thuộc tính đối tượng bằng cách sử dụng biến làm khóa.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


Điều này hữu ích khi bạn muốn xây dựng một đối tượng theo từng bước. Ví dụ:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Bạn thậm chí có thể sử dụng khóa động *trong khi tạo* đối tượng bằng cách sử dụng dấu ngoặc vuông:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Đây được gọi là **thuộc tính được tính toán**. Giá trị bên trong dấu ngoặc vuông sẽ được tính toán và kết quả được sử dụng làm khóa.


### Kiểu `Biểu tượng`


Ngoài chuỗi, JavaScript còn cho phép bạn sử dụng một kiểu đặc biệt gọi là `Symbol` làm khóa đối tượng.


Chúng ta hãy bắt đầu với một ví dụ đơn giản:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


Trong ví dụ này, `id` là một Symbol. Nó không phải là một chuỗi, nhưng vẫn hoạt động như một khóa. Nếu bạn thử ghi `user` vào bảng điều khiển, bạn sẽ thấy như sau:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


Một điều quan trọng nữa: mọi ký hiệu bạn tạo ra đều là duy nhất, ngay cả khi chúng được tạo ra bằng cùng một chuỗi.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Biểu tượng cho phép bạn định nghĩa các khóa không xung đột với các khóa thông thường. Ví dụ: giả sử bạn có một đối tượng với thuộc tính `name`, nhưng đối tượng đó sẽ được người dùng tùy chỉnh trong tương lai, theo những cách bạn không thể dự đoán, và người dùng đó cũng có thể thêm thuộc tính `name`. Nếu thuộc tính `name` ban đầu được định nghĩa bằng một chuỗi, nó sẽ bị ghi đè bởi thuộc tính mới, như sau:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Nếu chúng ta sử dụng Biểu tượng thay thế:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Như bạn thấy, thuộc tính `name` ban đầu bằng cách nào đó được bảo toàn theo cách này. Điều này có thể hữu ích trong một số trường hợp ngoại lệ.


## Đối tượng tiện ích

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript cung cấp cho chúng ta một số đối tượng tích hợp hữu ích giúp chúng ta thực hiện các thao tác như gỡ lỗi và tính toán.


### Các phương pháp `console` khác


Bạn đã thấy `console.log`, lệnh này in các giá trị ra màn hình.


Có một số phương pháp hữu ích khác có sẵn trên đối tượng `console` có thể giúp bạn gỡ lỗi chương trình của mình.


#### `console.warn`


In thông báo màu vàng (hoặc có biểu tượng cảnh báo trong một số môi trường):


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


In ra thông báo màu đỏ, giống như lỗi:


```javascript
console.error("Something went wrong!")
```


#### `console.table`


Hiển thị một mảng hoặc đối tượng dưới dạng bảng:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Thao tác này sẽ in ra một bảng như sau:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


Điều này có thể hữu ích để trực quan hóa dữ liệu có cấu trúc.


#### `console.time` và `console.timeEnd`


Bạn có thể đo thời gian thực hiện một việc gì đó:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


Điều này in ra nội dung tương tự như sau:


```
timer: 2.379ms
```


Hữu ích cho một số thử nghiệm hiệu suất đơn giản.


### Đối tượng `Toán học`


JavaScript cung cấp cho bạn một đối tượng `Math` với các phương thức hữu ích để thực hiện tính toán.


#### `Math.random()`


Trả về một số ngẫu nhiên giữa 0 (bao gồm) và 1 (không bao gồm):


```javascript
const r = Math.random()
console.log(r)
```


Ví dụ đầu ra:


```
0.4387429859
```


#### `Math.floor()` và `Math.ceil()`



- `Math.floor(n)` làm tròn **xuống** đến số nguyên gần nhất
- `Math.ceil(n)` làm tròn **lên** đến số nguyên gần nhất


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


Làm tròn đến số nguyên gần nhất:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` và `Math.min()`


Trả về giá trị lớn nhất hoặc nhỏ nhất từ danh sách số:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` và `Math.sqrt()`



- `Math.pow(a, b)` cung cấp cho bạn `a` lũy thừa của `b`
- `Math.sqrt(n)` cung cấp cho bạn căn bậc hai của `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# JavaScript nâng cao

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Các bộ sưu tập khác

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript cung cấp cho chúng ta một số kiểu tập hợp đặc biệt vượt ra ngoài mảng và đối tượng thông thường. Chúng bao gồm `Map` và `Set`.


Chúng giúp bạn lưu trữ và quản lý các nhóm giá trị, nhưng chúng hoạt động khác với những gì bạn đã thấy cho đến nay.


`Map` là một tập hợp các cặp **khóa-giá trị**, giống như một đối tượng. Tuy nhiên, nó có một số điểm khác biệt quan trọng:



- Các khóa có thể là **bất kỳ giá trị nào** chứ không chỉ là chuỗi.
- Thứ tự của các mục được giữ nguyên.
- Nó có các phương pháp tích hợp giúp làm việc dễ dàng hơn.


Bạn tạo một bản đồ mới như thế này:


```javascript
const myMap = new Map()
```


Thao tác này sẽ tạo ra một bản đồ trống. Để thêm các mục vào đó, hãy sử dụng `myMap.set(key, value)`:


```javascript
myMap.set("name", "Alice")
```


Thao tác này sẽ thêm khóa `"name"` có giá trị `"Alice"`.


Bạn cũng có thể sử dụng một số làm chìa khóa:


```javascript
myMap.set(42, "The answer")
```


Và thậm chí một đối tượng làm chìa khóa:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


Điều đó sẽ không hiệu quả với các đối tượng thông thường, chỉ cho phép sử dụng khóa chuỗi.


Để **lấy giá trị**, hãy sử dụng `myMap.get(key)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


Để **kiểm tra xem khóa có tồn tại hay không**, hãy sử dụng `myMap.has(key)`:


```javascript
console.log(myMap.has("name")) // true
```


Để **xóa khóa**, hãy sử dụng `myMap.delete(key)`:


```javascript
myMap.delete("name")
```


Để **xóa toàn bộ bản đồ**, hãy sử dụng `myMap.clear()`:


```javascript
myMap.clear()
```


Bản đồ rất hữu ích để quản lý các tập hợp giá trị lớn, vì việc truy cập các giá trị trên bản đồ lớn thường mang lại hiệu suất tốt hơn nhiều so với trên một đối tượng lớn.


### `Bộ`


`Set` là tập hợp chỉ chứa **giá trị** (không có khóa), trong đó mỗi giá trị phải **duy nhất**. Điều này có nghĩa là:



- Bạn không thể có cùng một giá trị hai lần
- Các giá trị được lưu trữ theo thứ tự bạn thêm chúng


Bạn tạo một tập hợp như thế này:


```javascript
const mySet = new Set()
```


Để **thêm giá trị**, hãy sử dụng `mySet.add(value)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Mặc dù chúng ta đã thử thêm `2` hai lần, tập hợp chỉ giữ lại một bản sao.


Để **kiểm tra xem giá trị có nằm trong tập hợp hay không**, hãy sử dụng `mySet.has(value)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Để **xóa một giá trị**, hãy sử dụng `mySet.delete(value)`:


```javascript
mySet.delete(2)
```


Để **xóa mọi thứ**, hãy sử dụng `mySet.clear()`:


```javascript
mySet.clear()
```


`Set` hữu ích khi bạn muốn giữ một tập hợp các giá trị duy nhất mà không cần phải kiểm tra thủ công các giá trị trùng lặp:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


`Set` giúp bạn tránh các mục trùng lặp.


## Trình lặp

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


Hầu hết mọi thứ trong JavaScript mà bạn có thể lặp lại (như mảng, chuỗi, bản đồ, tập hợp) đều **có thể lặp lại**: chúng có thể cung cấp trình lặp cho nội dung của chúng.


**Trình lặp** là một đối tượng đặc biệt trong JavaScript giúp bạn duyệt qua danh sách các mục **từng mục một**.


### Trình lặp `Object`


Không giống như mảng hoặc bản đồ, các đối tượng thông thường **không thể lặp lại** với `for...of`. Nếu bạn thử cách này:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Bạn sẽ nhận được lỗi:


```
TypeError: user is not iterable
```


Đó là vì các đối tượng thuần túy không có trình lặp tích hợp. Nhưng JavaScript cung cấp cho bạn các công cụ khác để lặp qua chúng.


#### `Object.keys()`


Bạn có thể sử dụng `Object.keys(obj)` để lấy một mảng các **khóa** của đối tượng, sau đó lặp lại mảng đó:


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


Bản in này:


```
name
age
```


#### `Object.values()`


Để lặp qua các **giá trị**, hãy sử dụng `Object.values()`:


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


Bản in này:


```
Alice
30
```


#### `Object.entries()`


Nếu bạn muốn **cả khóa và giá trị**, hãy sử dụng `Object.entries()`:


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


Bản in này:


```
name is Alice
age is 30
```


Mặc dù các đối tượng không thể lặp lại trực tiếp, các phương thức này cung cấp cho bạn quyền truy cập đầy đủ vào nội dung của chúng theo cách hoạt động tốt với `for...of`.


Nhưng trình lặp hoạt động như thế nào?


### `Symbol.iterator`


Bí mật đằng sau tất cả các đối tượng lặp lại là một **biểu tượng** đặc biệt được gọi là `Symbol.iterator`.


Biểu tượng này là một khóa tích hợp cho biết với JavaScript: “Đối tượng này có thể được lặp lại”.


Khi bạn gọi `myIterable[Symbol.iterator]()`, JavaScript sẽ trả về cho bạn một **đối tượng lặp** với phương thức `.next()`.


Chúng ta hãy xem nó trông như thế nào:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Mỗi lần gọi hàm `.next()` sẽ trả về giá trị tiếp theo. Khi hoàn tất, nó sẽ trả về:


```javascript
{ value: undefined, done: true }
```


### `tiếp theo()`


Phương thức `.next()` được sử dụng để lấy phần tử tiếp theo từ chuỗi.


Mỗi lần bạn gọi `.next()`, bạn sẽ nhận được một đối tượng có hai khóa:



- `giá trị`: mục hiện tại
- `done`: một boolean cho bạn biết liệu quá trình lặp lại đã kết thúc hay chưa


Chúng ta hãy làm một ví dụ đầy đủ:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Bản in này:


```
Lina
Tom
Eva
```


Đây là cách vòng lặp `for...of` hoạt động bên trong: nó sử dụng mẫu này với `.next()`.


Bạn sẽ nhận được kết quả tương tự với


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Làm cho một lớp có thể lặp lại


Bạn cũng có thể định nghĩa **lớp lặp** của riêng mình bằng cách thêm phương thức `[Symbol.iterator]()`.


Giả sử chúng ta muốn một lớp biểu diễn một **dải số**, chẳng hạn như từ 1 đến 5.


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


Bản in này:


```
1
2
3
4
5
```


Sau đây là những gì đang xảy ra:



- Chúng tôi đã định nghĩa một lớp `Range`
- Bên trong lớp, chúng tôi đã triển khai `[Symbol.iterator]()`, do đó JavaScript biết cách lặp lại nó
- Phương thức `next()` trả về từng số một
- Khi chúng ta đạt đến `end`, nó trả về `{ done: true }`


Bây giờ lớp `Range` của chúng ta hoạt động giống như một mảng và chúng ta có thể sử dụng nó trong bất kỳ vòng lặp nào mong đợi một đối tượng lặp lại.


### Các hàm tạo và `yield`


Để giúp bạn tạo trình lặp dễ dàng hơn, JavaScript cung cấp cho bạn **các hàm tạo**, sử dụng từ khóa `function*` (là `function` với dấu `*` ở cuối) và từ khóa `yield`.


Chúng ta hãy thử nhé:


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


Mỗi `yield` trả về một giá trị và **tạm dừng** hàm cho đến khi `.next()` tiếp theo được gọi.


Bạn cũng có thể lặp lại trình tạo bằng `for...of`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Bản in này:


```
1
2
3
```


## Đồng thời với các lệnh gọi lại

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Cho đến nay, mã của chúng tôi vẫn **đồng bộ**: nó chạy từng dòng một, theo thứ tự. Nhưng một số việc trong thế giới thực đòi hỏi thời gian, và chúng tôi không muốn toàn bộ chương trình bị tạm dừng trong khi chờ đợi.


Trong chương này, chúng ta sẽ giới thiệu một khái niệm mới: **đồng thời**. Nó cho phép chúng ta điều chỉnh thứ tự thực hiện các tác vụ. Điều này hữu ích khi xử lý các tác vụ như bộ đếm thời gian, dữ liệu đầu vào của người dùng hoặc đọc tệp từ đĩa. JavaScript cung cấp nhiều công cụ khác nhau để thực hiện đồng thời.


### `đặt thời gian chờ`


Hàm `setTimeout` cho phép bạn **chạy một hàm sau**, sau một khoảng thời gian.


Ví dụ:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Bản in này:


```
Start
End
This runs after 2 seconds
```


Mặc dù `setTimeout` xuất hiện ở giữa mã, nhưng nó không chặn phần còn lại. Thay vào đó, nó lên lịch cho hàm chạy **sau** và ngay lập tức chuyển sang bước tiếp theo.


`2000` nghĩa là 2000 mili giây (tương đương 2 giây).

Sau đây là bản viết lại chi tiết hơn và thân thiện hơn với người mới bắt đầu của các phần **Callbacks** và **Promise**, sử dụng thao tác dữ liệu và chú thích rõ ràng trong suốt quá trình:


### Gọi lại


**Callback** chỉ là một hàm mà chúng ta cung cấp cho một hàm khác để có thể **gọi sau**.


Hãy xem xét một ví dụ thực tế sử dụng số. Hãy tưởng tượng chúng ta có một danh sách các số và muốn nhân đôi từng số, sau đó áp dụng một hàm (hàm gọi lại) vào mảng "nhân đôi" kết quả, nhưng chúng ta muốn thực hiện việc này sau một khoảng thời gian trễ nhỏ, như thể chúng ta đang chờ một tác vụ chậm (chẳng hạn như tải dữ liệu từ internet).


Sau đây là một hàm thực hiện điều đó bằng cách sử dụng **callback**:


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


Chúng ta hãy thử sử dụng hàm này:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


Sau 1 giây, thông tin này sẽ in ra:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**Chuyện gì đang xảy ra ở đây?**


1. Chúng ta truyền `input` làm danh sách các số mà chúng ta muốn nhân đôi.

2. Chúng ta cũng truyền một **hàm gọi lại** để cho chương trình biết phải làm gì *sau* khi nhân đôi.

3. Bên trong `doubleNumbers`, chúng ta mô phỏng độ trễ bằng cách sử dụng `setTimeout`, sau đó chúng ta thực hiện nhân đôi.

4. Sau khi hoàn tất, chúng ta gọi hàm callback trên mảng "doubled" kết quả.


Kỹ thuật này hiệu quả, nhưng hãy tưởng tượng bạn muốn thực hiện **nhiều bước hơn** sau đó, chẳng hạn như lọc ra các số nhỏ rồi cộng chúng lại. Bạn sẽ phải **lồng ghép** thêm nhiều hàm callback như thế này:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Đọc thì thấy Hard hơi lộn xộn. Kiểu này được gọi là **callback hell**, và đó chính xác là mục đích mà `Promise` được tạo ra.


## Đồng thời với Promises

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


`Promise` là một đối tượng JavaScript tích hợp biểu thị một giá trị sẽ **sẵn sàng trong tương lai**.


Chúng ta có thể tạo một Promise như thế này:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


Phần `new Promise()` tạo ra lời hứa.


Bên trong nó, chúng ta cung cấp cho nó một hàm có hai tham số:



- `resolve`, là một hàm chúng ta gọi khi mọi thứ thành công
- `reject`, là một hàm chúng ta gọi nếu có điều gì đó không ổn


Trong ví dụ trên, chúng ta chỉ giải quyết ngay lập tức bằng thông báo `"Đã hoạt động!"`.


### `.then()`


Để thực hiện một việc gì đó **sau khi** lời hứa được thực hiện, chúng ta sử dụng `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Bản in này:


```
The result is: 100
```


Giá trị chúng ta truyền vào `resolve()` sẽ được gửi đến hàm bên trong `.then()` dưới dạng `result`.


Hãy mô phỏng một tác vụ mất 2 giây bằng cách sử dụng `setTimeout`:


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


Lệnh này sẽ đợi 2 giây rồi in ra:


```
Done waiting!
```


### `từ chối()`


Hãy tạo một lời hứa **thất bại**:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


Bây giờ nếu chúng ta sử dụng `.then()` cho trường hợp này, sẽ không có gì xảy ra, vì `.then()` chỉ xử lý thành công.


Để xử lý lỗi, chúng ta sử dụng `.catch()`:


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


Chỉ in này


```
Caught an error: Something went wrong
```


Giá trị được truyền vào `reject()` sẽ được gửi đến hàm `.catch()`.


Hãy xây dựng một Promise **đôi khi hoạt động và đôi khi thất bại**, dựa trên một số điều kiện.


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


Bây giờ chúng ta có thể gọi nó và xử lý cả hai trường hợp:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Bản in này:


```
Success: Positive number
```


Và nếu chúng ta thử với một số khác:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Nó in ra:


```
Failure: Not a positive number
```


### Chuỗi các hoạt động sử dụng `Promise`



Chúng ta có thể viết lại ví dụ trước đó bằng cách sử dụng `Promise` và nó sẽ trông gọn gàng hơn nhiều.


Chúng ta hãy bắt đầu bằng cách viết một phiên bản mới của hàm nhân đôi, nhưng lần này, nó trả về một **lời hứa**:


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


Bây giờ chúng ta có thể sử dụng `.then()` để cho JavaScript biết phải làm gì với kết quả:


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


Bản in này:


```
Doubled numbers: [ 2, 4, 6 ]
```


Cho đến nay, cách này hoạt động giống như phiên bản gọi lại, nhưng bây giờ mã dễ mở rộng và đọc hơn.


Giả sử chúng ta muốn thêm nhiều bước hơn:


1. Đầu tiên, nhân đôi tất cả các số

2. Sau đó, loại bỏ các số nhỏ hơn 4

3. Cuối cùng, cộng tất cả lại với nhau


Chúng ta có thể viết một hàm cho mỗi bước, tất cả đều sử dụng lời hứa:


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


Bây giờ chúng ta có thể **xâu chuỗi** chúng lại với nhau như thế này:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


Bản in này:


```
Final result after all steps: 10
```


Chúng ta hãy cùng tìm hiểu xem điều này có tác dụng gì:


1. `doubleNumbers` nhân đôi mảng: `[2, 4, 6]`

2. `filterBigNumbers` xóa bất kỳ thứ gì ≤ 3: `[4, 6]`

3. `sumNumbers` cộng các số còn lại: `4 + 6 = 10`

4. Cuối cùng, chúng ta in kết quả.


Mỗi `.then()` chờ bước trước khi hoàn tất. Vì vậy, chúng ta có thể xây dựng một **chuỗi hành động** mà không cần lồng nhau. Điều này giúp mã dễ đọc hơn và dễ gỡ lỗi hơn.


## Đồng thời với `async`/`await`

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Chúng ta đã thấy chuỗi `Promise` giúp chúng ta tránh được lỗi gọi lại, nhưng chúng vẫn có thể khiến Hard đọc được một chút khi có nhiều bước liên quan.


Đó là lúc `async` và `await` xuất hiện. Chúng cho phép chúng ta viết mã bất đồng bộ **trông giống như mã đồng bộ**, giúp dễ hiểu hơn.


### `Async` là gì?


Khi bạn viết từ khóa `async` trước một hàm, JavaScript sẽ tự động gói giá trị trả về của hàm trong một Promise.


Chúng ta hãy xem một ví dụ cơ bản:


```javascript
async function greet() {
return "hello"
}
```


Nếu bạn gọi hàm này:


```javascript
const result = greet()
console.log(result)
```


Bạn sẽ thấy điều này:


```
Promise { 'hello' }
```


Mặc dù bạn vừa trả về một chuỗi, JavaScript vẫn chuyển đổi nó thành một Promise cho bạn. Bạn có thể lấy giá trị thực tế bằng cách sử dụng `.then()` như sau:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Hoặc bạn có thể sử dụng `await`...


### `await` là gì?


Từ khóa `await` cho JavaScript biết: "chờ cho đến khi Promise này hoàn tất, sau đó trả về kết quả".


Nhưng bạn chỉ có thể sử dụng `await` **bên trong một hàm bất đồng bộ**.


Hãy viết lại ví dụ bằng cách sử dụng `await`:


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


Bây giờ chúng ta có thể sử dụng kết quả như thể nó là một giá trị thông thường.


Bây giờ chúng ta hãy làm điều gì đó hữu ích hơn một chút.


### Mô phỏng sự chậm trễ với `await`


Chúng ta sẽ tạo một hàm `wait` đơn giản lấy một lượng mili giây làm đối số và chỉ giải quyết sau khoảng thời gian đó mà không làm gì khác:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


Chúng ta hãy thử sử dụng nó:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


Bản in này:


```
waiting 2 seconds...
done waiting
```


Bạn có thể nghĩ về `await` như là "tạm dừng ở đây cho đến khi lời hứa được thực hiện, sau đó tiếp tục".


Điều này cho phép bạn viết mã theo kiểu **từ trên xuống dưới** hoạt động không đồng bộ, không cần nối các lệnh gọi `.then()`.


### Đang chờ dữ liệu


Hãy sử dụng lại ví dụ trước, trong đó chúng ta nhân đôi các số, sau đó lọc, rồi tính tổng. Nhưng lần này, chúng ta sẽ sử dụng `async`/`await`.


Chúng ta sẽ tạo 3 hàm mô phỏng việc chờ đợi và trả về Promise:


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


Bây giờ chúng ta hãy viết hàm `async` để kết hợp chúng:


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


Bản in này:


```
Final result: 10
```


Cách này dễ đọc hơn nhiều so với việc nối `.then()` hoặc lồng các lệnh gọi lại.


Nó trông giống như một chương trình từng bước thông thường, nhưng nó vẫn hoạt động không đồng bộ.


## Trình lặp bất đồng bộ

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Bạn đã tìm hiểu về **trình lặp** và cách chúng ta có thể sử dụng `for...of` để lặp qua các mảng và các đối tượng lặp khác.


Nhưng nếu dữ liệu chúng ta muốn lặp lại mất thời gian để đến nơi thì sao?


Đôi khi chúng ta muốn lặp lại những thứ đến **không đồng bộ**, như tin nhắn từ cuộc trò chuyện, dòng từ tệp hoặc số từ nguồn chậm.


Để làm được điều đó, JavaScript cung cấp cho chúng ta **các trình lặp bất đồng bộ**.


### Các hàm tạo bất đồng bộ


Cách dễ nhất để tạo một trình lặp bất đồng bộ là sử dụng **hàm tạo bất đồng bộ**.


Chúng ta viết nó như thế này:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


Nó trông giống như một trình tạo thông thường, nhưng có `async` ở trước.


Bây giờ chúng ta có thể sử dụng `for await...of` để sử dụng các giá trị:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Lệnh này sẽ in ra:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Vậy sự khác biệt giữa máy phát điện thông thường và máy phát điện thông thường là gì?


Sự khác biệt là: bây giờ chúng ta có thể sử dụng `await` bên trong trình tạo.


Chúng ta hãy tạo lại trình trợ giúp trì hoãn:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


Bây giờ chúng ta hãy đưa ra các con số **một cách chậm rãi**:


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


Hãy thử sử dụng nó:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Tại sao nên sử dụng trình lặp bất đồng bộ?


Trình lặp bất đồng bộ hữu ích khi:



- Các giá trị không xuất hiện cùng một lúc.
- Bạn muốn xử lý từng vấn đề một, **khi chúng xuất hiện**.
- Bạn đang làm việc với Promises và muốn lặp lại theo cách gọn gàng.


Ví dụ, nếu bạn muốn tải từng tin nhắn từ máy chủ trò chuyện hoặc tải xuống một tệp lớn theo từng phần, trình lặp bất đồng bộ sẽ cho bạn cách viết vòng lặp `for` hoạt động với dữ liệu bị trì hoãn.


### `Symbol.asyncIterator`


Chúng ta cũng có thể sử dụng trình lặp bất đồng bộ trong các lớp tùy chỉnh.


Sau đây là một ví dụ tạo ra các số có độ trễ:


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


Bây giờ chúng ta có thể sử dụng `for await...of` giống như trước:


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


Điều này cho phép bạn tạo các đối tượng có thể được lặp lại một cách không đồng bộ


## Đường cú pháp Assignment

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Cú pháp đường" nghĩa là viết một cái gì đó ngắn gọn hơn hoặc dễ hiểu hơn, mà không thay đổi nội dung của nó. Đó chỉ là một cách diễn đạt hay hơn để diễn đạt cùng một điều.


JavaScript có một số cú pháp tích hợp cho phép chúng ta viết các khai báo gọn gàng và ngắn gọn hơn. Trong chương này, chúng ta sẽ xem xét cách gán giá trị dựa trên điều kiện, cập nhật biến bằng toán học, lấy giá trị từ mảng hoặc đối tượng, và sao chép hoặc kết hợp chúng với cú pháp đơn giản hơn.


### Toán tử ba ngôi


Trong JavaScript, bạn có thể gán giá trị dựa trên điều kiện bằng cách sử dụng **toán tử ba ngôi**, đây là cách viết tắt của `if...else`.


Thay vì làm:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Bạn có thể viết:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


Điều này có nghĩa là:



- Nếu `isMorning` là đúng, hãy sử dụng `"Chào buổi sáng"`
- Nếu không, hãy sử dụng `"Hello"`


Dạng tổng quát là:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Bạn cũng có thể sử dụng nó trong các biểu thức khác:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Chỉ cần đảm bảo sử dụng nó cho những quyết định **đơn giản**. Nếu logic phức tạp, hãy dùng `if...else`.


### Các nhà điều hành Assignment thay thế


JavaScript có **các toán tử phím tắt** để thực hiện các phép gán kết hợp với các phép toán.


Chúng ta hãy xem xét theo cách thông thường:


```javascript
let counter = 1
counter = counter + 1
```


Câu này có thể được rút gọn thành:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Sau đây là những điều phổ biến nhất:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Ví dụ:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Những điều này hữu ích khi bạn muốn cập nhật một biến bằng giá trị của chính nó.


### Phân hủy cấu trúc


**Phá cấu trúc** cho phép bạn lấy giá trị ra khỏi mảng hoặc đối tượng và lưu trữ chúng vào các biến một cách dễ dàng.


#### Mảng


Giả sử bạn có:


```javascript
const colors = ["red", "green", "blue"]
```


Thay vì làm:


```javascript
const first = colors[0]
const second = colors[1]
```


Bạn có thể làm:


```javascript
const [first, second] = colors
```


Điều này chỉ định:



- `đầu tiên` đến `"đỏ"`
- `thứ hai` đến `"Green"`


Bạn cũng có thể bỏ qua các giá trị:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Đối tượng


Bạn cũng có thể trích xuất giá trị từ các đối tượng:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Nếu thuộc tính có tên khác với biến bạn muốn, bạn có thể đổi tên nó:


```javascript
const { name: username } = user
console.log(username) // Alice
```


Phân tích cấu trúc giúp mã của bạn sạch hơn khi làm việc với các đối tượng và mảng.


### Cú pháp lan truyền


**Cú pháp lan truyền** sử dụng `...` để giải nén hoặc sao chép các giá trị.


#### Mảng


Bạn có thể sao chép hoặc hợp nhất các mảng:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Bạn cũng có thể sao chép một mảng:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Đối tượng


Bạn có thể làm tương tự với các đối tượng:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Bạn cũng có thể ghi đè các giá trị:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


Điều này rất hữu ích khi cập nhật đối tượng mà không thay đổi đối tượng gốc.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Chúng tôi đã đến Node như thế nào

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


Trong chương này chúng ta sẽ tìm hiểu một chút về bối cảnh lịch sử của JavaScript và NodeJS.


Bối cảnh lịch sử rất quan trọng trong phần mềm, vì chúng ta thường sử dụng các công cụ do người khác xây dựng và do đó chúng ta bị ảnh hưởng bởi các quyết định mà họ đưa ra trong quá khứ.


Hiểu được lý do cho những quyết định đó và cách chúng ta sử dụng các công cụ như vậy sẽ giúp chúng ta cảm thấy bớt bối rối hơn về những gì mình đang làm.


### Nguồn gốc của JavaScript


JavaScript ban đầu là một ngôn ngữ đơn giản được thiết kế để làm cho các trang web có tính tương tác.


Vào những năm 1990, các trình duyệt web như Netscape Navigator đã bổ sung JavaScript để các nhà phát triển có thể viết mã chạy trực tiếp trên trình duyệt.


Ý tưởng ban đầu là sử dụng Java làm ngôn ngữ cốt lõi để tạo trang web (với cái gọi là "ứng dụng Java") và JavaScript chỉ dành cho những mục đích nhỏ nhặt.


Thiết kế cốt lõi được thực hiện bởi Brendan Eich, lúc đó là nhân viên của Netscape, trong vòng chưa đầy 2 tuần.


Nhưng hầu hết mọi người thích sử dụng JavaScript hơn Java, và các ứng dụng Java cũng có một số vấn đề về bảo mật vào thời điểm đó, vì vậy cuối cùng Java đã không còn là một lựa chọn nữa và JavaScript đã trở thành tiêu chuẩn thực tế cho phát triển web.


### Động cơ V8


JavaScript là ngôn ngữ được thông dịch, trái ngược với ngôn ngữ được biên dịch như C.


Mã được viết bằng ngôn ngữ biên dịch sẽ được chuyển thành mã nhị phân và mã nhị phân này sẽ được đưa trực tiếp vào CPU của máy tính.


![](assets/en/6.webp)


Ngược lại, các ngôn ngữ được thông dịch có xu hướng thân thiện với người dùng hơn và gần với cách con người suy nghĩ ("cấp cao") hơn là cách máy móc hoạt động ("cấp thấp"); do đó, chúng thường có một máy ảo được xây dựng để chạy mã của chúng.


Máy ảo là một chương trình đặc biệt nằm giữa mã bạn viết và CPU, và thực thi mã của bạn (vì CPU không thể hiểu được mã đó).


Điều này cho phép bạn lập trình mà không cần biết quá nhiều về máy tính cơ bản, nhưng nó cũng phải trả giá về mặt hiệu suất, vì máy tính không chỉ chạy chương trình của bạn; nó chạy một chương trình (máy ảo) chạy chương trình đó.


Khi các ứng dụng web ngày càng phức tạp, nhu cầu cải thiện hiệu suất của JavaScript cũng tăng cao. Công cụ V8 là trình thông dịch hỗ trợ JavaScript trong Google Chrome. Công cụ này được Google phát triển và phát hành vào năm 2008.


Trong khi các công cụ JavaScript cũ chủ yếu là máy ảo truyền thống thì công cụ V8 là trình biên dịch JIT (just-in-time).


Mã JavaScript được đưa vào engine V8, và engine này sẽ cố gắng biên dịch các phần của mã thành các tệp nhị phân gốc ngay lập tức. Điều này cho phép bạn trải nghiệm ngôn ngữ cấp cao với hiệu suất gần bằng ngôn ngữ cấp thấp. Điều này đã biến JavaScript thành ngôn ngữ cấp cao nhanh nhất thế giới, một thứ gì đó "tốt nhất của cả hai thế giới".


### Thời gian chạy NodeJS


Mặc dù dễ sử dụng và thực thi khá nhanh, nhưng sau khi phát hành V8, JavaScript vẫn có một hạn chế rất lớn: nó chỉ có thể chạy trong trình duyệt.


Tại sao điều đó lại là vấn đề?


Vâng, vì trình duyệt thực thi mã được lấy từ hàng triệu nguồn khác nhau trên Internet nên chúng có thể dễ dàng bị nhiễm phần mềm độc hại, do đó chúng được "cách ly" khỏi phần còn lại của hệ điều hành.


![](assets/en/7.webp)


JavaScript không thể truy cập vào hệ thống tệp và các tài nguyên cục bộ khác trên máy tính của bạn (ít nhất là không dễ dàng như các ngôn ngữ khác), do đó, đây là một hạn chế đáng kể đối với loại ứng dụng bạn có thể xây dựng bằng JavaScript.


Năm 2009, Ryan Dahl đã xuất bản NodeJS, một môi trường chạy thực tế cho phép bạn sử dụng engine V8 bên ngoài trình duyệt, trực tiếp trên hệ điều hành gốc của máy tính. Nó cũng bổ sung nhiều tính năng hữu ích cho việc viết các chương trình phía máy chủ và dòng lệnh. Ví dụ: bạn có thể sử dụng NodeJS để tạo máy chủ web, đọc và ghi tệp, hoặc xây dựng các công cụ tự động hóa tác vụ.


![](assets/en/8.webp)


Trong khóa học này, chúng ta đã tìm hiểu các tính năng JavaScript có trong cả trình duyệt và NodeJS. Những tính năng này cho phép chúng ta định nghĩa và thao tác dữ liệu theo những cách trừu tượng. Trong vài bài học tiếp theo, chúng ta sẽ khám phá các tính năng dành riêng cho NodeJS và cho phép chúng ta tương tác với hệ điều hành.


## Đối số dòng lệnh

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS cho phép chúng ta xây dựng CLI (Giao diện dòng lệnh) cùng nhiều tính năng khác.


Để làm được điều đó, chúng ta cần một cách để nhận các đối số dòng lệnh, trong Node, điều này được thực hiện bằng cách sử dụng đối tượng `process` tích hợp sẵn.


### `quy trình`


NodeJS cung cấp một đối tượng đặc biệt gọi là `process` biểu diễn chương trình đang chạy hiện tại.


Bạn có thể sử dụng nó để kiểm tra môi trường, thư mục làm việc hiện tại và thậm chí thoát khỏi chương trình khi cần.


Ví dụ:


```javascript
console.log(process.platform)
```


Lệnh này sẽ in ra nền tảng hệ điều hành, như `win32`, `linux` hoặc `darwin` (Mac).


### `process.argv`


Khi bạn chạy chương trình NodeJS từ terminal, bạn có thể truyền thêm các từ (đối số) sau tên tập lệnh. Các từ này được lưu trữ trong `process.argv`.


Ví dụ, nếu bạn chạy lệnh này:


```
node my_script.js alpha beta
```


Bạn có thể in các đối số như thế này:


```javascript
console.log(process.argv)
```


Kết quả đầu ra có thể trông như thế này:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


Hai mục đầu tiên luôn là đường dẫn Node và đường dẫn tập lệnh của bạn. Bất kỳ từ nào bạn truyền vào tập lệnh sẽ nằm sau đó.


Mảng `process.argv` có thể được cắt như bất kỳ mảng nào khác bằng phương thức `.slice()`, do đó để chỉ lấy các đối số đã được truyền, bạn có thể làm


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Việc truy cập vào các đối số mà người dùng truyền đi là điều cơ bản để phát triển các ứng dụng dòng lệnh.


## Các mô-đun

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


Các thời gian chạy JavaScript như NodeJS thường coi mỗi tệp JavaScript là một mô-đun riêng biệt.


Hãy hình dung một module như một hộp. Hộp có không gian riêng, vì vậy các biến và hàm bạn khai báo trong đó không ảnh hưởng đến mã trong các hộp khác. Về cơ bản, mỗi module có phạm vi riêng.


Một mô-đun có thể xuất một số nội dung của nó, cho phép các mô-đun khác truy cập, và có thể nhập nội dung mà các mô-đun khác đã xuất. JavaScript cho phép bạn xuất và nhập nội dung giữa các mô-đun, để kết nối các tệp khác nhau.


Một chương trình JavaScript thường bao gồm nhiều mô-đun được kết nối với nhau.


Tại sao nên sử dụng mô-đun? Bằng cách chia mã thành các mô-đun, bạn có thể sắp xếp chương trình thành các phần nhỏ hơn, rõ ràng hơn và có thể tái sử dụng. Mỗi mô-đun chỉ có thể tập trung vào một loại tác vụ, chẳng hạn như xử lý các phép tính toán học, làm việc với tệp hoặc định dạng văn bản.


### Các mô-đun CommonJS


Trong NodeJS, hệ thống phổ biến nhất để quản lý các mô-đun được gọi là **CommonJS**.


Trong hệ thống này, bạn có thể chia sẻ (xuất) mã từ một mô-đun bằng cách sử dụng `module.exports` và tải (nhập) mã đó vào một tệp khác bằng cách sử dụng `require()`.


Để làm cho một thứ gì đó có sẵn bên ngoài một mô-đun, bạn gán nó cho `module.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


Ở đây, chuỗi `"Hello!"` là chuỗi mà mô-đun này xuất ra.


Để sử dụng mã được xuất từ tệp khác, bạn sử dụng hàm `require()` với đường dẫn đến tệp đó:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Bản in này:


```
Hello!
```


Bạn có thể xuất nhiều thứ bằng cách gom chúng lại với nhau trong một đối tượng ẩn danh, như


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS là hệ thống module ban đầu được NodeJS áp dụng. Sau đó, các module ES cũng được thêm vào.


### Mô-đun ES


NodeJS cũng hỗ trợ một loại module khác gọi là **ES Modules**, rất phổ biến trong phát triển web. Chúng sử dụng các từ khóa `export` và `import`.


Các mô-đun ES được phát triển cho trình duyệt và sau đó mới được thêm vào Node. Nếu muốn sử dụng chúng, bạn có thể phải sử dụng `.mjs` làm phần mở rộng tệp thay vì `.js`, tùy thuộc vào phiên bản Node bạn đang sử dụng.


Trong một tập tin có tên `greeting.mjs` chúng tôi viết


```javascript
export const greeting = "Hello!"
```

Như bạn có thể thấy, chúng ta đang xuất hằng số trực tiếp đến nơi nó được định nghĩa


Trong một tệp khác có tên là `index.mjs`, chúng tôi nhập nó:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


Bạn có thể xuất các khai báo khác nhau ở các phần khác nhau của tệp, như


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### Thư viện chuẩn NodeJS


NodeJS cũng bao gồm nhiều module tích hợp sẵn. Đây là những module được NodeJS cung cấp sẵn, hỗ trợ các tác vụ phổ biến như đọc tệp, làm việc với hệ điều hành hoặc kết nối mạng.


Ví dụ, mô-đun `os` cung cấp cho bạn thông tin về hệ điều hành của bạn:


```javascript
const os = require("os")

console.log(os.platform())
```


Bạn không cần phải cài đặt các module tích hợp này, chúng đi kèm với NodeJS. Chúng tạo thành "thư viện chuẩn" của thời gian chạy và được hầu hết các ứng dụng Node sử dụng để thực hiện các tác vụ như đọc tệp hoặc giao tiếp qua internet.


Các chương tiếp theo sẽ chỉ cho bạn một số ví dụ hữu ích về cách sử dụng chúng.


## Mô-đun `fs`

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


Mô-đun `fs` (viết tắt của **hệ thống tệp**) là một phần của thư viện chuẩn NodeJS. Nó cho phép bạn làm việc với tệp và thư mục trên máy tính: bạn có thể đọc tệp, ghi tệp, xóa tệp, đổi tên tệp, v.v.


Để sử dụng, trước tiên bạn cần nhập nó vào đầu tệp của mình:


```javascript
const fs = require("fs")
```


### API đồng bộ hóa


Cách đơn giản nhất để sử dụng `fs` là sử dụng phương thức **sync** của nó.


Các phương pháp này chặn chương trình cho đến khi chúng hoàn tất (do đó dòng mã tiếp theo sẽ không chạy cho đến khi thao tác hoàn tất).


Sau đây là một ví dụ về cách đọc tệp đồng bộ:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Nếu có tệp có tên `example.txt` trong cùng thư mục với tập lệnh của bạn, lệnh này sẽ in nội dung của tệp đó.


Bạn cũng có thể ghi vào tệp một cách đồng bộ:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Thao tác này sẽ tạo (hoặc ghi đè) một tệp có tên `output.txt` bằng văn bản.


Sau đây là một số thao tác phổ biến bạn có thể thực hiện với API này:


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


API đồng bộ hóa đơn giản và phù hợp với các tập lệnh nhỏ, nhưng vì nó chặn chương trình cho đến khi hoàn tất nên có thể làm chậm chương trình nếu bạn làm việc với các tệp lớn hoặc máy chủ.


### API gọi lại không đồng bộ


**API gọi lại** không chặn: nó cho phép NodeJS tiếp tục thực hiện các tác vụ khác trong khi thao tác tệp diễn ra.


Thay vì trả về kết quả trực tiếp, nó sử dụng một hàm (một **callback**) được gọi khi thao tác hoàn tất.


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


Sau đây là những gì xảy ra:



- `fs.readFile` bắt đầu đọc `example.txt`.
- NodeJS không chờ đợi, nó sẽ tiếp tục thực thi mã khác mà bạn có thể đã viết.
- Khi tệp được đọc xong, lệnh gọi lại sẽ chạy:



  - Nếu có lỗi, `err` sẽ chứa lỗi đó.
  - Nếu không, `data` sẽ chứa nội dung.


Sau đây là cách bạn ghi vào một tệp:


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


Ý tưởng tương tự: chương trình không dừng lại khi ghi tệp.


Một số ví dụ về những điều bạn có thể làm với API này:


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


API callback phù hợp hơn với máy chủ và các tác vụ lớn vì nó không làm tắc nghẽn chương trình, nhưng các callback lồng nhau có thể trở nên lộn xộn nếu bạn nối nhiều thao tác. Đó là lý do tại sao API async dựa trên promise được thêm vào.


### API hứa hẹn không đồng bộ


API dựa trên Promise rất hiện đại và hoạt động tốt với `.then()` và `async/await`. API này có sẵn dưới dạng `fs.promises`.


Bạn cần nhập thuộc tính `promises`:


```javascript
const fs = require("fs").promises
```


Sử dụng `.then()`:


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


Hoặc thậm chí tốt hơn, sử dụng `async/await`:


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


Ghi vào một tập tin:


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


Danh sách ví dụ thông thường cho API:


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


Khi viết mã, bạn thường sẽ cần sử dụng mã do người khác viết; ví dụ, các thư viện giúp bạn làm việc với ngày tháng, màu sắc, máy chủ hoặc hầu hết mọi thứ khác.


Thay vì tải xuống và sao chép tệp theo cách thủ công, bạn có thể sử dụng **trình quản lý gói**.


Trình quản lý gói là một công cụ:



- tải xuống các gói
- theo dõi các gói mà dự án của bạn cần
- đảm bảo mọi người trong nhóm của bạn đều có cùng phiên bản gói


### NPM là gì


Trong thế giới NodeJS, trình quản lý gói phổ biến nhất là **NPM**, viết tắt của *Node Package Manager*.


Bạn sẽ tự động nhận được NPM khi cài đặt NodeJS.


Bạn có thể kiểm tra xem mình có NPM hay không bằng cách chạy lệnh này trong terminal:


```
npm -v
```


Lệnh này sẽ in ra phiên bản NPM của bạn, như sau:


```
10.2.1
```


### Tạo một gói


Trong NodeJS, **gói** chỉ là một thư mục có chứa tệp `package.json`.


Chúng ta hãy cùng tạo từng bước một.


1. Tạo một thư mục mới cho dự án của bạn:


```
mkdir my_project
cd my_project
```


2. Chạy lệnh này:


```
npm init
```


Thao tác này sẽ bắt đầu thiết lập tương tác, hỏi bạn những câu hỏi như tên dự án, phiên bản, mô tả, v.v.


Nếu bạn không muốn trả lời mọi thứ và chỉ chấp nhận các giá trị mặc định, bạn có thể sử dụng:


```
npm init -y
```


Sau khi chạy, bạn sẽ thấy một tệp mới trong thư mục của mình có tên là:


```
package.json
```


### `gói.json`


Tệp `package.json` chỉ là tệp JSON lưu trữ siêu dữ liệu về dự án của bạn.


Sau đây là một ví dụ:


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


Một số lĩnh vực quan trọng:



- `name`: tên gói của bạn
- `version`: phiên bản hiện tại
- `main`: tệp điểm vào (như `index.js`)
- `scripts`: các lệnh bạn có thể chạy (như `npm start`)
- `dependencies`: liệt kê tất cả các gói mà dự án của bạn phụ thuộc vào


### Cài đặt gói


Giả sử bạn muốn sử dụng một gói nhất định có tên là `picocolors` để thêm màu vào đầu ra của thiết bị đầu cuối.


Bạn có thể cài đặt bằng cách chạy:


```
npm install picocolors
```


Bây giờ bạn có thể sử dụng nó trong dự án của mình. Tạo một tệp `index.js` với


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


và thử chạy nó. Thiết bị đầu cuối sẽ in ra phiên bản màu của văn bản.


NPM đã làm gì?



- Nó đã tải xuống gói và lưu trữ nó trong một thư mục con có tên là `node_modules/`
- nó đã thêm một mục trong `dependencies` vào `package.json` của bạn
- nó đã cập nhật tệp `package-lock.json`


`package-lock.json` là gì?


### `package-lock.json`


Tệp này được NPM tự động tạo ra.


Bạn có thể thắc mắc, nếu chúng ta đã có `package.json`, tại sao chúng ta lại cần một tệp khác?

Sau đây là lý do:



- `package.json` chỉ cho biết **phạm vi** phiên bản nào của gói mà dự án của bạn cần.

Ví dụ:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


`^1.1.0` có nghĩa là "bất kỳ phiên bản nào tương thích với 1.1.x", do đó rất linh hoạt.



- `package-lock.json` **đóng băng** phiên bản chính xác của từng gói và các gói phụ thuộc của chúng, để mọi người cài đặt dự án của bạn đều có cùng một thiết lập hoạt động.


Tại sao điều này lại quan trọng?


Nếu bạn làm việc theo nhóm, hoặc triển khai dự án của mình lên máy chủ, hoặc quay lại dự án trong tương lai, bạn muốn đảm bảo rằng dự án vẫn hoạt động theo cùng một cách.

Nếu các gói đã được cập nhật và bạn cài đặt lại mà không có tệp khóa, bạn có thể nhận được phiên bản hơi khác và hoạt động khác.


Bằng cách giữ `package-lock.json` trong dự án của bạn, NPM sẽ luôn cài đặt các phiên bản chính xác được liệt kê ở đó, đảm bảo rằng mọi người đều có cùng một môi trường.


`package-lock.json` khóa mọi thứ vào một phiên bản rất cụ thể, để làm cho dự án có thể tái tạo được trên các máy khác.


Nhưng nếu gói của bạn cần được nhiều người sử dụng, bạn có thể chọn không xác nhận nó, để NPM chỉ tìm thấy tệp `package.json` và được phép tự động cài đặt các phiên bản mới nhất được phép trong tệp đó.


Nhưng đây là những điều bạn nên quan tâm sau, khi bạn bắt đầu xuất bản mã của riêng mình. Hiện tại, chúng tôi đã giới thiệu những điều cơ bản về NPM chỉ để cho phép bạn tìm và sử dụng các thư viện do các nhà phát triển khác xuất bản trong dự án của bạn.



## Mạng trong NodeJS

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS thường được sử dụng làm ngôn ngữ cho phần phụ trợ: bạn có thể biến tập lệnh của mình thành máy chủ và cũng có thể sử dụng nó để gửi yêu cầu tới các máy chủ khác.


Trong chương này, chúng tôi sẽ giới thiệu một số tính năng mạng cơ bản cho phép bạn thực hiện điều đó.


### `lấy()`


Nếu bạn muốn chương trình của mình tải xuống dữ liệu từ một trang web hoặc API, bạn cần phải thực hiện **yêu cầu HTTP**.


Trong các phiên bản NodeJS hiện đại, bạn có thể sử dụng hàm `fetch()` tích hợp sẵn.


Sau đây là ví dụ về cách thực hiện yêu cầu GET tới API:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Khi bạn chạy lệnh này, bạn sẽ thấy nội dung tương tự như sau:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


Sau đây là những gì xảy ra:


1. `fetch()` lấy một URL và đưa ra yêu cầu.

2. Nó trả về một **Promise** giải quyết thành một đối tượng `Response`.

3. `response.text()` đọc nội dung phản hồi dưới dạng một chuỗi.


Nhưng chuỗi bạn nhận được thực ra là JSON. Đó là gì?


### JSON


Khi làm việc với API web, dữ liệu thường được gửi và nhận dưới dạng **JSON**, viết tắt của JavaScript Object Notation.


JSON chỉ là một định dạng văn bản trông rất giống các đối tượng JavaScript. Ví dụ:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


Đối tượng `JSON` là một tiện ích tích hợp trong JavaScript có thể được sử dụng để làm việc với định dạng dữ liệu này.


Bạn có thể chuyển đổi một đối tượng JavaScript thành chuỗi JSON bằng cách sử dụng `JSON.stringify()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Bản in này:


```
{"name":"Alice","age":30}
```


Bạn cũng có thể chuyển đổi văn bản JSON trở lại thành đối tượng JavaScript bằng cách sử dụng `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Bản in này:


```
{ name: 'Bob', age: 25 }
```


Hãy cẩn thận: `JSON.parse()` sẽ báo lỗi nếu chuỗi không phải là JSON hợp lệ.


```javascript
JSON.parse("not json") // ❌ Error!
```


Vì vậy hãy đảm bảo chuỗi được định dạng đúng.


### máy chủ `http`


NodeJS cho phép bạn tạo máy chủ web mà không cần cài đặt bất cứ thứ gì khác.


Bạn có thể sử dụng mô-đun `http` tích hợp để xử lý các yêu cầu từ máy khách và gửi phản hồi lại.


Sau đây là một ví dụ rất cơ bản:


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


Khi bạn chạy tập lệnh này và mở `http://localhost:3000` trong trình duyệt của mình, bạn sẽ thấy:


```
Hello from NodeJS server!
```


Đây là những gì đang xảy ra trong mã:


1. Bạn đã nhập máy chủ `http` từ thư viện chuẩn Node.

2. `http.createServer()` tạo một máy chủ. Bạn đã truyền cho `http.createServer()` một lệnh gọi lại `(req, res) => {...}` để được thực thi mỗi khi có người kết nối.

3. Bạn đã gán mã trạng thái 200 (biểu thị thao tác thành công) cho phản hồi. Bạn có thể đọc về mã trạng thái http [tại đây](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` gửi phản hồi và kết thúc kết nối.

4. `server.listen(3000)` khởi động máy chủ trên cổng 3000.


Bạn cũng có thể kiểm tra `req.url` và `req.method` trong yêu cầu để xử lý các đường dẫn hoặc loại yêu cầu khác nhau.


Ví dụ với định tuyến:


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


Đây là những ví dụ rất cơ bản. Để xây dựng các máy chủ tiên tiến hơn, hầu hết các nhà phát triển có thể sẽ tải xuống một thư viện back-end có sẵn như [express](https://www.npmjs.com/package/express).


## Xử lý dữ liệu: bộ đệm, sự kiện, luồng

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


Trong chương này chúng ta sẽ giới thiệu chủ yếu ba lớp đối tượng:



- `Buffer`, biểu diễn các khối dữ liệu nhị phân nhỏ
- `EventEmitter`, có thể được sử dụng để theo dõi một số bước của quy trình không đồng bộ bằng cách phát ra các tín hiệu gọi là "sự kiện"
- `Stream`, cho phép chúng ta xử lý phần lớn dữ liệu tại một `Buffer` tại một thời điểm và theo dõi quá trình bằng cách phát ra các sự kiện


Những điều này cực kỳ phổ biến trong mã NodeJS chuyên nghiệp, vì vậy ngay cả khi bạn có thể không sử dụng chúng trong các dự án đầu tiên của mình, thì việc có được hiểu biết cơ bản về thời điểm bạn cần tương tác với chúng vẫn rất tốt.


### Bộ đệm


Trong NodeJS, **bộ đệm** là một loại đối tượng được sử dụng để làm việc với dữ liệu nhị phân.


Bạn có thể coi bộ đệm như một thùng chứa có kích thước cố định dành cho các byte thô.


Sau đây là cách tạo bộ đệm từ một chuỗi:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


Điều này in ra nội dung tương tự như sau:


```
<Buffer 68 65 6c 6c 6f>
```


Những con số đó (`68`, `65`, `6c`, v.v.) là biểu diễn thập lục phân của các chữ cái trong `"hello"`.


Bạn có thể chuyển đổi nó trở lại thành chuỗi như thế này:


```javascript
console.log(buf.toString())
```


Bản in này:


```
hello
```


Bạn cũng có thể tạo một vùng đệm có kích thước nhất định chứa đầy số không:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


Điều này in ra nội dung tương tự như sau:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


Bạn có thể ghi vào bộ đệm:


```javascript
buf.write("abc")
console.log(buf)
```


Và bạn có thể truy cập từng byte riêng lẻ:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Bộ đệm đặc biệt hữu ích khi bạn cần thao tác dữ liệu ở mức rất thấp.


### Sự kiện


Trong JavaScript, **sự kiện** là thứ gì đó xảy ra trong chương trình mà bạn có thể phản ứng.


Ví dụ:



- một tập tin hoàn tất việc tải
- một bộ đếm thời gian tắt
- người dùng nhấp vào một nút
- một yêu cầu mạng trả về dữ liệu


**Sự kiện** chỉ là tín hiệu cho thấy có điều gì đó đã xảy ra và bạn có thể viết mã để lắng nghe những sự kiện đó và phản ứng lại chúng.


Trong NodeJS, nhiều đối tượng có thể phát ra sự kiện. Những đối tượng này được gọi là **EventEmitters**.


Sau đây là một ví dụ:


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


Bản in này:


```
Hello! An event happened.
```


Sau đây là nội dung:


1. Chúng ta tạo một đối tượng `EventEmitter`.

2. Chúng ta yêu cầu nó chạy lệnh gọi lại bất cứ khi nào sự kiện `"greet"` xảy ra, bằng cách sử dụng `.on("greet")`.

3. Sau đó, chúng ta kích hoạt sự kiện `"greet"` bằng cách sử dụng `.emit()`.

4. Cuộc gọi lại của chúng tôi được thực thi


Bạn có thể truyền dữ liệu cùng với sự kiện:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Bản in này:


```
Hello, Alice!
```


Bạn cũng có thể đăng ký người nghe cho các sự kiện khác:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Bạn có thể gắn bao nhiêu trình lắng nghe tùy thích vào một loại sự kiện và có thể kích hoạt nhiều loại sự kiện khác nhau từ cùng một trình phát.


Nhiều đối tượng trong NodeJS phát ra các sự kiện để thông báo cho phần còn lại của chương trình rằng có điều gì đó đang xảy ra.



### Luồng là gì?


Luồng kết hợp bộ đệm và sự kiện để giúp chúng ta xử lý dữ liệu.


Khi làm việc với các tệp, dữ liệu từ mạng, hoặc thậm chí là văn bản dài, chúng ta không phải lúc nào cũng cần (hoặc muốn) tải tất cả vào bộ nhớ cùng một lúc. Điều này có thể gây chậm, hoặc thậm chí làm sập chương trình nếu dữ liệu quá lớn.


Thay vào đó, chúng ta có thể xử lý dữ liệu **từng chút một** khi nó đến hoặc được đọc, giống như việc uống nước bằng ống hút thay vì cố gắng uống hết cả cốc cùng một lúc. Đây được gọi là **dòng**.


Trong NodeJS, luồng là một đối tượng cho phép bạn đọc dữ liệu từ nguồn hoặc ghi dữ liệu vào đích **từng phần một**.


NodeJS có bốn loại luồng chính:



- Có thể đọc**: các luồng bạn có thể đọc dữ liệu từ đó (giống như đọc tệp)
- Có thể ghi**: các luồng bạn có thể ghi dữ liệu vào (giống như ghi vào tệp)
- Duplex**: luồng có thể đọc và ghi được
- Chuyển đổi**: giống như luồng song công, nhưng chúng có thể thay đổi (biến đổi) dữ liệu khi nó chảy


### Luồng có thể đọc được


Giả sử bạn có một tệp `bigfile.txt` cần xử lý. Bạn có thể tạo một luồng đọc được bằng mô-đun `fs` để đọc từng phần của tệp.


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


Chuyện gì xảy ra ở đây?


1. `fs.createReadStream()` tạo một luồng có thể đọc được.

2. Bất cứ khi nào một phần của tệp đã sẵn sàng, luồng sẽ phát ra sự kiện `data` và cung cấp cho chúng ta một "khối" dữ liệu (một `Buffer`). Chúng ta in khối dữ liệu này.

3. Khi toàn bộ tệp đã được đọc, sự kiện `end` sẽ được kích hoạt.

4. Nếu có lỗi (ví dụ như tệp không tồn tại), sự kiện `error` sẽ được kích hoạt.


Bằng cách này, bạn có thể đọc các tệp lớn mà không cần tải tất cả vào bộ nhớ cùng một lúc.


Nếu chúng ta muốn dữ liệu đến dưới dạng có thể đọc được bằng con người (thay vì dạng nhị phân), chúng ta có thể chỉ định mã hóa của luồng:


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


Bây giờ, mã sẽ in tệp theo dạng dễ đọc đối với con người.


### Luồng có thể ghi


Luồng có thể ghi cho phép bạn gửi dữ liệu đến một nơi nào đó, từng phần một.


Sau đây là ví dụ về cách ghi vào tệp `target.txt` bằng luồng:


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


Sau đây là những gì xảy ra:


1. `fs.createWriteStream()` tạo một luồng có thể ghi.

2. Chúng ta viết một số văn bản vào đó bằng cách sử dụng `.write()`.

3. Khi hoàn tất, chúng ta gọi `.end()` để đóng luồng.

4. Khi tất cả dữ liệu đã được ghi, sự kiện `finish` sẽ được phát ra.

5. Nếu có điều gì đó không ổn, sự kiện `error` sẽ được kích hoạt.


Giống như luồng có thể đọc, luồng có thể ghi rất phù hợp với dữ liệu lớn vì chúng không cần phải lưu trữ mọi thứ trong bộ nhớ cùng một lúc.


### Dòng chảy ống


Một trong những điều tuyệt vời nhất về luồng là bạn có thể **kết nối** chúng lại với nhau: kết nối trực tiếp luồng có thể đọc với luồng có thể ghi.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Đây:



- Luồng có thể đọc được sẽ đọc từ `bigfile.txt`.
- Luồng có thể ghi sẽ ghi vào `copy.txt`.
- `.pipe()` gửi dữ liệu trực tiếp từ luồng có thể đọc sang luồng có thể ghi.


### Luồng song công


Luồng song công có thể đọc và ghi được. Một ví dụ là ổ cắm mạng: bạn có thể gửi dữ liệu đến và nhận dữ liệu từ nó.


Sau đây là một ví dụ rất đơn giản sử dụng mô-đun `net`:


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


Trong ví dụ này:



- Đối tượng `socket` là một luồng song công.
- Bạn có thể `write()` vào đó và cũng có thể lắng nghe các sự kiện `data` từ đó.


### Chuyển đổi luồng


Luồng biến đổi là luồng song công cũng sửa đổi dữ liệu đi qua nó.


Ví dụ, bạn có thể sử dụng mô-đun `zlib` tích hợp sẵn để nén hoặc giải nén dữ liệu.


Sau đây là cách nén tệp bằng luồng chuyển đổi:


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


Và để giải nén nó trở lại:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


Luồng chuyển đổi rất hữu ích cho các tác vụ như nén, mã hóa hoặc thay đổi định dạng tệp trong khi phát trực tuyến.


### Áp suất ngược


Đôi khi luồng ghi chậm xử lý dữ liệu. Nếu chúng ta tiếp tục đẩy dữ liệu vào luồng ghi nhanh hơn khả năng xử lý của nó, chúng ta có thể gặp sự cố. Hiện tượng này được gọi là **áp lực ngược**.


Nếu bạn gọi phương thức `.write()` trên một luồng có thể ghi, nó sẽ trả về một giá trị boolean thông báo cho bạn biết liệu luồng có cần tạm dừng hay không; bạn có thể phải kiểm tra giá trị trả về của nó, như sau:


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


Đây là một ví dụ minh họa về cách chuyển dữ liệu thủ công từ Readable sang Writable và quản lý áp suất ngược theo cách thủ công.


Thông thường, chúng ta sẽ truyền dữ liệu bằng phương thức `.pipe()`, phương thức này tự động xử lý áp suất ngược.


Vì vậy, bạn chỉ cần lo lắng về áp suất ngược khi vì lý do nào đó bạn phải gọi thủ công `.write()`.


## Ghi chú cuối cùng

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


Vậy là xong, nếu bạn làm theo các bài học, bây giờ bạn sẽ có thể viết một số chương trình đơn giản bằng NodeJS.


Tôi khuyên bạn nên làm chính xác như vậy: sau khi học những kiến thức cơ bản, hãy xây dựng một vài dự án cá nhân là cách tốt nhất để thực hành và trở thành một lập trình viên giỏi hơn.


Thực ra, điều quan trọng không phải là bạn xây dựng cái gì, mà là bạn thử thách bản thân mình để giải quyết vấn đề bằng mã.


Các ngôn ngữ lập trình hiện đại cực kỳ mạnh mẽ và NodeJS có lẽ là công cụ tốt nhất để thử nghiệm trong giai đoạn này của hành trình.


Chúc may mắn!


# Phần cuối


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Đánh giá & Xếp hạng


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Phần kết luận


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>