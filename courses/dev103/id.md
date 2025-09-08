---
name: Dasar-dasar JavaScript dan NodeJS
goal: Pelajari dasar-dasar pemrograman JavaScript dan pengembangan NodeJS untuk membangun aplikasi dan alat praktis.
objectives: 

  - Menguasai sintaksis, jenis, dan aliran kontrol JavaScript dasar
  - Memahami fungsi, objek, dan kelas dalam JavaScript
  - Pelajari teknik penanganan kesalahan dan debugging
  - Berkenalan dengan NodeJS dan ekosistemnya

---

# Mulai perjalanan pengembangan Anda


Selamat datang di kursus JavaScript dan NodeJS ini.


JavaScript adalah bahasa pemrograman yang paling populer di dunia: JavaScript adalah bahasa skrip untuk peramban modern, jadi pada dasarnya tidak mungkin untuk membangun aplikasi web modern tanpa menulis *beberapa* JavaScript; dan dengan runtime NodeJS, JavaScript juga dapat digunakan di luar peramban, untuk membuat skrip dan aplikasi yang berjalan langsung di komputer Anda.


Kursus ini dirancang untuk orang-orang yang benar-benar baru dalam pemrograman, atau yang telah menggunakan bahasa lain sebelumnya tetapi ingin memahami cara kerja JavaScript, terutama dalam konteks NodeJS.


Pada akhir kursus, Anda harus dapat menulis program Anda sendiri dalam JavaScript, menggunakan perpustakaan standar NodeJS, dan menginstal serta menggunakan paket pihak ketiga untuk membangun alat yang berguna.


+++
# JavaScript Dasar

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Pengaturan

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>


Pada bagian ini kita akan menyiapkan mesin kita untuk menulis dan menjalankan program JavaScript pertama kita.


Program JavaScript hanyalah sebuah kumpulan (satu atau lebih) file teks, yang berisi perintah yang akan dieksekusi oleh runtime JavaScript.


Nama file teks ini biasanya diakhiri dengan ekstensi file `.js`, seperti `my_script.js`, `my_program.js`, dan sebagainya.


Perintah yang dikandungnya ditulis dalam bahasa pemrograman JavaScript.


Runtime JavaScript adalah program khusus yang mengeksekusi file-file ini.


![](assets/en/1.webp)


### Instalasi NodeJS


Runtime JavaScript yang paling umum adalah NodeJS.


Anda dapat menginstalnya dengan mengikuti [petunjuk resmi](https://nodejs.org/en/download).


Halaman unduhan akan memberi Anda petunjuk untuk ketiga OS (Sistem Operasi) utama: Windows, Linux dan MacOS. Ini mengasumsikan Anda tahu cara membuka terminal di OS Anda.


Karena NodeJS tersedia untuk ketiga OS, program yang Anda tulis akan dapat dieksekusi di semua OS (kecuali beberapa kasus khusus).


Ini berarti Anda bisa, misalnya, menulis videogame sederhana dalam JavaScript di PC Windows dan memberikannya kepada teman Anda untuk menjalankannya di Mac-nya.


![](assets/en/2.webp)


### Pengeditan teks


Salah satu hal yang menarik dari pemrograman adalah Anda bisa menulis kode menggunakan editor teks apa pun, bahkan notepad bawaan OS Anda.


Ada beberapa editor teks yang dikhususkan untuk menulis kode, ada yang tersedia secara gratis, ada juga yang mengharuskan Anda membayar lisensi.


Pilihan editor kode adalah lubang kelinci raksasa yang melampaui ruang lingkup kursus ini, jadi kita tidak akan membicarakannya di sini. Jika Anda tidak tahu apa yang harus digunakan, editor gratis yang paling sering digunakan adalah [VSCode] (https://code.visualstudio.com/).


Interface sedikit membengkak, tetapi memiliki apa yang Anda butuhkan: editor berkas, penjelajah berkas (untuk memvisualisasikan berkas dan subdirektori dalam direktori yang Anda kerjakan), dan terminal untuk menjalankan kode Anda. Ia juga mendukung banyak plugin, dan dilengkapi dengan penyorotan sintaksis JavaScript secara default.


Jika Anda ingin sedikit lebih Cypherpunk-y, Anda dapat menggunakan [VSCodium] (https://vscodium.com/) sebagai gantinya.


### Program pertama (halo dunia)


Biasanya, ketika mempelajari bahasa pemrograman, program pertama yang ditulis seseorang adalah mencetak "halo dunia!" ke konsol.


Buat direktori bernama `my_js_code/`, dengan di dalamnya terdapat file bernama `main.js` (nama ini dapat diubah-ubah).


Buka direktori dengan VSCode.


Tulis kode ini ke dalam file Anda:


```javascript
console.log("hello world!")
```


Buka terminal dan jalankan perintah ini untuk menjalankan program:


```
node main.js
```


Hasilnya seharusnya adalah


```
hello world!
```


### Apa yang Terjadi


Dalam JavaScript, segala sesuatu adalah "objek".


`console` adalah sebuah objek, yang digunakan untuk men-debug program.


`console.log` adalah metode yang paling sering digunakan dari `console`. Metode ini hanya mencetak argumen apa pun yang Anda berikan kepadanya.


Anda memberikan argumen ke `console.log` menggunakan tanda kurung bulat `()`.


Jadi, misalnya, jika Anda ingin mencetak angka `1000`, Anda cukup menulis


```javascript
console.log(1000)
```


Kemudian jalankan dengan menjalankan


```
node main.js
```


di terminal Anda (mulai sekarang, kursus ini akan mengasumsikan bahwa Anda tahu bagaimana cara Anda mengeksekusi program).


Ini akan mencetak


```
1000
```


Anda dapat meneruskan beberapa hal, seperti


```javascript
console.log(16, 8, 1993)
```


Ini akan mencetak


```
16 8 1993
```


## Variabel dan komentar

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Program biasanya menjalankan operasi pada data.


Variabel seperti kotak bernama yang kita gunakan untuk menyimpan data. Variabel memungkinkan kita untuk mengaitkan sebuah data dengan nama tertentu, sehingga kita dapat mengambilnya nanti dengan menggunakan nama tersebut.


### deklarasi `biarkan`


Untuk mendeklarasikan sebuah variabel dalam JavaScript, kita dapat menggunakan kata kunci `let`.


Setelah menulis `let`, kita menulis nama yang ingin kita berikan pada variabel tersebut, lalu tanda `=`, dan kemudian nilai yang ingin kita simpan.


Sebagai contoh:


```javascript
let age = 25

console.log(age)
```


Nama variabel (secara teknis disebut "pengenal") biasanya dapat terdiri dari huruf, garis bawah (`_`), tanda dolar (`$`), dan angka, meskipun karakter pertama tidak boleh berupa angka.


Pada kode di atas, kita mendeklarasikan sebuah variabel bernama `umur` dan menyimpan nilai `25` di dalamnya.


Kemudian, kami mencetak nilai tersebut menggunakan `console.log(age)`.


Jika Anda menjalankan kode ini dengan `node main.js`, hasilnya adalah:


```
25
```


Pengenal peka terhadap huruf besar-kecil, yang berarti huruf kecil dan huruf besar dihitung sebagai perbedaan dalam pengenal, jadi misalnya


```javascript
let age = 25

let Age = 20

console.log(age)
```


akan mencetak 25, karena keduanya dianggap sebagai dua variabel yang benar-benar terpisah!


Anda juga dapat menyimpan string (teks) dalam sebuah variabel:


```javascript
let message = "hello again"

console.log(message)
```


Ini akan dicetak:


```
hello again
```


Sama seperti sebelumnya, kita menggunakan `console.log()` untuk mencetak nilai yang tersimpan di dalam variabel.


Sekarang mari kita lakukan keduanya bersama-sama:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


Menjalankan ini akan mencetak:


```
25
hello again
```

### Penugasan kembali


Variabel yang dideklarasikan dengan `let` dapat diubah setelah dibuat.


Ini disebut penugasan ulang.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Pertama, kita tetapkan `10` ke `skor`, kemudian mencetaknya.


Kemudian kita ubah nilai `skor` menjadi `15` dan mencetaknya lagi.


Keluarannya adalah:


```
10
15
```


Hal ini sangat berguna ketika nilai berubah seiring waktu, seperti dalam permainan di mana skor meningkat.


Mari kita tambahkan variabel lain ke dalam campuran:


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


Ini akan dicetak:


```
10
Alice
20
Bob
```


Seperti yang Anda lihat, baik `skor` maupun `pemain` telah diubah.


### deklarasi `const` deklarasi


Sering kali, kita tidak ingin sebuah variabel berubah setelah dibuat. Untuk itu, kita menggunakan `const`.


`const` adalah kependekan dari "konstan". Setelah Anda menetapkan nilai ke variabel `const`, Anda tidak dapat mengubahnya.


```javascript
const pi = 3.14
console.log(pi)
```


Cetakan ini:


```
3.14
```


Tetapi jika Anda mencoba melakukan ini:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript akan memberikan Anda kesalahan seperti:


```
TypeError: Assignment to constant variable.
```


Hal ini karena `pi` dideklarasikan dengan menggunakan `const`, dan Anda tidak dapat mengubah nilainya setelah itu. Anda menyampaikan kepada penerjemah JavaScript bahwa Anda tidak ingin variabel tersebut berubah.


Hal ini berguna karena mengurangi kemungkinan mengubahnya secara tidak sengaja. Ketika program menjadi sangat besar, dengan ribuan baris kode, tidak mungkin untuk mengikuti semua yang terjadi sekaligus (itulah alasan utama kita menggunakan komputer, untuk menjalankan proses kompleks yang tidak dapat kita hitung dengan otak kita), sehingga menjadi berguna untuk memiliki batasan seperti ini, yang membuat program lebih deterministik.


Praktik terbaik adalah selalu mendeklarasikan nilai kita sebagai `const`, kecuali jika kita yakin ingin memodifikasinya nanti.


### Komentar dalam JavaScript


Terkadang kita ingin menulis catatan dalam kode kita yang tidak dieksekusi. Ini disebut komentar.


Komentar diabaikan oleh program saat dijalankan, tetapi berguna untuk menjelaskan sesuatu kepada diri kita sendiri atau orang lain.


Untuk menulis komentar satu baris, gunakan `//`


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


Ini masih akan tetap mencetak:


```
10
```


Komentar-komentar tersebut hanya ada untuk dibaca oleh manusia.


Anda juga dapat menulis komentar multi-baris menggunakan `/*` dan `*/`


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


Ini akan mencetak


```
20
```


Dan komentar tersebut akan diabaikan.


Anda dapat menggunakan komentar untuk menambahkan anotasi kecil pada kode Anda, sehingga Anda dapat mengingat apa yang dilakukannya dan mengapa kode tersebut ditulis dengan cara tertentu. Hal ini juga dapat membantu programmer lain untuk memahaminya.


## Jenis dasar: angka, string, boolean

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


Dalam JavaScript, sebuah "tipe" memberi tahu Anda jenis data apa yang dimiliki oleh sebuah nilai.


Javascript memiliki beberapa tipe dasar, dan pada bagian ini kita akan mempelajari beberapa di antaranya.


### Operasi angka dan aritmatika


Jenis pertama yang akan kami perkenalkan adalah `angka`.


Angka dalam JavaScript dapat berupa bilangan bulat (seperti `5`) atau desimal (seperti `3.14`).


Anda dapat melakukan aritmatika dengan mereka: penjumlahan, pengurangan, perkalian, dan pembagian.


Berikut ini contoh dasarnya:


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


Ini akan dicetak:


```
15
5
50
2
```


Anda juga dapat menggunakan tanda kurung `()` untuk mengontrol urutan operasi:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Cetakan ini:


```
20
```


Tanpa tanda kurung, maka akan menjadi `2 + 3 * 4`, yaitu:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


Itu akan dicetak:


```
14
```


Karena dalam matematika biasa, perkalian terjadi sebelum penjumlahan.


### String dan interpolasi


Tipe JavaScript kedua yang akan kita perkenalkan adalah `string`.


String adalah potongan-potongan teks. Anda dapat menggunakan tanda kutip tunggal `'...'` atau tanda kutip ganda `"..."` untuk membuatnya.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Cetakan ini:


```
hello
Bob
```


Untuk menggabungkan string, Anda dapat menggunakan operator `+`:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Ini akan dicetak:


```
hello Bob
```


Tetapi ada cara yang lebih baik untuk menggabungkan string yang disebut **interpolasi string**. Anda menggunakan tanda kutip untuk mendeklarasikan string `` `...` `` dan menulis variabel menggunakan `${...}` di dalam string:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


Ini juga mencetak:


```
hello Bob
```


Anda dapat menyertakan ekspresi apa pun di dalam `${...}`:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Cetakan ini:


```
Next year, I will be 31 years old.
```


Interpolasi sangat umum dalam JavaScript modern.


### Boolean, perbandingan, dan operasi logika


Jenis ketiga yang akan kami perkenalkan adalah `boolean`. Dinamakan sesuai dengan nama matematikawan George Boole, yang menemukan logika boolean.


Boolean sangat sederhana: hanya ada dua nilai yang mungkin, yaitu `benar` dan `salah`.


Anda dapat menyimpannya dalam variabel:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Cetakan ini:


```
true
false
```


Anda dapat menggabungkan boolean menggunakan operator logika:



- `&&` berarti "dan", dan akan mengembalikan `true` hanya jika **kedua** nilainya `true`, jika tidak maka akan mengembalikan `false`
- `||` berarti "atau", dan akan mengembalikan `true` jika **setidaknya salah satu** dari nilainya adalah `true`, jika tidak (jika keduanya salah) maka akan mengembalikan `false`
- `!` berarti "tidak", diterapkan sebelum boolean, dan akan membaliknya: jika boolean tersebut bernilai `true` maka akan mengembalikan `false`, dan sebaliknya.


![](assets/en/3.webp)


Contoh:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


Anda dapat membandingkan nilai dalam JavaScript menggunakan operator seperti `>`, `<`, `===`, dan `!==`. Hasil perbandingan ini selalu berupa boolean.


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


Javascript juga memiliki `>=` yang berarti "lebih besar atau sama" dan `<=` yang berarti "lebih kecil atau sama".


Boolean, perbandingan, dan operator logika sering digabungkan dalam program untuk menyatakan kondisi yang rumit, seperti untuk memastikan "email telah sampai DAN berisi gambar yang saya butuhkan ATAU panjang email lebih panjang dari 10.000 karakter". Anda akan menemukan bahwa ini adalah blok bangunan yang penting untuk membangun logika program.


## Array, null, tidak terdefinisi

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


Pada bagian ini, kita akan membahas tiga jenis lagi yang sangat umum dalam program JavaScript:



- Larik**: urutan nilai
- undefined**: nilai khusus yang berarti "tidak ada yang ditetapkan"
- null**: nilai khusus lain yang berarti "sengaja dikosongkan"


### Akses array dan indeks


Sebuah **array** adalah sebuah tipe yang dapat menampung beberapa nilai dalam sebuah daftar.


Anda membuat larik dengan menggunakan tanda kurung siku `[]` dan memisahkan item dengan koma.


Berikut ini contoh dasarnya:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Cetakan ini:


```
[ 10, 2, 88 ]
```


Anda dapat menyimpan apa pun dalam larik, bukan hanya angka:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Cetakan ini:


```
[ 'apple', 42, true ]
```


Untuk mengakses item tertentu dalam larik, kita menggunakan **indeks**. Indeks adalah posisi item, dimulai dari **0**.


Jadi, dalam larik ini:


```javascript
const colors = ["red", "green", "blue"]
```



- `warna[0]` adalah `"merah"`
- `warna[1]` adalah `"Green"`
- `warna[2]` adalah `"biru"`


Mari kita coba:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Ini akan dicetak:


```
red
green
blue
```


Anda dapat menetapkan nilai ke indeks tertentu dari larik


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Ini akan dicetak:


```
[ 'red', 'yellow', 'blue' ]
```


Anda dapat menggunakan bilangan asli apa pun sebagai indeks, bahkan yang disimpan dalam sebuah variabel


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Ini akan dicetak:


```
green
```


Tetapi jika Anda mencoba mengakses indeks yang tidak ada, Anda akan mendapatkan `undefined`:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Cetakan ini:


```
undefined
```


Apa itu??


### `tidak terdefinisi`


Nilai khusus `undefined` berarti "tidak ada nilai yang ditetapkan".


Jika Anda membuat variabel namun tidak memberikan nilai, variabel tersebut akan menjadi `undefined`:


```javascript
const name
console.log(name)
```


Cetakan ini:


```
undefined
```


Karena kita tidak menetapkan apa pun pada `nama`, JavaScript menetapkannya ke `undefined` secara default.


Seperti yang terlihat sebelumnya, Anda juga bisa mendapatkan `undefined` ketika Anda mengakses indeks array yang tidak ada:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Cetakan ini:


```
undefined
```


### `null` dan cara mengatasinya


`null` juga merupakan nilai khusus. Ini berarti "tidak ada apa pun di sini, dan saya sengaja melakukannya."


Tidak seperti `undefined`, yang otomatis, `null` adalah sesuatu yang Anda tentukan sendiri.


Sebagai contoh:


```javascript
const currentUser = null
console.log(currentUser)
```


Cetakan ini:


```
null
```


Mengapa menggunakan `null`? Mungkin Anda mengharapkan sebuah nilai nanti, tetapi nilai tersebut belum siap:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Cetakan ini:


```
Alice
```


Jadi `null` berguna ketika Anda ingin mengatakan, misalnya, "Seharusnya ada sesuatu di sini nanti, tapi sekarang kosong."


## Blok dan aliran kontrol

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Sejauh ini, kita kebanyakan menulis baris kode yang berjalan satu demi satu.


Tetapi ketika kita membuat kode, kita dapat mengontrol urutan eksekusi kode tersebut.


Ini disebut **aliran kontrol**.


Mari kita mulai dengan memahami blok dan cakupan.


### Lingkup global


Setiap variabel yang kita deklarasikan ada dalam sebuah **scope**, yang berarti wilayah kode di mana variabel tersebut diketahui.


Jika Anda mendeklarasikan variabel di luar blok mana pun, variabel tersebut ada di dalam **cakupan global**.


```javascript
const color = "blue"
console.log(color)
```


Variabel `color` ini berada dalam lingkup global, sehingga dapat diakses dari mana saja di dalam file.


Jika Anda menambahkan lebih banyak baris:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


Baik `warna` dan `ukuran` adalah variabel global. Variabel-variabel ini tersedia di semua tempat di dalam file.


Namun, apa yang terjadi di dalam blok?


### Blok dan ruang lingkup lokal


Sebuah **blok** adalah sebuah potongan kode yang dikelilingi oleh kurung kurawal `{}`.


Variabel yang dideklarasikan dengan `let` atau `const` di dalam sebuah blok hanya ada di dalam blok tersebut.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Cetakan ini:


```
inside block
```


Tetapi jika Anda mencoba ini:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript akan memberikan Anda kesalahan seperti:


```
ReferenceError: message is not defined
```


Hal ini dikarenakan `pesan` dideklarasikan di dalam blok dan tidak ada di luar blok.


Ini berarti kita dapat menggunakan blok untuk mengisolasi bagian dari kode kita, dan memastikan bahwa "apa yang terjadi di dalam blok tetap berada di dalam blok" (seperti Las Vegas).


Mengatur kode kita dalam blok-blok memungkinkan kita juga untuk menyusun eksekusi program, dengan konstruksi aliran kontrol seperti `if`


### `jika`, `lain`


Terkadang kita ingin menjalankan kode **hanya jika** sesuatu yang benar. Untuk itulah pernyataan `if` digunakan.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Cetakan ini:


```
Am I an adult?
Yes I am!
```


Seperti yang Anda lihat, lihat kode yang membandingkan `myAge` dan `18`.

Dalam kasus ini operator `>=` mengembalikan `true`, sehingga blok akan dieksekusi.

Jika kondisinya tidak `true`, blok tidak akan dieksekusi.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Cetakan ini:


```
Am I an adult?
```


Anda dapat menambahkan blok `lain` untuk menangani kasus sebaliknya:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Cetakan ini:


```
Am I an adult?
No, I am not.
```


Baik blok `if` dan `else` masih berupa blok - jadi variabel yang dideklarasikan di dalamnya tidak ada di luar.


Jika kita ingin memastikan bahwa sesuatu itu **tidak** benar, apa yang bisa kita lakukan?


Seperti yang telah dibahas sebelumnya, JavaScript memiliki operator "not", yang membalik boolean. Jadi kita dapat melakukan


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

Ini masih mencetak:


```
Am I an adult?
No, I am not.
```

Karena kita menggunakan operator `!` untuk membalikkan variabel `dewasa`.


`if (!dewasa) {...}` harus dibaca sebagai "jika tidak dewasa..."


Dengan menggunakan blok, logika, dan operator pembanding, kita dapat menyusun eksekusi program, dengan mendefinisikan variabel yang harus bernilai 'benar' (atau 'salah') agar sesuatu dapat terjadi.


### `sementara`, `pecah`, `lanjutkan`


Perulangan `sementara` mengulang kode *selama* suatu kondisi bernilai benar.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Cetakan ini:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Ketika `count` menjadi 3, perulangan berhenti.


Anda dapat menghentikan perulangan lebih awal dengan menggunakan `break`:


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


Cetakan ini:


```
0
1
2
```


Karena ketika angka menjadi `3`, blok `if` akan dieksekusi dan menghentikan perulangan.


Anda dapat melewatkan sisa perulangan dengan menggunakan `continue`:


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


Cetakan ini:


```
1
2
4
5
```


Karena ketika angkanya adalah `3`, `terus` membuat program melewatkan baris yang mencetak angka tersebut.


### 'untuk... dari...'


Jika Anda memiliki sebuah larik, dan ingin melakukan sesuatu pada setiap item di dalamnya, Anda dapat menggunakan `untuk ... dari ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Cetakan ini:


```
apple
banana
cherry
```

Blok akan dieksekusi satu kali untuk setiap elemen larik.


`buah` di sini adalah variabel baru yang mengambil nilai dari setiap item dalam larik, untuk dioperasikan di dalam blok.


### 'untuk ... dalam ...'


Anda dapat menggunakan `for ... in` untuk mengulang kunci (indeks) dari sebuah larik:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Cetakan ini:


```
0
1
2
```


Anda juga dapat menggunakan indeks untuk mendapatkan nilainya:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Ini mencetak sama dengan `untuk ... dari`:


```
apple
banana
cherry
```


Dalam praktiknya, untuk array, Anda sebaiknya menggunakan `untuk ... dari`, karena lebih sederhana dan bersih.


### Loop terikat


Terkadang kita ingin mengulang beberapa kali, atau secara umum menulis sepotong kode yang mengulang sebuah blok sambil melacak sesuatu.

Itulah gunanya perulangan `untuk` yang dibatasi.

Perulangan berbatas biasanya membutuhkan tiga kondisi, dipisahkan dengan tanda titik koma `;`, seperti pada `(... ; ... ; ....)`.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Cetakan ini:


```
0
1
2
```


Mari kita jelaskan:



- `let i = 0`: mendeklarasikan sebuah variabel yang akan digunakan dalam blok (dalam hal ini adalah penghitung yang dimulai dari 0)
- `i < 3`: menyatakan sebuah kondisi menjadi `true` agar blok dapat dieksekusi (dalam kasus ini adalah "ulangi selama `i` kurang dari 3")
- `i = i + 1`: mendeklarasikan beberapa kode yang akan dijalankan setelah setiap eksekusi blok (dalam kasus ini "tambah `i` dengan 1")


Seperti yang Anda lihat, bounded loop digunakan untuk mendeklarasikan kondisi yang lebih kompleks untuk eksekusi berulang dari sebuah kode, namun seringkali hal ini tidak diperlukan.


### Label blok


Jika Anda harus menulis aliran kontrol yang lebih kompleks, JavaScript memungkinkan Anda memberi nama blok menggunakan **label** yang dapat digunakan dengan `break` atau `continue` untuk menentukan `di mana` untuk melompat kembali.


Contoh:


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


Cetakan ini:


```
Inside outer block
Inside inner block
Done
```


Kami menggunakan `break outer` untuk keluar dari blok `outer` sepenuhnya.


Anda juga dapat memberi label pada loop. Mari kita ambil contoh ini:


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

Ini adalah contoh yang sangat membosankan, tetapi mudah-mudahan ini memperjelas kebutuhan (sesekali) akan label.


## Memperkenalkan fungsi

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


Seiring dengan perkembangan program Anda, Anda akan sering ingin menggunakan kembali potongan-potongan kode.


Itulah gunanya **fungsi**: fungsi ini memungkinkan Anda mengelompokkan beberapa kode, memberinya nama, dan menjalankannya kapan pun Anda mau.


### Deklarasi fungsi


Untuk mendeklarasikan sebuah fungsi, kita dapat menggunakan kata kunci `function`. Kemudian kita beri nama, sepasang tanda kurung `()` dengan argumen yang dibutuhkan, dan blok kode `{}` yang akan dieksekusi. Mari kita mulai dengan fungsi yang tidak membutuhkan argumen:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Kode ini **mendeklarasikan** fungsi, tetapi belum **menjalankannya.


### Panggilan fungsi


Untuk menjalankan (atau "memanggil") fungsi, Anda menulis nama fungsi diikuti dengan tanda kurung:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Cetakan ini:


```
Hello!
```


Anda dapat memanggil fungsi ini sebanyak yang Anda inginkan:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Cetakan ini:


```
Hello!
Hello!
```


Kode di dalam fungsi hanya berjalan ketika Anda memanggilnya.


### Argumen fungsi (masukan ke fungsi)


Terkadang, Anda ingin sebuah fungsi bekerja dengan beberapa masukan. Anda dapat melakukannya dengan menambahkan **argumen** di dalam tanda kurung.


Sebagai contoh:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Sekarang fungsi ini mengambil **satu argumen** yang disebut `teman`.


Ketika Anda memanggil fungsi, Anda dapat mengoper suatu nilai:


```javascript
sayHelloTo("Tommy")
```


Cetakan ini:


```
Hello Tommy!
```


Anda dapat memanggil fungsi ini lagi dengan nama yang berbeda:


```javascript
sayHelloTo("Sam")
```


Cetakan ini:


```
Hello Sam!
```


Nilai yang Anda masukkan akan menggantikan variabel `teman` di dalam fungsi.


Anda juga dapat menggunakan lebih dari satu argumen:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Cetakan ini:


```
Hello Lina and Marco!
```


### `kembali` (keluaran dari fungsi)


Fungsi juga dapat **mengembalikan** nilai. Ini berarti fungsi tersebut mengirimkan nilai kembali ke tempat fungsi itu dipanggil.


Berikut adalah contoh sederhana:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Cetakan ini:


```
42
```


Fungsi `getNumber()` mengembalikan `42`, dan kita menyimpannya di `hasil`, lalu mencetaknya.


Anda juga dapat mengembalikan sesuatu yang Anda hitung:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Cetakan ini:


```
5
```


Setelah nilai `kembali` dikembalikan, fungsi akan berhenti. Apapun setelah `return` dalam blok tersebut tidak akan terjadi.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


Hanya untuk cetakan ini saja:


```
hi
```


karena hanya `"hai"` yang dikembalikan. Baris `console.log("ini tidak pernah berjalan")` dilewati.


Anda dapat menganggap fungsi sebagai sub-program kecil. Setiap fungsi dapat mengambil beberapa input, mengerjakannya, dan memberikan Anda beberapa output.


Apa yang terjadi jika kita mencoba menggunakan nilai balik suatu fungsi, tetapi fungsi tersebut tidak mengembalikan apa pun?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Ini akan mencetak `tidak terdefinisi`. Nilai balik dari fungsi yang tidak mengembalikan apa pun adalah `tidak terdefinisi`.


## Objek dan kelas

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript sering disebut sebagai bahasa berorientasi objek.


Artinya, ini membantu Anda mengatur kode Anda dengan mengelompokkan nilai dan fungsi menjadi **objek**.


### Apa yang dimaksud dengan `objek`?


Sebuah objek dapat berisi data dan fungsi yang beroperasi pada data tersebut. Ketika sebuah fungsi dimasukkan ke dalam sebuah objek, kita menyebutnya sebagai sebuah `metode`.


Objek pertama yang telah kita lihat adalah objek `konsol`. Ini adalah objek yang berisi beberapa metode untuk mencetak sesuatu di layar dan men-debug program kita.


Bahkan dapat mencetak sendiri; Anda dapat melakukan


```javascript
console.log(console)
```


dan akan mencetak daftar metode yang ada di dalamnya. Sebagai contoh, pada mesin saya, ia mencetak


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


Seperti yang Anda lihat, aplikasi ini memiliki banyak metode yang dapat Anda gunakan untuk melakukan debug!


Javascript memberikan kita cara yang berbeda untuk membuat objek baru yang dapat melakukan apa pun yang kita inginkan.


### Membuat objek


Cara termudah untuk membuat objek hanya dengan mengelompokkan data dan fungsi menggunakan **kurung kurawal** `{}`.


Hal ini menciptakan apa yang kami sebut sebagai **objek anonim**


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Ini menciptakan sebuah objek dan menyimpannya dalam variabel bernama `cat`.


Objek memiliki dua **properti**:



- `nama` dengan nilai `"Kumis"`
- `usia` dengan nilai `3`


Mari kita cetak:


```javascript
console.log(cat)
```


Cetakan ini:


```
{ name: 'Whiskers', age: 3 }
```


Anda dapat mengeluarkan properti dari objek menggunakan titik, seperti pada `objectName.propertyName`:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Anda juga dapat **mengubah** properti:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Seperti yang dapat Anda lihat, meskipun sebuah objek didefinisikan sebagai `const`, Anda masih dapat memodifikasi data yang dikandungnya.


Pada kasus objek, `const` hanya akan menghentikan Anda untuk menimpa seluruh objek:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Seperti yang telah disebutkan sebelumnya, objek juga dapat menyimpan **fungsi**, dan ketika sebuah fungsi merupakan bagian dari objek, kita menyebutnya **metode**.


Berikut ini sebuah contoh:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Objek ini memiliki:



- Sebuah properti `nama`
- Sebuah metode `speak()`


Mari kita sebut metodenya:


```javascript
cat.speak()
```


Ini mencetak:


```
Meow!
```


Metode dapat menggunakan data yang dikandung objek melalui kata kunci `this`.

`this` mengacu pada objek saat ini. Pada contoh ini, ini akan digunakan untuk mencetak nama kucing:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Cetakan ini:


```
Whiskers says meow!
```


Kata `ini` berarti "objek ini"... dalam hal ini, objek `kucing`.



Jenis objek seperti ini sangat bagus jika Anda hanya menginginkan sesuatu yang cepat dan sederhana. Tetapi jika Anda perlu membuat **banyak objek** dengan struktur yang sama, ada cara yang lebih baik, dan di situlah **kelas** masuk.


### Kelas dan konstruktor


Sebuah **class** adalah seperti cetak biru. Kelas memberi tahu JavaScript cara membuat jenis objek tertentu.


Anda mendefinisikan kelas dengan menggunakan kata kunci `class`, diikuti dengan nama kelas, dan dengan blok kurung kurawal `{}`.


```javascript
class Dog {}
```


Kelas biasanya dimulai dengan huruf besar, berdasarkan konvensi.


Anda dapat membuat objek baru dari sebuah kelas dengan menggunakan `new`:


```javascript
const hachiko = new Dog()
```


Cobalah untuk mencetak objek:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Anda akan mendapatkan


```
Dog {}
```


Seperti yang Anda lihat, kelas Dog kosong, sehingga objek `myDog` juga kosong.


Kita dapat mendefinisikan properti mana yang harus dimiliki objek Dog dengan menambahkan `constructor`.


Konstruktor adalah fungsi khusus yang berjalan ketika Anda membuat (atau "membangun") objek baru.


```javascript
class Dog {
constructor() { }
}
```


Kita ingin setiap Anjing memiliki nama, jadi kita menambahkan parameter `nama` ke fungsi tersebut:


```javascript
class Dog {
constructor(name) { }
}
```


Lalu kita menggunakan `this` untuk menyatakan bahwa `nama` adalah `nama` dari objek `Dog` yang sedang kita buat


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Mari kita coba menggunakannya sekarang:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


Ini mencetak sesuatu seperti:


```
Dog { name: 'hachiko' }
```


Seperti yang Anda lihat, metode `constructor` mengambil argumen yang Anda berikan ke kelas ketika Anda melakukan `new Dog()`, dan menggunakannya untuk membangun objek.


Mari kita uraikan:



- `class Dog` mendefinisikan kelas Dog.
- `constructor(name)` menyiapkan objek saat dibuat.
- `this.name = nama` menyimpan nilai dalam objek baru.
- `new Dog("hachiko")` membuat objek baru dari kelas, dengan properti `nama` yang diset ke `"hachiko"`.


Sekarang mari kita tambahkan metode ke kelas kita:


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


Ini akan mencetak


```javascript
hachiko says barf!
```


Jika kita melakukan hal yang sama untuk dua contoh Dog yang berbeda



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


kita mendapatkan


```
hachiko says barf!
bobby says barf!
```


metode `speak()` menggunakan properti `nama` dari `Dog` yang dipanggil.


Ini adalah alasan utama mengapa kelas ada: kelas memungkinkan kita mendefinisikan sekumpulan metode yang beroperasi pada data, dan kemudian membuat beberapa objek yang memiliki "bentuk" data yang sama.


Ketika kita memanggil sebuah metode pada salah satu objek ini, metode tersebut akan beroperasi pada data yang dimiliki oleh *objek tertentu*.


### Mengubah bentuk objek


Objek dalam JavaScript bersifat fleksibel. Bahkan setelah Anda membuatnya, Anda masih bisa menambahkan properti baru atau menghapus properti yang sudah ada.


Ini diperbolehkan, tetapi Anda harus menggunakannya dengan hati-hati.


Mari kita mulai dengan kelas `Dog` yang sederhana:


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


Pada titik ini, `myDog` hanya memiliki satu properti: `nama`. Kita masih dapat menambahkan properti baru setelah dibuat:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


Kita juga dapat menambahkan metode baru:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


Dan kita juga dapat menghapus properti, dengan menggunakan kata kunci `delete`.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


Hal ini berhasil, tetapi ada hal penting yang perlu diketahui: Mesin JavaScript seperti V8 (digunakan di Node.js dan browser Chrome) berjalan lebih cepat ketika objek Anda selalu mempertahankan properti yang sama. Jika Anda menambahkan atau menghapus properti setelah objek dibuat, hal ini akan memperlambat kinerja.


Pada program kecil, hal ini tidak terlalu penting. Tetapi dalam proyek yang lebih besar (seperti game), lebih baik mencantumkan semua properti dalam konstruktor dari awal, bahkan jika Anda tidak langsung menggunakannya. Hal ini akan menjaga bentuk objek tetap stabil dan membantu kode Anda berjalan lebih cepat.


Misalnya, bukannya ini:


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


Anda bisa melakukan


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


Kedua versi ini dapat digunakan, tetapi versi kedua lebih baik untuk performa. Anda memberi tahu mesin di depan properti apa yang akan dimiliki setiap objek, dan mesin dapat mengoptimalkannya.


JavaScript memungkinkan Anda membentuk ulang objek secara bebas, tetapi ketika menggunakan kelas, sebaiknya rencanakan bentuk objek Anda sebelumnya.



### Pewarisan dengan `extends` dan `super()`


Terkadang Anda ingin membuat kelas yang *hampir* sama dengan kelas lain, tetapi dengan beberapa fitur tambahan.


Daripada memodifikasi bentuk objek (yang seperti yang disebutkan sebelumnya tidak optimal untuk kinerja), atau harus menulis ulang kelas baru dari awal, JavaScript memungkinkan Anda menggunakan sesuatu yang disebut **inheritance**.


Pewarisan berarti satu kelas dapat **memperluas** kelas lainnya. Kelas baru mendapatkan semua properti dan metode dari kelas lama, dan Anda dapat menambahkan lebih banyak atau mengubah apa yang Anda butuhkan.


Katakanlah kita memiliki kelas dasar bernama `Kendaraan`:


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


Sekarang kami ingin membuat kelas `Mobil`. Mobil adalah sejenis kendaraan, tetapi kita mungkin ingin mobil memiliki beberapa fitur tambahan atau pesan yang berbeda saat dinyalakan. Daripada menulis ulang semuanya, kita dapat menggunakan `extends`:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Kelas `Mobil` sekarang **mewarisi** semua yang ada pada `Kendaraan`. Kelas ini mendapatkan properti `brand`, dan kita telah mengganti metode `start()` dengan versi kita sendiri.


![](assets/en/4.webp)


Mari kita coba:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Cetakan ini:


```
Toyota car is ready to drive!
```


Meskipun `Mobil` tidak memiliki konstruktornya sendiri, ia tetap menggunakan konstruktor dari `Kendaraan`. Tetapi jika kita ingin menulis konstruktor khusus di `Mobil`, kita bisa, kita hanya perlu menyertakan pemanggilan ke konstruktor induknya menggunakan `super()`.


Begini caranya:


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



Cetakan ini:


```
Toyota Corolla is ready to drive!
```


Jadi untuk meringkas



- `extends` berarti satu kelas didasarkan pada kelas lainnya.
- `super()` digunakan untuk memanggil konstruktor kelas yang Anda perluas.
- Kelas baru mendapatkan semua properti dan metode dari kelas aslinya.
- Anda dapat **mengganti** metode (seperti `start()`) untuk membuatnya melakukan sesuatu yang berbeda.


Hal ini sangat membantu ketika Anda memiliki beberapa benda yang mirip (seperti mobil, truk, dan sepeda) dan Anda ingin mereka berbagi kode namun tetap berperilaku dengan caranya sendiri.


### `instanceof`


Kata kunci `instanceof` memeriksa apakah sebuah objek dibuat dari kelas tertentu.


Katakanlah kita memiliki kelas bernama `User`:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Cetakan ini:


```
true
```


Mengkonfirmasi bahwa `pengguna biasa` adalah `Pengguna`. Hal ini karena `pengguna biasa` dibuat dengan menggunakan kelas `Pengguna`.


Ini juga bekerja dengan kelas yang diwariskan. Sebagai contoh, berikut ini adalah kelas `Admin` yang memperluas `User`:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Kedua baris tersebut menghasilkan nilai `true`. Hal ini karena `Admin` adalah subkelas dari `Pengguna`, oleh karena itu `kamiAdmin` adalah `Admin` dan `Pengguna`


# JavaScript Tingkat Menengah

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Penanganan Kesalahan

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


Ketika Anda menulis program JavaScript yang lebih kompleks, Anda akan menemukan **error**. Ini adalah situasi tak terduga di mana terjadi kesalahan. Mungkin sebuah variabel `tidak terdefinisi` tetapi Anda mencoba menggunakannya, atau beberapa kode menerima jenis input yang salah.


Jika kita tidak menangani kesalahan ini dengan benar, program kita mungkin akan crash atau berperilaku tidak sesuai harapan. JavaScript menyediakan alat untuk mendeteksi dan mengelola kesalahan ini sehingga kita dapat menanganinya dengan lebih baik.


### Kesalahan umum: mengakses nilai pada `undefined`


Berikut adalah situasi umum yang menyebabkan kesalahan:


```javascript
const user = undefined
console.log(user.name)
```


Jika Anda menjalankan kode ini, Anda akan mendapatkan kesalahan yang terlihat seperti ini:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


Itulah yang diberitahukan JavaScript kepada Anda: "Hei, Anda mencoba mendapatkan properti `nama` dari sesuatu yang `tidak terdefinisi`, dan itu tidak masuk akal." Dan seperti yang Anda lihat, ketika kesalahan seperti ini terjadi, program akan berhenti berjalan kecuali Anda secara khusus menulis kode untuk menangkap dan menanganinya.


### `membuang` kesalahan


Terkadang Anda ingin secara manual `membangkitkan kesalahan` dalam kode Anda. Dalam hal ini, Anda menggunakan kata kunci `throw`.


```javascript
throw new Error("This is a custom error message")
```


Hal ini segera menghentikan program dan mencetak:


```
Uncaught Error: This is a custom error message
```


Anda dapat menggunakan `throw` untuk menerapkan aturan dalam program Anda. Sebagai contoh:


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


Pemanggilan kedua menyebabkan kesalahan karena membagi dengan nol tidak diperbolehkan dalam contoh ini.


### Menangkap kesalahan dengan `coba...tangkap`


Jika Anda tidak ingin program Anda crash ketika terjadi kesalahan, Anda dapat menangkap kesalahan tersebut dengan menggunakan blok `try...catch`. Hal ini sangat membantu ketika Anda ingin program Anda tetap berjalan meskipun terjadi kegagalan.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Keluaran:


```
Oops! Something went wrong.
```


Begini cara kerjanya:



- Kode di dalam blok `try` akan dicoba terlebih dahulu.
- Jika terjadi kesalahan, JavaScript **melompat ke blok `tangkap`, melewatkan blok `coba` lainnya.
- Blok `catch` menerima kesalahan, sehingga Anda dapat mencetaknya, atau menanganinya dengan cara lain, seperti misalnya


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Keluaran:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### Blok `akhirnya`


Anda juga dapat menambahkan blok `akhirnya`. Ini adalah kode yang **selalu berjalan**, baik ketika terjadi kesalahan atau tidak.


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


Keluaran:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Menghindari Bug

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


Bab ini menunjukkan beberapa jebakan paling umum dalam JavaScript, dan cara menghindarinya.


### `var` dan Assignment tanpa deklarasi


Pada kode JavaScript yang lebih lama, variabel sering dideklarasikan dengan menggunakan kata kunci `var`. Tidak seperti `let` dan `const`, yang telah Anda pelajari, `var` dapat berperilaku dengan cara yang membingungkan.


Sebagai contoh:


```javascript
{
var message = "hello"
}
console.log(message)
```


Anda mungkin mengharapkan `pesan` hanya ada di dalam blok, tetapi ternyata tidak. `var` mengabaikan cakupan blok dan membuat variabel tersedia di seluruh fungsi atau file.


Hal ini dapat menyebabkan perilaku yang tidak diharapkan, terutama pada program yang lebih besar. Karena alasan ini, kode JavaScript modern harus selalu menggunakan `let` atau `const`, bukan `var`.


Lebih buruk lagi, JavaScript memungkinkan Anda menetapkan nilai ke variabel **tanpa mendeklarasikannya sama sekali**:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Hal ini menciptakan sebuah variabel global `nama` baru tanpa deklarasi. Hal ini dapat terjadi secara diam-diam dan menyebabkan bug yang sulit dilacak oleh Hard, terutama jika itu hanya kesalahan ketik. Selalu deklarasikan variabel dengan menggunakan `let` atau `const`.


### Sistem tipe lemah


JavaScript diketik dengan lemah, yang berarti JavaScript secara otomatis mengonversi nilai dari satu tipe ke tipe lainnya jika diperlukan. Hal ini disebut pemaksaan tipe, dan meskipun nyaman, namun sering kali menyebabkan hasil yang membingungkan.


Sebagai contoh:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


Pada contoh-contoh ini, JavaScript mencoba menebak apa yang Anda maksud. Terkadang JavaScript mengubah string menjadi angka, atau boolean menjadi angka, atau string menjadi string. Hal ini dapat membuat kode Anda berperilaku dengan cara yang tidak terduga.


Menyadari sistem pengetikan JavaScript yang lemah adalah hal yang penting. Ketika segala sesuatunya mulai bertindak aneh, itu mungkin disebabkan oleh pemaksaan pengetikan yang tidak terduga.


### "gunakan dengan ketat"


Anda dapat mengaktifkan mode yang lebih ketat yang mengubah beberapa kesalahan diam menjadi kesalahan nyata, dan menghentikan Anda menggunakan beberapa fitur bahasa yang lebih berbahaya.


Untuk mengaktifkan mode yang lebih ketat ini, tambahkan baris ini di bagian atas file atau fungsi Anda:


```javascript
"use strict"
```


Sebagai contoh:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Tanpa mode ketat, JavaScript akan secara diam-diam membuat variabel global yang disebut `nama`. Tetapi dengan mode ketat, ini menjadi kesalahan nyata, membantu Anda menangkap bug lebih awal.


Mode ketat juga menonaktifkan beberapa fitur JavaScript yang sudah ketinggalan zaman, dan membuat kode Anda lebih mudah dioptimalkan dan dipelihara.


## Nilai vs Referensi

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript memperlakukan berbagai jenis nilai dengan cara yang berbeda.


Beberapa nilai akan **disalin** saat Anda menetapkannya ke variabel.


Yang lainnya **dibagi** ketika Anda menetapkannya ke variabel baru, jadi jika Anda mengubah salah satunya, variabel yang lain juga akan berubah.


### Lulus dengan nilai


Ketika sebuah nilai dilewatkan **dengan nilai**, JavaScript membuat **salinan** dari nilai tersebut.


Jadi, jika Anda mengubah salah satunya, tidak akan memengaruhi yang lain.


Hal ini terjadi pada tipe primitif, seperti:



- angka
- string
- boolean (`benar` dan `salah`)
- `null`
- `tidak terdefinisi`


Mari kita lihat sebuah contoh:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


Kami memberi `b` nilai dari `a`, tetapi kemudian kami mengubah `b` menjadi `10`.


Karena angka diteruskan berdasarkan nilai, JavaScript menyalin `5` ke dalam `b`. `5` di `b` tidak bergantung pada `5` asli di `a`, sehingga mengubah nilai `b` tidak berpengaruh pada `a`.


Mari kita coba dengan seutas tali:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Sekali lagi, mengubah `nama2` tidak mempengaruhi `nama1`, karena string juga diteruskan dengan nilai.


Hal yang sama terjadi ketika Anda mengoper primitif ke sebuah fungsi: fungsi tersebut akan disalin. Jadi fungsi tersebut tidak dapat mengubah yang asli.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Meskipun di dalam fungsi `1` ditambahkan ke `x`, `angka` asli tidak berubah.


Itu karena hanya **copy** yang diteruskan ke dalam fungsi.


### Lulus dengan referensi


Objek dilewatkan **dengan referensi**.


Itu berarti alih-alih menyalinnya, JavaScript hanya meneruskan **reference** ke variabel tersebut, dan jika Anda memodifikasinya, semua variabel lain yang menunjuk ke variabel tersebut juga akan melihat perubahannya.


Sebagai contoh:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Baik `orang1` maupun `orang2` menunjuk ke objek yang sama dalam memori.


Jadi, ketika kita mengubah `person2.name`, kita juga mengubah `person1.name`, karena keduanya melihat hal yang sama.


Larik adalah objek, jadi mari kita coba hal yang sama dengan array:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


Kita telah mendorong `4` ke dalam `daftar2`, tetapi `daftar1` juga terpengaruh, karena keduanya merujuk ke larik yang sama.


Mari kita lihat apa yang terjadi ketika kita mengoper sebuah objek ke sebuah fungsi:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


Fungsi ini mengubah objek! Itu karena fungsi tersebut menerima **referensi** ke objek `orang` yang asli.


Ia tidak mendapatkan salinannya. Ia mendapatkan akses ke objek asli, dan dengan itu ia mendapatkan kemampuan untuk memodifikasinya.


Penting untuk mengingat perbedaan ini, karena jika tidak, kode kita akan berperilaku berbeda dari yang kita harapkan. Sebagai contoh, kita mungkin menulis sebuah fungsi dengan harapan bahwa fungsi tersebut tidak akan mengubah argumen yang diterimanya, dan kemudian mengetahui bahwa fungsi tersebut ternyata mengubah argumen tersebut (karena argumen tersebut adalah objek, sehingga dilewatkan melalui referensi).


## Bekerja dengan Fungsi

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


Anda telah mempelajari cara mendeklarasikan dan menggunakan fungsi dalam JavaScript. Tetapi JavaScript memberi Anda lebih banyak alat untuk bekerja dengan fungsi dengan cara yang hebat.


### Fungsi panah


Fungsi panah adalah cara yang lebih singkat untuk menulis fungsi. Alih-alih menggunakan kata kunci `fungsi`, kita menggunakan tanda panah (`=>`).


Berikut ini fungsi normalnya:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


Versi panah terlihat seperti ini:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Jika fungsi memiliki **hanya satu baris**, Anda dapat melewatkan tanda kurung dan `kembali`:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Jika fungsi memiliki **hanya satu parameter**, Anda bahkan dapat melewatkan tanda kurung di sekitar parameter:


```javascript
const greet = name => `Hello, ${name}!`
```


Fungsi panah sangat umum digunakan dalam JavaScript modern, karena fungsi ini memungkinkan untuk mengekspresikan fungsi sederhana dengan boilerplate yang jauh lebih sedikit.


### Parameter default


Terkadang Anda ingin sebuah fungsi memiliki **nilai default** jika tidak ada argumen yang diberikan.


Anda dapat melakukannya seperti ini:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


Nilai default `"teman"` digunakan ketika tidak ada yang dimasukkan.


### Parameter penyebaran (`...`)


Bagaimana jika fungsi Anda mengambil sejumlah argumen yang fleksibel?


Anda dapat menggunakan **spread operator** (`...`) untuk mengumpulkannya ke dalam sebuah array:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Anda kemudian dapat menggunakan loop untuk memproses setiap item:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


Operator spread berguna ketika Anda tidak tahu berapa banyak argumen yang akan diteruskan.


### Fungsi tingkat tinggi


Fungsi **tingkat yang lebih tinggi** adalah fungsi yang:



- mengambil fungsi lain sebagai masukan
- dan/atau mengembalikan fungsi sebagai keluaran


Berikut adalah contoh sederhana:


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


Cetakan ini:


```
Hello, friend!
Hello, friend!
```


Kita bisa memberikan fungsi panah padanya:


```javascript
runTwice(
() => console.log("Hello!")
)
```


Cetakan ini:


```
Hello!
Hello!
```


Anda juga dapat menulis fungsi yang **mengembalikan** fungsi lain:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


Fungsi `makeGreeter` adalah fungsi yang membangun fungsi lain. Fungsi ini menerima sebuah string dan mengembalikan sebuah fungsi baru yang menggunakan string tersebut dalam panggilan `console.log`.


Pola semacam ini sangat dahsyat, karena memungkinkan Anda meninggalkan "lubang" dalam fungsi Anda yang bisa Anda isi nanti dengan perilaku yang Anda perlukan.


### `peta()`, `filter()`, `kurangi()`


JavaScript memberi Anda beberapa metode bawaan yang berguna untuk digunakan dengan array.


Metode-metode ini mengambil fungsi sebagai argumen, sehingga mereka juga merupakan fungsi tingkat tinggi.


`map()` mengubah setiap item dalam sebuah larik menjadi sesuatu yang lain.


Contoh:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Setiap angka digandakan, dan hasilnya adalah larik baru.


`filter()` menghapus item dari larik jika tidak lulus tes.


Contoh:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Hanya entri larik yang memiliki kondisi `x > 2` yang mengembalikan nilai `true` yang disimpan.


`reduce()` digunakan untuk menggabungkan semua item dalam sebuah larik menjadi satu nilai.


Contoh:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


`reduce` melewati larik dan, dalam contoh ini, menerapkan operator `+` di antara `1` dan `2`, lalu di antara `3` dan `3` yang dihasilkan, lalu di antara `6` dan `4` yang dihasilkan, hingga memiliki jumlah semua entri larik (yaitu 10).


Anda dapat menggunakan `reduce()` untuk banyak hal seperti total, rata-rata, atau membuat nilai baru selangkah demi selangkah.


Metode-metode ini (`map`, `filter`, `reduce`) merupakan alat bantu yang kuat untuk memproses data tanpa menulis perulangan manual.


Anda bahkan dapat menggabungkannya dalam suatu rangkaian operasi, seperti ini:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Bekerja dengan Objek

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


Pada bab ini, kita akan mempelajari beberapa alat yang kuat dan sedikit lebih canggih untuk bekerja dengan objek dalam JavaScript.


### Properti Pribadi


Terkadang, kita ingin menyembunyikan sebuah properti dari sebuah objek agar tidak dapat diubah atau diakses dari luar objek tersebut. JavaScript memberi kita cara untuk melakukan hal ini dengan menggunakan `#` sebelum nama properti. Hal ini akan membuat sebuah properti **private**, yang hanya dapat diakses dari dalam kelas.


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


Properti pribadi sangat membantu ketika Anda ingin mencegah perubahan yang tidak disengaja.


### properti `statis`


Terkadang, Anda ingin sebuah properti menjadi milik kelas itu sendiri, bukan milik setiap objek yang Anda buat dari kelas tersebut. Untuk itulah kegunaan dari `static`. Sebuah properti `statis` terdapat di dalam kelas dan semua objek dari kelas tersebut akan merujuk ke properti tersebut.


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


Ini berguna untuk menyimpan data dan metode bersama yang berlaku untuk seluruh kelompok objek, bukan hanya satu.


### `dapatkan` dan `set`


Dalam JavaScript, `get` dan `set` memungkinkan Anda membuat properti yang *terlihat* seperti variabel biasa, tetapi sebenarnya menjalankan kode khusus di latar belakang.


Metode `get`terjadi ketika Anda mencoba untuk *membaca* sebuah properti. Metode ini dideklarasikan dengan menulis `get` sebelum metode dengan nama properti.


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


Meskipun `fullName` bukan properti biasa, kita dapat menggunakannya seperti properti, dan di belakang layar menjalankan fungsi `get` untuk membangun nama lengkap.


Metode `set`ter berjalan ketika Anda *menetapkan* sebuah nilai ke sebuah properti. Metode ini memungkinkan Anda untuk mengontrol apa yang terjadi ketika seseorang mencoba mengubah nilai tersebut. Metode ini dideklarasikan dengan menulis `set` sebelum metode dengan nama properti.


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


Ketika kita melakukan `user.fullName = "John Smith"`, ini akan menjalankan metode `set` dan memperbarui nilai `firstName` dan `lastName`.


Jadi, meskipun terlihat seperti kita hanya mengatur variabel sederhana, sebenarnya kita memicu logika yang memperbarui properti lain.


## Kunci dan Nilai

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Setiap properti dalam objek JavaScript memiliki **kunci** (juga disebut nama properti) dan **nilai**.


Sebagai contoh:


```javascript
const user = {
name: "Alice",
age: 30
}
```


Pada objek ini, `"nama"` dan `"usia"` adalah kunci, dan "Alice" dan `30` adalah nilainya.


### Akses Dinamis


Terkadang, Anda tidak mengetahui nama sebuah properti sebelumnya... mungkin Anda mendapatkannya dari masukan pengguna, atau membacanya dari sebuah variabel. Anda masih bisa mengaksesnya dengan menggunakan notasi **bracket**, seperti `myObject["keyName"]`.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


Kami mengoperkan string `nama` ke objek untuk mendapatkan nilai yang sesuai.


Kita dapat menyimpan kunci ke sebuah variabel dan menggunakannya untuk mengakses nilai yang sesuai nanti, seperti


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Dinamis Assignment


Anda juga dapat membuat atau memperbarui properti objek menggunakan variabel sebagai kunci.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


Hal ini sangat membantu apabila Anda ingin membuat objek selangkah demi selangkah. Sebagai contoh:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Anda bahkan dapat menggunakan kunci dinamis *sambil membuat* objek menggunakan tanda kurung siku:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Ini disebut dengan **properti yang dihitung**. Nilai di dalam tanda kurung siku dievaluasi, dan hasilnya digunakan sebagai kunci.


### jenis `Simbol`


Selain string, JavaScript juga memungkinkan Anda menggunakan tipe khusus yang disebut `Symbol` sebagai kunci objek.


Mari kita mulai dengan contoh sederhana:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


Pada contoh ini, `id` adalah sebuah Simbol. Ini bukan sebuah string, tetapi masih berfungsi sebagai kunci. Jika Anda mencoba memasukkan `user` ke konsol, Anda akan melihat ini:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


Hal penting lainnya: setiap simbol yang Anda buat adalah unik, meskipun dibuat menggunakan string yang sama.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Simbol memungkinkan Anda mendefinisikan kunci yang tidak akan berbenturan dengan kunci biasa. Sebagai contoh, katakanlah Anda memiliki objek dengan properti `nama`, namun objek tersebut akan disesuaikan oleh pengguna di masa mendatang, dengan cara yang tidak dapat Anda prediksi, dan pengguna tersebut dapat menambahkan properti `nama` juga. Jika properti `nama` yang asli didefinisikan dengan string, properti tersebut akan ditimpa oleh properti yang baru, seperti ini:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Jika kita menggunakan Simbol sebagai gantinya:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Seperti yang Anda lihat, properti `nama` asli entah bagaimana dipertahankan dengan cara ini. Hal ini dapat berguna dalam kasus tepi tertentu.


## Objek Utilitas

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript memberi kita beberapa objek bawaan yang berguna yang membantu kita melakukan hal-hal seperti debugging dan operasi matematika.


### Metode `konsol` lainnya


Anda telah melihat `console.log`, yang mencetak nilai ke layar.


Ada beberapa metode berguna lainnya yang tersedia pada objek `console` yang dapat membantu Anda men-debug program Anda.


#### `console.warn`


Mencetak pesan dengan warna kuning (atau dengan ikon peringatan di beberapa lingkungan):


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


Mencetak pesan dengan warna merah, seperti kesalahan:


```javascript
console.error("Something went wrong!")
```


#### `konsol.tabel`


Menampilkan larik atau objek sebagai tabel:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Ini mencetak tabel seperti:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


Hal ini dapat berguna untuk memvisualisasikan data terstruktur.


#### `console.time` dan `console.timeEnd`


Anda dapat mengukur berapa lama waktu yang dibutuhkan:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


Ini mencetak sesuatu seperti:


```
timer: 2.379ms
```


Berguna untuk beberapa pengujian performa sederhana.


### Objek `Matematika`


JavaScript memberi Anda objek `Math` dengan metode yang berguna untuk melakukan perhitungan.


#### `Math.random()`


Mengembalikan angka acak antara 0 (inklusif) dan 1 (eksklusif):


```javascript
const r = Math.random()
console.log(r)
```


Contoh keluaran:


```
0.4387429859
```


#### `Math.floor()` dan `Math.ceil()`



- `Math.floor(n)` membulatkan **ke bawah** ke bilangan bulat terdekat
- `Math.ceil(n)` membulatkan **ke atas** ke bilangan bulat terdekat


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


Membulatkan ke bilangan bulat terdekat:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` dan `Math.min()`


Mengembalikan nilai terbesar atau terkecil dari daftar angka:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` dan `Math.sqrt()`



- `Math.pow(a, b)` memberi Anda `a` dengan pangkat `b`
- `Math.sqrt(n)` memberi Anda akar kuadrat dari `n`


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# JavaScript Tingkat Lanjut

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Koleksi lainnya

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript memberi kita beberapa tipe koleksi khusus yang melampaui array dan objek biasa. Ini termasuk `Map` dan `Set`.


Mereka membantu Anda menyimpan dan mengelola kelompok nilai, tetapi cara kerjanya berbeda dengan apa yang telah Anda lihat sejauh ini.


Sebuah `Peta` adalah sebuah koleksi dari **pasangan nilai kunci**, seperti halnya sebuah objek. Namun memiliki beberapa perbedaan penting:



- Tuts dapat berupa **nilai apa pun**, bukan hanya string.
- Urutan item dipertahankan.
- Aplikasi ini memiliki metode built-in untuk mempermudah pengerjaannya.


Anda membuat peta baru seperti ini:


```javascript
const myMap = new Map()
```


Hal ini akan membuat sebuah peta kosong. Untuk menambahkan entri ke dalamnya, gunakan `myMap.set(key, value)`:


```javascript
myMap.set("name", "Alice")
```


Ini menambahkan kunci "nama" dengan nilai "Alice".


Anda juga dapat menggunakan angka sebagai kunci:


```javascript
myMap.set(42, "The answer")
```


Dan bahkan sebuah benda sebagai kunci:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


Hal itu tidak akan bekerja dengan objek biasa, yang hanya mengizinkan tombol string.


Untuk **mendapatkan sebuah nilai**, gunakan `myMap.get(key)`:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


Untuk **memeriksa apakah sebuah kunci ada**, gunakan `myMap.has(key)`:


```javascript
console.log(myMap.has("name")) // true
```


Untuk **menghapus kunci**, gunakan `myMap.delete(key)`:


```javascript
myMap.delete("name")
```


Untuk **menghapus seluruh peta**, gunakan `myMap.clear()`:


```javascript
myMap.clear()
```


Peta sangat bagus untuk mengelola koleksi nilai yang besar, karena mengakses nilai pada peta yang besar biasanya memberikan kinerja yang jauh lebih baik daripada objek yang besar.


### "Set


Sebuah `Set` adalah kumpulan **nilai saja** (tanpa kunci), di mana setiap nilai harus **unik**. Itu artinya:



- Anda tidak dapat memiliki nilai yang sama dua kali
- Nilai-nilai disimpan sesuai urutan Anda menambahkannya


Anda membuat satu set seperti ini:


```javascript
const mySet = new Set()
```


Untuk **menambahkan nilai**, gunakan `mySet.add(value)`:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


Meskipun kami mencoba menambahkan `2` dua kali, set hanya akan menyimpan satu salinan.


Untuk **memeriksa apakah suatu nilai ada di dalam set**, gunakan `mySet.has(value)`:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Untuk **menghapus nilai**, gunakan `mySet.delete(nilai)`:


```javascript
mySet.delete(2)
```


Untuk **menghapus semuanya**, gunakan `mySet.clear()`:


```javascript
mySet.clear()
```


Sebuah `Set` berguna ketika Anda ingin menyimpan koleksi nilai unik tanpa harus memeriksa duplikasi secara manual:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


`Set` menghindari duplikasi untuk Anda.


## Iterator

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


Sebagian besar hal dalam JavaScript yang dapat Anda ulangi (seperti array, string, peta, set) adalah **iterable**: mereka dapat menyediakan iterator untuk isinya.


Iterator adalah objek khusus dalam JavaScript yang membantu Anda menelusuri daftar item **satu per satu**.


### iterator `Objek`


Tidak seperti array atau peta, objek biasa **tidak dapat diiterasi** dengan `for...of`. Jika Anda mencoba ini:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Anda akan mendapatkan kesalahan:


```
TypeError: user is not iterable
```


Hal ini karena objek biasa tidak memiliki iterator bawaan. Tetapi JavaScript memberi Anda alat lain untuk mengulanginya.


#### `Object.keys()`


Anda dapat menggunakan `Object.keys(obj)` untuk mendapatkan larik **kunci** objek, lalu mengulanginya:


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


Cetakan ini:


```
name
age
```


#### `Object.values()`


Untuk mengulang **nilai**, gunakan `Object.values()`:


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


Cetakan ini:


```
Alice
30
```


#### `Object.entries()`


Jika Anda menginginkan **kunci dan nilai**, gunakan `Object.entries()`:


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


Cetakan ini:


```
name is Alice
age is 30
```


Meskipun objek tidak dapat diiterasi secara langsung, metode ini memberi Anda akses penuh ke kontennya dengan cara yang bekerja dengan baik dengan `for...of`.


Tetapi bagaimana cara kerja iterator?


### `Simbol.iterator`


Rahasia di balik semua iterabel adalah **simbol** khusus yang disebut `Symbol.iterator`.


Simbol ini adalah kunci bawaan yang memberi tahu JavaScript: "Objek ini dapat diulang."


Ketika Anda memanggil `myIterable[Symbol.iterator]()`, JavaScript akan mengembalikan objek **iterator** dengan metode `.next()`.


Mari kita lihat seperti apa bentuknya:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Setiap pemanggilan ke `.next()` akan memberikan nilai berikutnya. Setelah selesai, fungsi ini akan kembali:


```javascript
{ value: undefined, done: true }
```


### `next () `


Metode `.next()` digunakan untuk mendapatkan item berikutnya dari urutan.


Setiap kali Anda memanggil `.next()`, Anda akan mendapatkan sebuah objek dengan dua tombol:



- `nilai`: item saat ini
- `done`: boolean yang memberi tahu Anda jika iterasi telah selesai


Mari kita lihat contoh lengkapnya:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Cetakan ini:


```
Lina
Tom
Eva
```


Inilah cara kerja perulangan `for...of` di bawah tenda: perulangan ini menggunakan pola ini dengan `.next()`.


Anda akan mendapatkan hasil yang sama dengan


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Membuat kelas dapat diulang


Anda juga dapat mendefinisikan **kelas iterable** Anda sendiri dengan menambahkan metode `[Symbol.iterator]()`.


Katakanlah kita menginginkan sebuah kelas yang merepresentasikan **rentang angka**, misalnya dari 1 hingga 5.


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


Cetakan ini:


```
1
2
3
4
5
```


Inilah yang terjadi:



- Kita telah mendefinisikan sebuah kelas `Range`
- Di dalam kelas, kita mengimplementasikan `[Symbol.iterator]()`, sehingga JavaScript tahu bagaimana cara mengulangnya
- Metode `next()` mengembalikan setiap angka satu per satu
- Ketika kita mencapai `akhir`, ia akan mengembalikan `{ done: true }`


Sekarang kelas `Range` kita bekerja seperti sebuah array, dan kita dapat menggunakannya dalam setiap loop yang mengharapkan sebuah perulangan.


### Fungsi generator dan `hasil`


Untuk mempermudah pembuatan iterator, JavaScript memberi Anda **fungsi generator**, dengan menggunakan kata kunci `function` (yaitu `function` dengan `*` di akhir) dan kata kunci `yield`.


Mari kita coba:


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


Setiap `hasil` mengembalikan sebuah nilai, dan **menghentikan sementara** fungsi sampai `.next()` berikutnya dipanggil.


Anda juga dapat mengulang sebuah generator dengan `for...of`:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Cetakan ini:


```
1
2
3
```


## Konkurensi dengan panggilan balik

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Hingga saat ini, kode kita bersifat **sinkron**: kode ini berjalan satu per satu, secara berurutan. Tetapi beberapa hal di dunia nyata membutuhkan waktu, dan kita tidak ingin seluruh program berhenti sejenak saat menunggu.


Dalam bab ini kami akan memperkenalkan konsep baru: **konkurensi**. Konsep ini memungkinkan kita untuk memanipulasi urutan pengerjaan sesuatu. Hal ini berguna ketika berurusan dengan hal-hal seperti pengatur waktu, masukan dari pengguna, atau membaca file dari disk. JavaScript menawarkan alat yang berbeda untuk melakukan konkurensi.


### `setTimeout`


Fungsi `setTimeout` memungkinkan Anda **menjalankan fungsi di lain waktu**, setelah beberapa waktu berlalu.


Contoh:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Cetakan ini:


```
Start
End
This runs after 2 seconds
```


Meskipun `setTimeout` muncul di tengah-tengah kode, ia tidak memblokir sisanya. Sebaliknya, ia menjadwalkan fungsi untuk dijalankan ** nanti**, dan segera melanjutkan.


Angka `2000` berarti 2000 milidetik (yaitu 2 detik).

Berikut ini adalah penulisan ulang yang lebih bertele-tele dan ramah pemula untuk bagian **Callbacks** dan **Promise**, menggunakan manipulasi data dan anotasi yang jelas di seluruh bagian:


### Panggilan balik


Sebuah **callback** hanyalah sebuah fungsi yang kita berikan ke fungsi lain sehingga dapat **dipanggil nanti**.


Mari kita lihat contoh nyata menggunakan angka. Bayangkan kita memiliki daftar angka, dan kita ingin menggandakan setiap angka, lalu menerapkan fungsi (callback) ke larik "dua kali lipat" yang dihasilkan, tetapi kita ingin melakukannya setelah penundaan kecil, seolah-olah kita menunggu sesuatu yang lambat (seperti memuat data dari internet).


Berikut ini adalah fungsi yang melakukan hal tersebut dengan menggunakan **callback**:


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


Mari kita coba menggunakan fungsi ini:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


Setelah 1 detik, ini akan mencetak:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**Apa yang terjadi di sini?


1. Kita memberikan `input` sebagai daftar angka yang ingin kita gandakan.

2. Kita juga memberikan **fungsi callback** yang memberi tahu program apa yang harus dilakukan *setelah* penggandaan.

3. Di dalam `doubleNumbers`, kita mensimulasikan penundaan dengan menggunakan `setTimeout`, lalu kita melakukan penggandaan.

4. Setelah selesai, kita panggil pemanggilan kembali pada array "dua kali lipat" yang dihasilkan.


Teknik ini berhasil, tetapi bayangkan Anda ingin melakukan **langkah lebih lanjut** setelah itu, seperti menyaring angka-angka kecil dan kemudian menjumlahkannya. Anda harus membuat lebih banyak pemanggilan balik seperti ini:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Ini adalah Hard yang sulit dibaca dan berantakan. Gaya ini disebut **callback hell**, dan inilah yang diciptakan `Promise` untuk memperbaikinya.


## Kesesuaian dengan Janji

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


Sebuah `Promise` adalah objek JavaScript bawaan yang merepresentasikan sebuah nilai yang akan **disiapkan di masa depan**.


Kita dapat membuat Janji seperti ini:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


Bagian `janji baru () ` menciptakan janji.


Di dalamnya, kami memberinya fungsi dengan dua parameter:



- `resolve`, adalah fungsi yang kita panggil ketika semuanya berhasil
- `reject`, adalah fungsi yang kita panggil jika terjadi kesalahan


Pada contoh di atas, kita langsung menyelesaikannya dengan pesan "Berhasil!".


### `.then()`


Untuk melakukan sesuatu **setelah** janji selesai, kita menggunakan `.then()`:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Cetakan ini:


```
The result is: 100
```


Nilai yang kita lewati ke `resolve()` akan dikirim ke fungsi di dalam `.then()` sebagai `hasil`.


Mari kita simulasikan tugas yang membutuhkan waktu 2 detik dengan menggunakan `setTimeout`:


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


Ini akan menunggu selama 2 detik, kemudian mencetak:


```
Done waiting!
```


### `menolak() `


Mari kita buat janji yang **gagal**:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


Sekarang jika kita menggunakan `.then()` pada ini, tidak ada yang akan terjadi, karena `.then()` hanya menangani keberhasilan.


Untuk menangani kesalahan, kita menggunakan `.catch()`:


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


Ini hanya mencetak


```
Caught an error: Something went wrong
```


Nilai yang diteruskan ke `reject()` dikirim ke fungsi `.catch()`.


Mari kita buat Janji yang **terkadang berhasil dan terkadang gagal**, berdasarkan beberapa kondisi.


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


Sekarang kita bisa menyebutnya dan menangani kedua kasus tersebut:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Cetakan ini:


```
Success: Positive number
```


Dan jika kita mencoba dengan nomor yang berbeda:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Ini mencetak:


```
Failure: Not a positive number
```


### Operasi rantai menggunakan `Promise`s



Kita dapat menulis ulang contoh sebelumnya menggunakan `Promise`, dan akan terlihat lebih bersih.


Mari kita mulai dengan menulis versi baru dari fungsi penggandaan kita, tetapi kali ini, fungsi ini mengembalikan **janji**:


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


Sekarang kita dapat menggunakan `.then()` untuk memberi tahu JavaScript apa yang harus dilakukan dengan hasilnya:


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


Cetakan ini:


```
Doubled numbers: [ 2, 4, 6 ]
```


Sejauh ini, cara kerjanya sama dengan versi callback, tetapi sekarang kodenya lebih mudah diperluas dan dibaca.


Katakanlah kita ingin menambahkan lebih banyak langkah:


1. Pertama, gandakan semua angka

2. Kemudian, hapus angka yang lebih kecil dari 4

3. Terakhir, tambahkan semuanya bersama-sama


Kita dapat menulis satu fungsi untuk setiap langkah, semuanya menggunakan janji:


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


Sekarang kita bisa merantai mereka seperti ini:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


Cetakan ini:


```
Final result after all steps: 10
```


Mari kita telusuri apa yang dilakukannya:


1. `doubleNumbers` menggandakan larik: `[2, 4, 6]`

2. `filterBigNumbers` menghapus apa pun yang ≤ 3: `[4, 6]`

3. `jumlahBilangan` menambahkan angka-angka yang tersisa: `4 + 6 = 10`

4. Terakhir, kami mencetak hasilnya.


Setiap `.then()` menunggu langkah sebelum selesai. Jadi kita dapat membangun **rantai aksi** tanpa bersarang. Hal ini membuat kode lebih mudah dibaca dan lebih mudah di-debug.


## Konkurensi dengan `asinkronisasi`/`menunggu`

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Kita telah melihat bagaimana rantai `Promise` membantu kita menghindari neraka callback, tetapi rantai ini masih dapat membuat Hard terbaca ketika ada banyak langkah yang terlibat.


Di situlah `async` dan `tunggu` berperan. Keduanya memungkinkan kita menulis kode asinkron **yang terlihat seperti kode sinkron**, sehingga lebih mudah dipahami.


### Apa yang dimaksud dengan `asinkronisasi`?


Ketika Anda menulis kata kunci `async` sebelum sebuah fungsi, JavaScript secara otomatis membungkus nilai kembalian fungsi tersebut dengan Promise.


Mari kita lihat contoh dasarnya:


```javascript
async function greet() {
return "hello"
}
```


Jika Anda memanggil fungsi ini:


```javascript
const result = greet()
console.log(result)
```


Anda akan melihat ini:


```
Promise { 'hello' }
```


Meskipun Anda baru saja mengembalikan sebuah string, JavaScript mengubahnya menjadi sebuah Promise untuk Anda. Anda bisa mendapatkan nilai sebenarnya menggunakan `.then()` seperti ini:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Atau Anda dapat menggunakan `tunggu`...


### Apa yang dimaksud dengan `menunggu`?


Kata kunci `tunggu` memberi tahu JavaScript: "tunggu hingga Janji ini selesai, lalu berikan hasilnya."


Tetapi Anda hanya dapat menggunakan `menunggu` **di dalam fungsi asinkronisasi**.


Mari kita tulis ulang contoh tersebut dengan menggunakan `tunggu`:


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


Sekarang, kita dapat menggunakan hasilnya seolah-olah itu adalah nilai biasa.


Mari kita lakukan sesuatu yang lebih berguna sekarang.


### Mensimulasikan penundaan dengan `tunggu`


Kita akan membuat fungsi `tunggu` sederhana yang mengambil jumlah milidetik sebagai argumen dan hanya menyelesaikannya setelah beberapa milidetik, tanpa melakukan hal lain:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


Mari kita coba menggunakannya:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


Cetakan ini:


```
waiting 2 seconds...
done waiting
```


Anda dapat menganggap `menunggu` sebagai "berhenti sejenak di sini sampai janji selesai, lalu lanjutkan."


Hal ini memungkinkan Anda untuk menulis kode dengan cara **atas-ke-bawah** yang berperilaku asinkron, tanpa merantai panggilan `.then()`.


### Menunggu data


Mari kita gunakan kembali contoh sebelumnya, di mana kita menggandakan angka, lalu memfilter, lalu menjumlahkan. Namun kali ini, kita akan menggunakan `async`/`tunggu`.


Kita akan membuat 3 fungsi yang mensimulasikan menunggu, dan mengembalikan Promises:


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


Sekarang mari kita tuliskan fungsi `async` untuk menggabungkan keduanya:


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


Cetakan ini:


```
Final result: 10
```


Ini jauh lebih mudah dibaca daripada merantai `.then()` atau callback bersarang.


Kelihatannya seperti program langkah-demi-langkah biasa, tetapi masih berperilaku asinkron.


## Iterator Asinkron

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Anda telah mempelajari tentang **iterator** dan bagaimana kita dapat menggunakan `for...of` untuk mengulang larik dan hal-hal lain yang dapat diulang.


Tetapi, bagaimana jika data yang ingin kita ulangi membutuhkan waktu untuk tiba?


Terkadang kita ingin mengulang hal-hal yang datang secara **asinkron**, seperti pesan dari obrolan, baris dari file, atau nomor dari sumber yang lambat.


Untuk melakukan hal itu, JavaScript memberi kita **iterator asinkronisasi**.


### Fungsi generator asinkronisasi


Cara termudah untuk membuat iterator asinkronisasi adalah dengan menggunakan **fungsi generator asinkronisasi**.


Kami menulisnya seperti ini:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


Ini terlihat seperti generator biasa, tetapi dengan `asinkronisasi` di depannya.


Kita sekarang dapat menggunakan `untuk menunggu...dari` untuk mengkonsumsi nilai:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Ini akan dicetak:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Jadi apa bedanya dengan generator biasa?


Perbedaannya adalah: kita sekarang dapat menggunakan `menunggu` di dalam generator.


Mari kita buat penolong penundaan lagi:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


Sekarang mari kita hasilkan angka **secara perlahan**:


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


Cobalah menggunakannya:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Mengapa menggunakan iterator asinkron?


Iterator asinkronisasi berguna ketika:



- Nilai-nilai tersebut tidak datang sekaligus.
- Anda ingin menanganinya satu per satu, **saat mereka datang**.
- Anda bekerja dengan Promises, dan ingin mengulang dengan cara yang bersih.


Misalnya, jika Anda ingin memuat pesan dari server obrolan satu per satu, atau mengunduh file besar dalam beberapa bagian, iterator asinkronisasi memberi Anda cara untuk menulis perulangan `for` yang bekerja dengan data yang tertunda.


### `Symbol.asyncIterator`


Kita juga dapat menggunakan iterator asinkronisasi di kelas khusus.


Berikut ini contoh yang menghasilkan angka dengan penundaan:


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


Kita sekarang dapat menggunakan `untuk menunggu...dari` seperti sebelumnya:


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


Hal ini memungkinkan Anda untuk membuat objek yang dapat diulang secara asinkron


## Gula sintesis Assignment

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Syntax sugar" berarti menulis sesuatu dengan cara yang lebih singkat atau lebih mudah, tanpa mengubah apa yang dilakukannya. Ini hanya cara yang lebih baik untuk mengatakan hal yang sama.


JavaScript memiliki beberapa sintaksis bawaan yang memungkinkan kita menulis deklarasi yang lebih bersih dan lebih pendek. Pada bab ini, kita akan melihat cara menetapkan nilai berdasarkan kondisi, memperbarui variabel dengan matematika, mengambil nilai dari larik atau objek, dan menyalin atau menggabungkannya dengan sintaks yang lebih sederhana.


### Operator Ternary


Dalam JavaScript, Anda dapat menetapkan nilai berdasarkan kondisi menggunakan **operator **ternary**, yang merupakan cara singkat untuk menulis `if...else`.


Alih-alih melakukan:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Anda dapat menulis:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


Ini berarti:



- Jika `isMorning` benar, gunakan `"Selamat pagi"`
- Jika tidak, gunakan `"Halo"`


Bentuk umumnya adalah:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Anda juga dapat menggunakannya di dalam ekspresi lain:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Pastikan Anda menggunakannya untuk keputusan yang **sederhana**. Jika logikanya rumit, gunakanlah `jika... maka`.


### Operator Assignment Alternatif


JavaScript memiliki **operator pintas** untuk melakukan tugas yang dikombinasikan dengan operasi.


Mari kita lihat cara yang normal:


```javascript
let counter = 1
counter = counter + 1
```


Hal ini dapat dipersingkat menjadi:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


Berikut ini adalah yang paling umum:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Contoh:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Ini berguna ketika Anda ingin memperbarui variabel menggunakan nilainya sendiri.


### Penghancuran


**Destructuring** memungkinkan Anda mengambil nilai dari array atau objek dan menyimpannya ke dalam variabel dengan mudah.


#### Susunan


Misalkan saja Anda punya:


```javascript
const colors = ["red", "green", "blue"]
```


Alih-alih melakukan:


```javascript
const first = colors[0]
const second = colors[1]
```


Anda bisa melakukannya:


```javascript
const [first, second] = colors
```


Ini menugaskan:



- "pertama" ke "merah
- 'kedua' ke 'Green'


Anda juga dapat melewatkan nilai:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Objek


Anda juga dapat mengekstrak nilai dari objek:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Jika properti memiliki nama yang berbeda dengan variabel yang Anda inginkan, Anda dapat mengganti namanya:


```javascript
const { name: username } = user
console.log(username) // Alice
```


Destrukturisasi membuat kode Anda menjadi lebih bersih ketika bekerja dengan objek dan array.


### Sintaks Penyebaran


Sintaks **spread** menggunakan `...` untuk membongkar atau menyalin nilai.


#### Susunan


Anda dapat menyalin atau menggabungkan array:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Anda juga dapat mengkloning array:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Objek


Anda dapat melakukan hal yang sama dengan objek:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Anda juga dapat mengganti nilai:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


Hal ini sangat berguna apabila memperbarui objek tanpa mengubah aslinya.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Bagaimana kita bisa sampai ke Node

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


Pada bab ini kita akan mempelajari sedikit konteks sejarah tentang JavaScript dan NodeJS.


Konteks historis sangat penting dalam perangkat lunak, karena kita sering menggunakan alat yang dibuat oleh orang lain, dan karena itu kita dipengaruhi oleh keputusan yang diambil di masa lalu oleh mereka.


Memahami alasan dari keputusan tersebut, dan bagaimana alat yang kita gunakan menjadi seperti sekarang ini, akan membantu kita untuk tidak terlalu bingung dengan apa yang kita lakukan.


### Asal-usul JavaScript


JavaScript dimulai sebagai bahasa sederhana yang dirancang untuk membuat halaman web menjadi interaktif.


Pada tahun 1990-an, peramban web seperti Netscape Navigator menambahkan JavaScript sehingga pengembang dapat menulis kode yang berjalan langsung di peramban.


Ide awalnya adalah menggunakan Java sebagai bahasa inti untuk membuat situs web (dengan apa yang disebut "applet Java"), dan JavaScript hanya untuk hal-hal kecil.


Desain inti dikerjakan oleh Brendan Eich, yang pada saat itu adalah seorang karyawan di Netscape, dalam waktu kurang dari 2 minggu.


Tetapi kebanyakan orang lebih suka menggunakan JavaScript daripada Java, dan juga applet Java memiliki beberapa masalah keamanan pada saat itu, sehingga akhirnya Java tidak lagi menjadi pilihan dan JavaScript menjadi standar de facto untuk pengembangan web.


### Mesin V8


JavaScript adalah bahasa yang diinterpretasikan, berbeda dengan bahasa yang dikompilasi seperti C.


Kode yang ditulis dalam bahasa yang dikompilasi akan diubah menjadi biner, dan biner tersebut diumpankan langsung ke CPU komputer.


![](assets/en/6.webp)


Di sisi lain, bahasa Interpred cenderung lebih ramah pengguna, dan lebih dekat dengan cara berpikir manusia ("tingkat tinggi") daripada cara kerja mesin ("tingkat rendah"); sehingga mereka biasanya memiliki mesin virtual yang dibangun untuk menjalankan kode mereka.


Mesin virtual adalah program khusus yang berada di antara kode yang Anda tulis dan CPU, dan mengeksekusi kode Anda (karena CPU tidak dapat memahaminya).


Hal ini memungkinkan Anda untuk memprogram tanpa mengetahui terlalu banyak tentang mesin yang mendasarinya, tetapi juga memiliki biaya dalam hal kinerja, karena komputer tidak hanya menjalankan program Anda; komputer menjalankan program (mesin virtual) yang menjalankan program Anda.


Ketika aplikasi web menjadi semakin kompleks, ada permintaan untuk meningkatkan kinerja JavaScript. Mesin V8 adalah penerjemah yang mendukung JavaScript di Google Chrome. Mesin ini dikembangkan di Google dan dirilis pada tahun 2008.


Sementara mesin JavaScript yang lebih tua sebagian besar merupakan mesin virtual tradisional, mesin V8 adalah kompiler JIT (just-in-time).


Kode JavaScript diumpankan ke mesin V8, dan mesin mencoba mengkompilasi bagian-bagiannya sebagai binari asli dengan cepat. Hal ini memungkinkan Anda untuk mendapatkan pengalaman bahasa tingkat tinggi, dengan kinerja yang sedikit lebih dekat dengan bahasa tingkat rendah. Hal ini menjadikan JavaScript sebagai bahasa tingkat tinggi tercepat di dunia, sedikit "terbaik dari kedua dunia".


### Waktu berjalan NodeJS


Meskipun mudah digunakan dan cukup cepat untuk dieksekusi, setelah rilis V8 JavaScript tetap memiliki keterbatasan yang besar: JavaScript hanya dapat berjalan di dalam browser.


Mengapa hal itu menjadi masalah?


Nah, karena peramban mengeksekusi kode yang diambil dari jutaan sumber berbeda di internet, peramban dapat dengan mudah masuk ke dalam malware, sehingga mereka "di-sandbox" dari sistem operasi lainnya.


![](assets/en/7.webp)


JavaScript tidak dapat mengakses sistem file dan sumber daya lokal lainnya di komputer Anda (setidaknya tidak semudah bahasa lain), jadi ini merupakan batasan yang signifikan pada jenis aplikasi yang dapat Anda buat dengan JavaScript.


Pada tahun 2009, Ryan Dahl menerbitkan NodeJS, yang merupakan sebuah runtime yang memungkinkan Anda untuk menggunakan mesin V8 di luar peramban, langsung pada sistem operasi asli komputer Anda. NodeJS juga menambahkan banyak fitur yang berguna untuk menulis program sisi server dan baris perintah. Sebagai contoh, Anda bisa menggunakan NodeJS untuk membuat server web, membaca dan menulis berkas, atau membuat alat yang mengotomatiskan tugas.


![](assets/en/8.webp)


Dalam kursus ini, kita telah menjelajahi fitur-fitur JavaScript yang ada di peramban dan NodeJS. Fitur-fitur tersebut memungkinkan kita untuk mendefinisikan data dan memanipulasinya dengan cara yang abstrak. Dalam beberapa pelajaran berikutnya, kita akan menjelajahi fitur-fitur yang spesifik untuk NodeJS dan memungkinkan kita untuk berinteraksi dengan sistem operasi.


## Argumen baris perintah

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS memungkinkan kita, antara lain, untuk membangun CLI (Command Line Interfaces).


Untuk itu kita membutuhkan cara untuk menerima argumen baris perintah, yang di Node dilakukan dengan menggunakan objek `process` bawaan.


### `proses`


NodeJS menyediakan objek khusus yang disebut `process` yang merepresentasikan program yang sedang berjalan.


Anda dapat menggunakannya untuk memeriksa lingkungan, direktori kerja saat ini, dan bahkan keluar dari program bila diperlukan.


Sebagai contoh:


```javascript
console.log(process.platform)
```


Ini mencetak platform sistem operasi, seperti `win32`, `linux`, atau `darwin` (Mac).


### `process.argv`


Ketika Anda menjalankan program NodeJS dari terminal, Anda dapat memasukkan kata-kata tambahan (argumen) setelah nama skrip. Argumen-argumen ini disimpan di dalam `process.argv`.


Misalnya, jika Anda menjalankan perintah ini:


```
node my_script.js alpha beta
```


Anda dapat mencetak argumen seperti ini:


```javascript
console.log(process.argv)
```


Keluarannya mungkin terlihat seperti ini:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


Dua item pertama selalu merupakan jalur Node dan jalur skrip Anda. Kata-kata tambahan yang Anda masukkan ke skrip akan muncul setelah itu.


Larik `process.argv` dapat dipotong seperti larik lainnya menggunakan metode `.slice()`, jadi untuk mendapatkan argumen yang dilewatkan saja Anda dapat melakukan


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Memiliki akses ke argumen yang diberikan pengguna merupakan hal mendasar untuk mengembangkan aplikasi baris perintah.


## Modul

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


Runtime JavaScript seperti NodeJS biasanya memperlakukan setiap berkas JavaScript sebagai modul terpisah.


Bayangkan sebuah modul sebagai sebuah kotak. Kotak memiliki ruang privatnya sendiri, sehingga variabel dan fungsi yang Anda deklarasikan di dalamnya tidak akan mengganggu kode di kotak lain. Pada dasarnya, setiap modul memiliki ruang lingkupnya sendiri.


Sebuah modul dapat mengekspor beberapa kontennya, membuatnya tersedia untuk modul lain, dan dapat mengimpor konten yang telah diekspor oleh modul lain. JavaScript memungkinkan Anda mengekspor dan mengimpor konten antar modul, untuk menghubungkan file yang berbeda.


Program JavaScript sering kali terdiri dari beberapa modul yang saling terhubung satu sama lain.


Mengapa menggunakan modul? Dengan membagi kode Anda menjadi beberapa modul, Anda dapat mengatur program Anda menjadi bagian-bagian yang lebih kecil, lebih jelas, dan dapat digunakan kembali. Setiap modul dapat fokus pada satu jenis tugas, seperti menangani perhitungan matematika, bekerja dengan file, atau memformat teks.


### Modul-modul CommonJS


Di NodeJS, sistem yang paling umum untuk mengelola modul disebut **CommonJS**.


Dalam sistem ini, Anda dapat membagikan (mengekspor) kode dari modul menggunakan `module.exports` dan memuat (mengimpor) kode tersebut ke dalam file lain menggunakan `require()`.


Untuk membuat sesuatu tersedia di luar modul, Anda menetapkannya ke `module.exports`:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


Di sini, string `"Halo!"` adalah apa yang diekspor oleh modul ini.


Untuk menggunakan kode yang diekspor dari file lain, Anda menggunakan fungsi `require()` dengan path ke file tersebut:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Cetakan ini:


```
Hello!
```


Anda dapat mengekspor beberapa hal dengan menggabungkannya dalam sebuah objek anonim, seperti


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS adalah sistem modul yang pada awalnya diadopsi oleh NodeJS. Belakangan modul ES juga ditambahkan.


### Modul ES


NodeJS juga mendukung jenis modul lain yang disebut **ES Modules**, yang populer dalam pengembangan web. Modul ini menggunakan kata kunci `export` dan `import`.


Modul ES dikembangkan untuk peramban dan baru kemudian ditambahkan ke Node. Jika Anda ingin menggunakannya, Anda mungkin harus menggunakan `.mjs` sebagai ekstensi file, bukan `.js`, tergantung versi Node yang Anda gunakan.


Dalam satu file bernama `greeting.mjs` kita menulis


```javascript
export const greeting = "Hello!"
```

Seperti yang Anda lihat, kita mengekspor konstanta secara langsung ke tempat konstanta tersebut didefinisikan


Di file lain bernama `index.mjs`, kita mengimpornya:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


Anda dapat mengekspor deklarasi yang berbeda di berbagai bagian file, seperti


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### Perpustakaan standar NodeJS


NodeJS juga menyertakan banyak modul bawaan. Ini adalah modul siap pakai yang disediakan oleh NodeJS yang membantu tugas-tugas umum seperti membaca berkas, bekerja dengan sistem operasi, atau menyambung ke jaringan.


Sebagai contoh, modul `os` memberikan informasi tentang sistem operasi Anda:


```javascript
const os = require("os")

console.log(os.platform())
```


Anda tidak perlu menginstal modul-modul bawaan ini, modul-modul ini sudah disertakan dengan NodeJS. Modul-modul ini membentuk "pustaka standar" dari runtime, dan digunakan oleh sebagian besar aplikasi Node untuk melakukan hal-hal seperti membaca file atau berkomunikasi melalui internet.


Bab-bab berikutnya akan menunjukkan kepada Anda beberapa contoh penggunaannya yang berguna.


## Modul `fs`

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


Modul `fs` (kependekan dari **file system**) adalah bagian dari pustaka standar NodeJS. Modul ini memungkinkan Anda untuk bekerja dengan berkas dan direktori di komputer Anda: Anda dapat membaca berkas, menulis berkas, menghapus berkas, mengganti nama berkas, dan banyak lagi.


Untuk menggunakannya, pertama-tama Anda harus mengimpornya di bagian atas file Anda:


```javascript
const fs = require("fs")
```


### Sinkronisasi API


Cara paling sederhana untuk menggunakan `fs` adalah dengan metode **sync**.


Metode ini memblokir program hingga selesai (sehingga baris kode berikutnya tidak akan berjalan hingga operasi selesai).


Berikut ini contoh pembacaan file secara sinkron:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Jika ada file bernama `example.txt` di direktori yang sama dengan skrip Anda, ini akan mencetak isinya.


Anda juga dapat menulis ke file secara sinkron:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Ini membuat (atau menimpa) file bernama `output.txt` dengan teks.


Berikut adalah beberapa operasi umum yang dapat Anda lakukan dengan API ini:


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


Sync API sederhana dan bagus untuk skrip kecil, tetapi karena memblokir program hingga selesai, ini bisa memperlambat jika Anda bekerja dengan file besar atau server.


### API asinkronisasi panggilan balik


API pemanggilan kembali (callback API) tidak memblokir: API ini memungkinkan NodeJS untuk terus melakukan hal-hal lain ketika operasi berkas terjadi.


Alih-alih mengembalikan hasilnya secara langsung, dibutuhkan sebuah fungsi (**callback**) yang akan dipanggil ketika operasi selesai.


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


Inilah yang terjadi:



- `fs.readFile` mulai membaca `example.txt`.
- NodeJS tidak menunggu, melainkan melanjutkan untuk mengeksekusi kode lain yang mungkin telah Anda tulis.
- Ketika file selesai dibaca, pemanggilan kembali akan berjalan:



  - Jika terjadi kesalahan, `err` berisi kesalahan.
  - Jika tidak, `data` berisi konten.


Berikut ini cara Anda menulis ke file:


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


Ide yang sama: program tidak berhenti saat menulis file.


Beberapa contoh hal yang dapat Anda lakukan dengan API ini:


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


API pemanggilan kembali lebih baik untuk server dan tugas-tugas besar karena tidak memblokir program, tetapi pemanggilan kembali bersarang dapat berantakan jika Anda merantai banyak operasi. Itulah sebabnya API asinkronisasi berbasis janji ditambahkan.


### API asinkronisasi yang dijanjikan


API berbasis Promise modern dan bekerja dengan baik dengan `.then()` dan `async/wait`. API ini tersedia sebagai `fs.promises`.


Anda perlu mengimpor properti `janji`:


```javascript
const fs = require("fs").promises
```


Menggunakan `.then()`:


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


Atau bahkan lebih baik lagi, dengan menggunakan `async/wait`:


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


Menulis ke file:


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


Daftar contoh yang biasa untuk API:


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


Ketika Anda menulis kode, Anda akan sering perlu menggunakan kode yang ditulis oleh orang lain; misalnya, pustaka untuk membantu Anda bekerja dengan tanggal, warna, server, atau hampir semua hal lainnya.


Daripada mengunduh dan menyalin file secara manual, Anda dapat menggunakan **pengelola paket**.


Manajer paket adalah alat yang:



- paket unduhan
- melacak paket mana yang dibutuhkan proyek Anda
- memastikan semua orang di tim Anda memiliki versi paket yang sama


### Apa itu NPM


Di dunia NodeJS, manajer paket yang paling populer adalah **NPM**, yang merupakan singkatan dari *Node Package Manager*.


Anda mendapatkan NPM secara otomatis ketika Anda menginstal NodeJS.


Anda dapat memeriksa apakah Anda memiliki NPM dengan menjalankan ini di terminal Anda:


```
npm -v
```


Ini mencetak versi NPM yang Anda miliki, seperti:


```
10.2.1
```


### Membuat paket


Di NodeJS, **paket** hanyalah sebuah direktori dengan berkas `paket.json` di dalamnya.


Mari kita buat satu langkah demi langkah.


1. Buat folder baru untuk proyek Anda:


```
mkdir my_project
cd my_project
```


2. Jalankan perintah ini:


```
npm init
```


Ini akan memulai penyiapan interaktif, menanyakan pertanyaan seperti nama proyek Anda, versi, deskripsi, dll.


Jika Anda tidak ingin menjawab semuanya dan hanya menerima default, Anda dapat menggunakan:


```
npm init -y
```


Setelah menjalankannya, Anda akan melihat file baru di folder Anda yang bernama:


```
package.json
```


### `package.json`


File `package.json` hanyalah file JSON yang menyimpan metadata tentang proyek Anda.


Berikut ini sebuah contoh:


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


Beberapa bidang yang penting:



- `nama`: nama paket Anda
- `versi`: versi saat ini
- `main`: berkas titik masuk (seperti `index.js`)
- `scripts`: perintah yang dapat Anda jalankan (seperti `npm start`)
- `dependencies`: daftar semua paket yang bergantung pada proyek Anda


### Menginstal paket


Katakanlah Anda ingin menggunakan paket tertentu yang disebut `picocolors` untuk menambahkan warna pada output terminal Anda.


Anda dapat menginstalnya dengan menjalankannya:


```
npm install picocolors
```


Anda sekarang dapat menggunakannya dalam proyek Anda. Buatlah berkas `index.js` dengan


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


dan coba jalankan. Terminal akan mencetak versi teks berwarna.


Apa yang dilakukan NPM?



- Ia mengunduh paket dan menyimpannya dalam subfolder bernama `node_modules/`
- menambahkan entri di bawah `dependencies` di `package.json` Anda
- memperbarui file `package-lock.json`


Apa yang dimaksud dengan `package-lock.json`?


### `paket-kunci.json`


File ini secara otomatis dibuat oleh NPM.


Anda mungkin bertanya-tanya, jika kita sudah memiliki `package.json`, mengapa kita membutuhkan file lain?

Inilah alasannya:



- `paket.json` hanya menyatakan versi **range** paket yang dibutuhkan proyek Anda.

Contoh:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


`^1.1.0` berarti "versi apa pun yang kompatibel dengan 1.1.x", jadi ini fleksibel.



- `package-lock.json` **membekukan** versi yang tepat dari setiap paket dan sub-ketergantungannya, sehingga setiap orang yang menginstal proyek Anda akan mendapatkan penyiapan kerja yang sama persis.


Mengapa ini penting?


Jika Anda bekerja dalam sebuah tim, atau Anda menerapkan proyek Anda ke server, atau Anda kembali lagi di masa mendatang, Anda ingin memastikan bahwa proyek tersebut masih bekerja dengan cara yang sama.

Jika paket-paket telah diperbarui dan Anda menginstal ulang tanpa file kunci, Anda mungkin akan mendapatkan versi yang sedikit berbeda yang berperilaku berbeda.


Dengan menyimpan `package-lock.json` di dalam proyek Anda, NPM akan selalu menginstal versi yang sama persis dengan yang tercantum di sana, memastikan bahwa setiap orang memiliki lingkungan yang sama.


`package-lock.json` mengunci semuanya ke versi yang sangat spesifik, untuk membuat proyek lebih mudah direproduksi di mesin lain.


Tetapi jika paket Anda perlu digunakan oleh banyak orang, Anda dapat memilih untuk tidak melakukan komit, sehingga NPM hanya menemukan berkas `package.json` dan diizinkan untuk menginstal secara otomatis versi terbaru yang diizinkan dalam berkas tersebut.


Namun, ini adalah hal-hal yang harus Anda khawatirkan nanti, setelah Anda mulai mempublikasikan kode Anda sendiri. Untuk saat ini, kami memperkenalkan dasar-dasar NPM hanya untuk memungkinkan Anda menemukan dan menggunakan pustaka yang diterbitkan oleh pengembang lain dalam proyek Anda.



## Jaringan di NodeJS

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS sering digunakan sebagai bahasa untuk backend: Anda dapat mengubah skrip Anda menjadi server, dan juga menggunakannya untuk membuat permintaan ke server lain.


Pada bab ini kami akan memperkenalkan beberapa fitur jaringan dasar yang memungkinkan Anda untuk melakukannya.


### `fetch()`


Jika Anda ingin program Anda mengunduh data dari situs web atau API, Anda perlu membuat **permintaan HTTP**.


Pada versi modern NodeJS, Anda dapat menggunakan fungsi `fetch()` bawaan.


Berikut ini contoh membuat permintaan GET ke API:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Ketika Anda menjalankannya, Anda akan melihat sesuatu seperti:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


Inilah yang terjadi:


1. `fetch()` mengambil sebuah URL dan membuat permintaan.

2. Ini mengembalikan **Promise** yang diselesaikan ke objek `Response`.

3. `response.text()` membaca badan respons sebagai sebuah string.


Tetapi string yang Anda dapatkan kembali sebenarnya adalah JSON. Apa itu?


### JSON


Ketika bekerja dengan API web, data sering dikirim dan diterima sebagai **JSON**, yang merupakan singkatan dari JavaScript Object Notation.


JSON hanyalah sebuah format teks yang sangat mirip dengan objek JavaScript. Sebagai contoh:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


Objek `JSON` adalah utilitas bawaan dalam JavaScript yang dapat digunakan untuk bekerja dengan format data ini.


Anda dapat mengonversi objek JavaScript menjadi string JSON menggunakan `JSON.stringify()`:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Cetakan ini:


```
{"name":"Alice","age":30}
```


Anda juga dapat mengonversi teks JSON kembali menjadi objek JavaScript menggunakan `JSON.parse()`:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Cetakan ini:


```
{ name: 'Bob', age: 25 }
```


Hati-hati: `JSON.parse() ` akan melemparkan kesalahan jika string bukan JSON yang valid.


```javascript
JSON.parse("not json") // ❌ Error!
```


Jadi, pastikan string diformat dengan benar.


### server `http`


NodeJS memungkinkan Anda untuk membuat server web tanpa menginstal apa pun.


Anda dapat menggunakan modul `http` bawaan untuk menangani permintaan dari klien dan mengirimkan respons balik.


Berikut ini adalah contoh yang sangat mendasar:


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


Ketika Anda menjalankan skrip ini dan membuka `http://localhost:3000` di browser Anda, Anda akan melihatnya:


```
Hello from NodeJS server!
```


Inilah yang terjadi di dalam kode:


1. Anda mengimpor server `http` dari pustaka standar Node.

2. `http.createServer()` membuat server. Anda mengoper ke `http.createServer()` sebuah pemanggilan balik `(req, res) => {...}` untuk dieksekusi setiap kali ada orang yang terhubung.

3. Anda telah menetapkan kode status 200 (yang mengindikasikan operasi yang berhasil) pada respons. Anda dapat membaca tentang kode status http [di sini](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

3. `res.end()` mengirimkan respons dan mengakhiri koneksi.

4. `server.listen(3000)` memulai server pada port 3000.


Anda juga dapat memeriksa `req.url` dan `req.method` dalam permintaan untuk menangani jalur atau jenis permintaan yang berbeda.


Contoh dengan perutean:


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


Ini adalah contoh yang sangat mendasar. Untuk membangun server yang lebih canggih, sebagian besar pengembang mungkin akan mengunduh pustaka backend yang sudah jadi seperti [express] (https://www.npmjs.com/package/express).


## Memproses data: buffer, peristiwa, aliran

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


Dalam bab ini, kami akan memperkenalkan terutama tiga kelas objek:



- `Buffer`, yang mewakili potongan kecil data biner
- `EventEmitter`, yang dapat digunakan untuk melacak suatu langkah melalui proses asinkron dengan memancarkan sinyal yang disebut "peristiwa"
- `Stream`, yang memungkinkan kita untuk memproses sebagian besar data satu `Buffer` pada satu waktu, dan yang melacak proses dengan memancarkan peristiwa


Hal ini sangat umum dalam kode NodeJS profesional, jadi meskipun Anda mungkin tidak menggunakannya dalam proyek pertama Anda, ada baiknya untuk mendapatkan pemahaman dasar ketika Anda perlu berinteraksi dengan mereka


### Penyangga


Di NodeJS, **buffer** adalah jenis objek yang digunakan untuk bekerja dengan data biner.


Anda dapat menganggap buffer sebagai wadah ukuran tetap untuk byte mentah.


Berikut ini cara membuat buffer dari string:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


Ini mencetak sesuatu seperti:


```
<Buffer 68 65 6c 6c 6f>
```


Angka-angka tersebut (`68`, `65`, `6c`, dst.) adalah representasi heksadesimal dari huruf-huruf pada `"halo".


Anda dapat mengonversinya kembali ke string seperti ini:


```javascript
console.log(buf.toString())
```


Cetakan ini:


```
hello
```


Anda juga dapat membuat buffer dengan ukuran tertentu yang diisi dengan angka nol:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


Ini mencetak sesuatu seperti:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


Anda dapat menulis ke dalam buffer:


```javascript
buf.write("abc")
console.log(buf)
```


Dan Anda dapat mengakses setiap byte:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Buffer sangat berguna ketika Anda perlu memanipulasi data pada tingkat yang sangat rendah.


### Acara


Dalam JavaScript, sebuah **event** adalah sesuatu yang terjadi dalam program Anda yang dapat Anda tanggapi.


Sebagai contoh:



- file selesai dimuat
- pengatur waktu berbunyi
- pengguna mengklik sebuah tombol
- permintaan jaringan mengembalikan data


Sebuah **event** hanyalah sebuah sinyal bahwa sesuatu telah terjadi, dan Anda dapat menulis kode untuk mendengarkan peristiwa tersebut dan bereaksi terhadapnya.


Di NodeJS, banyak objek yang dapat memancarkan event. Objek-objek ini disebut **EventEmiters**.


Berikut ini sebuah contoh:


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


Cetakan ini:


```
Hello! An event happened.
```


Ini dia:


1. Kita membuat objek `EventEmitter`.

2. Kita memerintahkannya untuk menjalankan pemanggilan balik setiap kali peristiwa `"greet"` terjadi, dengan menggunakan `.on("greet")`.

3. Kemudian, kita memicu event `"greet" menggunakan `.emit()`.

4. Panggilan balik kami dieksekusi


Anda dapat meneruskan data bersama dengan acara tersebut:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Cetakan ini:


```
Hello, Alice!
```


Anda juga dapat mendaftarkan pendengar untuk acara lainnya:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Anda dapat melampirkan sebanyak mungkin pendengar ke suatu jenis acara, dan Anda dapat menembakkan berbagai jenis acara dari pemancar yang sama.


Banyak objek di NodeJS yang memancarkan peristiwa untuk memberi tahu seluruh program bahwa ada sesuatu yang terjadi.



### Apa yang dimaksud dengan aliran?


Stream menggabungkan buffer dan peristiwa untuk membantu kita memproses data.


Ketika kita bekerja dengan file, data dari jaringan, atau bahkan teks yang panjang, kita tidak selalu perlu (atau ingin) memuat semuanya ke dalam memori sekaligus. Hal ini akan menjadi lambat, atau bahkan membuat program menjadi macet jika datanya terlalu besar.


Sebagai gantinya, kita dapat memproses data **sedikit demi sedikit**, saat data tersebut tiba atau dibaca, seperti meminum air melalui sedotan alih-alih mencoba meminum seluruh gelas sekaligus. Ini disebut **aliran**.


Di NodeJS, stream adalah objek yang memungkinkan Anda membaca data dari sumber atau menulis data ke tujuan **satu per satu**.


NodeJS memiliki empat jenis aliran utama:



- Dapat dibaca**: aliran yang dapat Anda baca datanya (seperti membaca file)
- Dapat Ditulis**: stream yang dapat Anda tulis datanya (seperti menulis ke file)
- Duplex**: aliran yang dapat dibaca dan ditulis
- Transform**: seperti aliran dupleks, tetapi dapat mengubah (mentransformasikan) data saat mengalir


### Aliran yang dapat dibaca


Katakanlah Anda memiliki `bigfile.txt` untuk diproses. Anda dapat membuat aliran yang dapat dibaca dengan modul `fs` untuk membaca file sepotong demi sepotong.


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


Apa yang terjadi di sini?


1. `fs.createReadStream()` membuat stream yang dapat dibaca.

2. Setiap kali sebuah bagian dari file siap, stream memancarkan peristiwa `data` dan memberi kita sebuah "potongan" data (sebuah `Buffer`). Kami mencetak potongan tersebut.

3. Ketika seluruh file telah dibaca, peristiwa `end` dipicu.

4. Jika ada kesalahan (seperti file tidak ada), peristiwa `error` akan dipicu.


Dengan cara ini, Anda dapat membaca file berukuran besar tanpa memuat semuanya ke dalam memori sekaligus.


Jika kita ingin data tiba dalam bentuk yang dapat dibaca manusia (bukan biner), kita dapat menentukan pengkodean aliran:


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


Kode sekarang akan mencetak file dalam bentuk yang dapat dibaca manusia.


### Aliran yang dapat ditulis


Stream yang dapat ditulis memungkinkan Anda mengirim data ke suatu tempat, potongan demi potongan.


Berikut ini contoh penulisan ke file `target.txt` menggunakan stream:


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


Inilah yang terjadi:


1. `fs.createWriteStream()` membuat sebuah stream yang dapat ditulis.

2. Kita menulis beberapa teks ke dalamnya dengan menggunakan `.write()`.

3. Setelah selesai, kita panggil `.end()` untuk menutup stream.

4. Ketika semua data telah ditulis, peristiwa `finish` dipancarkan.

5. Jika terjadi kesalahan, peristiwa `error` akan dipicu.


Sama seperti stream yang dapat dibaca, stream yang dapat ditulis bagus untuk data besar karena tidak perlu menyimpan semuanya dalam memori sekaligus.


### Aliran perpipaan


Salah satu hal yang paling keren tentang stream adalah Anda dapat menyambungkannya: hubungkan stream yang dapat dibaca secara langsung ke stream yang dapat ditulis.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


Ini:



- Aliran yang dapat dibaca dibaca dari `bigfile.txt`.
- Aliran yang dapat ditulis menulis ke `copy.txt`.
- `.pipe()` mengirimkan data secara langsung dari aliran yang dapat dibaca ke aliran yang dapat ditulis.


### Aliran dupleks


Aliran dupleks dapat dibaca dan ditulis. Salah satu contohnya adalah soket jaringan: Anda dapat mengirim data ke soket tersebut dan menerima data darinya.


Berikut adalah contoh yang sangat sederhana dengan menggunakan modul `net`:


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


Dalam contoh ini:



- Objek `socket` adalah aliran dupleks.
- Anda dapat `menulis()` padanya dan juga mendengarkan peristiwa `data` darinya.


### Mengubah aliran


Aliran transformasi adalah aliran dupleks yang juga memodifikasi data yang melewatinya.


Sebagai contoh, Anda dapat menggunakan modul `zlib` bawaan untuk mengompresi atau mendekompresi data.


Berikut ini cara mengompres file menggunakan stream transform:


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


Dan untuk mendekompresnya kembali:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


Transform stream sangat berguna untuk tugas-tugas seperti kompresi, enkripsi, atau mengubah format file saat streaming.


### Tekanan balik


Kadang-kadang aliran yang dapat ditulis lambat dalam menangani data. Jika kita terus mendorong data ke writeable lebih cepat daripada yang dapat ditangani, kita mungkin mengalami masalah. Ini disebut **tekanan balik**.


Jika Anda memanggil metode `.write()` pada stream yang dapat ditulis, metode ini akan mengembalikan sebuah boolean yang menginformasikan kepada Anda jika stream tersebut membutuhkan jeda; Anda mungkin harus memeriksa nilai kembalinya, seperti ini:


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


Ini adalah contoh ilustrasi dari pemipaan data secara manual dari Readable ke Writable, dan mengelola tekanan balik secara manual.


Biasanya kita akan menyalurkan data menggunakan metode `.pipe()`, yang menangani tekanan balik secara otomatis.


Jadi, Anda hanya perlu khawatir tentang tekanan balik ketika karena suatu alasan Anda memanggil `.write()` secara manual.


## Catatan akhir

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


Jadi, itu saja, jika Anda mengikuti pelajaran ini, Anda seharusnya sudah bisa menulis beberapa program sederhana di NodeJS.


Saya menyarankan untuk melakukan hal tersebut: setelah mempelajari dasar-dasarnya, membangun beberapa proyek pribadi adalah cara terbaik untuk berlatih dan menjadi programmer yang lebih baik.


Tidak masalah apa yang Anda buat, yang penting adalah Anda menantang diri sendiri untuk memecahkan masalah dengan kode.


Bahasa pemrograman modern sangat kuat, dan NodeJS mungkin merupakan toolbox terbaik untuk bereksperimen dalam fase perjalanan Anda.


Semoga berhasil!


# Bagian akhir


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Ulasan & Peringkat


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Kesimpulan


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>