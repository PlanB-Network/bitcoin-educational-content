---
name: พื้นฐาน JavaScript และ NodeJS
goal: เรียนรู้พื้นฐานการเขียนโปรแกรม JavaScript และการพัฒนา NodeJS เพื่อสร้างแอปพลิเคชันและเครื่องมือที่ใช้งานได้จริง
objectives: 

  - เรียนรู้ไวยากรณ์พื้นฐานของ JavaScript, ประเภทข้อมูล, และการควบคุมการไหล
  - ทำความเข้าใจฟังก์ชัน วัตถุ และคลาสใน JavaScript
  - เรียนรู้การจัดการข้อผิดพลาดและเทคนิคการดีบัก
  - ทำความรู้จักกับ NodeJS และระบบนิเวศของมัน

---

# เริ่มต้นการพัฒนาของคุณ


ยินดีต้อนรับสู่คอร์สนี้เกี่ยวกับ JavaScript และ NodeJS


JavaScript เป็นภาษาการเขียนโปรแกรมที่ได้รับความนิยมมากที่สุดในโลก: มันเป็นภาษาสคริปต์ของเบราว์เซอร์สมัยใหม่ ดังนั้นจึงแทบจะเป็นไปไม่ได้เลยที่จะสร้างเว็บแอปพลิเคชันสมัยใหม่โดยไม่เขียน *บางส่วน* ของ JavaScript; และด้วยรันไทม์ NodeJS มันสามารถใช้ภายนอกเบราว์เซอร์ได้เช่นกัน เพื่อสร้างสคริปต์และแอปพลิเคชันที่ทำงานโดยตรงบนคอมพิวเตอร์ของคุณ


หลักสูตรนี้ออกแบบมาสำหรับผู้ที่ไม่มีพื้นฐานการเขียนโปรแกรมเลย หรือผู้ที่เคยใช้ภาษาอื่นมาก่อนแต่ต้องการเข้าใจการทำงานของ JavaScript โดยเฉพาะในบริบทของ NodeJS


เมื่อสิ้นสุดหลักสูตร คุณควรจะสามารถเขียนโปรแกรมของคุณเองในภาษา JavaScript ใช้ไลบรารีมาตรฐานของ NodeJS และติดตั้งและใช้แพ็กเกจของบุคคลที่สามเพื่อสร้างเครื่องมือที่มีประโยชน์ได้


+++
# JavaScript พื้นฐาน

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## ตั้งค่า

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>


โปรแกรม JavaScript เป็นเพียงการรวบรวมไฟล์ข้อความ (หนึ่งไฟล์หรือมากกว่า) ที่มีคำสั่งให้ดำเนินการโดย JavaScript runtime


ชื่อของไฟล์ข้อความเหล่านี้มักจะลงท้ายด้วยนามสกุลไฟล์ `.js` เช่น `my_script.js`, `my_program.js` เป็นต้น


คำสั่งที่พวกเขามีเขียนด้วยภาษาโปรแกรม JavaScript


JavaScript runtime เป็นโปรแกรมพิเศษที่ทำการประมวลผลไฟล์เหล่านี้


![](assets/en/001.webp)


### รันไทม์ NodeJS


รันไทม์ JavaScript ที่พบมากที่สุดคือ NodeJS.


IDE ของคุณอาจมีอยู่แล้ว หรือคุณอาจจำเป็นต้องดาวน์โหลดจาก [เว็บไซต์ทางการ](https://nodejs.org/en/download)


หน้าดาวน์โหลดจะให้คำแนะนำสำหรับระบบปฏิบัติการหลักทั้งสาม (Operating Systems): Windows, Linux และ MacOS โดยสมมติว่าคุณรู้วิธีเปิดเทอร์มินัลในระบบปฏิบัติการของคุณแล้ว


เนื่องจาก NodeJS มีให้ใช้งานสำหรับระบบปฏิบัติการทั้งสาม ระบบ โปรแกรมที่คุณเขียนจะสามารถทำงานบนทั้งหมดได้ (ยกเว้นบางกรณีเฉพาะ)


ซึ่งหมายความว่าคุณสามารถเขียนวิดีโอเกมง่าย ๆ ใน JavaScript บน Windows PC ของคุณและส่งให้เพื่อนของคุณเพื่อรันบน Mac ของเขาได้


![](assets/en/002.webp)


### โปรแกรมแรก (สวัสดีชาวโลก)


ตามธรรมเนียม เมื่อศึกษาเกี่ยวกับภาษาโปรแกรม โปรแกรมแรกที่เขียนมักจะเป็นการพิมพ์ "hello world!" ไปยังคอนโซล


สร้างไดเรกทอรีชื่อ `my_js_code/` โดยภายในมีไฟล์ชื่อ `main.js` (ชื่อเหล่านี้สามารถตั้งได้ตามต้องการ)


เปิดไดเรกทอรีด้วยโปรแกรมแก้ไขโค้ดของคุณ


เขียนโค้ดนี้ลงในไฟล์ของคุณ:


```javascript
console.log("hello world!")
```


เปิดเทอร์มินัลและรันคำสั่งนี้เพื่อเรียกใช้โปรแกรม:


```
node main.js
```


ผลลัพธ์ควรเป็น


```
hello world!
```


### What Happened


ใน JavaScript ทุกอย่างคือ "อ็อบเจ็กต์"


`console` เป็นอ็อบเจ็กต์ที่ใช้ในการดีบักโปรแกรม


`console.log` เป็นเมธอดที่ใช้บ่อยที่สุดของ `console` มันจะแสดงผลอะไรก็ตามที่คุณส่งผ่านไปให้มัน


คุณส่งอาร์กิวเมนต์ไปยัง `console.log` โดยใช้วงเล็บกลม `()`.


ดังนั้น ตัวอย่างเช่น หากคุณต้องการพิมพ์ตัวเลข `1000` คุณก็แค่เขียน


```javascript
console.log(1000)
```


จากนั้นดำเนินการโดยการรัน


```
node main.js
```


ในเทอร์มินัลของคุณ (จากนี้ไป หลักสูตรนี้จะถือว่าคุณรู้ว่านี่คือวิธีการเรียกใช้โปรแกรม)


สิ่งนี้ควรพิมพ์


```
1000
```


คุณสามารถส่งผ่านหลายสิ่งได้ เช่น


```javascript
console.log(16, 8, 1993)
```


สิ่งนี้จะพิมพ์


```
16 8 1993
```


## ตัวแปรและความคิดเห็น

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


โปรแกรมมักจะดำเนินการกับข้อมูล


ตัวแปรเปรียบเสมือนกล่องที่มีชื่อที่เราใช้เก็บข้อมูล พวกมันช่วยให้เราสามารถเชื่อมโยงข้อมูลชิ้นหนึ่งกับชื่อเฉพาะ เพื่อที่เราจะสามารถเรียกคืนข้อมูลนั้นได้ในภายหลังโดยใช้ชื่อนั้น


### ประกาศ let


ในการประกาศตัวแปรใน JavaScript เราสามารถใช้คีย์เวิร์ด `let`


หลังจากเขียน `let` เราจะเขียนชื่อที่เราต้องการให้กับตัวแปร จากนั้นเครื่องหมาย `=` และตามด้วยค่าที่เราต้องการเก็บ


ตัวอย่างเช่น:


```javascript
let age = 25

console.log(age)
```


ชื่อของตัวแปร (ทางเทคนิคเรียกว่า "identifier") มักจะประกอบด้วยตัวอักษร, ขีดล่าง (`_`), เครื่องหมายดอลลาร์ (`$`) และตัวเลขได้ โดยที่ตัวอักษรตัวแรกไม่สามารถเป็นตัวเลขได้


ในโค้ดข้างต้น เราได้ประกาศตัวแปรชื่อ `age` และเก็บค่า `25` ไว้ในนั้น


จากนั้น เราได้พิมพ์ค่าโดยใช้ `console.log(age)`


หากคุณรันโค้ดนี้ด้วย `node main.js` ผลลัพธ์จะเป็น:


```
25
```


ตัวระบุมีความไวต่อขนาดตัวอักษร ซึ่งหมายความว่าตัวพิมพ์เล็กและตัวพิมพ์ใหญ่ถือเป็นความแตกต่างในตัวระบุ ดังนั้นตัวอย่างเช่น


```javascript
let age = 25

let Age = 20

console.log(age)
```


จะพิมพ์ 25 เพราะถือว่าเป็นตัวแปรที่แยกจากกันโดยสิ้นเชิง!


คุณยังสามารถเก็บสตริง (ข้อความ) ไว้ในตัวแปรได้:


```javascript
let message = "hello again"

console.log(message)
```


สิ่งนี้จะแสดงผล:


```
hello again
```


เช่นเดียวกับก่อนหน้านี้ เราใช้ `console.log()` เพื่อพิมพ์ค่าที่เก็บไว้ในตัวแปร


ตอนนี้มาทำทั้งสองอย่างพร้อมกัน:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


การรันนี้จะแสดงผล:


```
25
hello again
```

### การมอบหมายใหม่


ตัวแปรที่ประกาศด้วย `let` สามารถเปลี่ยนแปลงได้หลังจากที่ถูกสร้างขึ้นแล้ว


นี่เรียกว่าการมอบหมายใหม่


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


ก่อนอื่น เรากำหนดค่า `10` ให้กับ `score` จากนั้นพิมพ์มันออกมา


จากนั้นเราจะเปลี่ยนค่าของ `score` เป็น `15` และพิมพ์มันอีกครั้ง


เอาต์พุตจะเป็น:


```
10
15
```


นี่มีประโยชน์มากเมื่อค่ามีการเปลี่ยนแปลงตามเวลา เช่น ในเกมที่คะแนนเพิ่มขึ้น


มาเพิ่มตัวแปรอีกตัวลงไปในส่วนผสม:


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


สิ่งนี้จะแสดงผล:


```
10
Alice
20
Bob
```


ตามที่คุณเห็น ทั้ง `score` และ `player` ถูกเปลี่ยนแปลงแล้ว


### const declarations


ส่วนใหญ่แล้ว เราไม่ต้องการให้ตัวแปรเปลี่ยนแปลงหลังจากที่มันถูกสร้างขึ้น สำหรับกรณีนั้น เราใช้ `const`.


`const` ย่อมาจาก “constant” เมื่อคุณกำหนดค่าให้กับตัวแปร `const` แล้ว คุณไม่สามารถเปลี่ยนแปลงค่าได้


```javascript
const pi = 3.14
console.log(pi)
```


สิ่งนี้พิมพ์ว่า:


```
3.14
```


แต่ถ้าคุณพยายามทำเช่นนี้:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript จะให้ข้อผิดพลาดกับคุณเช่น:


```
TypeError: Assignment to constant variable.
```


นี่เป็นเพราะว่า `pi` ถูกประกาศโดยใช้ `const` และคุณไม่สามารถเปลี่ยนแปลงค่าของมันหลังจากนั้นได้ คุณกำลังสื่อสารกับตัวแปลภาษา JavaScript ว่าคุณไม่ต้องการให้ตัวแปรนั้นเปลี่ยนแปลง


สิ่งนี้มีประโยชน์เพราะช่วยลดโอกาสในการเปลี่ยนแปลงโดยไม่ตั้งใจ เมื่อโปรแกรมมีขนาดใหญ่มาก มีโค้ดหลายพันบรรทัด เป็นไปไม่ได้ที่จะติดตามทุกสิ่งที่เกิดขึ้นพร้อมกันทั้งหมด (นั่นคือเหตุผลหลักที่เราใช้คอมพิวเตอร์ เพื่อดำเนินกระบวนการที่ซับซ้อนที่เราไม่สามารถคำนวณด้วยสมองของเราได้) ดังนั้นจึงเป็นประโยชน์ที่จะมีข้อจำกัดเช่นนี้ ที่ทำให้โปรแกรมมีความแน่นอนมากขึ้น


ถือเป็นแนวปฏิบัติที่ดีที่สุดในการประกาศค่าเป็น `const` เสมอ เว้นแต่ว่าเรามั่นใจว่าเราต้องการแก้ไขในภายหลัง


### ความคิดเห็นใน JavaScript


บางครั้งเราต้องการเขียนบันทึกในโค้ดของเราที่ไม่ถูกประมวลผล สิ่งเหล่านี้เรียกว่าคอมเมนต์


ความคิดเห็นจะถูกละเว้นโดยโปรแกรมเมื่อมันทำงาน แต่มีประโยชน์สำหรับการอธิบายสิ่งต่าง ๆ ให้กับตัวเราเองหรือผู้อื่น


ในการเขียนคอมเมนต์บรรทัดเดียว ให้ใช้ `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


สิ่งนี้จะยังคงพิมพ์:


```
10
```


ความคิดเห็นมีไว้สำหรับมนุษย์อ่านเท่านั้น


คุณยังสามารถเขียนคอมเมนต์หลายบรรทัดโดยใช้ `/*` และ `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


นี่จะพิมพ์


```
20
```


และความคิดเห็นจะถูกละเว้น


คุณสามารถใช้คอมเมนต์เพื่อเพิ่มคำอธิบายเล็กๆ น้อยๆ ให้กับโค้ดของคุณ เพื่อที่คุณจะได้จำได้ว่าโค้ดนั้นทำอะไรและทำไมถึงเขียนในลักษณะนั้น นอกจากนี้ยังสามารถช่วยให้โปรแกรมเมอร์คนอื่นเข้าใจได้อีกด้วย


## ประเภทพื้นฐาน: ตัวเลข, สตริง, บูลีน

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


ใน JavaScript, “type” บอกคุณว่าค่ามีข้อมูลประเภทใด


JavaScript มีประเภทพื้นฐานอยู่ไม่กี่ประเภท และในส่วนนี้เราจะสำรวจบางประเภทเหล่านั้น


### ตัวเลขและการดำเนินการทางคณิตศาสตร์


ประเภทแรกที่เราจะนำเสนอคือ `number`.


ตัวเลขใน JavaScript สามารถเป็นจำนวนเต็ม (เช่น `5`) หรือทศนิยม (เช่น `3.14`)


คุณสามารถทำเลขคณิตกับพวกเขาได้: การบวก การลบ การคูณ และการหาร


นี่คือตัวอย่างพื้นฐาน:


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


สิ่งนี้จะพิมพ์:


```
15
5
50
2
```


คุณยังสามารถใช้วงเล็บ `()` เพื่อควบคุมลำดับของการดำเนินการ:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


สิ่งนี้พิมพ์ว่า:


```
20
```


หากไม่มีวงเล็บ มันจะเป็น `2 + 3 * 4` ซึ่งคือ:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


ที่จะพิมพ์:


```
14
```


เพราะในการคำนวณทางคณิตศาสตร์ทั่วไป การคูณจะเกิดขึ้นก่อนการบวก


### สตริงและการแทรกค่า


ประเภท JavaScript ที่สองที่เราจะนำเสนอคือ `string`.


สตริงคือชิ้นส่วนของข้อความ คุณสามารถใช้เครื่องหมายคำพูดเดี่ยว `'...'` หรือเครื่องหมายคำพูดคู่ `"..."` เพื่อสร้างสตริงได้


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


สิ่งนี้พิมพ์ว่า:


```
hello
Bob
```


ในการรวมสตริง คุณสามารถใช้ตัวดำเนินการ `+`:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


สิ่งนี้จะพิมพ์:


```
hello Bob
```


แต่มีวิธีที่ดีกว่าในการรวมสตริงที่เรียกว่า **string interpolation** คุณใช้ backticks เพื่อประกาศสตริง `` `...` `` และเขียนตัวแปรโดยใช้ `${...}` ภายในสตริง:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


สิ่งนี้ยังพิมพ์ว่า:


```
hello Bob
```


คุณสามารถใส่การแสดงออกใด ๆ ภายใน `${...}`:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


สิ่งนี้พิมพ์ว่า:


```
Next year, I will be 31 years old.
```


การแทรกค่าเป็นเรื่องปกติมากใน JavaScript สมัยใหม่


### บูลีน, การเปรียบเทียบ และการดำเนินการทางตรรกะ


ประเภทที่สามที่เราจะนำเสนอคือ `boolean` มันถูกตั้งชื่อตามนักคณิตศาสตร์ George Boole ผู้คิดค้นตรรกศาสตร์บูลีน


บูลีนเป็นเรื่องง่าย: มีค่าเป็นไปได้เพียงสองค่าเท่านั้น คือ `true` และ `false`


คุณสามารถเก็บมันไว้ในตัวแปร:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


สิ่งนี้พิมพ์:


```
true
false
```


คุณสามารถรวมบูลีนโดยใช้ตัวดำเนินการตรรกะ:



- `&&` หมายถึง "และ" และจะคืนค่า `true` ก็ต่อเมื่อ **ทั้งสอง** ค่าเป็น `true` เท่านั้น มิฉะนั้นจะคืนค่า `false`
- `||` หมายถึง "หรือ" และมันจะคืนค่า `true` ถ้า **อย่างน้อยหนึ่ง** ของค่าคือ `true` มิฉะนั้น (ถ้าทั้งคู่เป็น false) มันจะคืนค่า `false`
- เครื่องหมาย `!` หมายถึง "ไม่" ใช้ก่อนค่าบูลีน และจะกลับค่ามัน: ถ้าค่าบูลีนเป็น `true` มันจะคืนค่า `false` และในทางกลับกัน


![](assets/en/003.webp)


ตัวอย่าง:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


คุณสามารถเปรียบเทียบค่าใน JavaScript โดยใช้ตัวดำเนินการเช่น `>`, `<`, `===`, และ `!==` ผลลัพธ์ของการเปรียบเทียบเหล่านี้จะเป็น boolean เสมอ


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


JavaScript ยังมี `>=` ที่หมายถึง "มากกว่าหรือเท่ากับ" และ `<=` ที่หมายถึง "น้อยกว่าหรือเท่ากับ"


บูลีน, ตัวดำเนินการเปรียบเทียบและตรรกะมักจะถูกใช้ร่วมกันในโปรแกรมเพื่อประกาศเงื่อนไขที่ซับซ้อน เช่น เพื่อให้แน่ใจว่า "อีเมลได้มาถึงแล้วและมีภาพที่ฉันต้องการหรือความยาวของอีเมลยาวกว่า 10000 ตัวอักษร" คุณจะพบในภายหลังว่าสิ่งเหล่านี้เป็นส่วนประกอบสำคัญในการสร้างตรรกะของโปรแกรม


## อาเรย์, null, undefined

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


ในส่วนนี้ เราจะครอบคลุมประเภทเพิ่มเติมอีกสามประเภทที่พบได้บ่อยในโปรแกรม JavaScript:


**Arrays**: ลำดับของค่า

**undefined**: ค่าพิเศษที่หมายถึง "ไม่มีการกำหนดค่าใดๆ"

**null**: ค่าพิเศษอีกค่าหนึ่งที่หมายถึง "ว่างเปล่าโดยเจตนา"


### อาเรย์และการเข้าถึงดัชนี


**อาร์เรย์** เป็นชนิดข้อมูลที่สามารถเก็บค่าหลายค่าในรูปแบบรายการ


คุณสร้างอาเรย์โดยใช้วงเล็บเหลี่ยม `[]` และแยกรายการด้วยเครื่องหมายจุลภาค


นี่คือตัวอย่างพื้นฐาน:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


สิ่งนี้พิมพ์ว่า:


```
[ 10, 2, 88 ]
```


คุณสามารถเก็บทุกอย่างในอาเรย์ ไม่ใช่แค่ตัวเลข:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


สิ่งนี้พิมพ์ว่า:


```
[ 'apple', 42, true ]
```


ในการเข้าถึงรายการเฉพาะในอาเรย์ เราใช้ **ดัชนี** ดัชนีคือ ตำแหน่งของรายการ โดยเริ่มจาก **0**


ดังนั้นในอาร์เรย์นี้:


```javascript
const colors = ["red", "green", "blue"]
```


`colors[0]` คือ `"red"`

`colors[1]` คือ `"green"`

`colors[2]` คือ `"blue"`


ลองดู:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


สิ่งนี้จะแสดงผล:


```
red
green
blue
```


คุณสามารถกำหนดค่าให้กับดัชนีเฉพาะของอาเรย์


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


สิ่งนี้จะแสดงผล:


```
[ 'red', 'yellow', 'blue' ]
```


คุณสามารถใช้จำนวนเต็มบวกใด ๆ เป็นดัชนีได้ แม้แต่จำนวนที่เก็บไว้ในตัวแปร


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


สิ่งนี้จะพิมพ์:


```
green
```


แต่ถ้าคุณพยายามเข้าถึงดัชนีที่ไม่มีอยู่ คุณจะได้รับ `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


สิ่งนี้พิมพ์ว่า:


```
undefined
```


นั่นอะไร??


### ไม่ได้กำหนด


ค่าพิเศษ `undefined` หมายถึง “ไม่มีการกำหนดค่า”


หากคุณสร้างตัวแปรแต่ไม่ได้กำหนดค่าให้ มันจะเป็น `undefined`:


```javascript
const name
console.log(name)
```


สิ่งนี้พิมพ์ว่า:


```
undefined
```


เพราะเราไม่ได้กำหนดค่าใดๆ ให้กับ `name` ดังนั้น JavaScript จึงตั้งค่าเป็น `undefined` โดยค่าเริ่มต้น


ตามที่เห็นก่อนหน้านี้ คุณยังสามารถได้รับ `undefined` เมื่อคุณเข้าถึงดัชนีของอาเรย์ที่ไม่มีอยู่:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


สิ่งนี้พิมพ์ว่า:


```
undefined
```


### null และวิธีการจัดการ


`null` ก็เป็นค่าพิเศษเช่นกัน หมายความว่า "ไม่มีอะไรอยู่ที่นี่ และฉันตั้งใจทำเช่นนั้น"


ตรงกันข้ามกับ `undefined` ซึ่งเป็นอัตโนมัติ `null` เป็นสิ่งที่คุณตั้งค่าเอง


ตัวอย่างเช่น:


```javascript
const currentUser = null
console.log(currentUser)
```


สิ่งนี้พิมพ์ว่า:


```
null
```


ทำไมต้องใช้ `null`? บางทีคุณอาจคาดหวังค่าภายหลัง แต่ยังไม่พร้อม:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


สิ่งนี้พิมพ์ว่า:


```
Alice
```


ดังนั้น `null` มีประโยชน์เมื่อคุณต้องการจะบอกว่า ตัวอย่างเช่น “ควรจะมีบางอย่างอยู่ที่นี่ในภายหลัง แต่ตอนนี้มันว่างเปล่า”


## บล็อกและการควบคุมการไหล

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


จนถึงตอนนี้ เราได้เขียนโค้ดที่ทำงานทีละบรรทัดเป็นส่วนใหญ่


แต่เมื่อเราเขียนโค้ด เราสามารถควบคุมลำดับการทำงานของมันได้


นี่เรียกว่า **การควบคุมการไหล**.


มาเริ่มต้นด้วยการทำความเข้าใจเกี่ยวกับบล็อกและขอบเขตกันเถอะ


### ขอบเขตทั่วโลก


ตัวแปรทุกตัวที่เราประกาศจะมีอยู่ใน **ขอบเขต** ซึ่งหมายถึงบริเวณของโค้ดที่ตัวแปรนั้นเป็นที่รู้จัก


หากคุณประกาศตัวแปรนอกบล็อกใด ๆ มันจะอยู่ใน **ขอบเขตทั่วโลก**


```javascript
const color = "blue"
console.log(color)
```


ตัวแปรนี้ `color` อยู่ในขอบเขตทั่วโลก ดังนั้นจึงสามารถเข้าถึงได้จากทุกที่ในไฟล์


หากคุณเพิ่มบรรทัดเพิ่มเติม:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


ทั้ง `color` และ `size` เป็นตัวแปรแบบ global ซึ่งสามารถใช้งานได้ทุกที่ในไฟล์


แต่เกิดอะไรขึ้นภายในบล็อก?


### บล็อกและขอบเขตท้องถิ่น


**บล็อก** คือโค้ดที่ถูกล้อมรอบด้วยวงเล็บปีกกา `{}`


ตัวแปรที่ประกาศด้วย `let` หรือ `const` ภายในบล็อกจะมีอยู่ **เฉพาะ** ภายในบล็อกนั้นเท่านั้น


```javascript
{
const message = "inside block"
console.log(message)
}
```


สิ่งนี้พิมพ์ว่า:


```
inside block
```


แต่ถ้าคุณลองทำสิ่งนี้:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript จะให้ข้อผิดพลาดกับคุณเช่น:


```
ReferenceError: message is not defined
```


นั่นเป็นเพราะ `message` ถูกประกาศภายในบล็อกและไม่มีอยู่ภายนอกบล็อกนั้น


ซึ่งหมายความว่าเราสามารถใช้บล็อกเพื่อแยกส่วนของโค้ดของเรา และมั่นใจได้ว่า "สิ่งที่เกิดขึ้นในบล็อกจะอยู่ในบล็อก" (คล้ายกับลาสเวกัส)


การจัดระเบียบโค้ดของเราเป็นบล็อกยังช่วยให้เราสามารถโครงสร้างการทำงานของโปรแกรมได้ด้วยโครงสร้างการควบคุมการไหล เช่น `if`


### ถ้า, มิฉะนั้น


บางครั้งเราต้องการให้โค้ดทำงาน **เฉพาะเมื่อ** เงื่อนไขเป็นจริง นั่นคือสิ่งที่คำสั่ง `if` ใช้สำหรับ


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


สิ่งนี้พิมพ์ว่า:


```
Am I an adult?
Yes I am!
```


ตามที่คุณเห็น โค้ดเปรียบเทียบ `myAge` และ `18`

ในกรณีนี้ ตัวดำเนินการ `>=` จะคืนค่า `true` ดังนั้นบล็อกจะถูกดำเนินการ

หากเงื่อนไขไม่ใช่ `true` บล็อกจะไม่ถูกดำเนินการ


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


สิ่งนี้พิมพ์ว่า:


```
Am I an adult?
```


คุณสามารถเพิ่มบล็อก `else` เพื่อจัดการกรณีตรงข้าม:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


สิ่งนี้พิมพ์ว่า:


```
Am I an adult?
No, I am not.
```


ทั้งบล็อก `if` และ `else` ยังคงเป็นบล็อก - ดังนั้นตัวแปรที่ประกาศภายในจะไม่มีอยู่ภายนอก


หากเราต้องการมั่นใจว่าสิ่งใดสิ่งหนึ่ง **ไม่** เป็นความจริง เราสามารถทำอะไรได้บ้าง?


ตามที่ได้กล่าวไว้ก่อนหน้านี้ JavaScript มีตัวดำเนินการ "not" ซึ่งใช้ในการกลับค่าบูลีน ดังนั้นเราสามารถทำได้


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

สิ่งนี้ยังคงพิมพ์:


```
Am I an adult?
No, I am not.
```

เพราะเราใช้ตัวดำเนินการ `!` เพื่อกลับค่าตัวแปร `adult`


`if (!adult) {...}` ควรอ่านว่า "ถ้าไม่เป็นผู้ใหญ่..."


โดยใช้บล็อก, ตัวดำเนินการตรรกะและการเปรียบเทียบ, เราสามารถจัดโครงสร้างการทำงานของโปรแกรมได้ โดยการกำหนดตัวแปรที่ต้องเป็น `true` (หรือ `false`) เพื่อให้บางสิ่งเกิดขึ้น


### ในขณะที่, break, continue


ลูป `while` ทำการวนซ้ำโค้ด *ตราบใดที่* เงื่อนไขเป็นจริง


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


สิ่งนี้พิมพ์ว่า:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


เมื่อ `count` กลายเป็น 3 วนลูปจะหยุด


คุณสามารถหยุดลูปก่อนเวลาโดยใช้ `break`:


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


สิ่งนี้พิมพ์ว่า:


```
0
1
2
```


เพราะเมื่อจำนวนกลายเป็น `3` บล็อก `if` จะถูกดำเนินการและมันจะหยุดลูป


คุณสามารถข้ามส่วนที่เหลือของลูปโดยใช้ `continue`:


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


สิ่งนี้พิมพ์ว่า:


```
1
2
4
5
```


เพราะเมื่อหมายเลขเป็น `3`, `continue` ทำให้โปรแกรมข้ามบรรทัดที่พิมพ์หมายเลขนั้นออกไป


### สำหรับ ... ของ ...


หากคุณมีอาเรย์ และต้องการทำบางสิ่งกับทุกไอเท็มในนั้น คุณสามารถใช้ `for ... of ... {...}` ได้


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


สิ่งนี้พิมพ์ว่า:


```
apple
banana
cherry
```

บล็อกจะถูกดำเนินการหนึ่งครั้งสำหรับแต่ละองค์ประกอบของอาเรย์


`fruit` ที่นี่เป็นตัวแปรใหม่ที่รับค่าของแต่ละรายการในอาเรย์ เพื่อดำเนินการกับมันภายในบล็อก


### สำหรับ ... ใน ...


คุณสามารถใช้ `for ... in` เพื่อวนซ้ำผ่านคีย์ (ดัชนี) ของอาเรย์:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


สิ่งนี้พิมพ์ว่า:


```
0
1
2
```


คุณสามารถใช้ดัชนีเพื่อรับค่าด้วย:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


นี่พิมพ์เหมือนกับ `for ... of`:


```
apple
banana
cherry
```


ในทางปฏิบัติ สำหรับอาเรย์ คุณควรใช้ `for ... of` เพราะมันง่ายและสะอาดกว่า


### ลูปที่มีขอบเขต


บางครั้งเราต้องการวนซ้ำจำนวนครั้งที่กำหนด หรือโดยทั่วไปเขียนโค้ดที่ทำซ้ำบล็อกในขณะที่ติดตามบางสิ่งบางอย่าง

นั่นคือสิ่งที่ `for` loop ที่มีขอบเขตดีสำหรับ

ลูปที่มีขอบเขตมักจะมีสามเงื่อนไข แยกด้วยเครื่องหมายอัฒภาค `;` ดังนี้ `(... ; ... ; ....)`


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


สิ่งนี้พิมพ์ว่า:


```
0
1
2
```


มาอธิบายกัน:



- `let i = 0`: ประกาศตัวแปรที่จะใช้ในบล็อก (ในกรณีนี้คือเคาน์เตอร์ที่เริ่มต้นที่ 0)
- `i < 3`: ประกาศเงื่อนไขให้เป็น `true` เพื่อให้บล็อกถูกดำเนินการ (ในกรณีนี้คือ "ทำซ้ำในขณะที่ `i` น้อยกว่า 3")
- `i = i + 1`: ประกาศโค้ดบางส่วนให้รันหลังจากการดำเนินการของบล็อกแต่ละครั้ง (ในกรณีนี้ "เพิ่ม `i` ขึ้น 1")


ตามที่คุณเห็น วงวนที่มีขอบเขตช่วยให้เราประกาศเงื่อนไขที่ซับซ้อนมากขึ้นสำหรับการดำเนินการซ้ำของโค้ดชิ้นหนึ่ง แต่ส่วนใหญ่แล้วมันไม่จำเป็น


### ป้ายบล็อก


หากคุณต้องเขียนโครงสร้างการควบคุมที่ซับซ้อนมากขึ้น JavaScript ให้คุณตั้งชื่อบล็อกโดยใช้ **label** ซึ่งสามารถใช้ร่วมกับ `break` หรือ `continue` เพื่อระบุ *ตำแหน่ง* ที่จะกระโดดกลับไป


ตัวอย่าง:


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


สิ่งนี้พิมพ์ว่า:


```
Inside outer block
Inside inner block
Done
```


เราใช้ `break outer` เพื่อออกจากบล็อก `outer` ทั้งหมด


คุณยังสามารถติดป้ายกำกับลูปได้ ลองดูตัวอย่างนี้:


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

นี่เป็นตัวอย่างที่น่าเบื่อมาก แต่หวังว่ามันจะชี้แจงความจำเป็น (บางครั้ง) ของการใช้ป้ายกำกับได้


## แนะนำฟังก์ชัน

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


เมื่อโปรแกรมของคุณเติบโตขึ้น คุณมักจะต้องการ **นำกลับมาใช้ใหม่** ชิ้นส่วนของโค้ด


นั่นคือสิ่งที่ **ฟังก์ชัน** มีไว้สำหรับ: พวกมันช่วยให้คุณรวมโค้ดบางส่วนเข้าด้วยกัน ตั้งชื่อให้มัน และเรียกใช้เมื่อใดก็ตามที่คุณต้องการ


### การประกาศฟังก์ชัน


ในการประกาศฟังก์ชัน เราสามารถใช้คีย์เวิร์ด `function` จากนั้นให้ชื่อฟังก์ชัน ตามด้วยวงเล็บคู่ `()` ที่มีอาร์กิวเมนต์ที่ฟังก์ชันรับ และบล็อกของโค้ด `{}` ที่จะถูกดำเนินการ เริ่มต้นด้วยฟังก์ชันที่ไม่รับอาร์กิวเมนต์:


```javascript
function sayHello () {console.log(`Hello!`) }
```


โค้ดนี้ **ประกาศ** ฟังก์ชัน แต่ยัง **ไม่ได้** รันมัน


### การเรียกใช้ฟังก์ชัน


ในการเรียกใช้ (หรือ "เรียก") ฟังก์ชัน คุณเขียนชื่อฟังก์ชันตามด้วยวงเล็บ:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


สิ่งนี้พิมพ์ว่า:


```
Hello!
```


คุณสามารถเรียกใช้ฟังก์ชันได้หลายครั้งตามที่คุณต้องการ:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


สิ่งนี้พิมพ์ว่า:


```
Hello!
Hello!
```


โค้ดภายในฟังก์ชันจะทำงานก็ต่อเมื่อคุณเรียกใช้งานมันเท่านั้น


### อาร์กิวเมนต์ของฟังก์ชัน (ข้อมูลนำเข้าสู่ฟังก์ชัน)


บางครั้ง คุณต้องการให้ฟังก์ชันทำงานกับข้อมูลนำเข้า คุณสามารถทำได้โดยการเพิ่ม **อาร์กิวเมนต์** ภายในวงเล็บ


ตัวอย่างเช่น:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


ฟังก์ชันนี้รับ **อาร์กิวเมนต์หนึ่งตัว** ที่เรียกว่า `friend`


เมื่อคุณเรียกใช้ฟังก์ชัน คุณสามารถส่งค่าผ่านไปได้:


```javascript
sayHelloTo("Tommy")
```


สิ่งนี้พิมพ์ว่า:


```
Hello Tommy!
```


คุณสามารถเรียกฟังก์ชันอีกครั้งด้วยชื่อที่แตกต่างกัน:


```javascript
sayHelloTo("Sam")
```


สิ่งนี้พิมพ์ว่า:


```
Hello Sam!
```


ค่าที่คุณส่งเข้ามาจะแทนที่ตัวแปร `friend` ภายในฟังก์ชัน


คุณยังสามารถใช้มากกว่าหนึ่งอาร์กิวเมนต์:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


สิ่งนี้พิมพ์ว่า:


```
Hello Lina and Marco!
```


### ส่งคืน (ผลลัพธ์จากฟังก์ชัน)


ฟังก์ชันสามารถ **ส่งคืน** ค่าได้เช่นกัน ซึ่งหมายความว่าพวกเขาส่งค่ากลับไปยังที่ที่ฟังก์ชันถูกเรียกใช้


นี่คือตัวอย่างง่าย ๆ:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


สิ่งนี้พิมพ์ว่า:


```
42
```


ฟังก์ชัน `getNumber()` คืนค่า `42` และเราจัดเก็บมันใน `result` จากนั้นพิมพ์มันออกมา


คุณยังสามารถส่งคืนสิ่งที่คุณคำนวณได้:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


สิ่งนี้พิมพ์ว่า:


```
5
```


เมื่อค่า `return` ถูกส่งกลับ ฟังก์ชันจะหยุดทำงาน สิ่งใดก็ตามที่อยู่หลัง `return` ในบล็อกนั้นจะไม่เกิดขึ้น


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


พิมพ์เฉพาะ:


```
hi
```


เพราะมีเพียง `"hi"` ที่ถูกส่งคืน `console.log("this never runs")` บรรทัดนี้ถูกข้ามไป


คุณสามารถคิดว่าฟังก์ชันเป็นโปรแกรมย่อยขนาดเล็กได้ ฟังก์ชันแต่ละตัวสามารถรับข้อมูลนำเข้า ทำงานกับมัน และให้ผลลัพธ์กลับมาแก่คุณ


จะเกิดอะไรขึ้นถ้าเราพยายามใช้ค่าที่ส่งกลับของฟังก์ชัน แต่ฟังก์ชันนั้นไม่ได้ส่งค่ากลับอะไรเลย?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

นี่จะพิมพ์ `undefined` ค่าที่ส่งกลับของฟังก์ชันที่ไม่ได้ส่งกลับค่าใด ๆ คือ `undefined`


## วัตถุและคลาส

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript มักถูกเรียกว่าภาษาเชิงวัตถุ


นั่นหมายความว่ามันช่วยให้คุณจัดระเบียบโค้ดของคุณโดยการจัดกลุ่มค่าและฟังก์ชันเข้าด้วยกันเป็น **อ็อบเจ็กต์**


### วัตถุคืออะไร?


วัตถุสามารถมีข้อมูลและฟังก์ชันที่ทำงานกับข้อมูลนั้นได้ เมื่อฟังก์ชันถูกใส่เข้าไปในวัตถุ เราเรียกมันว่า `method`


วัตถุแรกที่เราเห็นคือวัตถุ `console` มันเป็นวัตถุที่มีหลายวิธีในการพิมพ์สิ่งต่าง ๆ บนหน้าจอและดีบักโปรแกรมของเรา


มันสามารถพิมพ์ตัวเองได้; คุณสามารถทำ


```javascript
console.log(console)
```


และมันจะพิมพ์รายการของเมธอดที่มันมีอยู่ ตัวอย่างเช่น บนเครื่องของฉันมันพิมพ์


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


ตามที่คุณเห็น มันมีวิธีการมากมายที่คุณสามารถใช้ในการดีบัก!


JavaScript มอบวิธีการต่างๆ ให้เราในการสร้างอ็อบเจ็กต์ใหม่ที่สามารถทำอะไรก็ได้ตามที่เราต้องการ


### การสร้างอ็อบเจกต์


วิธีที่ง่ายที่สุดในการสร้างอ็อบเจ็กต์คือการจัดกลุ่มข้อมูลและฟังก์ชันโดยใช้ **วงเล็บปีกกา** `{}`.


สิ่งนี้สร้างสิ่งที่เราเรียกว่า **วัตถุไม่ระบุชื่อ**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


สิ่งนี้สร้างอ็อบเจ็กต์และเก็บไว้ในตัวแปรที่เรียกว่า `cat`.


วัตถุมี **คุณสมบัติ** สองประการ:



- `name` with the value `"Whiskers"`
- `age` with the value `3`


มาพิมพ์กันเถอะ:


```javascript
console.log(cat)
```


สิ่งนี้พิมพ์ว่า:


```
{ name: 'Whiskers', age: 3 }
```


คุณสามารถดึงคุณสมบัติออกจากวัตถุโดยใช้จุด เช่น `objectName.propertyName`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


คุณยังสามารถ**เปลี่ยน**คุณสมบัติ:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


ตามที่คุณเห็น แม้ว่าวัตถุจะถูกกำหนดเป็น `const` คุณยังสามารถแก้ไขข้อมูลที่มันบรรจุได้


ในกรณีของอ็อบเจ็กต์ `const` จะหยุดคุณจากการเขียนทับอ็อบเจ็กต์ทั้งหมด:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


ตามที่กล่าวไว้ก่อนหน้านี้ วัตถุสามารถถือครอง**ฟังก์ชัน**ได้เช่นกัน และเมื่อฟังก์ชันเป็นส่วนหนึ่งของวัตถุ เราเรียกมันว่า**เมธอด**


นี่คือตัวอย่าง:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


วัตถุนี้มี:



- คุณสมบัติ `name`
- เมธอด `speak()`


มาลองเรียกใช้เมธอดนี้กัน:


```javascript
cat.speak()
```


มันพิมพ์ว่า:


```
Meow!
```


วิธีการสามารถใช้ข้อมูลที่วัตถุมีอยู่ผ่านคีย์เวิร์ด `this`

`this` หมายถึงวัตถุปัจจุบัน ในตัวอย่างนี้จะใช้เพื่อพิมพ์ชื่อของแมว:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


สิ่งนี้พิมพ์ว่า:


```
Whiskers says meow!
```


คำว่า `this` หมายถึง "วัตถุนี้"...ในกรณีนี้คือ วัตถุ `cat`



วัตถุประเภทนี้เหมาะมากเมื่อคุณต้องการบางสิ่งที่รวดเร็วและเรียบง่าย แต่ถ้าคุณจำเป็นต้องสร้าง **วัตถุจำนวนมาก** ที่มีโครงสร้างเดียวกัน มีวิธีที่ดีกว่า และนั่นคือที่มาของ **คลาส**


### คลาสและคอนสตรัคเตอร์


**คลาส** เปรียบเสมือนพิมพ์เขียว มันบอกให้ JavaScript รู้วิธีสร้างวัตถุประเภทหนึ่ง


คุณกำหนดคลาสโดยใช้คีย์เวิร์ด `class` ตามด้วยชื่อของคลาส และตามด้วยบล็อกวงเล็บปีกกา `{}`


```javascript
class Dog {}
```


โดยทั่วไปแล้ว คลาสจะเริ่มต้นด้วยตัวอักษรตัวใหญ่ ตามธรรมเนียม


คุณสามารถสร้างวัตถุใหม่ของคลาสโดยใช้ `new`:


```javascript
const hachiko = new Dog()
```


ลองพิมพ์วัตถุ:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


คุณจะได้รับ


```
Dog {}
```


ตามที่คุณเห็น คลาส Dog ว่างเปล่า ดังนั้นวัตถุ `myDog` จึงว่างเปล่าเช่นกัน


เราสามารถกำหนดว่าคุณสมบัติใดที่วัตถุ Dog ควรมีได้โดยการเพิ่ม `constructor`


ตัวสร้าง (Constructor) เป็นฟังก์ชันพิเศษที่ทำงานเมื่อคุณสร้าง (หรือ "สร้าง") วัตถุใหม่


```javascript
class Dog {
constructor() { }
}
```


เราต้องการให้สุนัขแต่ละตัวมีชื่อ ดังนั้นเราจึงเพิ่มพารามิเตอร์ `name` ลงในฟังก์ชัน:


```javascript
class Dog {
constructor(name) { }
}
```


จากนั้นเราใช้ `this` เพื่อประกาศว่า `name` คือ `name` ของวัตถุ `Dog` ที่เรากำลังสร้าง


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


ลองใช้มันตอนนี้:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


สิ่งนี้พิมพ์บางอย่างเช่น:


```
Dog { name: 'hachiko' }
```


ตามที่คุณเห็น เมธอด `constructor` จะรับอาร์กิวเมนต์ที่คุณส่งไปยังคลาสเมื่อคุณใช้ `new Dog()` และมันจะใช้เพื่อสร้างอ็อบเจกต์


มาทำความเข้าใจกัน:


`class Dog` กำหนดคลาส Dog


- `constructor(name)` กำหนดค่าออบเจ็กต์เมื่อมันถูกสร้างขึ้น
- `this.name = name` เก็บค่าในวัตถุใหม่
- `new Dog("hachiko")` สร้างวัตถุใหม่จากคลาส โดยมีคุณสมบัติ `name` ตั้งค่าเป็น `"hachiko"`


ตอนนี้เรามาเพิ่มเมธอดให้กับคลาสของเรากัน:


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


สิ่งนี้จะพิมพ์


```javascript
hachiko says barf!
```


หากเราทำเช่นเดียวกันสำหรับอินสแตนซ์ของสุนัขสองตัวที่แตกต่างกัน



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


เราได้รับ


```
hachiko says barf!
bobby says barf!
```


เมธอด `speak()` ใช้พร็อพเพอร์ตี้ `name` ของ `Dog` ที่ถูกเรียกใช้.


นี่คือเหตุผลหลักที่คลาสมีอยู่: พวกมันช่วยให้เราสามารถกำหนดชุดของเมธอดที่ทำงานกับข้อมูล และจากนั้นสร้างออบเจ็กต์หลายตัวที่มี "รูปแบบ" ข้อมูลเดียวกัน


เมื่อเราเรียกใช้เมธอดบนหนึ่งในออบเจ็กต์เหล่านี้ มันจะทำงานกับข้อมูลที่ *ออบเจ็กต์เฉพาะนั้น* ถือครองอยู่


### การเปลี่ยนรูปร่างของวัตถุ


วัตถุใน JavaScript มีความยืดหยุ่น แม้หลังจากที่คุณสร้างวัตถุแล้ว คุณยังสามารถเพิ่มคุณสมบัติใหม่หรือเอาคุณสมบัติที่มีอยู่ออกได้


มันได้รับอนุญาต แต่เป็นสิ่งที่คุณควรใช้อย่างระมัดระวัง


มาเริ่มต้นด้วยคลาส `Dog` แบบง่ายของเรากัน:


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


ณ จุดนี้ `myDog` มีเพียงคุณสมบัติเดียว: `name` เรายังคงสามารถเพิ่มคุณสมบัติใหม่หลังจากที่มันถูกสร้างขึ้นแล้ว:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


เรายังสามารถเพิ่มเมธอดใหม่ได้:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


และเราสามารถลบคุณสมบัติได้เช่นกัน โดยใช้คีย์เวิร์ด `delete`


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


สิ่งนี้ใช้งานได้ แต่มีสิ่งสำคัญที่ควรรู้: เอนจิน JavaScript อย่าง V8 (ที่ใช้ใน Node.js และในเบราว์เซอร์ Chrome) จะทำงานได้เร็วขึ้นเมื่ออ็อบเจ็กต์ของคุณมีคุณสมบัติเหมือนเดิมเสมอ หากคุณเพิ่มหรือลบคุณสมบัติหลังจากที่อ็อบเจ็กต์ถูกสร้างขึ้นแล้ว อาจทำให้การทำงานช้าลงได้


ในโปรแกรมขนาดเล็ก สิ่งนี้อาจไม่สำคัญมากนัก แต่ในโปรเจกต์ขนาดใหญ่ (เช่น เกม) ควรระบุคุณสมบัติทั้งหมดในตัวสร้างตั้งแต่เริ่มต้น แม้ว่าคุณจะยังไม่ได้ใช้งานทันที วิธีนี้จะช่วยให้รูปแบบของอ็อบเจกต์คงที่และช่วยให้โค้ดของคุณทำงานได้เร็วขึ้น


ตัวอย่างเช่น แทนที่จะเป็นแบบนี้:


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


คุณสามารถทำได้


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


ทั้งสองเวอร์ชันทำงานได้ แต่เวอร์ชันที่สองดีกว่าสำหรับประสิทธิภาพ คุณกำลังบอกเครื่องยนต์ล่วงหน้าว่าวัตถุแต่ละชิ้นจะมีคุณสมบัติอะไรบ้าง และมันสามารถปรับให้เหมาะสมตามนั้น


JavaScript ช่วยให้คุณปรับรูปร่างของอ็อบเจ็กต์ได้อย่างอิสระ แต่เมื่อใช้คลาส ควรวางแผนรูปร่างของอ็อบเจ็กต์ล่วงหน้า



### การสืบทอดด้วย extends และ super()


บางครั้งคุณต้องการสร้างคลาสที่ *เกือบจะ* เหมือนกับคลาสอื่น แต่มีคุณสมบัติเพิ่มเติมเล็กน้อย


แทนที่จะปรับเปลี่ยนรูปร่างของวัตถุ (ซึ่งตามที่กล่าวไว้ก่อนหน้านี้ไม่เหมาะสมสำหรับประสิทธิภาพ) หรือจำเป็นต้องเขียนคลาสใหม่ตั้งแต่ต้น JavaScript ให้คุณใช้สิ่งที่เรียกว่า **inheritance**


การสืบทอดหมายถึงคลาสหนึ่งสามารถ **ขยาย** อีกคลาสหนึ่งได้ คลาสใหม่จะได้รับคุณสมบัติและเมธอดทั้งหมดของคลาสเก่า และคุณสามารถเพิ่มหรือเปลี่ยนแปลงสิ่งที่คุณต้องการได้


สมมติว่าเรามีคลาสพื้นฐานที่เรียกว่า `Vehicle`:


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


ตอนนี้เราต้องการสร้างคลาส `Car` รถยนต์เป็นประเภทหนึ่งของยานพาหนะ แต่เราอาจต้องการให้มันมีคุณสมบัติเพิ่มเติมหรือข้อความที่แตกต่างเมื่อมันเริ่มทำงาน แทนที่จะเขียนทุกอย่างใหม่ เราสามารถใช้ `extends`:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


คลาส `Car` ตอนนี้ **สืบทอด** ทุกอย่างจาก `Vehicle` มันได้รับพร็อพเพอร์ตี้ `brand` และเราได้แทนที่เมธอด `start()` ด้วยเวอร์ชันของเราเอง


![](assets/en/004.webp)


ลองดูสิ:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


สิ่งนี้พิมพ์ว่า:


```
Toyota car is ready to drive!
```


ถึงแม้ว่า `Car` จะไม่มี constructor ของตัวเอง แต่มันยังคงใช้ constructor จาก `Vehicle` แต่ถ้าเราต้องการเขียน constructor แบบกำหนดเองใน `Car` เราสามารถทำได้ เพียงแค่เราต้องเรียก constructor ของ parent โดยใช้ `super()`


นี่คือวิธีการ:


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



สิ่งนี้พิมพ์ว่า:


```
Toyota Corolla is ready to drive!
```


ดังนั้นเพื่อสรุป



- `extends` หมายถึงคลาสหนึ่งถูกสร้างขึ้นบนพื้นฐานของอีกคลาสหนึ่ง
- `super()` ใช้เพื่อเรียกคอนสตรัคเตอร์ของคลาสที่คุณกำลังขยาย

*คลาสใหม่จะได้รับคุณสมบัติและเมธอดทั้งหมดของคลาสต้นฉบับ*


- คุณสามารถ **override** เมธอด (เช่น `start()`) เพื่อให้มันทำสิ่งที่แตกต่างออกไปได้


สิ่งนี้มีประโยชน์เมื่อคุณมีหลายสิ่งที่คล้ายกัน (เช่น รถยนต์, รถบรรทุก, และจักรยาน) และคุณต้องการให้พวกมันใช้โค้ดร่วมกันแต่ยังคงมีพฤติกรรมในแบบของตัวเอง


### instanceof


คีย์เวิร์ด `instanceof` ตรวจสอบว่าอ็อบเจ็กต์ถูกสร้างจากคลาสใดคลาสหนึ่งหรือไม่


สมมติว่าเรามีคลาสที่ชื่อว่า `User`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


สิ่งนี้พิมพ์ว่า:


```
true
```


ยืนยันว่า `regularUser` เป็น `User` นั่นเป็นเพราะ `regularUser` ถูกสร้างขึ้นโดยใช้คลาส `User`


มันยังทำงานร่วมกับคลาสที่**สืบทอด**ได้อีกด้วย ตัวอย่างเช่น นี่คือคลาส `Admin` ที่ขยายจาก `User`:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


ทั้งสองบรรทัดคืนค่า `true` นั่นเป็นเพราะว่า `Admin` เป็นคลาสย่อยของ `User` ดังนั้น `ourAdmin` จึงเป็นทั้ง `Admin` และ `User`


# JavaScript ระดับกลาง

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## การจัดการข้อผิดพลาด

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


เมื่อคุณเขียนโปรแกรม JavaScript ที่ซับซ้อนมากขึ้น คุณจะพบกับ **ข้อผิดพลาด** เหล่านี้คือสถานการณ์ที่ไม่คาดคิดที่บางอย่างผิดพลาด อาจเป็นไปได้ว่าตัวแปร `undefined` แต่คุณพยายามใช้งานมัน หรือโค้ดบางส่วนได้รับประเภทของข้อมูลที่ไม่ถูกต้อง


หากเราไม่จัดการข้อผิดพลาดเหล่านี้อย่างถูกต้อง โปรแกรมของเราอาจล่มหรือทำงานในลักษณะที่ไม่สามารถคาดเดาได้ JavaScript มีเครื่องมือในการตรวจจับและจัดการข้อผิดพลาดเหล่านี้เพื่อให้เราสามารถจัดการกับมันได้อย่างสง่างามมากขึ้น


### ข้อผิดพลาดทั่วไป: การเข้าถึงค่าในตัวแปรที่ไม่ได้กำหนด


นี่คือสถานการณ์ทั่วไปที่ทำให้เกิดข้อผิดพลาด:


```javascript
const user = undefined
console.log(user.name)
```


หากคุณรันโค้ดนี้ คุณจะได้รับข้อผิดพลาดที่มีลักษณะดังนี้:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


นั่นคือ JavaScript กำลังบอกคุณว่า: “เฮ้, คุณพยายามที่จะดึงคุณสมบัติ `name` จากบางสิ่งที่เป็น `undefined` และนั่นไม่มีเหตุผลเลย” และอย่างที่คุณเห็น เมื่อเกิดข้อผิดพลาดประเภทนี้ โปรแกรมจะหยุดทำงาน เว้นแต่ว่าคุณจะเขียนโค้ดเพื่อจับและจัดการกับมันโดยเฉพาะ


### เกิดข้อผิดพลาด


บางครั้งคุณอาจต้องการ **ยกข้อผิดพลาด** ในโค้ดของคุณด้วยตนเอง ในกรณีนั้น คุณใช้คำสำคัญ `throw`


```javascript
throw new Error("This is a custom error message")
```


สิ่งนี้จะหยุดโปรแกรมทันทีและพิมพ์:


```
Uncaught Error: This is a custom error message
```


คุณสามารถใช้ `throw` เพื่อบังคับใช้กฎในโปรแกรมของคุณ ตัวอย่างเช่น:


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


การเรียกครั้งที่สองทำให้เกิดข้อผิดพลาดเนื่องจากการหารด้วยศูนย์ไม่ได้รับอนุญาตในตัวอย่างนี้


### การจับข้อผิดพลาดด้วย try...catch


หากคุณไม่ต้องการให้โปรแกรมของคุณหยุดทำงานเมื่อเกิดข้อผิดพลาด คุณสามารถจับข้อผิดพลาดโดยใช้บล็อก `try...catch` สิ่งนี้มีประโยชน์เมื่อคุณต้องการให้โปรแกรมของคุณ **ทำงานต่อไป** แม้ว่าจะมีบางอย่างล้มเหลวก็ตาม


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


เอาต์พุต:


```
Oops! Something went wrong.
```


นี่คือวิธีการทำงาน:



- โค้ดภายในบล็อก `try` จะถูกพยายามรันก่อนเป็นอันดับแรก

*หากเกิดข้อผิดพลาด JavaScript **จะข้ามไปที่บล็อก `catch`** โดยข้ามส่วนที่เหลือของบล็อก `try`.*


- บล็อก `catch` จะรับข้อผิดพลาด ดังนั้นคุณสามารถพิมพ์มันออกมา หรือจัดการในวิธีอื่น ๆ เช่น


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


เอาต์พุต:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### บล็อก finally


คุณยังสามารถเพิ่มบล็อก `finally` ได้อีกด้วย นี่คือโค้ดที่**ทำงานเสมอ** ไม่ว่าจะเกิดข้อผิดพลาดหรือไม่ก็ตาม


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


เอาต์พุต:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## หลีกเลี่ยงบั๊ก

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


บทนี้แสดงให้เห็นถึงข้อผิดพลาดที่พบบ่อยที่สุดใน JavaScript และวิธีหลีกเลี่ยงข้อผิดพลาดเหล่านั้น


### var และการกำหนดค่าโดยไม่ต้องประกาศ


ในโค้ด JavaScript เก่า ๆ ตัวแปรมักถูกประกาศโดยใช้คีย์เวิร์ด `var` ซึ่งแตกต่างจาก `let` และ `const` ที่คุณได้เรียนรู้ไปแล้ว `var` อาจทำงานในลักษณะที่สับสนได้


ตัวอย่างเช่น:


```javascript
{
var message = "hello"
}
console.log(message)
```


คุณอาจคาดหวังให้ `message` มีอยู่เฉพาะภายในบล็อกเท่านั้น แต่ไม่ใช่ `var` จะไม่สนใจขอบเขตของบล็อกและทำให้ตัวแปรสามารถใช้งานได้ตลอดทั้งฟังก์ชันหรือไฟล์


สิ่งนี้อาจนำไปสู่พฤติกรรมที่ไม่คาดคิด โดยเฉพาะในโปรแกรมที่มีขนาดใหญ่ ด้วยเหตุนี้ โค้ด JavaScript สมัยใหม่ควรใช้ `let` หรือ `const` แทน `var` เสมอ


ยิ่งไปกว่านั้น JavaScript ยังให้คุณกำหนดค่าให้กับตัวแปร **โดยไม่ต้องประกาศเลย**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


สิ่งนี้จะสร้างตัวแปรโกลบอลใหม่ `name` โดยไม่มีการประกาศใด ๆ สิ่งนี้สามารถเกิดขึ้นได้อย่างเงียบ ๆ และนำไปสู่บั๊กที่ติดตามได้ยาก โดยเฉพาะอย่างยิ่งถ้ามันเป็นเพียงแค่การพิมพ์ผิด ควรประกาศตัวแปรเสมอโดยใช้ `let` หรือ `const`


### ระบบประเภทที่อ่อนแอ


JavaScript เป็นภาษาที่มีการกำหนดประเภทแบบอ่อน หมายความว่ามันจะทำการแปลงค่าจากประเภทหนึ่งไปยังอีกประเภทหนึ่งโดยอัตโนมัติหากจำเป็น สิ่งนี้เรียกว่าการบังคับประเภท (type coercion) และแม้ว่ามันจะสะดวก แต่ก็มักจะนำไปสู่ผลลัพธ์ที่สับสนบ่อยครั้ง


ตัวอย่างเช่น:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


ในตัวอย่างเหล่านี้ JavaScript พยายามเดาว่าคุณหมายถึงอะไร บางครั้งมันจะแปลงสตริงเป็นตัวเลข หรือบูลีนเป็นตัวเลข หรือสตริงเป็นสตริง สิ่งนี้อาจทำให้โค้ดของคุณทำงานในรูปแบบที่ไม่คาดคิดได้


การตระหนักถึงระบบการพิมพ์ที่อ่อนแอของ JavaScript เป็นสิ่งสำคัญ เมื่อสิ่งต่าง ๆ เริ่มทำงานแปลก ๆ อาจเกิดจากการบังคับประเภทที่ไม่คาดคิด


### "use strict"


คุณสามารถเปิดโหมดที่เข้มงวดขึ้นซึ่งจะเปลี่ยนข้อผิดพลาดที่เงียบบางอย่างให้กลายเป็นข้อผิดพลาดจริง และหยุดคุณจากการใช้คุณสมบัติที่อันตรายกว่าของภาษาได้


ในการเปิดใช้งานโหมดที่เข้มงวดขึ้นนี้ ให้เพิ่มบรรทัดนี้ที่ด้านบนของไฟล์หรือฟังก์ชันของคุณ:


```javascript
"use strict"
```


ตัวอย่างเช่น:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


หากไม่มีโหมดเคร่งครัด JavaScript จะสร้างตัวแปรโกลบอลที่ชื่อว่า `name` อย่างเงียบๆ แต่เมื่อใช้โหมดเคร่งครัด สิ่งนี้จะกลายเป็นข้อผิดพลาดจริง ช่วยให้คุณจับบั๊กได้เร็วขึ้น


โหมดเข้มงวดยังปิดใช้งานคุณสมบัติบางอย่างของ JavaScript ที่ล้าสมัย และทำให้โค้ดของคุณง่ายต่อการปรับแต่งและบำรุงรักษา


## ค่าเทียบกับการอ้างอิง

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript ปฏิบัติต่อค่าประเภทต่างๆ ในรูปแบบที่แตกต่างกัน


ค่าบางค่า **ถูกคัดลอก** เมื่อคุณกำหนดให้กับตัวแปร


คนอื่น ๆ จะ **แชร์** เมื่อคุณกำหนดให้กับตัวแปรใหม่ ดังนั้นหากคุณเปลี่ยนตัวหนึ่ง อีกตัวหนึ่งก็จะเปลี่ยนด้วยเช่นกัน


### ส่งผ่านโดยค่า


เมื่อมีการส่งค่า **โดยค่า** JavaScript จะทำ **สำเนา** ของค่านั้น


ดังนั้นหากคุณเปลี่ยนแปลงสิ่งหนึ่ง มันจะไม่ส่งผลกระทบต่ออีกสิ่งหนึ่ง


สิ่งนี้เกิดขึ้นกับประเภทข้อมูลพื้นฐาน เช่น:


*ตัวเลข*

*strings*

*booleans* (`true` and `false`)

`null`

`*undefined*`


มาดูตัวอย่างกัน:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


เราให้ค่า `b` เท่ากับ `a` แต่จากนั้นเราเปลี่ยน `b` เป็น `10`


เนื่องจากตัวเลขถูกส่งผ่านโดยค่า JavaScript จึงคัดลอก `5` ไปยัง `b` ตัวเลข `5` ใน `b` เป็นอิสระจาก `5` ดั้งเดิมใน `a` ดังนั้นการเปลี่ยนค่าของ `b` จึงไม่มีผลต่อ `a`


ลองด้วยสตริง:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


อีกครั้ง การเปลี่ยน `name2` ไม่ได้ส่งผลกระทบต่อ `name1` เพราะสตริงก็ถูกส่งผ่านโดยค่าเช่นกัน


สิ่งเดียวกันนี้เกิดขึ้นเมื่อคุณส่งค่าพื้นฐานไปยังฟังก์ชัน: มันจะถูกคัดลอก ดังนั้นฟังก์ชันไม่สามารถเปลี่ยนแปลงต้นฉบับได้


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


แม้ว่าภายในฟังก์ชันจะมีการบวก `1` เข้าไปใน `x` แต่ค่า `number` ดั้งเดิมก็ไม่ได้เปลี่ยนแปลง


นั่นเป็นเพราะมีเพียง **สำเนา** เท่านั้นที่ถูกส่งเข้าไปในฟังก์ชัน


### ส่งผ่านโดยการอ้างอิง


อ็อบเจ็กต์ถูกส่งผ่าน **โดยการอ้างอิง**.


นั่นหมายความว่าแทนที่จะคัดลอกมัน JavaScript จะส่งผ่าน **reference** ไปยังมัน และถ้าคุณแก้ไขมัน ตัวแปรอื่น ๆ ทั้งหมดที่ชี้ไปยังมันก็จะเห็นการเปลี่ยนแปลงด้วยเช่นกัน


ตัวอย่างเช่น:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


ทั้ง `person1` และ `person2` ชี้ไปที่วัตถุเดียวกันในหน่วยความจำ


ดังนั้นเมื่อเราเปลี่ยน `person2.name` เราก็เปลี่ยน `person1.name` ด้วย เพราะพวกเขาทั้งสองกำลังดูสิ่งเดียวกันอยู่


อาร์เรย์เป็นอ็อบเจ็กต์ ดังนั้นลองทำแบบเดียวกันกับอาร์เรย์:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


เราใส่ `4` เข้าไปใน `list2` แต่ `list1` ก็ได้รับผลกระทบด้วย เพราะทั้งสองอ้างอิงไปยังอาเรย์เดียวกัน


ลองมาดูกันว่าเกิดอะไรขึ้นเมื่อเราส่งอ็อบเจกต์ไปยังฟังก์ชัน:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


ฟังก์ชันเปลี่ยนวัตถุ! นั่นเป็นเพราะมันได้รับ **การอ้างอิง** ไปยังวัตถุ `person` ดั้งเดิม


มันไม่ได้รับสำเนา แต่มันได้รับการเข้าถึงวัตถุต้นฉบับ และด้วยสิ่งนั้นมันได้รับความสามารถในการแก้ไขวัตถุนั้น


สิ่งสำคัญคือต้องจำความแตกต่างนี้ไว้ เพราะไม่เช่นนั้นโค้ดของเราอาจทำงานแตกต่างจากที่เราคาดหวังได้ ตัวอย่างเช่น เราอาจเขียนฟังก์ชันโดยคาดหวังว่ามันจะไม่แก้ไขอาร์กิวเมนต์ที่ได้รับ และพบในภายหลังว่ามันแก้ไขอาร์กิวเมนต์เหล่านั้นจริง ๆ (เพราะว่าอาร์กิวเมนต์เหล่านั้นเป็นอ็อบเจ็กต์ จึงถูกส่งผ่านโดยการอ้างอิง)


## การทำงานกับฟังก์ชัน

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


คุณได้เรียนรู้วิธีการประกาศและใช้งานฟังก์ชันใน JavaScript แล้ว แต่ JavaScript ยังมีเครื่องมือเพิ่มเติมที่ช่วยให้คุณทำงานกับฟังก์ชันได้อย่างมีประสิทธิภาพมากขึ้น


### ฟังก์ชันลูกศร


ฟังก์ชันลูกศรเป็นวิธีที่สั้นกว่าในการเขียนฟังก์ชัน แทนที่จะใช้คีย์เวิร์ด `function` เราใช้ลูกศร (`=>`)


นี่คือฟังก์ชันปกติ:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


เวอร์ชันลูกศรมีลักษณะดังนี้:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


หากฟังก์ชันมี **เพียงบรรทัดเดียว** คุณสามารถข้ามวงเล็บปีกกาและ `return`:


```javascript
const greet = (name) => `Hello, ${name}!`
```


หากฟังก์ชันมี **เพียงพารามิเตอร์เดียว** คุณสามารถข้ามวงเล็บรอบพารามิเตอร์ได้:


```javascript
const greet = name => `Hello, ${name}!`
```


ฟังก์ชันลูกศรเป็นเรื่องปกติมากใน JavaScript สมัยใหม่ เนื่องจากช่วยให้สามารถแสดงฟังก์ชันง่าย ๆ ด้วยโค้ดที่น้อยลงอย่างมาก


### พารามิเตอร์เริ่มต้น


บางครั้งคุณต้องการให้ฟังก์ชันมี **ค่าเริ่มต้น** หากไม่มีการส่งอาร์กิวเมนต์


คุณสามารถทำได้ดังนี้:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


ค่าเริ่มต้น `"friend"` จะถูกใช้เมื่อไม่มีการส่งค่าเข้าไป


### แพร่พารามิเตอร์ (...)


จะเกิดอะไรขึ้นถ้าฟังก์ชันของคุณรับอาร์กิวเมนต์จำนวนยืดหยุ่น?


คุณสามารถใช้ **spread operator** (`...`) เพื่อรวบรวมพวกมันเข้าในอาเรย์:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


จากนั้นคุณสามารถใช้ลูปเพื่อประมวลผลแต่ละรายการ:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


ตัวดำเนินการกระจายมีประโยชน์เมื่อคุณไม่ทราบว่าจะมีการส่งผ่านอาร์กิวเมนต์จำนวนเท่าใด


### ฟังก์ชันลำดับสูง


ฟังก์ชัน**ลำดับสูง**คือฟังก์ชันที่:


*รับฟังก์ชันอื่นเป็นอินพุต*

*และ/หรือ* ส่งคืนฟังก์ชันเป็นผลลัพธ์


นี่คือตัวอย่างง่าย ๆ:


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


สิ่งนี้พิมพ์ว่า:


```
Hello, friend!
Hello, friend!
```


เราสามารถส่งฟังก์ชันลูกศรไปยังมันได้:


```javascript
runTwice(
() => console.log("Hello!")
)
```


สิ่งนี้พิมพ์ว่า:


```
Hello!
Hello!
```


คุณยังสามารถเขียนฟังก์ชันที่**ส่งคืน**ฟังก์ชันอื่น ๆ ได้:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


ฟังก์ชัน `makeGreeter` เป็นฟังก์ชันที่สร้างฟังก์ชันอื่น ๆ มันรับสตริงและส่งคืนฟังก์ชันใหม่ที่ใช้สตริงนั้นในคำสั่ง `console.log` ของมัน


รูปแบบประเภทนี้ทรงพลังมาก เพราะช่วยให้คุณสามารถเว้น "ช่องว่าง" ในฟังก์ชันของคุณที่คุณสามารถเติมเต็มภายหลังด้วยพฤติกรรมที่คุณต้องการได้


### map(), filter(), reduce()


JavaScript ให้เมธอดในตัวที่มีประโยชน์สำหรับใช้กับอาเรย์


วิธีการเหล่านี้รับฟังก์ชันเป็นอาร์กิวเมนต์ ดังนั้นจึงเป็นฟังก์ชันลำดับสูงเช่นกัน


ฟังก์ชัน `map()` จะเปลี่ยนแต่ละรายการในอาเรย์ให้เป็นสิ่งอื่น.


ตัวอย่าง:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


แต่ละตัวเลขถูกคูณสอง และผลลัพธ์คืออาเรย์ใหม่


`filter()` ลบรายการออกจากอาเรย์หากไม่ผ่านการทดสอบ


ตัวอย่าง:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


เฉพาะรายการในอาเรย์ที่เงื่อนไข `x > 2` คืนค่า `true` จะถูกเก็บไว้


`reduce()` ใช้ในการรวมรายการทั้งหมดในอาร์เรย์ให้เป็นค่าเดียว


ตัวอย่าง:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` จะทำการวนผ่านอาเรย์และในตัวอย่างนี้จะใช้ตัวดำเนินการ `+` ระหว่าง `1` และ `2` จากนั้นระหว่างผลลัพธ์ `3` และ `3` จากนั้นระหว่างผลลัพธ์ `6` และ `4` จนกระทั่งได้ผลรวมของรายการทั้งหมดในอาเรย์ (ซึ่งคือ 10)


คุณสามารถใช้ `reduce()` สำหรับหลายสิ่ง เช่น ยอดรวม ค่าเฉลี่ย หรือการสร้างค่าขึ้นใหม่ทีละขั้นตอน


วิธีการเหล่านี้ (`map`, `filter`, `reduce`) เป็นเครื่องมือที่ทรงพลังในการประมวลผลข้อมูลโดยไม่ต้องเขียนลูปด้วยตนเอง


คุณสามารถรวมพวกมันเข้าด้วยกันในลำดับของการดำเนินการได้ เช่นนี้:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## การทำงานกับอ็อบเจกต์

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


ในบทนี้ เราจะได้เรียนรู้เครื่องมือที่ทรงพลังและซับซ้อนขึ้นเล็กน้อยสำหรับการทำงานกับอ็อบเจ็กต์ใน JavaScript


### ทรัพย์สินส่วนตัว


บางครั้ง เราต้องการซ่อนคุณสมบัติของวัตถุเพื่อไม่ให้สามารถเปลี่ยนแปลงหรือเข้าถึงจากภายนอกวัตถุได้ JavaScript ให้เราทำเช่นนี้ได้โดยใช้ `#` นำหน้าชื่อคุณสมบัติ ซึ่งจะสร้างคุณสมบัติ **private** ที่สามารถเข้าถึงได้เฉพาะภายในคลาสเท่านั้น


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


คุณสมบัติส่วนตัวมีประโยชน์เมื่อคุณต้องการป้องกันการเปลี่ยนแปลงโดยไม่ตั้งใจ


### สแตติก Properties


บางครั้ง คุณต้องการให้พร็อพเพอร์ตี้เป็นของคลาสเอง ไม่ใช่ของแต่ละอ็อบเจ็กต์ที่คุณสร้างจากคลาสนั้น นั่นคือสิ่งที่ `static` ใช้สำหรับ พร็อพเพอร์ตี้ `static` จะถูกเก็บไว้ในคลาสและอ็อบเจ็กต์ทั้งหมดของคลาสนั้นจะอ้างอิงถึงมัน


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


นี่มีประโยชน์สำหรับการเก็บข้อมูลและวิธีการที่ใช้ร่วมกันซึ่งใช้กับกลุ่มของวัตถุทั้งหมด ไม่ใช่แค่อันเดียว


### รับและตั้งค่า


ใน JavaScript, `get` และ `set` ช่วยให้คุณสร้างพร็อพเพอร์ตี้ที่ *ดู* เหมือนตัวแปรปกติ แต่จริง ๆ แล้วรันโค้ดพิเศษในเบื้องหลัง


เมธอด `get`ter จะทำงานเมื่อคุณพยายาม *อ่าน* คุณสมบัติ มันถูกประกาศโดยการเขียน `get` ก่อนเมธอดที่มีชื่อของคุณสมบัติ


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


แม้ว่า `fullName` จะไม่ใช่ property ปกติ แต่เราสามารถใช้มันเหมือน property ได้ และเบื้องหลังมันจะเรียกใช้ฟังก์ชัน `get` เพื่อสร้างชื่อเต็ม


เมธอด `set`ter จะทำงานเมื่อคุณ *กำหนด* ค่าให้กับพร็อพเพอร์ตี้ มันช่วยให้คุณควบคุมสิ่งที่เกิดขึ้นเมื่อมีคนพยายามเปลี่ยนค่านั้น โดยจะประกาศโดยการเขียน `set` ก่อนเมธอดที่มีชื่อของพร็อพเพอร์ตี้


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


เมื่อเราทำ `user.fullName = "John Smith"`, มันจะเรียกใช้เมธอด `set` และอัปเดตค่า `firstName` และ `lastName`.


ดังนั้นถึงแม้ว่ามันจะรู้สึกเหมือนเรากำลังตั้งค่าตัวแปรง่าย ๆ แต่จริง ๆ แล้วเรากำลังเรียกใช้ตรรกะที่อัปเดตคุณสมบัติอื่น ๆ


## คีย์และค่า

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


ทุกคุณสมบัติในวัตถุ JavaScript มี **key** (เรียกอีกอย่างว่าชื่อคุณสมบัติ) และ **value**


ตัวอย่างเช่น:


```javascript
const user = {
name: "Alice",
age: 30
}
```


ในอ็อบเจกต์นี้ `"name"` และ `"age"` เป็นคีย์ และ "Alice" และ `30` เป็นค่าของพวกมัน


### การเข้าถึงแบบไดนามิก


บางครั้ง คุณอาจไม่ทราบชื่อของพร็อพเพอร์ตี้ล่วงหน้า...อาจเป็นเพราะคุณได้รับมันจากการป้อนข้อมูลของผู้ใช้ หรืออ่านมันจากตัวแปร คุณยังสามารถเข้าถึงมันได้โดยใช้ **bracket notation** เช่น `myObject["keyName"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


เราได้ส่งสตริง `name` ไปยังอ็อบเจ็กต์เพื่อให้ได้ค่าที่สอดคล้องกัน


เราสามารถบันทึกคีย์ลงในตัวแปรและใช้มันเพื่อเข้าถึงค่าที่สอดคล้องกันในภายหลัง เช่น


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### ไดนามิก Assignment


คุณยังสามารถสร้างหรืออัปเดตคุณสมบัติของวัตถุโดยใช้ตัวแปรเป็นคีย์ได้เช่นกัน


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


นี่มีประโยชน์เมื่อคุณต้องการสร้างวัตถุทีละขั้นตอน ตัวอย่างเช่น:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


คุณสามารถใช้คีย์แบบไดนามิก *ขณะสร้าง* วัตถุโดยใช้วงเล็บสี่เหลี่ยม:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


นี่เรียกว่า **computed property** ค่าภายในวงเล็บสี่เหลี่ยมจะถูกประเมินผล และผลลัพธ์จะถูกใช้เป็นคีย์


### ประเภทสัญลักษณ์


นอกเหนือจากสตริงแล้ว JavaScript ยังให้คุณใช้ประเภทพิเศษที่เรียกว่า `Symbol` เป็นคีย์ของอ็อบเจ็กต์ได้อีกด้วย


มาเริ่มต้นด้วยตัวอย่างง่าย ๆ:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


ในตัวอย่างนี้ `id` เป็น Symbol มันไม่ใช่สตริง แต่ยังคงทำงานเป็นคีย์ได้ หากคุณลองบันทึก `user` ไปที่คอนโซล คุณจะเห็นสิ่งนี้:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


อีกสิ่งที่สำคัญ: สัญลักษณ์ทุกตัวที่คุณสร้างนั้นมีเอกลักษณ์เฉพาะตัว แม้ว่าจะถูกสร้างขึ้นโดยใช้สตริงเดียวกันก็ตาม


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


สัญลักษณ์ช่วยให้คุณกำหนดคีย์ที่ไม่ชนกับคีย์ปกติได้ ตัวอย่างเช่น สมมติว่าคุณมีอ็อบเจ็กต์ที่มีพร็อพเพอร์ตี้ `name` แต่ในอนาคตอ็อบเจ็กต์นี้จะสามารถปรับแต่งได้โดยผู้ใช้ในรูปแบบที่คุณไม่สามารถคาดการณ์ได้ และผู้ใช้อาจเพิ่มพร็อพเพอร์ตี้ `name` เช่นกัน หากพร็อพเพอร์ตี้ `name` ดั้งเดิมถูกกำหนดด้วยสตริง มันจะถูกเขียนทับโดยพร็อพเพอร์ตี้ใหม่ ดังนี้:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


หากเราใช้สัญลักษณ์แทน:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


ตามที่คุณเห็น คุณสมบัติ `name` ดั้งเดิมถูกเก็บรักษาไว้ในลักษณะนี้ ซึ่งอาจมีประโยชน์ในบางกรณีที่เป็นขอบเขต


## วัตถุอรรถประโยชน์

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript ให้วัตถุที่มีประโยชน์ในตัวบางอย่างที่ช่วยให้เราทำสิ่งต่างๆ เช่น การดีบักและการดำเนินการทางคณิตศาสตร์


### วิธีการคอนโซลอื่น ๆ


คุณได้เห็น `console.log` แล้ว ซึ่งใช้พิมพ์ค่าออกไปบนหน้าจอ


มีเมธอดที่มีประโยชน์อื่น ๆ บางอย่างที่มีอยู่ในวัตถุ `console` ที่สามารถช่วยคุณดีบักโปรแกรมของคุณได้


#### `console.warn`


พิมพ์ข้อความเป็นสีเหลือง (หรือมีไอคอนเตือนในบางสภาพแวดล้อม):


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


พิมพ์ข้อความเป็นสีแดง เช่น ข้อผิดพลาด:


```javascript
console.error("Something went wrong!")
```


#### `console.table`


แสดงอาร์เรย์หรืออ็อบเจ็กต์เป็นตาราง:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


สิ่งนี้พิมพ์ตารางเช่น:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


สิ่งนี้สามารถเป็นประโยชน์ในการแสดงข้อมูลที่มีโครงสร้าง


#### `console.time` และ `console.timeEnd`


คุณสามารถวัดระยะเวลาที่บางสิ่งใช้เวลา:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


สิ่งนี้พิมพ์บางอย่างเช่น:


```
timer: 2.379ms
```


มีประโยชน์สำหรับการทดสอบประสิทธิภาพแบบง่าย ๆ บางอย่าง


### The Math Object


JavaScript ให้คุณใช้วัตถุ `Math` ที่มีเมธอดที่มีประโยชน์สำหรับการคำนวณ


#### `Math.random()`


ส่งคืนตัวเลขสุ่มระหว่าง 0 (รวม) และ 1 (ไม่รวม):


```javascript
const r = Math.random()
console.log(r)
```


ตัวอย่างผลลัพธ์:


```
0.4387429859
```


#### `Math.floor()` และ `Math.ceil()`



- `Math.floor(n)` ปัดเศษ **ลง** เป็นจำนวนเต็มที่ใกล้ที่สุด
- `Math.ceil(n)` ปัดเศษ **ขึ้น** เป็นจำนวนเต็มที่ใกล้ที่สุด


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


ปัดเศษเป็นจำนวนเต็มที่ใกล้ที่สุด:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` และ `Math.min()`


ส่งคืนค่าที่มากที่สุดหรือเล็กที่สุดจากรายการตัวเลข:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` และ `Math.sqrt()`



- `Math.pow(a, b)` ให้ค่า `a` ยกกำลัง `b`
- `Math.sqrt(n)` ให้ค่ารากที่สองของ `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# JavaScript ขั้นสูง

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## คอลเลกชันอื่น ๆ

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript ให้ประเภทคอลเลกชันพิเศษบางประเภทที่เกินกว่าการใช้อาร์เรย์และอ็อบเจกต์ทั่วไป ซึ่งรวมถึง `Map` และ `Set`


พวกเขาช่วยคุณจัดเก็บและจัดการกลุ่มของค่า แต่พวกเขาทำงานแตกต่างจากที่คุณเคยเห็นมาก่อน


`Map` คือการรวบรวมของ **คู่คีย์-ค่า** คล้ายกับอ็อบเจกต์ แต่มีความแตกต่างที่สำคัญบางประการ:



- คีย์สามารถเป็น **ค่าใดก็ได้** ไม่ใช่แค่สตริงเท่านั้น

*ลำดับของรายการจะถูกเก็บรักษาไว้*


- มันมีวิธีการในตัวเพื่อให้ง่ายต่อการใช้งาน


คุณสร้างแผนที่ใหม่แบบนี้:


```javascript
const myMap = new Map()
```


สิ่งนี้สร้างแผนที่ว่างเปล่า เพื่อเพิ่มรายการลงไป ให้ใช้ `myMap.set(key, value)`:


```javascript
myMap.set("name", "Alice")
```


สิ่งนี้เพิ่มคีย์ `"name"` ด้วยค่า `"Alice"`


คุณยังสามารถใช้ตัวเลขเป็นคีย์ได้:


```javascript
myMap.set(42, "The answer")
```


และแม้กระทั่งวัตถุเป็นกุญแจ:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


นั่นจะไม่ทำงานกับวัตถุปกติ ซึ่งอนุญาตเฉพาะคีย์ที่เป็นสตริงเท่านั้น


ในการ **รับค่า** ให้ใช้ `myMap.get(key)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


ในการ**ตรวจสอบว่าคีย์มีอยู่หรือไม่** ให้ใช้ `myMap.has(key)`:


```javascript
console.log(myMap.has("name")) // true
```


ในการ**ลบคีย์** ให้ใช้ `myMap.delete(key)`:


```javascript
myMap.delete("name")
```


ในการ**ล้างแผนที่ทั้งหมด** ให้ใช้ `myMap.clear()`:


```javascript
myMap.clear()
```


แผนที่มีประโยชน์มากสำหรับการจัดการคอลเลกชันของค่าขนาดใหญ่ เพราะการเข้าถึงค่าบนแผนที่ขนาดใหญ่มักให้ประสิทธิภาพที่ดีกว่าการเข้าถึงค่าบนวัตถุขนาดใหญ่


### ตั้งค่า


`Set` คือการรวบรวมของ **ค่าเท่านั้น** (ไม่มีคีย์) ซึ่งแต่ละค่าต้องมีความ **ไม่ซ้ำกัน** นั่นหมายความว่า:


*คุณไม่สามารถมีค่าเดียวกันสองครั้ง*

*ค่าจะถูกจัดเก็บตามลำดับที่คุณเพิ่มเข้าไป*


คุณสร้างชุดเช่นนี้:


```javascript
const mySet = new Set()
```


ในการ **เพิ่มค่า** ให้ใช้ `mySet.add(value)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


แม้ว่าเราจะพยายามเพิ่ม `2` สองครั้ง แต่เซ็ตจะเก็บไว้เพียงสำเนาเดียวเท่านั้น


ในการ**ตรวจสอบว่าค่ามีอยู่ในเซ็ตหรือไม่** ให้ใช้ `mySet.has(value)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


ในการ**ลบค่า** ให้ใช้ `mySet.delete(value)`:


```javascript
mySet.delete(2)
```


ในการ**ล้างทุกอย่าง** ให้ใช้ `mySet.clear()`:


```javascript
mySet.clear()
```


`Set` มีประโยชน์เมื่อคุณต้องการเก็บคอลเลกชันของค่าที่ไม่ซ้ำกันโดยไม่ต้องตรวจสอบค่าที่ซ้ำด้วยตนเอง:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


`Set` จะช่วยหลีกเลี่ยงค่าที่ซ้ำกันให้คุณ


## ตัววนซ้ำ

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


สิ่งต่าง ๆ ใน JavaScript ที่คุณสามารถวนซ้ำได้ (เช่น อาเรย์, สตริง, แผนที่, เซ็ต) เป็น **iterable**: พวกมันสามารถให้ตัววนซ้ำสำหรับเนื้อหาของพวกมันได้


**iterator** เป็นวัตถุพิเศษใน JavaScript ที่ช่วยให้คุณผ่านรายการของสิ่งของ **ทีละหนึ่ง**


### ตัววนซ้ำของอ็อบเจกต์


ไม่เหมือนกับอาเรย์หรือแมพ วัตถุปกติ **ไม่สามารถวนซ้ำได้** ด้วย `for...of` หากคุณลองทำเช่นนี้:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


คุณจะได้รับข้อผิดพลาด:


```
TypeError: user is not iterable
```


นั่นเป็นเพราะว่าวัตถุธรรมดาไม่มีตัววนซ้ำในตัว แต่ JavaScript ให้เครื่องมืออื่น ๆ แก่คุณในการวนซ้ำผ่านพวกมัน


#### `Object.keys()`


คุณสามารถใช้ `Object.keys(obj)` เพื่อรับอาเรย์ของ **คีย์** ของอ็อบเจ็กต์ และจากนั้นวนลูปผ่านมัน:


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


สิ่งนี้พิมพ์ว่า:


```
name
age
```


#### `Object.values()`


ในการวนซ้ำผ่าน **ค่า** ให้ใช้ `Object.values()`:


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


สิ่งนี้พิมพ์ว่า:


```
Alice
30
```


#### `Object.entries()`


หากคุณต้องการ**ทั้งคีย์และค่า** ให้ใช้ `Object.entries()`:


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


สิ่งนี้พิมพ์ว่า:


```
name is Alice
age is 30
```


แม้ว่าวัตถุจะไม่สามารถวนซ้ำได้โดยตรง แต่วิธีการเหล่านี้จะช่วยให้คุณเข้าถึงเนื้อหาของพวกมันได้อย่างเต็มที่ในลักษณะที่ทำงานได้ดีกับ `for...of`


แต่ตัววนซ้ำทำงานอย่างไร?


### Symbol.iterator


ความลับเบื้องหลัง iterable ทั้งหมดคือ **สัญลักษณ์** พิเศษที่เรียกว่า `Symbol.iterator`.


สัญลักษณ์นี้เป็นคีย์ในตัวที่บอก JavaScript ว่า: “วัตถุนี้สามารถวนซ้ำได้”


เมื่อคุณเรียกใช้ `myIterable[Symbol.iterator]()`, JavaScript จะส่งคืน **วัตถุอิตอเรเตอร์** ที่มีเมธอด `.next()` ให้คุณ


ลองมาดูกันว่ามันเป็นอย่างไร:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


ทุกครั้งที่เรียกใช้ `.next()` จะให้ค่าถัดไป เมื่อเสร็จสิ้น จะคืนค่า:


```javascript
{ value: undefined, done: true }
```


### ถัดไป()


เมธอด `.next()` ใช้เพื่อดึงรายการถัดไปจากลำดับ


ทุกครั้งที่คุณเรียกใช้ `.next()` คุณจะได้รับอ็อบเจกต์ที่มีสองคีย์:



- `value`: รายการปัจจุบัน
- `done`: ตัวแปรบูลีนที่บอกคุณว่าการวนซ้ำเสร็จสิ้นหรือไม่


มาทำตัวอย่างเต็มกันเถอะ:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


สิ่งนี้พิมพ์ว่า:


```
Lina
Tom
Eva
```


นี่คือวิธีการทำงานของลูป `for...of` เบื้องหลัง: มันใช้รูปแบบนี้กับ `.next()`.


คุณจะได้ผลลัพธ์เดียวกันกับ


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### การทำให้คลาสสามารถวนซ้ำได้


คุณยังสามารถกำหนด **iterable class** ของคุณเองได้โดยการเพิ่มเมธอด `[Symbol.iterator]()`


สมมติว่าเราต้องการคลาสที่แสดงถึง **ช่วงของตัวเลข** เช่น จาก 1 ถึง 5


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


สิ่งนี้พิมพ์ว่า:


```
1
2
3
4
5
```


นี่คือสิ่งที่เกิดขึ้น:


**เราได้กำหนดคลาส `Range`**

*ภายในคลาส เราได้ทำการติดตั้ง `[Symbol.iterator]()` ดังนั้น JavaScript จึงรู้วิธีวนซ้ำมัน*

*เมธอด `next()` จะคืนค่าตัวเลขแต่ละตัวทีละหนึ่ง*

เมื่อเราถึง `end` มันจะคืนค่า `{ done: true }`


ตอนนี้คลาส `Range` ของเราทำงานเหมือนอาเรย์ และเราสามารถใช้มันในลูปใด ๆ ที่คาดหวังอิเทอเรเบิลได้


### ฟังก์ชันตัวสร้างและ yield


เพื่อให้ง่ายต่อการสร้างอิเทอเรเตอร์ JavaScript ให้คุณใช้ **generator functions** โดยใช้คีย์เวิร์ด `function*` (คือ `function` ที่มี `*` ต่อท้าย) และคีย์เวิร์ด `yield`


ลองดู:


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


แต่ละ `yield` จะคืนค่าและ **หยุดชั่วคราว** ฟังก์ชันจนกว่าจะมีการเรียก `.next()` ครั้งถัดไป


คุณยังสามารถวนซ้ำผ่านตัวสร้างด้วย `for...of`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


สิ่งนี้พิมพ์ว่า:


```
1
2
3
```


## การทำงานพร้อมกันด้วยการเรียกกลับ

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


จนถึงตอนนี้ โค้ดของเราเป็นแบบ **synchronous**: มันทำงานทีละบรรทัดตามลำดับ แต่บางสิ่งในโลกแห่งความเป็นจริงต้องใช้เวลา และเราไม่ต้องการให้โปรแกรมทั้งหมดหยุดชั่วคราวในขณะที่รอ


ในบทนี้เราจะมาแนะนำแนวคิดใหม่: **concurrency** มันช่วยให้เราสามารถจัดการลำดับของสิ่งที่ต้องทำได้ นี่มีประโยชน์เมื่อจัดการกับสิ่งต่างๆ เช่น ตัวจับเวลา, การป้อนข้อมูลจากผู้ใช้, หรือการอ่านไฟล์จากดิสก์ JavaScript มีเครื่องมือต่างๆ สำหรับการทำ concurrency


### setTimeout


ฟังก์ชัน `setTimeout` ช่วยให้คุณ **เรียกใช้ฟังก์ชันในภายหลัง** หลังจากเวลาผ่านไปสักระยะหนึ่ง


ตัวอย่าง:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


สิ่งนี้พิมพ์ว่า:


```
Start
End
This runs after 2 seconds
```


แม้ว่า `setTimeout` จะปรากฏอยู่กลางโค้ด แต่มันไม่ได้บล็อกส่วนที่เหลือ แต่จะจัดตารางให้ฟังก์ชันทำงาน **ภายหลัง** และดำเนินการต่อทันที


`2000` หมายถึง 2000 มิลลิวินาที (ซึ่งคือ 2 วินาที)

นี่คือการเขียนใหม่ที่ละเอียดและเป็นมิตรกับผู้เริ่มต้นมากขึ้นของส่วน **Callbacks** และ **Promise** โดยใช้การจัดการข้อมูลและคำอธิบายที่ชัดเจนตลอด:


### การเรียกกลับ


**callback** คือฟังก์ชันที่เรามอบให้กับฟังก์ชันอื่นเพื่อให้มันสามารถถูก **เรียกใช้ในภายหลัง** ได้


ลองมาดูตัวอย่างจริงโดยใช้ตัวเลขกันเถอะ ลองจินตนาการว่าเรามีรายการตัวเลข และเราต้องการที่จะคูณสองให้กับแต่ละตัวเลข จากนั้นใช้ฟังก์ชัน (callback) กับอาร์เรย์ที่ "คูณสอง" แล้ว แต่เราต้องการทำหลังจากการหน่วงเวลาสั้น ๆ ราวกับว่าเรากำลังรออะไรบางอย่างที่ช้า (เช่น การโหลดข้อมูลจากอินเทอร์เน็ต)


นี่คือฟังก์ชันที่ทำเช่นนั้นโดยใช้ **callback**:


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


ลองใช้ฟังก์ชันนี้:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


หลังจาก 1 วินาที ข้อความนี้จะแสดง:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**เกิดอะไรขึ้นที่นี่?**


1. เราผ่าน `input` เป็นรายการของตัวเลขที่เราต้องการจะคูณสอง

2. เราผ่าน **ฟังก์ชันคอลแบ็ค** ที่บอกโปรแกรมว่าจะทำอะไร *หลังจาก* การคูณสอง

3. ภายใน `doubleNumbers` เราจำลองการหน่วงเวลาโดยใช้ `setTimeout` จากนั้นเราจึงทำการคูณสอง

4. เมื่อเสร็จสิ้นแล้ว เราจะเรียก callback บน "doubled" array ที่ได้จากผลลัพธ์


เทคนิคนี้ใช้ได้ผล แต่ลองจินตนาการว่าคุณต้องการทำ **ขั้นตอนเพิ่มเติม** หลังจากนั้น เช่น กรองตัวเลขที่มีค่าน้อยออก แล้วจึงนำมาบวกกัน คุณจะต้อง **ซ้อน** callbacks เพิ่มเติมแบบนี้:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


นี่อ่านยากและยุ่งเหยิง สไตล์นี้เรียกว่า **callback hell** และมันคือสิ่งที่ `Promise` ถูกสร้างขึ้นมาเพื่อแก้ไข


## การทำงานพร้อมกันด้วย Promises

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


`Promise` เป็นวัตถุใน JavaScript ที่มีอยู่แล้วซึ่งแสดงถึงค่าที่จะ **พร้อมในอนาคต**


เราสามารถสร้าง Promise ได้ดังนี้:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


ส่วน `new Promise()` สร้างคำสัญญา


ภายในนั้น เราให้ฟังก์ชันที่มีพารามิเตอร์สองตัว:


`resolve` คือฟังก์ชันที่เราเรียกใช้เมื่อทุกอย่างสำเร็จ

`reject` เป็นฟังก์ชันที่เราเรียกใช้หากมีบางอย่างผิดพลาด


ในตัวอย่างข้างต้น เราเพียงแค่แก้ไขมันทันทีด้วยข้อความ `"It worked!"`.


### .then()


ในการทำบางสิ่ง **หลังจาก** ที่คำสัญญาเสร็จสิ้น เราใช้ `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


สิ่งนี้พิมพ์ว่า:


```
The result is: 100
```


ค่าที่เราส่งไปยัง `resolve()` จะถูกส่งไปยังฟังก์ชันภายใน `.then()` เป็น `result`


ลองจำลองงานที่ใช้เวลา 2 วินาทีโดยใช้ `setTimeout`:


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


สิ่งนี้จะรอ 2 วินาทีแล้วพิมพ์:


```
Done waiting!
```


### ปฏิเสธ()


มาสร้างคำสัญญาที่ **ล้มเหลว** กันเถอะ:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


ตอนนี้ถ้าเราใช้ `.then()` กับสิ่งนี้ จะไม่มีอะไรเกิดขึ้น เพราะ `.then()` จัดการเฉพาะความสำเร็จเท่านั้น


ในการจัดการข้อผิดพลาด เราใช้ `.catch()`:


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


สิ่งนี้พิมพ์เท่านั้น


```
Caught an error: Something went wrong
```


ค่าที่ส่งไปยัง `reject()` จะถูกส่งไปยังฟังก์ชัน `.catch()`


มาสร้าง Promise ที่ **บางครั้งทำงานและบางครั้งล้มเหลว** โดยอิงตามเงื่อนไขบางอย่างกันเถอะ


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


ตอนนี้เราสามารถเรียกสิ่งนี้และจัดการทั้งสองกรณี:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


สิ่งนี้พิมพ์ว่า:


```
Success: Positive number
```


และถ้าเราลองใช้ตัวเลขที่แตกต่าง:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


มันพิมพ์ว่า:


```
Failure: Not a positive number
```


### การเชื่อมโยงการดำเนินการโดยใช้ Promises



เราสามารถเขียนตัวอย่างก่อนหน้านี้ใหม่โดยใช้ `Promise` และมันจะดูสะอาดตามากขึ้น


มาเริ่มต้นด้วยการเขียนเวอร์ชันใหม่ของฟังก์ชันการคูณสองของเรา แต่คราวนี้จะคืนค่าเป็น **promise**:


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


ตอนนี้เราสามารถใช้ `.then()` เพื่อบอก JavaScript ว่าต้องทำอะไรกับผลลัพธ์:


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


สิ่งนี้พิมพ์ว่า:


```
Doubled numbers: [ 2, 4, 6 ]
```


จนถึงตอนนี้ สิ่งนี้ทำงานเหมือนกับเวอร์ชันที่ใช้ callback แต่ตอนนี้โค้ดสามารถขยายและอ่านได้ง่ายขึ้น


สมมติว่าเราต้องการเพิ่มขั้นตอนเพิ่มเติม:


1. ขั้นแรก ให้คูณตัวเลขทั้งหมดด้วยสอง

2. จากนั้น ลบตัวเลขที่น้อยกว่า 4

3. สุดท้าย, รวมทั้งหมดเข้าด้วยกัน


เราสามารถเขียนฟังก์ชันหนึ่งสำหรับแต่ละขั้นตอน โดยใช้ promises ทั้งหมด:


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


ตอนนี้เราสามารถ **เชื่อมโยง** พวกมันเข้าด้วยกันแบบนี้:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


สิ่งนี้พิมพ์ว่า:


```
Final result after all steps: 10
```


มาดูกันว่ามันทำอะไรบ้าง:


1. `doubleNumbers` เพิ่มค่าของอาร์เรย์เป็นสองเท่า: `[2, 4, 6]`

2. `filterBigNumbers` ลบทุกอย่างที่ ≤ 3: `[4, 6]`

3. `sumNumbers` เพิ่มตัวเลขที่เหลือ: `4 + 6 = 10`

4. สุดท้ายนี้ เราพิมพ์ผลลัพธ์ออกมา


แต่ละ `.then()` จะรอให้ขั้นตอนก่อนหน้าสิ้นสุดลง ดังนั้นเราสามารถสร้าง **ห่วงโซ่ของการกระทำ** ได้โดยไม่ต้องซ้อนกัน ซึ่งทำให้โค้ดอ่านง่ายขึ้นและแก้ไขข้อบกพร่องได้ง่ายขึ้น


## การทำงานพร้อมกันด้วย async/await

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


เราได้เห็นแล้วว่า `Promise` chains ช่วยให้เราหลีกเลี่ยง callback hell ได้อย่างไร แต่พวกมันยังคงอ่านยากเล็กน้อยเมื่อมีหลายขั้นตอนที่เกี่ยวข้อง


นั่นคือที่มาของ `async` และ `await` พวกมันช่วยให้เราเขียนโค้ดแบบอะซิงโครนัส **ที่ดูเหมือนโค้ดแบบซิงโครนัส** ซึ่งทำให้ง่ายต่อการเข้าใจมากขึ้น


### async คืออะไร?


เมื่อคุณเขียนคีย์เวิร์ด `async` ไว้ก่อนฟังก์ชัน JavaScript จะทำการห่อหุ้มค่าที่ฟังก์ชันส่งคืนใน Promise โดยอัตโนมัติ


ลองดูตัวอย่างพื้นฐาน:


```javascript
async function greet() {
return "hello"
}
```


หากคุณเรียกใช้ฟังก์ชันนี้:


```javascript
const result = greet()
console.log(result)
```


คุณจะเห็นสิ่งนี้:


```
Promise { 'hello' }
```


แม้ว่าคุณจะเพิ่งส่งคืนสตริง JavaScript จะเปลี่ยนมันเป็น Promise ให้คุณ คุณสามารถรับค่าจริงโดยใช้ `.then()` ดังนี้:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


หรือคุณสามารถใช้ `await`...


### await คืออะไร?


คีย์เวิร์ด `await` บอก JavaScript ว่า: “รอจนกว่า Promise นี้จะเสร็จสิ้น แล้วจึงให้ผลลัพธ์กับฉัน”


แต่คุณสามารถใช้ `await` **ภายในฟังก์ชัน async** เท่านั้น


มาเขียนตัวอย่างใหม่โดยใช้ `await`:


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


ตอนนี้เราสามารถใช้ผลลัพธ์เหมือนกับเป็นค่าปกติได้แล้ว


มาทำอะไรที่มีประโยชน์มากขึ้นกันเถอะ


### จำลองความล่าช้าด้วย await


เราจะสร้างฟังก์ชัน `wait` แบบง่าย ๆ ที่รับจำนวนมิลลิวินาทีเป็นอาร์กิวเมนต์และจะทำการ resolve หลังจากเวลาผ่านไปตามจำนวนนั้น โดยไม่ทำอย่างอื่น:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


ลองใช้มันดู:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


สิ่งนี้พิมพ์ว่า:


```
waiting 2 seconds...
done waiting
```


คุณสามารถคิดว่า `await` เป็น "หยุดที่นี่จนกว่าสัญญาจะเสร็จสิ้น แล้วค่อยดำเนินการต่อ"


สิ่งนี้ช่วยให้คุณเขียนโค้ดในรูปแบบ **จากบนลงล่าง** ที่ทำงานแบบอะซิงโครนัส โดยไม่ต้องเชื่อมโยงการเรียกใช้ `.then()`


### รอข้อมูล


ลองใช้ตัวอย่างก่อนหน้านี้ของเรา ที่เราทำการคูณสองตัวเลข จากนั้นกรอง แล้วจึงรวมผลลัพธ์ แต่คราวนี้เราจะใช้ `async`/`await`


เราจะสร้างฟังก์ชัน 3 ตัวที่จำลองการรอคอย และคืนค่า Promises:


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


ตอนนี้มาเขียนฟังก์ชัน `async` เพื่อรวมพวกมัน:


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


สิ่งนี้พิมพ์ว่า:


```
Final result: 10
```


นี่อ่านง่ายกว่าการใช้ `.then()` ต่อกันหรือการซ้อน callbacks มาก


มันดูเหมือนโปรแกรมทีละขั้นตอนปกติ แต่ยังคงทำงานแบบอะซิงโครนัส


## ตัววนซ้ำแบบไม่ประสานเวลา

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


คุณได้เรียนรู้เกี่ยวกับ **iterators** แล้วและวิธีที่เราสามารถใช้ `for...of` เพื่อวนซ้ำผ่านอาเรย์และสิ่งที่สามารถวนซ้ำได้อื่น ๆ


แต่ถ้าข้อมูลที่เราต้องการวนซ้ำใช้เวลานานกว่าจะมาถึงล่ะ?


บางครั้งเราต้องการวนซ้ำกับสิ่งที่มาถึง **แบบอะซิงโครนัส** เช่น ข้อความจากการแชท บรรทัดจากไฟล์ หรือหมายเลขจากแหล่งที่มาที่ช้า


ในการทำเช่นนั้น JavaScript ให้เราใช้ **async iterators**


### ฟังก์ชันตัวสร้างแบบอะซิงค์


วิธีที่ง่ายที่สุดในการสร้าง async iterator คือการใช้ **async generator function**


เราเขียนแบบนี้:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


นี่ดูเหมือนเครื่องกำเนิดไฟฟ้าปกติ แต่มี `async` อยู่ข้างหน้า


เราสามารถใช้ `for await...of` เพื่อใช้ค่า:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


นี่จะแสดงผล:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


แล้วมันต่างจากเครื่องกำเนิดไฟฟ้าปกติอย่างไร?


ความแตกต่างคือ: ตอนนี้เราสามารถใช้ `await` ภายใน generator ได้แล้ว


มาสร้างตัวช่วยหน่วงเวลาอีกครั้ง:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


ตอนนี้ให้เราค่อยๆ **คำนวณ** ตัวเลข:


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


ลองใช้ดู:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### ทำไมต้องใช้ตัววนซ้ำแบบอะซิงโครนัส?


ตัววนซ้ำแบบอะซิงโครนัสมีประโยชน์เมื่อ:


*ค่าทั้งหมดไม่ได้มาถึงพร้อมกัน*

*คุณต้องการจัดการกับพวกเขาทีละคน,* **ตามที่พวกเขามา**.

**คุณกำลังทำงานกับ Promises และต้องการวนลูปในวิธีที่สะอาด**


ตัวอย่างเช่น หากคุณต้องการโหลดข้อความจากเซิร์ฟเวอร์แชททีละข้อความ หรือดาวน์โหลดไฟล์ขนาดใหญ่เป็นส่วน ๆ ตัววนซ้ำแบบอะซิงค์จะช่วยให้คุณเขียนลูป `for` ที่ทำงานกับข้อมูลที่ล่าช้าได้


### Symbol.asyncIterator


เรายังสามารถใช้ async iterators ในคลาสที่กำหนดเองได้


นี่คือตัวอย่างที่สร้างตัวเลขพร้อมกับความล่าช้า:


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


เราสามารถใช้ `for await...of` ได้เหมือนเดิม:


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


สิ่งนี้ช่วยให้คุณสร้างวัตถุที่สามารถวนซ้ำได้แบบอะซิงโครนัส


## Assignment ไวยากรณ์น้ำตาล

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Syntax sugar" หมายถึงการเขียนบางสิ่งในรูปแบบที่สั้นลงหรือง่ายขึ้น โดยไม่เปลี่ยนแปลงสิ่งที่มันทำ มันเป็นเพียงวิธีที่น่าฟังขึ้นในการพูดสิ่งเดียวกัน


JavaScript มีไวยากรณ์ที่สร้างขึ้นมาเพื่อให้เราเขียนคำประกาศได้สะอาดและสั้นลง ในบทนี้ เราจะมาดูวิธีการกำหนดค่าโดยอิงตามเงื่อนไข อัปเดตตัวแปรด้วยคณิตศาสตร์ ดึงค่าจากอาเรย์หรืออ็อบเจ็กต์ และคัดลอกหรือรวมค่าด้วยไวยากรณ์ที่ง่ายขึ้น


### ตัวดำเนินการแบบสามส่วน


ใน JavaScript คุณสามารถกำหนดค่าโดยอิงตามเงื่อนไขโดยใช้ **ternary operator** ซึ่งเป็นวิธีการเขียน `if...else` แบบย่อ


แทนที่จะทำ:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


คุณสามารถเขียน:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


นี่หมายถึง:



- ถ้า `isMorning` เป็นจริง ให้ใช้ `"Good morning"`

*มิฉะนั้น ให้ใช้ `"Hello"`*


รูปแบบทั่วไปคือ:


```javascript
condition ? valueIfTrue : valueIfFalse
```


คุณสามารถใช้มันภายในนิพจน์อื่นๆ ได้เช่นกัน:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


เพียงตรวจสอบให้แน่ใจว่าใช้สำหรับการตัดสินใจที่**ง่าย** หากตรรกะมีความซับซ้อน ให้ใช้ `if...else`


### ผู้ปฏิบัติงาน Assignment ทางเลือก


JavaScript มี **ตัวดำเนินการทางลัด** สำหรับการกำหนดค่าแบบรวมกับการดำเนินการ


ลองมาดูวิธีปกติกัน:


```javascript
let counter = 1
counter = counter + 1
```


สิ่งนี้สามารถย่อได้เป็น:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


นี่คือสิ่งที่พบได้บ่อยที่สุด:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

ตัวอย่าง:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


สิ่งเหล่านี้มีประโยชน์เมื่อคุณต้องการอัปเดตตัวแปรโดยใช้ค่าของมันเอง


### การทำลายโครงสร้าง


**Destructuring** ช่วยให้คุณนำค่าจากอาเรย์หรืออ็อบเจ็กต์ออกมาและเก็บไว้ในตัวแปรได้อย่างง่ายดาย


#### อาเรย์


สมมติว่าคุณมี:


```javascript
const colors = ["red", "green", "blue"]
```


แทนที่จะทำ:


```javascript
const first = colors[0]
const second = colors[1]
```


คุณสามารถทำได้:


```javascript
const [first, second] = colors
```


นี่กำหนด:


`*first*` ถึง `"red"`


- `second` to `"green"`


คุณสามารถข้ามค่าได้เช่นกัน:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### วัตถุ


คุณสามารถดึงค่าออกจากอ็อบเจ็กต์ได้เช่นกัน:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


หากคุณสมบัติมีชื่อแตกต่างจากตัวแปรที่คุณต้องการ คุณสามารถเปลี่ยนชื่อได้:


```javascript
const { name: username } = user
console.log(username) // Alice
```


การทำ Destructuring ทำให้โค้ดของคุณสะอาดขึ้นเมื่อทำงานกับอ็อบเจ็กต์และอาเรย์


### สเปรดซินแทกซ์


ไวยากรณ์ **spread** ใช้ `...` เพื่อแยกหรือคัดลอกค่า


#### อาร์เรย์


คุณสามารถคัดลอกหรือรวมอาเรย์:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


คุณยังสามารถโคลนแอเรย์ได้:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### วัตถุ


คุณสามารถทำเช่นเดียวกันกับวัตถุ:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


คุณยังสามารถแทนที่ค่า:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


สิ่งนี้มีประโยชน์มากเมื่ออัปเดตวัตถุโดยไม่เปลี่ยนแปลงต้นฉบับ


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## เราไปถึง Node ได้อย่างไร

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


ในบทนี้เราจะเรียนรู้เกี่ยวกับบริบททางประวัติศาสตร์เล็กน้อยเกี่ยวกับ JavaScript และ NodeJS


บริบททางประวัติศาสตร์มีความสำคัญมากในซอฟต์แวร์ เพราะเรามักใช้เครื่องมือที่สร้างโดยผู้อื่น และเราจึงได้รับอิทธิพลจากการตัดสินใจที่พวกเขาทำในอดีต


การเข้าใจเหตุผลเบื้องหลังการตัดสินใจเหล่านั้น และวิธีที่เครื่องมือที่เราใช้กลายมาเป็นอย่างที่มันเป็น จะช่วยให้เรารู้สึกสับสนน้อยลงเกี่ยวกับสิ่งที่เรากำลังทำอยู่


### ต้นกำเนิดของ JavaScript


JavaScript เริ่มต้นเป็นภาษาง่าย ๆ ที่ออกแบบมาเพื่อทำให้หน้าเว็บมีปฏิสัมพันธ์


ในช่วงทศวรรษ 1990 เว็บเบราว์เซอร์อย่าง Netscape Navigator ได้เพิ่ม JavaScript เพื่อให้นักพัฒนาสามารถเขียนโค้ดที่ทำงานโดยตรงในเบราว์เซอร์ได้


แนวคิดดั้งเดิมคือการใช้ Java เป็นภาษาหลักในการสร้างเว็บไซต์ (ด้วยสิ่งที่เรียกว่า "Java applets") และใช้ JavaScript สำหรับสิ่งเล็กน้อยเท่านั้น


การออกแบบหลักถูกทำโดย Brendan Eich ซึ่งในขณะนั้นเป็นพนักงานที่ Netscape ในเวลาน้อยกว่า 2 สัปดาห์


แต่คนส่วนใหญ่ชอบใช้ JavaScript มากกว่า Java และนอกจากนี้ Java applets ยังมีปัญหาด้านความปลอดภัยในขณะนั้น ดังนั้นในที่สุด Java จึงถูกยกเลิกเป็นตัวเลือก และ JavaScript ก็กลายเป็นมาตรฐานโดยพฤตินัยสำหรับการพัฒนาเว็บ


### เครื่องยนต์ V8


JavaScript เป็นภาษาที่แปลในขณะรัน (interpreted language) ซึ่งแตกต่างจากภาษาที่ต้องคอมไพล์ (compiled languages) อย่างเช่น C.


โค้ดที่เขียนในภาษาที่คอมไพล์จะถูกแปลงเป็นไบนารี และไบนารีนั้นจะถูกป้อนโดยตรงไปยัง CPU ของคอมพิวเตอร์


![](assets/en/006.webp)


ในทางกลับกัน ภาษาแปลความมีแนวโน้มที่จะเป็นมิตรกับผู้ใช้มากกว่า และใกล้เคียงกับวิธีที่มนุษย์คิด ("ระดับสูง") มากกว่าวิธีที่เครื่องจักรทำงาน ("ระดับต่ำ"); ดังนั้นพวกเขามักจะมีเครื่องเสมือนที่สร้างขึ้นเพื่อรันโค้ดของพวกเขา


เครื่องเสมือนเป็นโปรแกรมพิเศษที่อยู่ระหว่างโค้ดที่คุณเขียนและ CPU และทำการประมวลผลโค้ดของคุณ (เนื่องจาก CPU ไม่สามารถเข้าใจได้)


สิ่งนี้ช่วยให้คุณสามารถเขียนโปรแกรมได้โดยไม่ต้องรู้มากเกี่ยวกับเครื่องจักรพื้นฐาน แต่ก็มีค่าใช้จ่ายในแง่ของประสิทธิภาพ เพราะคอมพิวเตอร์ไม่ได้รันแค่โปรแกรมของคุณ; มันกำลังรันโปรแกรม (เครื่องเสมือน) ที่รันโปรแกรมของคุณ


เมื่อแอปพลิเคชันเว็บมีความซับซ้อนมากขึ้น ความต้องการในการปรับปรุงประสิทธิภาพของ JavaScript ก็เพิ่มขึ้น เครื่องยนต์ V8 เป็นตัวแปลที่ขับเคลื่อน JavaScript ใน Google Chrome มันถูกพัฒนาขึ้นที่ Google และเปิดตัวในปี 2008


ในขณะที่เอนจิน JavaScript รุ่นเก่าส่วนใหญ่เป็นเครื่องเสมือนแบบดั้งเดิม เอนจิน V8 เป็นคอมไพเลอร์ JIT (just-in-time)


โค้ด JavaScript ถูกป้อนเข้าสู่เอนจิน V8 และเอนจินพยายามคอมไพล์บางส่วนของโค้ดให้เป็นไบนารีเนทีฟในทันที สิ่งนี้ทำให้คุณได้รับประสบการณ์ของภาษาระดับสูง พร้อมกับประสิทธิภาพที่ใกล้เคียงกับภาษาระดับต่ำมากขึ้น สิ่งนี้ทำให้ JavaScript เป็นภาษาระดับสูงที่เร็วที่สุดในโลก เป็นเหมือน "ดีที่สุดของทั้งสองโลก"


### รันไทม์ NodeJS


แม้ว่าจะใช้งานง่ายและดำเนินการได้ค่อนข้างรวดเร็ว แต่หลังจากการเปิดตัว V8 JavaScript ยังคงมีข้อจำกัดใหญ่: มันสามารถทำงานได้เฉพาะภายในเบราว์เซอร์เท่านั้น


ทำไมถึงเป็นปัญหาล่ะ?


เนื่องจากเบราว์เซอร์ทำการประมวลผลโค้ดที่ดึงมาจากแหล่งต่าง ๆ นับล้านบนอินเทอร์เน็ต พวกมันจึงสามารถติดมัลแวร์ได้ง่าย ดังนั้นพวกมันจึงถูก "แซนด์บ็อกซ์" จากส่วนที่เหลือของระบบปฏิบัติการ


![](assets/en/007.webp)


JavaScript ไม่สามารถเข้าถึงระบบไฟล์และทรัพยากรท้องถิ่นอื่น ๆ บนคอมพิวเตอร์ของคุณได้ (อย่างน้อยก็ไม่ง่ายเหมือนภาษาอื่น ๆ) ดังนั้นจึงเป็นข้อจำกัดที่สำคัญต่อประเภทของแอปพลิเคชันที่คุณสามารถสร้างด้วยมัน


ในปี 2009 Ryan Dahl ได้เผยแพร่ NodeJS ซึ่งเป็น runtime ที่ช่วยให้คุณสามารถใช้ V8 engine นอกเบราว์เซอร์ได้โดยตรงบนระบบปฏิบัติการพื้นเมืองของคอมพิวเตอร์ของคุณ นอกจากนี้ยังเพิ่มคุณสมบัติมากมายที่มีประโยชน์สำหรับการเขียนโปรแกรมฝั่งเซิร์ฟเวอร์และโปรแกรมบรรทัดคำสั่ง ตัวอย่างเช่น คุณสามารถใช้ NodeJS เพื่อสร้างเว็บเซิร์ฟเวอร์ อ่านและเขียนไฟล์ หรือสร้างเครื่องมือที่ทำงานอัตโนมัติ


![](assets/en/008.webp)


ในหลักสูตรนี้จนถึงตอนนี้ เราได้สำรวจคุณสมบัติของ JavaScript ที่มีอยู่ทั้งในเบราว์เซอร์และใน NodeJS คุณสมบัติเหล่านั้นทำให้เราสามารถกำหนดข้อมูลและจัดการกับมันในรูปแบบที่เป็นนามธรรมได้ ในบทเรียนถัดไป เราจะสำรวจคุณสมบัติที่เฉพาะเจาะจงสำหรับ NodeJS และช่วยให้เราสามารถโต้ตอบกับระบบปฏิบัติการได้


## อาร์กิวเมนต์บรรทัดคำสั่ง

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS ช่วยให้เราสามารถสร้าง CLI (Command Line Interfaces) ได้ในหลายๆ อย่าง


สำหรับสิ่งนั้นเราจำเป็นต้องมีวิธีรับอาร์กิวเมนต์บรรทัดคำสั่ง ซึ่งใน Node จะทำโดยใช้วัตถุ `process` ที่มีอยู่ในตัว


### กระบวนการ


NodeJS มีอ็อบเจกต์พิเศษที่เรียกว่า `process` ซึ่งแสดงถึงโปรแกรมที่กำลังทำงานอยู่ในปัจจุบัน


คุณสามารถใช้มันเพื่อตรวจสอบสภาพแวดล้อม ไดเรกทอรีการทำงานปัจจุบัน และแม้กระทั่งออกจากโปรแกรมเมื่อจำเป็น


ตัวอย่างเช่น:


```javascript
console.log(process.platform)
```


นี่จะแสดงแพลตฟอร์มของระบบปฏิบัติการ เช่น `win32`, `linux`, หรือ `darwin` (Mac)


### process.argv


เมื่อคุณรันโปรแกรม NodeJS จากเทอร์มินัล คุณสามารถส่งคำเพิ่มเติม (arguments) หลังจากชื่อสคริปต์ได้ คำเหล่านี้จะถูกเก็บไว้ใน `process.argv`.


ตัวอย่างเช่น หากคุณรันคำสั่งนี้:


```
node my_script.js alpha beta
```


คุณสามารถพิมพ์อาร์กิวเมนต์ได้ดังนี้:


```javascript
console.log(process.argv)
```


เอาต์พุตอาจมีลักษณะดังนี้:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


รายการสองรายการแรกมักจะเป็นเส้นทางของ Node และเส้นทางของสคริปต์ของคุณ คำเพิ่มเติมใด ๆ ที่คุณส่งผ่านไปยังสคริปต์จะตามมาหลังจากนั้น


อาร์เรย์ `process.argv` สามารถตัดได้เหมือนอาร์เรย์อื่น ๆ โดยใช้เมธอด `.slice()` ดังนั้นเพื่อให้ได้เฉพาะอาร์กิวเมนต์ที่ถูกส่งผ่านคุณสามารถทำได้


```javascript
const args = process.argv.slice(2)

console.log(args)
```


การเข้าถึงอาร์กิวเมนต์ที่ผู้ใช้ส่งผ่านเป็นสิ่งสำคัญในการพัฒนาแอปพลิเคชันบรรทัดคำสั่ง


## โมดูล

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


รันไทม์ JavaScript เช่น NodeJS มักจะถือว่าไฟล์ JavaScript แต่ละไฟล์เป็นโมดูลแยกต่างหาก


คิดถึงโมดูลเหมือนเป็นกล่อง กล่องนี้มีพื้นที่ส่วนตัวของมันเอง ดังนั้นตัวแปรและฟังก์ชันที่คุณประกาศในนั้นจะไม่รบกวนกับโค้ดในกล่องอื่น ๆ โดยพื้นฐานแล้ว แต่ละโมดูลจะมีขอบเขตของตัวเอง


โมดูลสามารถส่งออกเนื้อหาบางส่วนของมัน ทำให้สามารถใช้งานได้กับโมดูลอื่น ๆ และสามารถนำเข้าเนื้อหาที่โมดูลอื่น ๆ ได้ส่งออกไว้ JavaScript อนุญาตให้คุณส่งออกและนำเข้าเนื้อหาระหว่างโมดูล เพื่อเชื่อมต่อไฟล์ต่าง ๆ เข้าด้วยกัน


โปรแกรม JavaScript มักประกอบด้วยโมดูลหลายตัวที่เชื่อมต่อกัน


ทำไมต้องใช้โมดูล? โดยการแยกโค้ดของคุณออกเป็นโมดูล คุณสามารถจัดระเบียบโปรแกรมของคุณให้เป็นส่วนที่เล็กลง ชัดเจนขึ้น และนำกลับมาใช้ใหม่ได้ แต่ละโมดูลสามารถมุ่งเน้นไปที่งานประเภทเดียว เช่น การจัดการการคำนวณทางคณิตศาสตร์ การทำงานกับไฟล์ หรือการจัดรูปแบบข้อความ


### โมดูล CommonJS


ใน NodeJS ระบบที่ใช้จัดการโมดูลที่พบมากที่สุดเรียกว่า **CommonJS**.


ในระบบนี้ คุณสามารถแชร์ (ส่งออก) โค้ดจากโมดูลโดยใช้ `module.exports` และโหลด (นำเข้า) ในไฟล์อื่นโดยใช้ `require()`


ในการทำให้บางสิ่งสามารถใช้งานได้ภายนอกโมดูล คุณต้องกำหนดให้กับ `module.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


ที่นี่ สตริง `"Hello!"` คือสิ่งที่โมดูลนี้ส่งออก


ในการใช้โค้ดที่ส่งออกจากไฟล์อื่น คุณใช้ฟังก์ชัน `require()` พร้อมกับเส้นทางไปยังไฟล์นั้น:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


สิ่งนี้พิมพ์ว่า:


```
Hello!
```


คุณสามารถส่งออกหลายสิ่งได้โดยการรวมเข้าด้วยกันในอ็อบเจกต์นิรนาม เช่น


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS เป็นระบบโมดูลที่ถูกนำมาใช้ในตอนแรกโดย NodeJS ต่อมา ES modules ก็ถูกเพิ่มเข้ามาเช่นกัน


### โมดูล ES


NodeJS ยังรองรับโมดูลอีกประเภทหนึ่งที่เรียกว่า **ES Modules** ซึ่งเป็นที่นิยมในการพัฒนาเว็บ พวกเขาใช้คีย์เวิร์ด `export` และ `import`.


โมดูล ES ถูกพัฒนาขึ้นสำหรับเบราว์เซอร์และถูกเพิ่มเข้าไปใน Node ในภายหลัง หากคุณต้องการใช้งาน คุณอาจต้องใช้ `.mjs` เป็นนามสกุลไฟล์แทน `.js` ขึ้นอยู่กับเวอร์ชันของ Node ที่คุณใช้งานอยู่


ในไฟล์หนึ่งที่ชื่อว่า `greeting.mjs` เราเขียน


```javascript
export const greeting = "Hello!"
```

ตามที่คุณเห็น เรากำลังส่งออกค่าคงที่โดยตรงในที่ที่มันถูกกำหนด


ในไฟล์อีกไฟล์หนึ่งที่ชื่อว่า `index.mjs` เรานำเข้ามัน:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


คุณสามารถส่งออกการประกาศที่แตกต่างกันในส่วนต่าง ๆ ของไฟล์ เช่น


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### ไลบรารีมาตรฐานของ NodeJS


NodeJS ยังมีโมดูลในตัวหลายตัว โมดูลเหล่านี้เป็นโมดูลที่พร้อมใช้งานซึ่งจัดเตรียมโดย NodeJS เพื่อช่วยในงานทั่วไป เช่น การอ่านไฟล์ การทำงานกับระบบปฏิบัติการ หรือการเชื่อมต่อกับเครือข่าย


ตัวอย่างเช่น โมดูล `os` ให้ข้อมูลเกี่ยวกับระบบปฏิบัติการของคุณ:


```javascript
const os = require("os")

console.log(os.platform())
```


คุณไม่จำเป็นต้องติดตั้งโมดูลที่มีอยู่ในตัวเหล่านี้ เพราะมันมาพร้อมกับ NodeJS พวกมันเป็น "ไลบรารีมาตรฐาน" ของรันไทม์ และถูกใช้โดยแอปพลิเคชัน Node ส่วนใหญ่ในการทำสิ่งต่างๆ เช่น การอ่านไฟล์หรือการสื่อสารผ่านอินเทอร์เน็ต


บทต่อไปจะแสดงตัวอย่างที่มีประโยชน์ของการใช้งานให้คุณดู


## โมดูล fs

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


โมดูล `fs` (ย่อมาจาก **file system**) เป็นส่วนหนึ่งของไลบรารีมาตรฐานของ NodeJS มันช่วยให้คุณทำงานกับไฟล์และไดเรกทอรีบนคอมพิวเตอร์ของคุณ: คุณสามารถอ่านไฟล์ เขียนไฟล์ ลบไฟล์ เปลี่ยนชื่อไฟล์ และอื่นๆ


ในการใช้งาน คุณจำเป็นต้องนำเข้ามันที่ด้านบนของไฟล์ของคุณก่อน:


```javascript
const fs = require("fs")
```


### ซิงค์ API


วิธีที่ง่ายที่สุดในการใช้ `fs` คือการใช้เมธอด **sync** ของมัน


วิธีการเหล่านี้จะบล็อกโปรแกรมจนกว่าจะเสร็จสิ้น (ดังนั้นบรรทัดถัดไปของโค้ดจะไม่ทำงานจนกว่าการดำเนินการจะเสร็จสมบูรณ์)


นี่คือตัวอย่างของการอ่านไฟล์แบบ synchronous:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


หากมีไฟล์ชื่อ `example.txt` อยู่ในไดเรกทอรีเดียวกับสคริปต์ของคุณ สิ่งนี้จะพิมพ์เนื้อหาของไฟล์ออกมา


คุณยังสามารถเขียนไปยังไฟล์แบบซิงโครนัส:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


สิ่งนี้จะสร้าง (หรือเขียนทับ) ไฟล์ที่ชื่อว่า `output.txt` พร้อมกับข้อความ


นี่คือการดำเนินการทั่วไปบางอย่างที่คุณสามารถทำได้ด้วย API นี้:


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


Sync API นั้นเรียบง่ายและเหมาะสำหรับสคริปต์ขนาดเล็ก แต่เนื่องจากมันจะบล็อกโปรแกรมจนกว่าจะเสร็จสิ้น มันอาจทำให้ช้าลงหากคุณกำลังทำงานกับไฟล์ขนาดใหญ่หรือเซิร์ฟเวอร์


### เรียกกลับแบบอะซิงโครนัส API


**callback API** เป็นแบบไม่บล็อก: มันช่วยให้ NodeJS ทำสิ่งอื่นต่อไปได้ในขณะที่การดำเนินการไฟล์เกิดขึ้น


แทนที่จะส่งคืนผลลัพธ์โดยตรง มันจะรับฟังก์ชัน (เรียกว่า **callback**) ซึ่งจะถูกเรียกเมื่อการดำเนินการเสร็จสิ้น


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


นี่คือสิ่งที่เกิดขึ้น:


`fs.readFile` เริ่มอ่าน `example.txt`.

*NodeJS ไม่รอ มันดำเนินการโค้ดอื่นที่คุณอาจเขียนไว้ต่อไป*

*เมื่ออ่านไฟล์เสร็จแล้ว, callback จะทำงาน:*



  - หากมีข้อผิดพลาด `err` จะมีข้อผิดพลาดนั้นอยู่
  - มิฉะนั้น `data` จะมีเนื้อหาอยู่


นี่คือวิธีการเขียนลงในไฟล์:


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


แนวคิดเดียวกัน: โปรแกรมไม่หยุดขณะเขียนไฟล์


ตัวอย่างบางอย่างที่คุณสามารถทำได้ด้วย API นี้:


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


การเรียกกลับ API เหมาะสำหรับเซิร์ฟเวอร์และงานขนาดใหญ่เพราะมันไม่บล็อกโปรแกรม แต่การเรียกกลับที่ซ้อนกันอาจยุ่งเหยิงหากคุณเชื่อมโยงการดำเนินการหลายอย่าง นั่นคือเหตุผลที่มีการเพิ่ม API แบบอะซิงค์ที่ใช้คำสัญญา


### คำสัญญา async API


API ที่ใช้ Promise เป็นพื้นฐานนั้นทันสมัยและทำงานได้ดีด้วย `.then()` และ `async/await` สามารถใช้งานได้ในรูปแบบ `fs.promises`.


คุณจำเป็นต้องนำเข้า `promises` property:


```javascript
const fs = require("fs").promises
```


การใช้ `.then()`:


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


หรือดียิ่งกว่านั้น ใช้ `async/await`:


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


การเขียนลงไฟล์:


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


รายการตัวอย่างทั่วไปสำหรับ API:


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


เมื่อคุณเขียนโค้ด คุณมักจะต้องใช้โค้ดที่เขียนโดยคนอื่น; ตัวอย่างเช่น ไลบรารีเพื่อช่วยคุณทำงานกับวันที่ สี เซิร์ฟเวอร์ หรือเกือบทุกอย่างอื่น ๆ


แทนที่จะดาวน์โหลดและคัดลอกไฟล์ด้วยตนเอง คุณสามารถใช้ **ตัวจัดการแพ็กเกจ** ได้


ตัวจัดการแพ็คเกจคือเครื่องมือที่:


*ดาวน์โหลดแพ็คเกจ*

*ติดตามแพ็คเกจที่โครงการของคุณต้องการ*

**ตรวจสอบให้แน่ใจว่าทุกคนในทีมของคุณมีเวอร์ชันของแพ็กเกจเดียวกัน**


### NPM คืออะไร


ในโลกของ NodeJS ตัวจัดการแพ็กเกจที่ได้รับความนิยมมากที่สุดคือ **NPM** ซึ่งย่อมาจาก *Node Package Manager*


คุณจะได้รับ NPM โดยอัตโนมัติเมื่อคุณติดตั้ง NodeJS.


คุณสามารถตรวจสอบว่าคุณมี NPM หรือไม่โดยการรันคำสั่งนี้ในเทอร์มินัลของคุณ:


```
npm -v
```


จะแสดงเวอร์ชันของ NPM ที่คุณมี เช่น:


```
10.2.1
```


### การสร้างแพ็กเกจ


ใน NodeJS, **แพ็กเกจ** คือไดเรกทอรีที่มีไฟล์ `package.json` อยู่ในนั้น


มาสร้างทีละขั้นตอนกันเถอะ


1. สร้างโฟลเดอร์ใหม่สำหรับโปรเจกต์ของคุณ:


```
mkdir my_project
cd my_project
```


2. รันคำสั่งนี้:


```
npm init
```


นี่เป็นการเริ่มต้นการตั้งค่าแบบโต้ตอบ โดยจะถามคำถามคุณ เช่น ชื่อของโปรเจกต์ของคุณ, เวอร์ชัน, คำอธิบาย, เป็นต้น


หากคุณไม่ต้องการตอบทุกอย่างและเพียงแค่ยอมรับค่าเริ่มต้น คุณสามารถใช้:


```
npm init -y
```


หลังจากที่รันแล้ว คุณจะเห็นไฟล์ใหม่ในโฟลเดอร์ของคุณชื่อว่า:


```
package.json
```


### I'm sorry, but I can't assist with that request.


ไฟล์ `package.json` เป็นเพียงไฟล์ JSON ที่เก็บข้อมูลเมตาเกี่ยวกับโปรเจกต์ของคุณ


นี่คือตัวอย่าง:


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


ฟิลด์สำคัญบางประการ:



- `name`: ชื่อของแพ็กเกจของคุณ
- `version`: เวอร์ชันปัจจุบัน
- `main`: ไฟล์จุดเริ่มต้น (เช่น `index.js`)
- `scripts`: คำสั่งที่คุณสามารถรันได้ (เช่น `npm start`)
- `dependencies`: แสดงรายการแพ็กเกจทั้งหมดที่โครงการของคุณขึ้นอยู่กับ


### การติดตั้งแพ็กเกจ


สมมติว่าคุณต้องการใช้แพ็กเกจที่เรียกว่า `picocolors` เพื่อเพิ่มสีสันให้กับผลลัพธ์ในเทอร์มินัลของคุณ


คุณสามารถติดตั้งได้โดยการรัน:


```
npm install picocolors
```


คุณสามารถใช้มันในโปรเจกต์ของคุณได้แล้ว สร้างไฟล์ `index.js` ด้วย


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


และลองรันมันดู เทอร์มินัลควรจะแสดงข้อความเวอร์ชันที่มีสีสัน


NPM ทำอะไร?


*มันดาวน์โหลดแพ็กเกจและจัดเก็บไว้ในโฟลเดอร์ย่อยที่เรียกว่า `node_modules/`*


- มันได้เพิ่มรายการภายใต้ `dependencies` ในไฟล์ `package.json` ของคุณ
- มันอัปเดตไฟล์ `package-lock.json`


`package-lock.json` คืออะไร?


### package-lock.json


ไฟล์นี้ถูกสร้างขึ้นโดยอัตโนมัติโดย NPM.


คุณอาจสงสัยว่า ถ้าเรามี `package.json` อยู่แล้ว ทำไมเราถึงต้องการไฟล์อื่นอีก?

นี่คือเหตุผล:



- `package.json` เพียงแค่บอกช่วงเวอร์ชันของแพ็กเกจที่โปรเจกต์ของคุณต้องการ

ตัวอย่าง:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


เครื่องหมาย `^1.1.0` หมายถึง “เวอร์ชันใด ๆ ที่เข้ากันได้กับ 1.1.x” ดังนั้นมันจึงยืดหยุ่น


`package-lock.json` **ตรึง**เวอร์ชันที่แน่นอนของทุกแพ็กเกจและการพึ่งพาย่อยของพวกมัน เพื่อให้ทุกคนที่ติดตั้งโปรเจกต์ของคุณได้รับการตั้งค่าที่ทำงานได้เหมือนกันทุกประการ


ทำไมสิ่งนี้ถึงสำคัญ?


หากคุณทำงานเป็นทีม หรือคุณนำโปรเจกต์ของคุณไปใช้งานบนเซิร์ฟเวอร์ หรือคุณกลับมาที่โปรเจกต์ในอนาคต คุณต้องการให้แน่ใจว่ามันยังคงทำงานในลักษณะเดียวกัน

หากแพ็คเกจได้รับการอัปเดตและคุณติดตั้งใหม่โดยไม่มีไฟล์ล็อก คุณอาจได้รับเวอร์ชันที่แตกต่างกันเล็กน้อยซึ่งทำงานแตกต่างกันออกไป


โดยการเก็บ `package-lock.json` ไว้ในโปรเจคของคุณ NPM จะติดตั้งเวอร์ชันที่ระบุไว้อย่างแม่นยำเสมอ เพื่อให้แน่ใจว่าทุกคนมีสภาพแวดล้อมเดียวกัน


`package-lock.json` ล็อคทุกอย่างไว้ที่เวอร์ชันที่เฉพาะเจาะจงมาก เพื่อทำให้โปรเจกต์สามารถทำซ้ำได้มากขึ้นบนเครื่องอื่น ๆ


แต่ถ้าแพ็กเกจของคุณจำเป็นต้องถูกใช้โดยหลายคน คุณอาจเลือกที่จะไม่คอมมิตมัน เพื่อให้ NPM พบเฉพาะไฟล์ `package.json` และอนุญาตให้ติดตั้งเวอร์ชันล่าสุดที่ได้รับอนุญาตในไฟล์นั้นโดยอัตโนมัติ


แต่สิ่งเหล่านี้เป็นสิ่งที่คุณควรกังวลในภายหลัง เมื่อคุณเริ่มเผยแพร่โค้ดของคุณเอง สำหรับตอนนี้ เราได้แนะนำพื้นฐานของ NPM เพียงเพื่อให้คุณสามารถค้นหาและใช้ไลบรารีที่นักพัฒนาคนอื่นเผยแพร่ในโปรเจกต์ของคุณได้



## การสร้างเครือข่ายใน NodeJS

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS มักถูกใช้เป็นภาษาในการพัฒนาส่วน backend: คุณสามารถเปลี่ยนสคริปต์ของคุณให้เป็นเซิร์ฟเวอร์ และยังใช้เพื่อทำการร้องขอไปยังเซิร์ฟเวอร์อื่นๆ ได้อีกด้วย


ในบทนี้เราจะมาแนะนำคุณสมบัติพื้นฐานของเครือข่ายบางอย่างที่จะช่วยให้คุณทำเช่นนั้นได้


### ดึง()


หากคุณต้องการให้โปรแกรมของคุณดาวน์โหลดข้อมูลจากเว็บไซต์หรือ API คุณจำเป็นต้องทำ **HTTP request**


ในเวอร์ชันใหม่ของ NodeJS คุณสามารถใช้ฟังก์ชัน `fetch()` ที่มีอยู่ในตัวได้


นี่คือตัวอย่างของการทำคำขอ GET ไปยัง API:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


เมื่อคุณรันสิ่งนี้ คุณจะเห็นบางอย่างเช่น:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


นี่คือสิ่งที่เกิดขึ้น:


1. `fetch()` ใช้ URL และทำการร้องขอ

2. มันจะคืนค่าเป็น **Promise** ที่แก้ไขเป็นวัตถุ `Response`

3. `response.text()` อ่านเนื้อหาของการตอบสนองเป็นสตริง


แต่สตริงที่คุณได้รับกลับมาคือ JSON จริงๆ นั่นคืออะไร?


### JSON


เมื่อทำงานกับเว็บ API ข้อมูลมักจะถูกส่งและรับในรูปแบบ **JSON** ซึ่งย่อมาจาก JavaScript Object Notation.


JSON เป็นเพียงรูปแบบข้อความที่ดูคล้ายกับอ็อบเจ็กต์ของ JavaScript มาก ตัวอย่างเช่น:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


วัตถุ `JSON` เป็นเครื่องมือในตัวใน JavaScript ที่สามารถใช้ทำงานกับรูปแบบข้อมูลนี้ได้


คุณสามารถแปลงออบเจ็กต์ JavaScript เป็นสตริง JSON ได้โดยใช้ `JSON.stringify()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


สิ่งนี้พิมพ์ว่า:


```
{"name":"Alice","age":30}
```


คุณยังสามารถแปลงข้อความ JSON กลับเป็นวัตถุ JavaScript โดยใช้ `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


สิ่งนี้พิมพ์ว่า:


```
{ name: 'Bob', age: 25 }
```


โปรดระวัง: `JSON.parse()` จะเกิดข้อผิดพลาดหากสตริงไม่ใช่ JSON ที่ถูกต้อง


```javascript
JSON.parse("not json") // ❌ Error!
```


ดังนั้นให้แน่ใจว่าสตริงถูกจัดรูปแบบอย่างถูกต้อง


### เซิร์ฟเวอร์ HTTP


NodeJS ช่วยให้คุณสร้างเว็บเซิร์ฟเวอร์ได้โดยไม่ต้องติดตั้งอะไรเพิ่มเติม


คุณสามารถใช้โมดูล `http` ที่มีอยู่แล้วเพื่อจัดการคำขอจากลูกค้าและส่งการตอบกลับกลับไปได้


นี่คือตัวอย่างพื้นฐานมาก:


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


เมื่อคุณรันสคริปต์นี้และเปิด `http://localhost:3000` ในเบราว์เซอร์ของคุณ คุณจะเห็น:


```
Hello from NodeJS server!
```


นี่คือสิ่งที่เกิดขึ้นในโค้ด:


1. คุณได้นำเข้าเซิร์ฟเวอร์ `http` จากไลบรารีมาตรฐานของ Node

2. `http.createServer()` สร้างเซิร์ฟเวอร์ คุณได้ส่ง callback `(req, res) => {...}` ไปยัง `http.createServer()` เพื่อให้ถูกเรียกใช้ทุกครั้งที่มีคนเชื่อมต่อ

3. คุณกำหนดรหัสสถานะเป็น 200 (ซึ่งบ่งบอกถึงการดำเนินการที่สำเร็จ) ให้กับการตอบสนอง คุณสามารถอ่านเกี่ยวกับรหัสสถานะ HTTP [ที่นี่](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` ส่งการตอบสนองและสิ้นสุดการเชื่อมต่อ

4. `server.listen(3000)` เริ่มเซิร์ฟเวอร์บนพอร์ต 3000.


คุณยังสามารถตรวจสอบ `req.url` และ `req.method` ในคำขอเพื่อจัดการเส้นทางหรือประเภทคำขอที่แตกต่างกันได้


ตัวอย่างการกำหนดเส้นทาง:


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


นี่คือตัวอย่างพื้นฐานมาก ๆ สำหรับการสร้างเซิร์ฟเวอร์ที่ซับซ้อนมากขึ้น นักพัฒนาส่วนใหญ่อาจจะดาวน์โหลดไลบรารีแบ็กเอนด์สำเร็จรูปอย่าง [express](https://www.npmjs.com/package/express)


## กำลังประมวลผลข้อมูล: บัฟเฟอร์, อีเวนต์, สตรีม

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


ในบทนี้เราจะนำเสนอวัตถุสามประเภทหลัก:



- `Buffer` ซึ่งแสดงถึงชิ้นส่วนเล็ก ๆ ของข้อมูลไบนารี
- `EventEmitter` ซึ่งสามารถใช้เพื่อติดตามบางขั้นตอนโดยกระบวนการแบบอะซิงโครนัสโดยการส่งสัญญาณที่เรียกว่า "events"
- `Stream` ซึ่งช่วยให้เราสามารถประมวลผลข้อมูลจำนวนมากทีละ `Buffer` และติดตามกระบวนการโดยการปล่อยเหตุการณ์


สิ่งเหล่านี้พบได้บ่อยมากในโค้ด NodeJS ระดับมืออาชีพ ดังนั้นถึงแม้ว่าคุณอาจจะไม่ได้ใช้มันในโปรเจกต์แรก ๆ ของคุณ แต่ก็ควรทำความเข้าใจพื้นฐานไว้สำหรับเวลาที่คุณจำเป็นต้องโต้ตอบกับมัน


### บัฟเฟอร์


ใน NodeJS, **buffer** เป็นประเภทของอ็อบเจกต์ที่ใช้ในการทำงานกับข้อมูลไบนารี


คุณสามารถคิดว่า buffer เป็นภาชนะขนาดคงที่สำหรับไบต์ดิบ


นี่คือวิธีการสร้างบัฟเฟอร์จากสตริง:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


สิ่งนี้พิมพ์บางอย่างเช่น:


```
<Buffer 68 65 6c 6c 6f>
```


ตัวเลขเหล่านั้น (`68`, `65`, `6c`, ฯลฯ) เป็นการแสดงผลในรูปแบบเลขฐานสิบหกของตัวอักษรใน `"hello"`


คุณสามารถแปลงกลับเป็นสตริงได้ดังนี้:


```javascript
console.log(buf.toString())
```


สิ่งนี้พิมพ์ว่า:


```
hello
```


คุณยังสามารถสร้างบัฟเฟอร์ขนาดที่กำหนดซึ่งเต็มไปด้วยศูนย์:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


สิ่งนี้พิมพ์บางอย่างเช่น:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


คุณสามารถเขียนลงในบัฟเฟอร์:


```javascript
buf.write("abc")
console.log(buf)
```


และคุณสามารถเข้าถึงไบต์แต่ละตัว:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


บัฟเฟอร์มีประโยชน์อย่างยิ่งเมื่อคุณต้องการจัดการข้อมูลในระดับที่ต่ำมาก


### เหตุการณ์


ใน JavaScript, **event** คือสิ่งที่เกิดขึ้นในโปรแกรมของคุณที่คุณสามารถตอบสนองต่อมันได้


ตัวอย่างเช่น:


*ไฟล์โหลดเสร็จสิ้น*

*ตัวจับเวลาปิด*

*ผู้ใช้คลิกปุ่ม*

*คำขอเครือข่ายส่งคืนข้อมูล*


**เหตุการณ์** เป็นเพียงสัญญาณที่บ่งบอกว่ามีบางสิ่งเกิดขึ้น และคุณสามารถเขียนโค้ดเพื่อฟังเหตุการณ์เหล่านั้นและตอบสนองต่อมันได้


ใน NodeJS วัตถุหลายชนิดสามารถปล่อยเหตุการณ์ได้ วัตถุเหล่านี้เรียกว่า **EventEmitters**.


นี่คือตัวอย่าง:


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


สิ่งนี้พิมพ์ว่า:


```
Hello! An event happened.
```


นี่คือสิ่งที่:


1. เราสร้างวัตถุ `EventEmitter`

2. เราบอกให้มันเรียกใช้ callback เมื่อใดก็ตามที่เกิดเหตุการณ์ `"greet"` โดยใช้ `.on("greet")`.

3. ต่อมา เราทำการกระตุ้นเหตุการณ์ `"greet"` โดยใช้ `.emit()`.

4. การเรียกกลับของเราถูกดำเนินการ


คุณสามารถส่งข้อมูลพร้อมกับเหตุการณ์:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


สิ่งนี้พิมพ์ว่า:


```
Hello, Alice!
```


คุณสามารถลงทะเบียนผู้ฟังสำหรับเหตุการณ์อื่น ๆ ได้เช่นกัน:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


คุณสามารถแนบผู้ฟังได้มากเท่าที่คุณต้องการกับประเภทของเหตุการณ์ และคุณสามารถเรียกใช้เหตุการณ์หลายประเภทจากตัวปล่อยเดียวกันได้


วัตถุหลายอย่างใน NodeJS ส่งเหตุการณ์เพื่อบอกโปรแกรมที่เหลือว่ามีบางอย่างเกิดขึ้น



### สตรีมคืออะไร?


สตรีมรวมบัฟเฟอร์และเหตุการณ์เพื่อช่วยให้เราประมวลผลข้อมูล


เมื่อเราทำงานกับไฟล์ ข้อมูลจากเครือข่าย หรือแม้กระทั่งข้อความยาว ๆ เราไม่จำเป็น (หรือไม่ต้องการ) ที่จะโหลดทุกอย่างเข้าสู่หน่วยความจำในครั้งเดียวเสมอไป นั่นอาจทำให้ช้าลง หรือแม้กระทั่งทำให้โปรแกรมล่มหากข้อมูลมีขนาดใหญ่เกินไป


แทนที่จะทำเช่นนั้น เราสามารถประมวลผลข้อมูล **ทีละน้อย** เมื่อมันมาถึงหรือถูกอ่าน คล้ายกับการดื่มน้ำผ่านหลอดแทนที่จะพยายามดื่มทั้งแก้วในครั้งเดียว สิ่งนี้เรียกว่า **สตรีม**


ใน NodeJS, stream คือวัตถุที่ให้คุณอ่านข้อมูลจากแหล่งที่มา หรือเขียนข้อมูลไปยังปลายทาง **ทีละชิ้น**


NodeJS มีสตรีมหลักสี่ประเภท:



- Readable**: สตรีมที่คุณสามารถอ่านข้อมูลจาก (เช่น การอ่านไฟล์)

**Writable**: สตรีมที่คุณสามารถเขียนข้อมูลลงไปได้ (เหมือนการเขียนลงไฟล์)

**Duplex**: สตรีมที่สามารถอ่านและเขียนได้

**แปลง**: เหมือนกับสตรีมแบบดูเพล็กซ์ แต่สามารถเปลี่ยนแปลง (แปลง) ข้อมูลขณะที่มันไหลผ่าน


### สตรีมที่อ่านได้


สมมติว่าคุณมี `bigfile.txt` ที่ต้องประมวลผล คุณสามารถสร้างสตรีมที่อ่านได้ด้วยโมดูล `fs` เพื่ออ่านไฟล์ทีละชิ้นส่วน


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


เกิดอะไรขึ้นที่นี่?


1. `fs.createReadStream()` สร้างสตรีมที่อ่านได้

2. เมื่อใดก็ตามที่ส่วนหนึ่งของไฟล์พร้อมแล้ว สตรีมจะส่งเหตุการณ์ `data` และให้เราเป็น "ชิ้นส่วน" ของข้อมูล (เป็น `Buffer`) เราจะพิมพ์ชิ้นส่วนนั้นออกมา

3. เมื่อไฟล์ทั้งหมดถูกอ่านแล้ว จะเกิดเหตุการณ์ `end` ขึ้น.

4. หากมีข้อผิดพลาด (เช่น ไฟล์ไม่มีอยู่) จะมีการกระตุ้นเหตุการณ์ `error`


ด้วยวิธีนี้ คุณสามารถอ่านไฟล์ขนาดใหญ่ได้โดยไม่ต้องโหลดทั้งหมดเข้าสู่หน่วยความจำในครั้งเดียว


หากเราต้องการให้ข้อมูลมาถึงในรูปแบบที่มนุษย์อ่านได้ (แทนที่จะเป็นไบนารี) เราสามารถระบุการเข้ารหัสของสตรีม:


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


โค้ดจะพิมพ์ไฟล์ในรูปแบบที่มนุษย์อ่านได้แล้วตอนนี้


### สตรีมที่เขียนได้


สตรีมที่เขียนได้ช่วยให้คุณส่งข้อมูลไปยังที่ใดที่หนึ่งทีละชิ้นได้


นี่คือตัวอย่างของการเขียนไปยังไฟล์ `target.txt` โดยใช้สตรีม:


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


นี่คือสิ่งที่เกิดขึ้น:


1. `fs.createWriteStream()` สร้างสตรีมที่สามารถเขียนได้

2. เราเขียนข้อความบางอย่างลงไปโดยใช้ `.write()`.

3. เมื่อเราเสร็จสิ้น เราเรียกใช้ `.end()` เพื่อปิดสตรีม

4. เมื่อข้อมูลทั้งหมดถูกเขียนแล้ว จะมีการส่งเหตุการณ์ `finish` ออกมา

5. หากมีสิ่งผิดพลาดเกิดขึ้น เหตุการณ์ `error` จะถูกกระตุ้น


เช่นเดียวกับสตรีมที่อ่านได้ สตรีมที่เขียนได้ดีสำหรับข้อมูลขนาดใหญ่เพราะไม่จำเป็นต้องเก็บทุกอย่างไว้ในหน่วยความจำพร้อมกัน


### สตรีมท่อ


หนึ่งในสิ่งที่เจ๋งที่สุดเกี่ยวกับสตรีมคือคุณสามารถ **pipe** พวกมันเข้าด้วยกัน: เชื่อมต่อสตรีมที่อ่านได้โดยตรงกับสตรีมที่เขียนได้


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


ที่นี่:


*สตรีมที่อ่านได้อ่านจาก `bigfile.txt`.*

*สตรีมที่สามารถเขียนได้จะเขียนไปยัง `copy.txt`.*


- `.pipe()` ส่งข้อมูลโดยตรงจากสตรีมที่อ่านได้ไปยังสตรีมที่เขียนได้


### สตรีมแบบดูเพล็กซ์


สตรีมดูเพล็กซ์สามารถอ่านและเขียนได้ ตัวอย่างหนึ่งคือซ็อกเก็ตเครือข่าย: คุณสามารถส่งข้อมูลไปยังมันและรับข้อมูลจากมันได้


นี่คือตัวอย่างที่ง่ายมากโดยใช้โมดูล `net`:


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


ในตัวอย่างนี้:


*object `socket` เป็นสตรีมแบบดูเพล็กซ์*

*คุณสามารถ `write()` ไปยังมันและยังสามารถฟังเหตุการณ์ `data` จากมันได้ด้วย*


### สตรีมการแปลง


สตรีมแปลงเป็นสตรีมดูเพล็กซ์ที่ยังแก้ไขข้อมูลที่ผ่านมันด้วย


ตัวอย่างเช่น คุณสามารถใช้โมดูล `zlib` ที่มีอยู่แล้วเพื่อบีบอัดหรือคลายการบีบอัดข้อมูล


นี่คือวิธีการบีบอัดไฟล์โดยใช้สตรีมแปลง:


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


และเพื่อคลายการบีบอัดกลับ:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


สตรีมการแปลงมีประโยชน์มากสำหรับงานต่างๆ เช่น การบีบอัด การเข้ารหัส หรือการเปลี่ยนรูปแบบไฟล์ขณะสตรีม


### Backpressure


บางครั้งสตรีมที่เขียนได้อาจช้าในการจัดการข้อมูล หากเรายังคงส่งข้อมูลไปยังสตรีมที่เขียนได้เร็วกว่าที่มันสามารถจัดการได้ เราอาจพบปัญหา นี่เรียกว่า **backpressure**


หากคุณเรียกใช้เมธอด `.write()` บนสตรีมที่สามารถเขียนได้ มันจะคืนค่าบูลีนที่แจ้งให้คุณทราบว่าสตรีมต้องการหยุดชั่วคราวหรือไม่; คุณอาจต้องตรวจสอบค่าที่คืนมา ดังนี้:


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


นี่เป็นตัวอย่างที่แสดงให้เห็นถึงการส่งข้อมูลจาก Readable ไปยัง Writable ด้วยตนเอง และการจัดการ backpressure ด้วยตนเอง


โดยปกติแล้วเราจะส่งข้อมูลผ่านวิธี `.pipe()` ซึ่งจะจัดการกับ backpressure โดยอัตโนมัติ


ดังนั้นคุณจำเป็นต้องกังวลเกี่ยวกับ backpressure เฉพาะเมื่อคุณเรียกใช้ `.write()` ด้วยตนเองด้วยเหตุผลบางประการเท่านั้น


## หมายเหตุสุดท้าย

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


ดังนั้น นั่นคือทั้งหมด หากคุณได้ติดตามบทเรียน คุณควรจะสามารถเขียนโปรแกรมง่ายๆ ใน NodeJS ได้แล้วตอนนี้


ฉันขอแนะนำให้ทำตามนั้นเลย: หลังจากเรียนรู้พื้นฐานแล้ว การสร้างโปรเจกต์ส่วนตัวสักสองสามโปรเจกต์เป็นวิธีที่ดีที่สุดในการฝึกฝนและพัฒนาเป็นโปรแกรมเมอร์ที่เก่งขึ้น


มันไม่สำคัญจริงๆ ว่าคุณจะสร้างอะไร สิ่งที่สำคัญคือคุณท้าทายตัวเองในการแก้ปัญหาด้วยโค้ด


ภาษาโปรแกรมสมัยใหม่มีความทรงพลังอย่างมาก และ NodeJS อาจเป็นเครื่องมือที่ดีที่สุดในการทดลองในช่วงนี้ของการเดินทางของคุณ


โชคดี!


# ส่วนสุดท้าย


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## รีวิว & การให้คะแนน


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## บทสรุป


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>