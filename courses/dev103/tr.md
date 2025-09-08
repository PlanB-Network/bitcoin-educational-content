---
name: JavaScript ve NodeJS Temelleri
goal: Pratik uygulamalar ve araçlar oluşturmak için JavaScript programlama temellerini ve NodeJS geliştirmeyi öğrenin.
objectives: 

  - Temel JavaScript sözdizimi, türleri ve kontrol akışında uzmanlaşma
  - JavaScript'te fonksiyonları, nesneleri ve sınıfları anlama
  - Hata işleme ve hata ayıklama tekniklerini öğrenin
  - NodeJS ve ekosistemi ile tanışın

---

# Gelişim yolculuğunuza başlayın


JavaScript ve NodeJS hakkındaki bu kursa hoş geldiniz.


JavaScript dünyadaki en popüler programlama dilidir: modern tarayıcıların komut dosyası dilidir, bu nedenle *biraz* JavaScript yazmadan modern bir web uygulaması oluşturmak temelde imkansızdır; ve NodeJS çalışma zamanı ile doğrudan bilgisayarınızda çalışan komut dosyaları ve uygulamalar oluşturmak için tarayıcıların dışında da kullanılabilir.


Bu eğitim, programlamaya tamamen yeni başlayan veya daha önce başka diller kullanmış ancak JavaScript'in özellikle NodeJS bağlamında nasıl çalıştığını anlamak isteyen kişiler için tasarlanmıştır.


Eğitimin sonunda JavaScript'te kendi programlarınızı yazabilmeli, NodeJS standart kütüphanesini kullanabilmeli ve kullanışlı araçlar oluşturmak için üçüncü taraf paketleri yükleyip kullanabilmelisiniz.


+++
# Temel JavaScript

<partId>a617327c-e5a2-52ca-9380-c63f44623dd4</partId>


## Kurulum

<chapterId>ba05a290-1782-5268-87c9-62fd09590e05</chapterId>


Bu bölümde ilk JavaScript programımızı yazmak ve çalıştırmak için makinemizi kuracağız.


Bir JavaScript programı, bir JavaScript çalışma zamanı tarafından yürütülecek komutları içeren (bir veya daha fazla) metin dosyasının bir koleksiyonudur.


Bu metin dosyalarının adları genellikle `.js` dosya uzantısı ile biter, örneğin `my_script.js`, `my_program.js` vb.


İçerdikleri komutlar JavaScript programlama dilinde yazılmıştır.


JavaScript çalışma zamanı, bu dosyaları çalıştıran özel bir programdır.


![](assets/en/1.webp)


### NodeJS kurulumu


En yaygın JavaScript çalışma zamanı NodeJS'dir.


Resmi talimatları] (https://nodejs.org/en/download) takip ederek yükleyebilirsiniz.


İndirme sayfası size üç büyük OS (İşletim Sistemi) için de talimatlar sağlayacaktır: Windows, Linux ve MacOS. İşletim sisteminizde bir terminali nasıl açacağınızı bildiğinizi varsayar.


NodeJS her üç işletim sistemi için de kullanılabilir olduğundan, yazdığınız programlar hepsinde çalıştırılabilecektir (bazı uç durumlar hariç).


Bu, örneğin Windows PC'nizde JavaScript'te basit bir video oyunu yazabileceğiniz ve Mac'inde çalıştırması için arkadaşınıza verebileceğiniz anlamına gelir.


![](assets/en/2.webp)


### Metin düzenleme


Programlamanın en güzel yanlarından biri, işletim sisteminizin varsayılan not defteri de dahil olmak üzere herhangi bir metin düzenleyicisini kullanarak kod yazabilmenizdir.


Kod yazmak için özelleşmiş bazı metin editörleri vardır, bazıları ücretsiz olarak kullanılabilir, diğerleri ise bir lisans için ödeme yapmanızı gerektirir.


Kod editörü seçimi bu kursun kapsamını aşan dev bir tavşan deliğidir, bu yüzden burada bundan bahsetmeyeceğiz. Ne kullanacağınızı bilmiyorsanız, en çok kullanılan ücretsiz editör [VSCode](https://code.visualstudio.com/).


Interface biraz şişirilmiş, ancak ihtiyacınız olan her şeye sahip: bir dosya editörü, bir dosya gezgini (üzerinde çalıştığınız dizindeki dosyaları ve alt dizinleri görselleştirmek için) ve kodunuzu çalıştırmak için bir terminal. Ayrıca birçok eklentiyi destekler ve varsayılan olarak JavaScript sözdizimi vurgulama ile birlikte gelir.


Biraz daha Cypherpunk-y olmak istiyorsanız, bunun yerine [VSCodium](https://vscodium.com/) kullanabilirsiniz.


### İlk program (hello world)


Geleneksel olarak, bir programlama dilini öğrenirken, yazılan ilk program konsola "hello world!" yazdırmaktan ibarettir.


İçinde `main.js` adlı bir dosya bulunan `my_js_code/` adlı bir dizin oluşturun (bu isimler isteğe bağlıdır).


Dizini VSCode ile açın.


Bu kodu dosyanıza yazın:


```javascript
console.log("hello world!")
```


Bir terminal açın ve programı çalıştırmak için bu komutu yürütün:


```
node main.js
```


Sonuç şöyle olmalıdır


```
hello world!
```


### Neler Oldu


JavaScript'te her şey bir "nesne "dir.


konsol`, programda hata ayıklamak için kullanılan bir nesnedir.


`console.log`, `console`un en çok kullanılan yöntemidir. Sadece ona aktardığınız argümanları yazdırır.


Argümanları `console.log` dosyasına `()` yuvarlak parantezlerini kullanarak aktarırsınız.


Örneğin, `1000` sayısını yazdırmak istiyorsanız, sadece şunu yazarsınız


```javascript
console.log(1000)
```


Ardından çalıştırarak çalıştırın


```
node main.js
```


(şu andan itibaren, bu kurs bir programı bu şekilde çalıştırdığınızı bildiğinizi varsayacaktır).


Bu yazdırılmalıdır


```
1000
```


Birden fazla şey geçirebilirsiniz, örneğin


```javascript
console.log(16, 8, 1993)
```


Bu yazdıracaktır


```
16 8 1993
```


## Değişkenler ve yorumlar

<chapterId>23050ab7-343b-5edf-9d37-e4e782e27ce0</chapterId>


Programlar genellikle veriler üzerinde işlem yapar.


Değişkenler, verileri saklamak için kullandığımız adlandırılmış kutular gibidir. Bir veri parçasını belirli bir adla ilişkilendirmemize olanak tanırlar, böylece daha sonra bu adı kullanarak onu geri alabiliriz.


### let` bildirimleri


JavaScript'te bir değişken bildirmek için `let` anahtar sözcüğünü kullanabiliriz.


Let` yazdıktan sonra değişkene vermek istediğimiz ismi, ardından bir `=` işareti ve ardından saklamak istediğimiz değeri yazıyoruz.


Örneğin:


```javascript
let age = 25

console.log(age)
```


Bir değişkenin adı (teknik olarak "tanımlayıcı" olarak adlandırılır) genellikle harf, alt çizgi (`_`), dolar işareti (`$`) ve sayı içerebilir, ancak ilk karakter sayı olamaz.


Yukarıdaki kodda, `age` adında bir değişken tanımladık ve içine `25` değerini kaydettik.


Ardından, `console.log(age)` kullanarak değeri yazdırdık.


Bu kodu `node main.js` ile çalıştırırsanız, çıktı şöyle olacaktır:


```
25
```


Tanımlayıcılar büyük/küçük harfe duyarlıdır, yani küçük ve büyük harfler tanımlayıcılarda farklılık olarak sayılır, bu nedenle örneğin


```javascript
let age = 25

let Age = 20

console.log(age)
```


25 yazdıracaktır, çünkü bunlar tamamen ayrı iki değişken olarak kabul edilir!


Dizeleri (metin) bir değişkende de saklayabilirsiniz:


```javascript
let message = "hello again"

console.log(message)
```


Bu yazdırılacaktır:


```
hello again
```


Tıpkı daha önce olduğu gibi, değişkende saklanan değeri yazdırmak için `console.log()` kullandık.


Şimdi ikisini birlikte yapalım:


```javascript
let age = 25

let message = "hello again"

console.log(age)

console.log(message)
```


Bunu çalıştırmak yazdıracaktır:


```
25
hello again
```

### Yeniden Görevlendirme


Let` ile bildirilen değişkenler oluşturulduktan sonra değiştirilebilir.


Buna yeniden atama denir.


```javascript
let score = 10

console.log(score)

score = 15

console.log(score)
```


Önce `score` değerine `10` atıyoruz, sonra da yazdırıyoruz.


Daha sonra `score` değerini `15` olarak değiştirip tekrar yazdırıyoruz.


Çıktı şu şekilde olacaktır:


```
10
15
```


Bu, skorun arttığı bir oyunda olduğu gibi, değer zaman içinde değiştiğinde çok kullanışlıdır.


Karışıma bir değişken daha ekleyelim:


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


Bu yazdırılacaktır:


```
10
Alice
20
Bob
```


Gördüğünüz gibi, hem `score` hem de `player` değiştirildi.


### `const` bildirimleri


Ancak çoğu zaman, bir değişkenin oluşturulduktan sonra değişmesini istemeyiz. Bunun için `const` kullanırız.


const` "sabit" kelimesinin kısaltmasıdır. Bir `const` değişkenine bir değer atadığınızda, onu değiştiremezsiniz.


```javascript
const pi = 3.14
console.log(pi)
```


Bu baskılar:


```
3.14
```


Ama bunu yapmaya çalışırsan:


```javascript
const pi = 3.14
console.log(pi)

pi = 99 // this line will cause an error
console.log(pi)
```


JavaScript size aşağıdaki gibi bir hata verecektir:


```
TypeError: Assignment to constant variable.
```


Bunun nedeni `pi` değişkeninin `const` kullanılarak bildirilmiş olmasıdır ve bundan sonra değerini değiştiremezsiniz. JavaScript yorumlayıcısına bu değişkenin değişmesini istemediğinizi iletmiş olursunuz.


Bu yararlıdır çünkü yanlışlıkla değiştirme olasılığını azaltır. Programlar binlerce satır kodla çok büyük hale geldiğinde, aynı anda olan her şeye ayak uydurmak imkansızdır (bilgisayarları kullanmamızın ana nedeni budur, beynimizle hesaplayamadığımız karmaşık işlemleri yürütmek için), bu nedenle programı daha deterministik hale getiren bunun gibi kısıtlamalara sahip olmak yararlı olur.


Daha sonra değiştirmek istediğimizden emin olmadığımız sürece, değerlerimizi her zaman `const` olarak bildirmek en iyi uygulama olarak kabul edilir.


### JavaScript'te Yorumlar


Bazen kodumuza çalıştırılmayan notlar yazmak isteriz. Bunlara yorum denir.


Yorumlar program çalışırken program tarafından göz ardı edilir, ancak kendimize veya diğer insanlara bir şeyler açıklamak için kullanışlıdır.


Tek satırlık bir yorum yazmak için `//` kullanın


```javascript
// This is a comment
const x = 10 // This is also a comment
console.log(x)
```


Bu yine de yazdırılacaktır:


```
10
```


Yorumlar sadece insanların okuması için var.


Ayrıca `/*` ve `*/` kullanarak çok satırlı yorumlar da yazabilirsiniz


```javascript
/*
This is a multi-line comment.
It can span several lines.
*/
const y = 20
console.log(y)
```


Bu yazdıracaktır


```
20
```


Ve yorum görmezden gelinecektir.


Yorumları kodunuza küçük ek açıklamalar eklemek için kullanabilirsiniz, böylece ne işe yaradığını ve neden belirli bir şekilde yazıldığını hatırlayabilirsiniz. Ayrıca diğer programcıların anlamasına da yardımcı olabilir.


## Temel türler: sayılar, dizeler, booleanlar

<chapterId>cfdb04f6-21a8-5143-bbf9-7aaae04962f0</chapterId>


JavaScript'te bir "tür", bir değerin ne tür bir veri olduğunu söyler.


Javascript'in birkaç temel türü vardır ve bu bölümde bunlardan bazılarını inceleyeceğiz.


### Sayılar ve aritmetik işlemler


Tanıtacağımız ilk tür `number`dır.


JavaScript'teki sayılar tam sayı (`5` gibi) veya ondalık sayı (`3.14` gibi) olabilir.


Onlarla aritmetik yapabilirsiniz: toplama, çıkarma, çarpma ve bölme.


İşte basit bir örnek:


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


Bu yazdırılacaktır:


```
15
5
50
2
```


İşlem sırasını kontrol etmek için `()` parantezlerini de kullanabilirsiniz:


```javascript
const result = (2 + 3) * 4
console.log(result)
```


Bu baskılar:


```
20
```


Parantezler olmasaydı, `2 + 3 * 4` olurdu, yani:


```javascript
const result = 2 + 3 * 4
console.log(result)
```


Bu yazdırır:


```
14
```


Çünkü normal matematikte çarpma işlemi toplama işleminden önce gerçekleşir.


### Dizeler ve enterpolasyon


Tanıtacağımız ikinci JavaScript türü `string`dir.


Dizeler metin parçalarıdır. Bunları oluşturmak için tek tırnak `'...'` veya çift tırnak `"..."` kullanabilirsiniz.


```javascript
const greeting = "hello"
const name = 'Bob'
console.log(greeting)
console.log(name)
```


Bu baskılar:


```
hello
Bob
```


Dizeleri birleştirmek için `+` operatörünü kullanabilirsiniz:


```javascript
const greeting = "hello"
const space = " "
const name = "Bob"

const fullGreeting = greeting + space + name
console.log(fullGreeting)
```


Bu yazdırılacaktır:


```
hello Bob
```


Ancak dizeleri birleştirmenin **dize enterpolasyonu** adı verilen daha güzel bir yolu vardır. `` `...`` dizesini bildirmek ve dizenin içine `${...}` kullanarak değişkenler yazmak için geri işaretlerini kullanırsınız:


```javascript
const greeting = "hello"
const name = "Bob"

const fullGreeting = `${greeting} ${name}`
console.log(fullGreeting)
```


Bu da yazdırılır:


```
hello Bob
```


Herhangi bir ifadeyi `${...}` içine dahil edebilirsiniz:


```javascript
const age = 30
console.log(`Next year, I will be ${age + 1} years old.`)
```


Bu baskılar:


```
Next year, I will be 31 years old.
```


Enterpolasyon modern JavaScript'te çok yaygındır.


### Booleans, karşılaştırma ve mantık işlemleri


Tanıtacağımız üçüncü tip `boolean`dır. Adını boolean mantığını icat eden matematikçi George Boole'dan almıştır.


Booleanlar basittir: sadece iki olası değer, `true` ve `false`.


Bunları değişkenlerde saklayabilirsiniz:


```javascript
const theSkyIsBlue = true
const thisCourseIsBad = false

console.log(theSkyIsBlue)
console.log(thisCourseIsBad)
```


Bu baskılar:


```
true
false
```


Mantık operatörlerini kullanarak boolean'ları birleştirebilirsiniz:



- `&&` "ve" anlamına gelir ve yalnızca **her iki** değer de `doğru` ise `doğru` döndürür, aksi takdirde `yanlış` döndürür
- ||` "veya" anlamına gelir ve değerlerden **en az biri** "doğru" ise "doğru", aksi takdirde (her ikisi de yanlışsa) "yanlış" döndürür
- !` "değil" anlamına gelir, bir boolean'dan önce uygulanır ve onu tersine çevirir: boolean `true` ise `false` döndürür veya tam tersi.


![](assets/en/3.webp)


Örnekler:


```javascript
const isSunny = true
const isWarm = true

console.log(isSunny && isWarm)  // true
console.log(isSunny || isWarm)  // true
console.log(!isSunny)           // false
```


JavaScript'te `>`, `<`, `===` ve `!==` gibi operatörleri kullanarak değerleri karşılaştırabilirsiniz. Bu karşılaştırmaların sonucu her zaman bir boolean'dır.


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


Javascript'te ayrıca "daha büyük veya eşit" anlamına gelen `>=` ve "daha küçük veya eşit" anlamına gelen `<=` vardır.


Booleans, karşılaştırma ve mantıksal operatörler genellikle programlarda "e-posta geldi VE ihtiyacım olan resmi içeriyor VEYA e-postanın uzunluğu 10000 karakterden uzun" gibi karmaşık koşulları bildirmek için birleştirilir. Daha sonra bunların programın mantığını oluşturmak için gerekli yapı taşları olduğunu göreceksiniz.


## Diziler, null, undefined

<chapterId>7bf18183-5eae-53ed-83d2-b04982145d81</chapterId>


Bu bölümde, JavaScript programlarında çok yaygın olan üç türü daha ele alacağız:



- Diziler**: değer dizileri
- undefined**: "hiçbir şey atanmadı" anlamına gelen özel bir değer
- null**: "kasıtlı olarak boş" anlamına gelen başka bir özel değer


### Diziler ve dizin erişimi


Bir **dizi**, bir listede birden çok değeri tutabilen bir türdür.


Köşeli parantez `[]` kullanarak ve öğeleri virgülle ayırarak bir dizi oluşturursunuz.


İşte basit bir örnek:


```javascript
const numbers = [10, 2, 88]
console.log(numbers)
```


Bu baskılar:


```
[ 10, 2, 88 ]
```


Bir dizide yalnızca sayıları değil, her şeyi saklayabilirsiniz:


```javascript
const things = ["apple", 42, true]
console.log(things)
```


Bu baskılar:


```
[ 'apple', 42, true ]
```


Dizideki belirli bir öğeye erişmek için bir **index** kullanırız. İndeks, **0**'dan başlayarak öğenin konumudur.


Yani bu dizide:


```javascript
const colors = ["red", "green", "blue"]
```



- renk[0]`, `"kırmızı"`dır
- `colors[1]`, `"Green"`dir
- renk[2]`, `"mavi"`dir


Hadi deneyelim:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[0])
console.log(colors[1])
console.log(colors[2])
```


Bu yazdırılacaktır:


```
red
green
blue
```


Bir dizinin belirli bir indeksine değer atayabilirsiniz


```javascript
const colors = ["red", "green", "blue"]

colors[1] = "yellow"

console.log(colors)
```


Bu yazdırılacaktır:


```
[ 'red', 'yellow', 'blue' ]
```


Herhangi bir doğal sayıyı indeks olarak kullanabilirsiniz, hatta bir değişkende saklanan bir sayıyı bile


```javascript

const i = 1
const colors = ["red", "green", "blue"]
console.log(colors[i])
```


Bu yazdırılacaktır:


```
green
```


Ancak var olmayan bir dizine erişmeye çalışırsanız, `undefined' alırsınız:


```javascript
const colors = ["red", "green", "blue"]
console.log(colors[3])
```


Bu baskılar:


```
undefined
```


O da ne?


### `undefined`


Özel değer `tanımlanmamış`, "değer atanmamış" anlamına gelir.


Bir değişken oluşturur ancak ona bir değer vermezseniz, değişken `tanımlanmamış` olacaktır:


```javascript
const name
console.log(name)
```


Bu baskılar:


```
undefined
```


Name`e herhangi bir şey atamadığımız için, JavaScript varsayılan olarak onu `undefined` olarak ayarlar.


Daha önce görüldüğü gibi, var olmayan bir dizi dizinine eriştiğinizde de `undefined' alabilirsiniz:


```javascript
const fruits = ["banana", "apple"]
console.log(fruits[2]) // There is no index 2
```


Bu baskılar:


```
undefined
```


### null` ve ona nasıl davranılacağı


null` da özel bir değerdir. "Burada hiçbir şey yok ve ben bunu bilerek yaptım" anlamına gelir


Otomatik olan `undefined`ın aksine, `null` sizin ayarladığınız bir şeydir.


Örneğin:


```javascript
const currentUser = null
console.log(currentUser)
```


Bu baskılar:


```
null
```


Neden `null` kullanılıyor? Belki daha sonra bir değer bekliyorsunuz, ancak henüz hazır değil:


```javascript
let winner = null

// Later in the program:
winner = "Alice"

console.log(winner)
```


Bu baskılar:


```
Alice
```


Bu nedenle `null`, örneğin "Burada daha sonra bir şey olmalı, ancak şu anda boş" demek istediğinizde kullanışlıdır


## Bloklar ve kontrol akışı

<chapterId>be985168-2636-5b0d-a48f-ac1bbfbff8a7</chapterId>


Şimdiye kadar çoğunlukla birbiri ardına çalışan kod satırları yazdık.


Ancak kod yazdığımızda, bunun yürütülme sırasını kontrol edebiliriz.


Buna **kontrol akışı** denir.


Blokları ve kapsamı anlamakla başlayalım.


### Küresel kapsam


Bildirdiğimiz her değişken bir **kapsam** içinde bulunur, bu da değişkenin bilindiği kod bölgesi anlamına gelir.


Bir değişkeni herhangi bir bloğun dışında bildirirseniz, **global kapsam** içinde var olur.


```javascript
const color = "blue"
console.log(color)
```


Bu `color` değişkeni global kapsamdadır, bu nedenle dosyanın herhangi bir yerinden erişilebilir.


Daha fazla satır eklerseniz:


```javascript
const color = "blue"
console.log(color)

const size = "large"
console.log(color)
console.log(size)
```


Hem `color` hem de `size` global değişkenlerdir. Dosyanın her yerinde kullanılabilirler.


Peki bir bloğun içinde ne olur?


### Bloklar ve yerel kapsam


Bir **block**, `{}` küme parantezleriyle çevrili bir kod parçasıdır.


Bir blok içinde `let` veya `const` ile bildirilen değişkenler **sadece** o blok içinde var olur.


```javascript
{
const message = "inside block"
console.log(message)
}
```


Bu baskılar:


```
inside block
```


Ama bunu denersen:


```javascript
{
const message = "inside block"
}
console.log(message) // Error!
```


JavaScript size aşağıdaki gibi bir hata verecektir:


```
ReferenceError: message is not defined
```


Bunun nedeni `message'ın blok içinde bildirilmiş olması ve blok dışında var olmamasıdır.


Bu, kodumuzun bazı bölümlerini izole etmek için blokları kullanabileceğimiz ve "blokta olanın blokta kalacağından" emin olabileceğimiz anlamına gelir (Las Vegas gibi).


Kodumuzu bloklar halinde düzenlemek, `if` gibi kontrol akışı yapılarıyla programın yürütülmesini de yapılandırmamızı sağlar


### `if`, `else`


Bazen kodu **sadece** bir şey doğruysa çalıştırmak isteriz. İşte `if` deyimi bunun içindir.


```javascript
const myAge = 20

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Bu baskılar:


```
Am I an adult?
Yes I am!
```


Gördüğünüz gibi, kod `myAge` ve `18` değerlerini karşılaştırıyor.

Bu durumda `>=` işleci `true` döndürür, böylece blok yürütülür.

Koşul `true` değilse, blok yürütülmez.


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
}
```


Bu baskılar:


```
Am I an adult?
```


Tersi durumu ele almak için bir `else` bloğu ekleyebilirsiniz:


```javascript
const myAge = 17

console.log("Am I an adult?")

if (myAge >= 18) {
console.log("Yes I am!")
} else {
console.log("No, I am not.")
}
```


Bu baskılar:


```
Am I an adult?
No, I am not.
```


Hem `if` hem de `else` blokları hala bloktur - bu nedenle içlerinde bildirilen değişkenler dışarıda mevcut değildir.


Bir şeyin **doğru** olmadığından emin olmak istiyorsak, ne yapabiliriz?


Daha önce tartışıldığı gibi, JavaScript'te boole'ları çeviren bir "not" operatörü vardır. Böylece şunu yapabiliriz


```javascript
const myAge = 17

const adult = myAge >= 18

console.log("Am I an adult?")

if (!adult) {
console.log("No, I am not.")
}
```

Bu hala yazdırıyor:


```
Am I an adult?
No, I am not.
```

Çünkü `adult` değişkenini ters çevirmek için `!` operatörünü kullandık.


"if (!adult) {...}" ifadesi "if not adult..." şeklinde okunmalıdır


Blokları, mantık ve karşılaştırma operatörlerini kullanarak, bir şeyin gerçekleşmesi için `doğru` (veya `yanlış`) olması gereken değişkenleri tanımlayarak programın yürütülmesini yapılandırabiliriz.


### `while`, `break`, `continue`


Bir `while` döngüsü, bir koşul doğru olduğu sürece * kodu tekrarlar.


```javascript
let count = 0

while (count < 3) {
console.log("Count is", count)
count = count + 1
}
console.log("the loop is over!")
```


Bu baskılar:


```
Count is 0
Count is 1
Count is 2
the loop is over!
```


Sayım 3 olduğunda döngü durur.


Bir döngüyü `break` kullanarak erken durdurabilirsiniz:


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


Bu baskılar:


```
0
1
2
```


Çünkü sayı `3` olduğunda, `if` bloğu yürütülür ve döngüyü durdurur.


Bir döngünün geri kalanını `continue` kullanarak atlayabilirsiniz:


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


Bu baskılar:


```
1
2
4
5
```


Çünkü sayı `3` olduğunda, `continue` programın sayıyı yazdıran satırı atlamasına neden oldu.


### "... için ...`


Bir diziniz varsa ve içindeki her öğeye bir şey yapmak istiyorsanız, `for ... of ... {...}`.


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const fruit of fruits) {
console.log(fruit)
}
```


Bu baskılar:


```
apple
banana
cherry
```

Blok, dizinin her bir elemanı için bir kez çalıştırılacaktır.


buradaki `fruit`, blok içinde üzerinde işlem yapmak için dizideki her öğenin değerini alan yeni bir değişkendir.


### `için ... içinde ...`


Bir dizinin anahtarları (indeksleri) üzerinde döngü yapmak için `for ... in` kullanabilirsiniz:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(index)
}
```


Bu baskılar:


```
0
1
2
```


Değeri almak için indeksi de kullanabilirsiniz:


```javascript
const fruits = ["apple", "banana", "cherry"]

for (const index in fruits) {
console.log(fruits[index])
}
```


Bu `for ... of` ile aynı çıktıyı verir:


```
apple
banana
cherry
```


Pratikte, diziler için, daha basit ve temiz olduğu için `for ... of` kullanmayı tercih etmelisiniz.


### Sınırlandırılmış döngüler


Bazen belirli sayıda döngü yapmak veya genel olarak bir şeyi takip ederken bir bloğu tekrarlayan bir kod parçası yazmak isteriz.

Sınırlandırılmış `for' döngüsü bu işe yarar.

Sınırlandırılmış bir döngü genellikle `(... ; ... ; ....)` gibi noktalı virgül `;` ile ayrılmış üç koşul alır.


```javascript
for (let i = 0; i < 3; i = i + 1) {
console.log(i)
}
```


Bu baskılar:


```
0
1
2
```


Açıklayalım:



- let i = 0`: blokta kullanılacak bir değişken bildirir (bu durumda 0'dan başlayan bir sayaçtır)
- i < 3`: bloğun yürütülmesi için `doğru` olması gereken bir koşul bildirir (bu durumda "i` 3`ten küçükken tekrarla")
- i = i + 1`: bloğun her yürütülmesinden sonra çalıştırılacak bazı kodlar bildirir (bu durumda "`i`yi 1 artır")


Gördüğünüz gibi sınırlı döngü, bir kod parçasının tekrar tekrar yürütülmesi için daha karmaşık koşullar bildirmemizi sağlar, ancak çoğu zaman gerekli değildir.


### Blok etiketleri


Daha karmaşık bir kontrol akışı yazmanız gerekiyorsa JavaScript, `break` veya `continue` tarafından *nereye* geri dönüleceğini belirtmek için kullanılabilecek bir **label** kullanarak bir bloğu adlandırmanıza olanak tanır.


Örnek:


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


Bu baskılar:


```
Inside outer block
Inside inner block
Done
```


Outer` bloğundan tamamen çıkmak için `break outer` kullandık.


Döngüleri de etiketleyebilirsiniz. Bu örneği ele alalım:


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

Bu çok sıkıcı bir örnekti ama umarım etiketlere olan (zaman zaman) ihtiyacı açıklığa kavuşturmuştur.


## Fonksiyonların tanıtılması

<chapterId>cc324715-09c2-5cf7-9e6f-47a6f16bc04d</chapterId>


Programlarınız büyüdükçe, genellikle kod parçalarını **yeniden kullanmak** isteyeceksiniz.


Fonksiyonlar** bunun içindir: bazı kodları bir araya getirmenize, bir isim vermenize ve istediğiniz zaman çalıştırmanıza izin verirler.


### İşlev bildirimi


Bir fonksiyon bildirmek için `function` anahtar sözcüğünü kullanabiliriz. Sonra ona bir isim, aldığı argümanlarla birlikte bir çift parantez `()` ve çalıştırılacak bir kod bloğu `{}` veririz. Hiçbir argüman almayan bir fonksiyonla başlayalım:


```javascript
function sayHello () {console.log(`Hello!`) }
```


Bu kod işlevi **bildirir**, ancak henüz **çalıştırmaz**.


### İşlev çağrıları


Fonksiyonu çalıştırmak (veya "çağırmak") için, adını ve ardından parantezleri yazarsınız:


```javascript
function sayHello () {console.log(`Hello!`) }
sayHello()
```


Bu baskılar:


```
Hello!
```


Fonksiyonu istediğiniz kadar çağırabilirsiniz:


```javascript
function sayHello() {
console.log("Hello!")
}

sayHello()
sayHello()
```


Bu baskılar:


```
Hello!
Hello!
```


İşlevin içindeki kod yalnızca siz onu çağırdığınızda çalışır.


### Fonksiyon argümanları (fonksiyonlara girdi)


Bazen bir fonksiyonun bazı girdilerle çalışmasını istersiniz. Bunu parantezlerin içine **argümanlar** ekleyerek yapabilirsiniz.


Örneğin:


```javascript
function sayHelloTo (friend) {
console.log(`Hello ${friend}!`)
}
```


Şimdi bu fonksiyon `friend` adında **bir argüman** alır.


Fonksiyonu çağırdığınızda bir değer aktarabilirsiniz:


```javascript
sayHelloTo("Tommy")
```


Bu baskılar:


```
Hello Tommy!
```


Fonksiyonu farklı bir isimle tekrar çağırabilirsiniz:


```javascript
sayHelloTo("Sam")
```


Bu baskılar:


```
Hello Sam!
```


Aktardığınız değer, fonksiyon içindeki `friend` değişkeninin yerini alır.


Birden fazla argüman da kullanabilirsiniz:


```javascript
function greetTwoPeople(person1, person2) {
console.log(`Hello ${person1} and ${person2}!`)
}

greetTwoPeople("Lina", "Marco")
```


Bu baskılar:


```
Hello Lina and Marco!
```


### `return` (fonksiyonlardan elde edilen çıktı)


Fonksiyonlar ayrıca **değer döndürebilir**. Bu, fonksiyonun çağrıldığı yere bir değer geri gönderdikleri anlamına gelir.


İşte basit bir örnek:


```javascript
function getNumber() {
return 42
}

const result = getNumber()
console.log(result)
```


Bu baskılar:


```
42
```


GetNumber()` işlevi `42` döndürür ve bunu `result` içinde saklarız, ardından yazdırırız.


Hesapladığınız bir şeyi de iade edebilirsiniz:


```javascript
function add(a, b) {
return a + b
}

const result = add(2, 3)
console.log(result)
```


Bu baskılar:


```
5
```


Bir değer `return` edildiğinde, fonksiyon durur. Bu blokta `return` değerinden sonra herhangi bir şey gerçekleşmez.


```javascript
function saySomething() {

return "hi"

console.log("this never runs")

}

const message = saySomething()
console.log(message)
```


Bu sadece yazdırır:


```
hi
```


çünkü sadece `"hi"` döndürülür. Console.log("this never runs")` satırı atlanır.


Fonksiyonları küçük alt programlar olarak düşünebilirsiniz. Her fonksiyon bir girdi alabilir, üzerinde çalışabilir ve size bir çıktı verebilir.


Bir işlevin dönüş değerini kullanmaya çalışırsak, ancak bu işlev hiçbir şey döndürmezse ne olur?


```javascript
function doesNothing () {}

const x = doesNothing()

console.log(x)
```

Bu `undefined` yazdıracaktır. Hiçbir şey döndürmeyen bir işlevin dönüş değeri `undefined`dır.


## Nesneler ve sınıflar

<chapterId>26689f25-8212-5057-8c21-3a05eee0ac75</chapterId>


JavaScript genellikle nesne yönelimli bir dil olarak adlandırılır.


Bu, değerleri ve işlevleri **nesneler** halinde gruplandırarak kodunuzu düzenlemenize yardımcı olduğu anlamına gelir.


### Nesne nedir?


Bir nesne veri ve bu veri üzerinde işlem yapan fonksiyonlar içerebilir. Bir fonksiyon bir nesneye yerleştirildiğinde buna `metot' deriz.


Gördüğümüz ilk nesne `console` nesnesiydi. Bu nesne, ekrana bir şeyler yazdırmak ve programlarımızda hata ayıklamak için birden fazla yöntem içeren bir nesnedir.


Kendi kendine bile yazdırabilir; şunları yapabilirsiniz


```javascript
console.log(console)
```


ve içerdiği yöntemlerin bir listesini yazdıracaktır. Örneğin, benim makinemde şunları yazdırdı


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


Gördüğünüz gibi, hata ayıklamak için kullanabileceğiniz çok sayıda yöntem var!


Javascript, yapmalarını istediğimiz her şeyi yapabilen yeni nesneler oluşturmak için bize farklı bir yol sunar.


### Nesne oluşturma


Bir nesne oluşturmanın en kolay yolu, verileri ve işlevleri **kıvırcık parantez** `{}` kullanarak gruplamaktır.


Bu, **anonim nesne** dediğimiz şeyi oluşturur


```javascript
const cat = {
name: "Whiskers",
age: 3
}
```


Bu, bir nesne oluşturur ve onu `cat` adlı bir değişkende saklar.


Nesnenin iki **özelliği** vardır:



- "Whiskers" değerine sahip `name`
- 3` değerine sahip `yaş`


Hadi basalım:


```javascript
console.log(cat)
```


Bu baskılar:


```
{ name: 'Whiskers', age: 3 }
```


Nesneden özellikleri `objectName.propertyName` gibi bir nokta kullanarak alabilirsiniz:


```javascript
console.log(cat.name)  // prints "Whiskers"
console.log(cat.age)   // prints 3
```


Ayrıca bir mülkü **değiştirebilirsiniz**:


```javascript
cat.age = 4
console.log(cat.age)  // now it prints 4
```


Gördüğünüz gibi, bir nesne `const` olarak tanımlanmış olsa bile, içerdiği verileri değiştirebilirsiniz.


Nesneler söz konusu olduğunda, `const` yalnızca tüm nesneyi geçersiz kılmanızı engelleyecektir:


```javascript
const cat = {
name: "Whiskers",
age: 3
}

cat.age = 5 // this works

cat = 5 // this throws an error, you're trying to reassign the whole object

```


Daha önce de belirtildiği gibi, nesneler **fonksiyonları** da tutabilir ve bir fonksiyon bir nesnenin parçası olduğunda, buna **metot** diyoruz.


İşte bir örnek:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log("Meow!")
}
}
```


Bu nesne vardır:



- Bir `name` özelliği
- Bir `speak()` yöntemi


Metodu çağıralım:


```javascript
cat.speak()
```


Yazıyor:


```
Meow!
```


Yöntemler, `this` anahtar sözcüğü aracılığıyla nesnenin içerdiği verileri kullanabilir.

this` geçerli nesneyi ifade eder. Bu örnekte, kedinin adını yazdırmak için kullanılacaktır:


```javascript
const cat = {
name: "Whiskers",
speak () {
console.log(`${this.name} says meow!`)
}
}

cat.speak()
```


Bu baskılar:


```
Whiskers says meow!
```


Bu sözcük "bu nesne" anlamına gelir... bu durumda, "kedi" nesnesi.



Bu tür nesneler, sadece hızlı ve basit bir şey istediğinizde harikadır. Ancak aynı yapıya sahip **çok sayıda nesne** oluşturmanız gerekiyorsa, daha iyi bir yol vardır ve **sınıflar** burada devreye girer.


### Sınıflar ve kurucular


Bir **sınıf** bir plan gibidir. JavaScript'e belirli bir nesne türünün nasıl oluşturulacağını söyler.


Bir sınıfı `class` anahtar sözcüğünü, ardından sınıfın adını ve bir küme parantezi `{}` bloğunu kullanarak tanımlarsınız.


```javascript
class Dog {}
```


Sınıflar geleneksel olarak genellikle büyük harfle başlar.


New` kullanarak bir sınıfın yeni bir nesnesini oluşturabilirsiniz:


```javascript
const hachiko = new Dog()
```


Nesneyi yazdırmayı deneyin:

```javascript
class Dog {}

const myDog = new Dog()

console.log(myDog)
```


Alacaksın


```
Dog {}
```


Gördüğünüz gibi Dog sınıfı boştur, dolayısıyla `myDog` nesnesi de boştur.


Dog nesnelerinin hangi özellikleri içermesi gerektiğini bir `constructor` ekleyerek tanımlayabiliriz.


Yapıcı, yeni bir nesne oluşturduğunuzda (veya "inşa ettiğinizde") çalışan özel bir işlevdir.


```javascript
class Dog {
constructor() { }
}
```


Her Dog'un bir adı olmasını istiyoruz, bu yüzden fonksiyona bir `name` parametresi ekliyoruz:


```javascript
class Dog {
constructor(name) { }
}
```


Ve sonra `name`nin oluşturduğumuz `Dog` nesnesinin `name`i olduğunu bildirmek için `this` kullanıyoruz


```javascript
class Dog {
constructor(name) {
this.name = name
}}
```


Şimdi kullanmayı deneyelim:


```javascript
class Dog {
constructor(name) {
this.name = name
}
}

const myDog = new Dog("hachiko")

console.log(myDog)
```


Bu, aşağıdaki gibi bir şey yazdırır:


```
Dog { name: 'hachiko' }
```


Gördüğünüz gibi, `constructor` yöntemi `new Dog()` yaptığınızda sınıfa aktardığınız argümanları alır ve nesneyi oluşturmak için kullanır.


Hadi parçalara ayıralım:



- class Dog`, Dog sınıfını tanımlar.
- `constructor(name)` nesne oluşturulduğunda onu ayarlar.
- this.name = name` değeri yeni nesnede saklar.
- `new Dog("hachiko")` sınıfından, `name` özelliği `"hachiko"` olarak ayarlanmış yeni bir nesne oluşturur.


Şimdi sınıfımıza bir yöntem ekleyelim:


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


Bu yazdıracaktır


```javascript
hachiko says barf!
```


Aynı şeyi iki farklı Dog örneği için yaparsak



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


elde ederiz


```
hachiko says barf!
bobby says barf!
```


speak()` yöntemi, çağrıldığı `Dog`un `name` özelliğini kullanır.


Sınıfların var olmasının ana nedeni budur: veriler üzerinde çalışan bir dizi yöntem tanımlamamıza ve ardından aynı veri "şeklini" paylaşan birden fazla nesne oluşturmamıza olanak tanırlar.


Bu nesnelerden biri üzerinde bir yöntem çağırdığımızda, bu yöntem *o belirli nesnenin* tuttuğu veriler üzerinde çalışacaktır.


### Bir nesnenin şeklini değiştirme


JavaScript'teki nesneler esnektir. Bir nesne oluşturduktan sonra bile yeni özellikler ekleyebilir veya var olanları kaldırabilirsiniz.


Buna izin verilir, ancak dikkatli kullanmanız gereken bir şeydir.


Basit `Dog` sınıfımızla başlayalım:


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


Bu noktada, `myDog` yalnızca bir özelliğe sahiptir: name`. Oluşturulduktan sonra da yeni özellikler ekleyebiliriz:


```javascript
myDog.age = 5

console.log(myDog.age) // prints 5
```


Ayrıca yeni bir yöntem de ekleyebiliriz:


```javascript
myDog.jump = function () {
console.log(`${this.name} jumps!`)
}

myDog.jump() // Fido jumps!
```


Ve `delete` anahtar sözcüğünü kullanarak özellikleri de kaldırabiliriz.


```javascript
delete myDog.name

console.log(myDog.name) // prints 'undefined'
```


Bu işe yarar, ancak burada bilmeniz gereken önemli bir şey var: V8 gibi JavaScript motorları (Node.js'de ve Chrome tarayıcısında kullanılır) nesneleriniz her zaman aynı özellikleri koruduğunda daha hızlı çalışır. Nesne oluşturulduktan sonra özellik ekler veya kaldırırsanız, bu durum işleri yavaşlatabilir.


Küçük programlarda bu çok önemli değildir. Ancak daha büyük projelerde (oyunlar gibi), hemen kullanmasanız bile yapıcıdaki tüm özellikleri en baştan listelemek daha iyidir. Bu, nesnenin şeklini sabit tutar ve kodunuzun daha hızlı çalışmasına yardımcı olur.


Örneğin, bunun yerine:


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


Yapabilirsin


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


Her iki versiyon da çalışır, ancak ikincisi performans açısından daha iyidir. Motora her nesnenin hangi özelliklere sahip olacağını önceden söylüyorsunuz ve o da buna göre optimize edebiliyor.


JavaScript nesneleri serbestçe yeniden şekillendirmenize izin verir, ancak sınıfları kullanırken nesnenizin şeklini önceden planlamak en iyisidir.



### Extends` ve `super()` ile kalıtım


Bazen başka bir sınıfla *neredeyse* aynı olan, ancak birkaç ekstra özelliğe sahip bir sınıf oluşturmak istersiniz.


Nesnelerin şeklini değiştirmek (ki daha önce de belirtildiği gibi performans için uygun değildir) veya sıfırdan yeni bir sınıf yazmak yerine, JavaScript **kalıtım** adı verilen bir şeyi kullanmanıza izin verir.


Kalıtım, bir sınıfın diğerini **genişletebileceği** anlamına gelir. Yeni sınıf eskisinin tüm özelliklerini ve yöntemlerini alır ve siz daha fazlasını ekleyebilir veya ihtiyacınız olanı değiştirebilirsiniz.


Diyelim ki `Vehicle` adında bir temel sınıfımız var:


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


Şimdi bir `Araba` sınıfı yapmak istiyoruz. Araba bir tür araçtır, ancak bazı ekstra özelliklere sahip olmasını veya çalıştığında farklı bir mesaj vermesini isteyebiliriz. Her şeyi yeniden yazmak yerine `extends` kullanabiliriz:


```javascript
class Car extends Vehicle {
start() {
console.log(`${this.brand} car is ready to drive!`)
}
}
```


Car` sınıfı artık her şeyi `Vehicle` sınıfından **devralıyor**. Marka` özelliğini alır ve `start()` metodunu kendi versiyonumuzla değiştirdik.


![](assets/en/4.webp)


Hadi deneyelim:


```javascript
const myCar = new Car("Toyota")
myCar.start()
```


Bu baskılar:


```
Toyota car is ready to drive!
```


Car`ın kendi kurucusu olmasa da, yine de `Vehicle`ın kurucusunu kullanır. Ancak `Car` içinde özel bir kurucu yazmak istersek, bunu yapabiliriz, sadece `super()` kullanarak ebeveyninin kurucusuna bir çağrı eklememiz gerekir.


Şöyle yapacağız:


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



Bu baskılar:


```
Toyota Corolla is ready to drive!
```


Özetlemek gerekirse



- "genişletir" bir sınıfın diğerine dayandığı anlamına gelir.
- super()`, genişletmekte olduğunuz sınıfın kurucusunu çağırmak için kullanılır.
- Yeni sınıf, orijinal sınıfın tüm özelliklerini ve yöntemlerini alır.
- Farklı bir şey yapmalarını sağlamak için yöntemleri (`start()` gibi) **override** edebilirsiniz.


Bu, benzer birkaç şeye sahip olduğunuzda (arabalar, kamyonlar ve bisikletler gibi) ve kod paylaşmalarını ancak yine de kendi yollarıyla davranmalarını istediğinizde yararlıdır.


### `instanceof`


`instanceof` anahtar sözcüğü, bir nesnenin belirli bir sınıftan oluşturulup oluşturulmadığını kontrol eder.


Diyelim ki `Kullanıcı` adında bir sınıfımız var:


```javascript
class User {
constructor(username) {
this.username = username
}
}

const regularUser = new User("julia123")

console.log(regularUser instanceof User)
```


Bu baskılar:


```
true
```


DüzenliKullanıcı`nın bir `Kullanıcı` olduğu doğrulanıyor. Çünkü `regularUser`, `User` sınıfı kullanılarak oluşturulmuştur.


Ayrıca **devralınmış** sınıflarla da çalışır. Örneğin, burada `Kullanıcı'yı genişleten bir `Yönetici` sınıfı var:


```javascript
class Admin extends User {}

const ourAdmin = new Admin("admin42")

console.log(ourAdmin instanceof Admin)   // true
console.log(ourAdmin instanceof User)    // true
```


Her iki satır da `true` döndürür. Çünkü `Admin`, `Kullanıcı`nın bir alt sınıfıdır, dolayısıyla `bizimAdmin` hem bir `Admin` hem de bir `Kullanıcı`dır


# Orta Seviye JavaScript

<partId>243f63ab-4f34-5c30-80cb-84ef46f6761d</partId>


## Hata İşleme

<chapterId>d0206bc5-d386-5e7f-9917-5803f392448c</chapterId>


Daha karmaşık JavaScript programları yazdıkça **hatalarla** karşılaşırsınız. Bunlar bir şeylerin yanlış gittiği beklenmedik durumlardır. Belki bir değişken `tanımsızdır' ama siz onu kullanmaya çalışırsınız ya da bazı kodlar yanlış türde girdi alır.


Bu hataları düzgün bir şekilde ele almazsak, programımız çökebilir veya öngörülemeyen şekillerde davranabilir. JavaScript, bu hataları tespit etmek ve yönetmek için araçlar sağlar, böylece bu hataları daha zarif bir şekilde ele alabiliriz.


### Yaygın hata: `undefined` üzerinde bir değere erişme


İşte hataya neden olan yaygın bir durum:


```javascript
const user = undefined
console.log(user.name)
```


Bu kodu çalıştırırsanız, şuna benzer bir hata alırsınız:


```
TypeError: Cannot read properties of undefined (reading 'name')
```


Bu JavaScript'in size söylediğidir: "Hey, `name` özelliğini `undefined` olan bir şeyden almaya çalıştın ve bu mantıklı değil." Gördüğünüz gibi, bu tür bir hata oluştuğunda, bunu yakalamak ve işlemek için özel olarak kod yazmadığınız sürece program çalışmayı durdurur.


### hata atma


Bazen kodunuzda manuel olarak bir **hatayı** yükseltmek istersiniz. Bu durumda `throw` anahtar sözcüğünü kullanırsınız.


```javascript
throw new Error("This is a custom error message")
```


Bu, programı hemen durdurur ve yazdırır:


```
Uncaught Error: This is a custom error message
```


Programınızdaki kuralları uygulamak için `throw` kullanabilirsiniz. Örneğin:


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


Bu örnekte sıfıra bölmeye izin verilmediği için ikinci çağrı bir hataya neden olur.


### Hataları `try...catch` ile yakalama


Bir hata oluştuğunda programınızın çökmesini istemiyorsanız, bir `try...catch` bloğu kullanarak hatayı yakalayabilirsiniz. Bu, bir şey başarısız olsa bile programınızın **devam etmesini** istediğinizde yararlıdır.


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log("Oops! Something went wrong.")
}
```


Çıktı:


```
Oops! Something went wrong.
```


Şöyle çalışıyor:



- Önce `try` bloğunun içindeki kod denenir.
- Bir hata oluşursa, JavaScript **catch` bloğuna** atlar ve `try` bloğunun geri kalanını atlar.
- Hatayı `catch` bloğu alır, böylece onu yazdırabilir veya başka bir şekilde işleyebilirsiniz, örneğin


```javascript
try {
const user = undefined
console.log(user.name)
console.log("End of the block") // this will never get printed
} catch (error) {
console.log(`The message of the error was: "${error.message}"`)
}
```


Çıktı:


```
The message of the error was: "Cannot read properties of undefined (reading 'name')"
```


### Sonunda` bloğu


Ayrıca bir `finally` bloğu da ekleyebilirsiniz. Bu, bir hata olsa da olmasa da **her zaman çalışan** koddur.


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


Çıktı:


```
Trying something risky...
Caught the error: Uh oh!
This will run no matter what.
```


## Böceklerden Kaçınma

<chapterId>db12d9f6-5806-514c-998e-0ae24805104e</chapterId>


Bu bölümde JavaScript'teki en yaygın tuzaklardan bazıları ve bunlardan nasıl kaçınılacağı gösterilmektedir.


### var` ve Assignment bildirimsiz


Eski JavaScript kodlarında, değişkenler genellikle `var` anahtar sözcüğü kullanılarak bildirilirdi. Daha önce öğrendiğiniz `let` ve `const`tan farklı olarak, `var` kafa karıştırıcı şekillerde davranabilir.


Örneğin:


```javascript
{
var message = "hello"
}
console.log(message)
```


Mesaj`ın yalnızca blok içinde var olmasını bekleyebilirsiniz, ancak öyle değildir. var` blok kapsamını yok sayar ve değişkeni tüm fonksiyon veya dosya boyunca kullanılabilir hale getirir.


Bu, özellikle büyük programlarda beklenmedik davranışlara yol açabilir. Bu nedenle, modern JavaScript kodu her zaman `var` yerine `let` veya `const` kullanmalıdır.


Daha da kötüsü, JavaScript değişkenlere **onları hiç bildirmeden** değer atamanıza izin verir:


```javascript
function greet() {
user = "Alice"
}
greet()
console.log(user) // prints "Alice"
```


Bu, herhangi bir bildirim olmaksızın yeni bir global değişken `name` oluşturur. Bu sessizce gerçekleşebilir ve özellikle sadece bir yazım hatasıysa, izlenmesi Hard olan hatalara yol açabilir. Değişkenleri her zaman `let` veya `const` kullanarak bildirin.


### Zayıf tip sistemi


JavaScript zayıf tiplidir, yani gerektiğinde değerleri otomatik olarak bir tipten diğerine dönüştürür. Buna tip zorlaması denir ve kullanışlı olsa da genellikle kafa karıştırıcı sonuçlara yol açar.


Örneğin:


```javascript
console.log("5" + 1)    // "51"
console.log("5" - 1)    // 4
console.log(true + 1)   // 2
console.log(null + 1)   // 1
```


Bu örneklerde JavaScript ne demek istediğinizi tahmin etmeye çalışır. Bazen dizeleri sayılara, booleanları sayılara veya dizeleri dizelere dönüştürür. Bu, kodunuzun beklenmedik şekillerde davranmasına neden olabilir.


JavaScript'in zayıf tipleme sisteminin farkında olmak önemlidir. Bir şeyler garip davranmaya başladığında, bunun nedeni beklenmedik tip zorlaması olabilir.


### `"use strict"`


Bazı sessiz hataları gerçek hatalara dönüştüren ve dilin daha tehlikeli özelliklerinden bazılarını kullanmanızı engelleyen daha katı bir modu etkinleştirebilirsiniz.


Bu daha katı modu etkinleştirmek için, dosyanızın veya işlevinizin en üstüne bu satırı ekleyin:


```javascript
"use strict"
```


Örneğin:


```javascript
"use strict"
name = "Alice" // ReferenceError: name is not defined
```


Sıkı mod olmadan, JavaScript sessizce `name` adında bir global değişken oluşturur. Ancak katı mod ile bu gerçek bir hata haline gelir ve hataları daha erken yakalamanıza yardımcı olur.


Strict modu ayrıca JavaScript'in bazı eski özelliklerini devre dışı bırakır ve kodunuzun optimize edilmesini ve bakımını kolaylaştırır.


## Değer vs Referans

<chapterId>bb898425-dc2f-5e5c-864b-0cb7a4a9aea9</chapterId>


JavaScript farklı türdeki değerleri farklı şekillerde ele alır.


Bazı değerler bir değişkene atandığında **kopyalanır**.


Diğerleri yeni bir değişkene atandığında **paylaşılır**, bu nedenle birini değiştirirseniz diğeri de değişir.


### Değere göre geçiş


Bir değer **değer** olarak aktarıldığında, JavaScript bunun bir **kopyasını** yapar.


Yani birini değiştirirseniz, diğerini etkilemez.


Bu, ilkel türlerde olur, örneğin:



- sayılar
- dizeler
- booleanlar (`true` ve `false`)
- `null`
- `undefined`


Bir örneğe bakalım:


```javascript
let a = 5
let b = a

b = 10

console.log(a) // 5
console.log(b) // 10
```


B`ye `a` değerini verdik, ancak daha sonra `b`yi `10` olarak değiştirdik.


Sayılar değere göre aktarıldığından, JavaScript `5`i `b`ye kopyalamıştır. B`deki `5`, `a`daki orijinal `5`ten bağımsızdır, bu nedenle `b`nin değerini değiştirmenin `a` üzerinde hiçbir etkisi yoktur.


Bir dize ile deneyelim:


```javascript
let name1 = "Alice"
let name2 = name1

name2 = "Bob"

console.log(name1) // Alice
console.log(name2) // Bob
```


Yine, `name2`nin değiştirilmesi `name1`i etkilemedi, çünkü dizeler de değer olarak aktarılır.


Bir ilkeli bir fonksiyona aktardığınızda da aynı şey olur: kopyalanır. Yani fonksiyon orijinali değiştiremez.


```javascript
function plusOne(x) {
x = x + 1
}

let number = 5

plusOne(number)

console.log(number) // 5
```


Fonksiyonun içinde `x`e `1` eklenmiş olsa da, orijinal `sayı` değişmedi.


Bunun nedeni, işleve yalnızca bir **kopyanın** aktarılmış olmasıdır.


### Referans ile geç


Nesneler **referans** ile aktarılır.


Yani JavaScript bunları kopyalamak yerine sadece bir **referans** iletir ve bunu değiştirirseniz, buna işaret eden diğer tüm değişkenler de değişikliği görecektir.


Örneğin:


```javascript
const person1 = { name: "Alice" }
const person2 = person1

person2.name = "Bob"

console.log(person1.name) // Bob
console.log(person2.name) // Bob
```


Hem `person1` hem de `person2` bellekte aynı nesneye işaret eder.


Yani `person2.name`i değiştirdiğimizde, `person1.name`i de değiştirdik, çünkü ikisi de aynı şeye bakıyor.


Diziler nesnelerdir, bu yüzden aynı şeyi bir dizi ile deneyelim:


```javascript
const list1 = [1, 2, 3]
const list2 = list1

list2.push(4)

console.log(list1) // [1, 2, 3, 4]
console.log(list2) // [1, 2, 3, 4]
```


4`ü `list2`ye ittik, ancak `list1` de etkilendi, çünkü ikisi de aynı diziye atıfta bulunuyor.


Bir nesneyi bir fonksiyona aktardığımızda ne olacağını görelim:


```javascript
function rename(user) {
user.name = "Charlie"
}

const person = { name: "Dana" }

rename(person)

console.log(person.name) // Charlie
```


İşlev nesneyi değiştirdi! Bunun nedeni, orijinal `person` nesnesine bir **referans** almış olmasıdır.


Bir kopyasını almadı. Orijinal nesneye erişti ve bununla birlikte onu değiştirme yeteneğine sahip oldu.


Bu ayrımı hatırlamak önemlidir, çünkü aksi takdirde kodumuz beklediğimizden farklı davranabilir. Örneğin, aldığı argümanları değiştirmeyeceği beklentisiyle bir fonksiyon yazabilir ve daha sonra aslında onları değiştirdiğini öğrenebiliriz (çünkü onlar nesnedir, bu yüzden referansla aktarılmışlardır).


## Fonksiyonlarla Çalışma

<chapterId>e0d277a8-c642-5af7-9e53-dee27c811967</chapterId>


JavaScript'te fonksiyonları nasıl bildireceğinizi ve kullanacağınızı zaten öğrendiniz. Ancak JavaScript, fonksiyonlarla güçlü şekillerde çalışmanız için size daha fazla araç sunar.


### Ok fonksiyonları


Ok fonksiyonları, fonksiyon yazmanın daha kısa bir yoludur. Fonksiyon` anahtar sözcüğünü kullanmak yerine bir ok (`=>`) kullanırız.


İşte normal bir fonksiyon:


```javascript
function greet(name) {
return `Hello, ${name}!`
}
```


Ok versiyonu şu şekilde görünür:


```javascript
const greet = (name) => {
return `Hello, ${name}!`
}
```


Eğer fonksiyon **sadece bir satırdan** oluşuyorsa, parantezleri atlayabilir ve `return` yapabilirsiniz:


```javascript
const greet = (name) => `Hello, ${name}!`
```


Fonksiyonun **sadece bir parametresi** varsa, parametrelerin etrafındaki parantezleri bile atlayabilirsiniz:


```javascript
const greet = name => `Hello, ${name}!`
```


Ok fonksiyonları modern JavaScript'te çok yaygındır, çünkü basit fonksiyonları önemli ölçüde daha az boilerplate ile ifade etmeyi sağlarlar.


### Varsayılan parametreler


Bazen bir fonksiyonun hiçbir argüman geçilmediğinde **varsayılan bir değere** sahip olmasını istersiniz.


Bunu şu şekilde yapabilirsiniz:


```javascript
function sayHello(name = "friend") {
console.log(`Hello, ${name}!`)
}

sayHello("Alice") // Hello, Alice!
sayHello()        // Hello, friend!
```


Hiçbir şey aktarılmadığında varsayılan değer `"friend"` kullanılır.


### Yayılma parametreleri (`...`)


Peki ya fonksiyonunuz esnek sayıda argüman alıyorsa?


Bunları bir dizide toplamak için **yayma operatörünü** (`...`) kullanabilirsiniz:


```javascript
function logAll(...items) {
console.log(items)
}

logAll(1, 2, 3) // [1, 2, 3]
logAll("a", "b") // ["a", "b"]
```


Daha sonra her bir öğeyi işlemek için bir döngü kullanabilirsiniz:


```javascript
function logEach(...items) {
for (const item of items) {
console.log(item)
}
}
```


Yayma operatörü, kaç argüman geçileceğini bilmediğinizde kullanışlıdır.


### Yüksek dereceli fonksiyonlar


Bir **yüksek dereceli fonksiyon** şu özelliklere sahip bir fonksiyondur:



- girdi olarak başka bir fonksiyon alır
- ve/veya çıktı olarak bir fonksiyon döndürür


İşte basit bir örnek:


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


Bu baskılar:


```
Hello, friend!
Hello, friend!
```


Ona bir ok fonksiyonu aktarabiliriz:


```javascript
runTwice(
() => console.log("Hello!")
)
```


Bu baskılar:


```
Hello!
Hello!
```


Diğer fonksiyonları **geri döndüren** fonksiyonlar da yazabilirsiniz:


```javascript
function makeGreeter(name) {
return () => console.log(`Hi, ${name}`)
}

const greetAlice = makeGreeter("Alice")
const greetBob = makeGreeter("Bob")

greetAlice() // Hi, Alice
greetBob() // Hi, Bob
```


MakeGreeter` fonksiyonu diğer fonksiyonları oluşturan bir fonksiyondur. Bir dize alır ve `console.log` çağrısında bu dizeyi kullanan yeni bir işlev döndürür.


Bu tür bir model çok güçlüdür, çünkü fonksiyonlarınızda daha sonra ihtiyacınız olan davranışla doldurabileceğiniz "boşluklar" bırakmanıza olanak tanır.


### `map()`, `filter()`, `reduce()`


JavaScript, dizilerle kullanmanız için size bazı yararlı yerleşik yöntemler sunar.


Bu metotlar argüman olarak fonksiyonları alır, dolayısıyla bunlar aynı zamanda üst düzey fonksiyonlardır.


map()` bir dizideki her öğeyi başka bir şeye dönüştürür.


Örnek:


```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(x => x * 2)

console.log(doubled) // [2, 4, 6]
```


Her sayı ikiye katlanır ve sonuç yeni bir dizidir.


filter()`, bir testi geçemeyen öğeleri diziden kaldırır.


Örnek:


```javascript
const numbers = [1, 2, 3, 4, 5]
const numbersGreaterThanTwo = numbers.filter(x => x > 2)

console.log(numbersGreaterThanTwo) // [3, 4, 5]
```


Yalnızca `x > 2` koşulunun `true` döndürdüğü dizi girdileri tutulur.


reduce()` bir dizideki tüm öğeleri tek bir değerde birleştirmek için kullanılır.


Örnek:


```javascript
const numbers = [1, 2, 3, 4]
const total = numbers.reduce((current, next) => current + next)

console.log(total) // 10
```


reduce` dizinin içinden geçer ve bu örnekte, `+` operatörünü `1` ve `2` arasına, sonra ortaya çıkan `3` ve `3` arasına, sonra ortaya çıkan `6` ve `4` arasına, tüm dizi girişlerinin toplamını elde edene kadar (ki bu 10'dur) uygular.


Toplamlar, ortalamalar veya adım adım yeni değerler oluşturmak gibi birçok şey için `reduce()` işlevini kullanabilirsiniz.


Bu yöntemler (`map`, `filter`, `reduce`) manuel döngüler yazmadan verileri işlemek için güçlü araçlardır.


Hatta bunları aşağıdaki gibi bir işlem zincirinde birleştirebilirsiniz:


```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers
.map(n => n * 2)        // Double each entry, obtain [2, 4, 6, 8, 10]
.filter(n => n > 3) // Keep only the entries bigger than 3, so you get [4, 6, 8, 10]
.reduce((n1, n2) => n1 + n2) // Adds them: 4 + 6 + 8 + 10 = 28

console.log(result) // 28
```


## Nesnelerle Çalışma

<chapterId>7842aada-f009-5518-b8e3-1104e166a035</chapterId>


Bu bölümde, JavaScript'te nesnelerle çalışmak için bazı güçlü ve biraz daha gelişmiş araçlar öğreneceğiz.


### Özel Mülkler


Bazen, bir nesnenin bir özelliğini gizlemek isteriz, böylece nesne dışından değiştirilemez veya erişilemez. JavaScript, özellik adından önce `#` kullanarak bunu yapmamız için bize bir yol sunar. Bu, yalnızca sınıfın içinden erişilebilen bir **özel** özellik oluşturur.


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


Özel özellikler, yanlışlıkla yapılan değişiklikleri önlemek istediğinizde yardımcı olur.


### statik` Özellikler


Bazen, bir özelliğin o sınıftan oluşturduğunuz her nesneye değil, sınıfın kendisine ait olmasını istersiniz. İşte `static` bunun içindir. Bir `static` özelliği sınıfın içinde yer alır ve bu sınıfın tüm nesneleri ona başvurur.


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


Bu, paylaşılan verileri ve yalnızca bir nesne için değil tüm nesne grubu için geçerli olan yöntemleri depolamak için kullanışlıdır.


### `get` ve `set`


JavaScript'te `get` ve `set` normal değişkenler gibi *görünen* ama aslında arka planda özel kod çalıştıran özellikler oluşturmanızı sağlar.


Bir özelliği *okumaya* çalıştığınızda bir `get`ter yöntemi çalışır. Özelliğin adını içeren bir yöntemden önce `get` yazılarak bildirilir.


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


Her ne kadar `fullName` normal bir özellik olmasa da, onu bir özellik gibi kullanabiliriz ve perde arkasında tam adı oluşturmak için `get` fonksiyonunu çalıştırır.


Bir `set`ter yöntemi, bir özelliğe *değer atadığınızda* çalışır. Birisi bu değeri değiştirmeye çalıştığında ne olacağını kontrol etmenizi sağlar. Özelliğin adını içeren bir yöntemden önce `set` yazılarak bildirilir.


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


User.fullName = "John Smith"` yaptığımızda, `set` yöntemini çalıştırır ve `firstName` ve `lastName` değerlerini günceller.


Yani sadece basit bir değişken ayarlıyormuşuz gibi görünse de, aslında diğer özellikleri güncelleyen mantığı tetikliyoruz.


## Anahtarlar ve Değerler

<chapterId>01a397b8-c12a-5c39-82b3-6d9ebbb72a29</chapterId>


Bir JavaScript nesnesindeki her özelliğin bir **anahtarı** (özellik adı da denir) ve bir **değeri** vardır.


Örneğin:


```javascript
const user = {
name: "Alice",
age: 30
}
```


Bu nesnede, `"name"` ve `"age"` anahtarlardır ve "Alice" ve `30` da bunların değerleridir.


### Dinamik Erişim


Bazen, bir özelliğin adını önceden bilemezsiniz... belki kullanıcı girdisinden alıyorsunuzdur veya bir değişkenden okuyorsunuzdur. Yine de `myObject["keyName"]` gibi **parantez gösterimini** kullanarak erişebilirsiniz.


```javascript
const user = {
name: "Alice",
age: 30
}

console.log(user["name"]) // Alice
```


İlgili değeri elde etmek için `name` dizesini nesneye aktardık.


Bir anahtarı bir değişkene kaydedebilir ve daha sonra ilgili değere erişmek için kullanabiliriz, örneğin


```javascript
const user = {
name: "Alice",
age: 30
}

const key = "name"

console.log(user[key]) // Alice
```


### Dinamik Assignment


Ayrıca değişkenleri anahtar olarak kullanarak nesne özellikleri oluşturabilir veya güncelleyebilirsiniz.


```javascript
const settings = {}

const key = "theme"
settings[key] = "dark"

console.log(settings) // { theme: "dark" }
```


Bu, bir nesneyi adım adım oluşturmak istediğinizde yardımcı olur. Örneğin:


```javascript
const user = {}

user["username"] = "bananaFan123"
user["email"] = "banana@fruit.com"

console.log(user)
// { username: "bananaFan123", email: "banana@fruit.com" }
```


Köşeli parantez kullanarak nesneyi oluştururken * dinamik bir anahtar bile kullanabilirsiniz:


```javascript
const key = "language"
const config = {
[key]: "JavaScript"
}

console.log(config.language) // JavaScript
```


Buna **hesaplanan özellik** denir. Köşeli parantezlerin içindeki değer değerlendirilir ve sonuç anahtar olarak kullanılır.


### `Sembol` Türü


Dizelere ek olarak JavaScript, nesne anahtarı olarak `Symbol` adlı özel bir türü kullanmanıza da izin verir.


Basit bir örnekle başlayalım:


```javascript
const id = Symbol("userID")

const user = {
name: "Bob",
[id]: 12345
}

console.log(user[id]) // 12345
```


Bu örnekte, `id` bir Semboldür. Bir dize değildir, ancak yine de bir anahtar olarak çalışır. Eğer konsola `user` yazmaya çalışırsanız, şunu göreceksiniz:


```javascript
console.log(user) // { name: 'Bob', [Symbol(userID)]: 12345 }
```


Bir diğer önemli husus: oluşturduğunuz her sembol, aynı dize kullanılarak oluşturulmuş olsalar bile benzersizdir.


```javascript
const a = Symbol("label")
const b = Symbol("label")

console.log(a === b) // false
```


Semboller, normal anahtarlarla çakışmayacak anahtarlar tanımlamanıza olanak tanır. Örneğin, `name` özelliğine sahip bir nesneniz olduğunu varsayalım, ancak nesne gelecekte bir kullanıcı tarafından tahmin edemeyeceğiniz şekillerde özelleştirilebilir ve bu kullanıcı da bir `name` özelliği ekleyebilir. Eğer orijinal `name` özelliği bir string ile tanımlanmışsa, bu şekilde yeni özelliğin üzerine yazılacaktır:


```javascript
const obj = {
name: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy' }
```


Bunun yerine bir Sembol kullanırsak:


```javascript
const name = Symbol("name")

const obj = {
[name]: "John"
}

obj.name = "Jimmy"

console.log(obj) // { name: 'Jimmy', [Symbol(name)]: 'John' }
```


Gördüğünüz gibi, orijinal `name` özelliği bu şekilde bir şekilde korunur. Bu, bazı uç durumlarda faydalı olabilir.


## Yardımcı Nesneler

<chapterId>516e74c8-2a11-545a-a4d1-c2cabb91a273</chapterId>


JavaScript bize hata ayıklama ve matematik işlemleri gibi şeyleri yapmamıza yardımcı olan bazı yararlı yerleşik nesneler sunar.


### Diğer `konsol` Yöntemleri


Değerleri ekrana yazdıran `console.log` dosyasını daha önce görmüştünüz.


Programlarınızda hata ayıklamanıza yardımcı olabilecek `console` nesnesi üzerinde kullanılabilen başka yararlı yöntemler de vardır.


#### `console.warn`


Sarı renkte (veya bazı ortamlarda bir uyarı simgesiyle) bir mesaj yazdırır:


```javascript
console.warn("This is just a warning.")
```


#### `console.error`


Hata gibi kırmızı renkte bir mesaj yazdırır:


```javascript
console.error("Something went wrong!")
```


#### `console.table`


Bir diziyi veya nesneyi tablo olarak görüntüler:


```javascript
const users = [
{ name: "Alice", age: 25 },
{ name: "Bob", age: 30 }
]

console.table(users)
```


Bu, aşağıdaki gibi bir tablo yazdırır:


```
┌─────────┬────────┬─────┐
│ (index) │  name  │ age │
├─────────┼────────┼─────┤
│    0    │ 'Alice'│  25 │
│    1    │ 'Bob'  │  30 │
└─────────┴────────┴─────┘
```


Bu, yapılandırılmış verileri görselleştirmek için yararlı olabilir.


#### `console.time` ve `console.timeEnd`


Bir şeyin ne kadar sürdüğünü ölçebilirsiniz:


```javascript
console.time("timer")
for (let i = 0; i < 1000000; i++) {}
console.timeEnd("timer")
```


Bu, aşağıdaki gibi bir şey yazdırır:


```
timer: 2.379ms
```


Bazı basit performans testleri için kullanışlıdır.


### Math` Nesnesi


JavaScript size hesaplamalar yapmak için kullanışlı yöntemlere sahip bir `Math` nesnesi verir.


#### `Math.random()`


0 (dahil) ile 1 (hariç) arasında rastgele bir sayı döndürür:


```javascript
const r = Math.random()
console.log(r)
```


Örnek çıktı:


```
0.4387429859
```


#### `Math.floor()` ve `Math.ceil()`



- math.floor(n)` en yakın tamsayıya **düşürerek** yuvarlar
- math.ceil(n)` **yukarı** en yakın tam sayıya yuvarlar


```javascript
console.log(Math.floor(4.9)) // 4
console.log(Math.ceil(4.1))  // 5
```


#### `Math.round()`


En yakın tamsayıya yuvarlar:


```javascript
console.log(Math.round(4.4)) // 4
console.log(Math.round(4.6)) // 5
```


#### `Math.max()` ve `Math.min()`


Bir sayı listesinden en büyük veya en küçük değeri döndürür:


```javascript
console.log(Math.max(5, 9, 3)) // 9
console.log(Math.min(5, 9, 3)) // 3
```


#### `Math.pow()` ve `Math.sqrt()`



- `Math.pow(a, b)` size `b`nin kuvveti kadar `a` verir
- `Math.sqrt(n)` size `n`nin karekökünü verir


```javascript
console.log(Math.pow(2, 3))   // 8
console.log(Math.sqrt(16))    // 4
```


# Gelişmiş JavaScript

<partId>72c30671-ca20-5617-92a5-d5ba7aa38c93</partId>


## Diğer koleksiyonlar

<chapterId>a9a70c6d-a343-5a46-a383-e288bc2700e3</chapterId>


JavaScript bize normal dizilerin ve nesnelerin ötesine geçen bazı özel koleksiyon türleri sunar. Bunlar arasında `Map` ve `Set` yer alır.


Değer gruplarını saklamanıza ve yönetmenize yardımcı olurlar, ancak şimdiye kadar gördüklerinizden farklı çalışırlar.


Bir `Map`, tıpkı bir nesne gibi **anahtar-değer çiftleri** koleksiyonudur. Ancak bazı önemli farklılıkları vardır:



- Anahtarlar sadece dizeler değil **herhangi bir değer** olabilir.
- Öğelerin sırası korunur.
- Onunla çalışmayı kolaylaştırmak için yerleşik yöntemleri vardır.


Bunun gibi yeni bir harita oluşturursunuz:


```javascript
const myMap = new Map()
```


Bu boş bir harita oluşturur. Buna girdi eklemek için `myMap.set(key, value)` kullanın:


```javascript
myMap.set("name", "Alice")
```


Bu, `"Alice"` değerine sahip bir `"name"` anahtarı ekler.


Anahtar olarak bir sayı da kullanabilirsiniz:


```javascript
myMap.set(42, "The answer")
```


Ve hatta anahtar olarak bir nesne:


```javascript
const objKey = { id: 1 }
myMap.set(objKey, "Object as key")
```


Bu, yalnızca dize anahtarlarına izin veren normal nesnelerle çalışmaz.


Bir **değer** almak için `myMap.get(key)` kullanın:


```javascript
console.log(myMap.get("name"))     // Alice
console.log(myMap.get(42))         // The answer
console.log(myMap.get(objKey))     // Object as key
```


Bir anahtarın var olup olmadığını kontrol etmek** için `myMap.has(key)` kullanın:


```javascript
console.log(myMap.has("name")) // true
```


Bir anahtarı **kaldırmak** için `myMap.delete(key)` kullanın:


```javascript
myMap.delete("name")
```


Tüm haritayı **temizlemek** için `myMap.clear()` işlevini kullanın:


```javascript
myMap.clear()
```


Haritalar büyük değer koleksiyonlarını yönetmek için harikadır, çünkü büyük bir haritadaki değerlere erişmek genellikle büyük bir nesneden çok daha iyi performans sağlar.


### `Set`


Bir `Set`, her bir değerin **tek** olması gereken, yalnızca **değerlerden** (anahtar yok) oluşan bir koleksiyondur. Bu şu anlama gelir:



- Aynı değere iki kez sahip olamazsınız
- Değerler, onları eklediğiniz sırayla saklanır


Bunun gibi bir set oluşturursunuz:


```javascript
const mySet = new Set()
```


Değer eklemek** için `mySet.add(value)` kullanın:


```javascript
mySet.add(1)
mySet.add(2)
mySet.add(2) // duplicate, will be ignored
```


2`yi iki kez eklemeye çalışmamıza rağmen, küme yalnızca bir kopya tutacaktır.


Bir değerin sette olup olmadığını kontrol etmek** için `mySet.has(value)` kullanın:


```javascript
console.log(mySet.has(2)) // true
console.log(mySet.has(3)) // false
```


Bir değeri **kaldırmak** için `mySet.delete(value)` kullanın:


```javascript
mySet.delete(2)
```


Her şeyi** temizlemek için `mySet.clear()` işlevini kullanın:


```javascript
mySet.clear()
```


Bir `Set`, yinelenenleri manuel olarak kontrol etmek zorunda kalmadan benzersiz değerlerden oluşan bir koleksiyon tutmak istediğinizde kullanışlıdır:


```javascript
const numberArray = [1, 2, 2, 3, 4, 4, 4, 5]

const numberSet = new Set(numberArray)

console.log(numberSet) // Set(5) { 1, 2, 3, 4, 5 }
```


Set` sizin için kopyaları önler.


## Yineleyiciler

<chapterId>61d24e5e-b7e4-541a-8322-778f61f26a72</chapterId>


JavaScript'te üzerinde döngü yapabileceğiniz çoğu şey (diziler, dizeler, haritalar, kümeler gibi) **iterable**'dır: içerikleri için yineleyiciler sağlayabilirler.


Bir **iterator**, JavaScript'te bir öğe listesinde **her seferinde bir tane olmak üzere** ilerlemenize yardımcı olan özel bir nesnedir.


### `Object` yineleyicileri


Dizilerin veya haritaların aksine, normal nesneler `for...of` ile yinelenemez**. Eğer bunu denerseniz:


```javascript
const user = {
name: "Alice",
age: 30
}

for (const value of user) {
console.log(value)
}
```


Bir hata alacaksınız:


```
TypeError: user is not iterable
```


Bunun nedeni, düz nesnelerin yerleşik bir yineleyiciye sahip olmamasıdır. Ancak JavaScript size bunlar üzerinde döngü oluşturmanız için başka araçlar sunar.


#### `Object.keys()`


Nesnenin **anahtarlarından** oluşan bir dizi elde etmek için `Object.keys(obj)` öğesini kullanabilir ve ardından bunun üzerinde döngü oluşturabilirsiniz:


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


Bu baskılar:


```
name
age
```


#### `Object.values()`


Değerler** üzerinde döngü yapmak için `Object.values()` işlevini kullanın:


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


Bu baskılar:


```
Alice
30
```


#### `Object.entries()`


Eğer **hem anahtar hem de değer** istiyorsanız, `Object.entries()` işlevini kullanın:


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


Bu baskılar:


```
name is Alice
age is 30
```


Nesneler doğrudan yinelenebilir olmasa da, bu yöntemler `for...of` ile iyi çalışan bir şekilde içeriklerine tam erişim sağlar.


Peki yineleyiciler nasıl çalışır?


### `Symbol.iterator`


Tüm yinelenebilirlerin arkasındaki sır, `Symbol.iterator` adı verilen özel bir **semboldür**.


Bu sembol JavaScript'e şunu söyleyen yerleşik bir anahtardır: "Bu nesne yinelenebilir."


MyIterable[Symbol.iterator]()` öğesini çağırdığınızda, JavaScript size `.next()` yöntemine sahip bir **iterator nesnesi** geri verir.


Bakalım bu neye benziyor:


```javascript
const colors = ["red", "green", "blue"]

const iterator = colors[Symbol.iterator]()

console.log(iterator.next()) // { value: 'red', done: false }
```


Her `.next()` çağrısı size bir sonraki değeri verir. İşi bittiğinde geri döner:


```javascript
{ value: undefined, done: true }
```


### `next()`


.next()` yöntemi, diziden bir sonraki öğeyi almak için kullanılır.


Her `.next()` çağrısında iki anahtarlı bir nesne elde edersiniz:



- `value`: geçerli öğe
- `done`: yinelemenin bitip bitmediğini söyleyen bir boolean


Tam bir örnek yapalım:


```javascript
const names = ["Lina", "Tom", "Eva"]      // declare an array
const iterator = names[Symbol.iterator]() // use the Symbol.iterator function to get an iterator for this array

let result = iterator.next()              // get the first element of the array

while (!result.done) {                    // repeat this loop until you reach the last element of the array, which is marked with { done: true }
console.log(result.value)               // print the value of each element
result = iterator.next()                // get the next element of the array
}
```


Bu baskılar:


```
Lina
Tom
Eva
```


Bir `for...of` döngüsü kaputun altında bu şekilde çalışır: `.next()` ile bu kalıbı kullanır.


Ile aynı sonucu elde edersiniz


```javascript
const names = ["Lina", "Tom", "Eva"]

for (const result of names) {
console.log(result)
}
```


### Bir sınıfı yinelenebilir yapma


Ayrıca bir `[Symbol.iterator]()` yöntemi ekleyerek kendi **iterable sınıfınızı** tanımlayabilirsiniz.


Diyelim ki 1'den 5'e kadar bir **sayı aralığını** temsil eden bir sınıf istiyoruz.


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


Bu baskılar:


```
1
2
3
4
5
```


İşte olanlar:



- Bir `Range` sınıfı tanımladık
- Sınıfın içinde `[Symbol.iterator]()` fonksiyonunu uyguladık, böylece JavaScript nasıl yineleyeceğini biliyor
- Next()` yöntemi her bir sayıyı tek tek geri verir
- Son`a ulaştığımızda, `{ done: true }` döndürür


Artık `Range` sınıfımız bir dizi gibi çalışır ve onu bir yinelenebilir bekleyen herhangi bir döngüde kullanabiliriz.


### Üreteç fonksiyonları ve `verim`


Yineleyiciler oluşturmayı kolaylaştırmak için JavaScript, `function*` anahtar sözcüğünü (sonunda `*` olan `function`) ve `yield` anahtar sözcüğünü kullanarak size **üretici işlevler** sunar.


Hadi deneyelim:


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


Her `yield` geri bir değer verir ve bir sonraki `.next()` çağrılana kadar fonksiyonu **duraklatır**.


Ayrıca `for...of` ile bir üreteç üzerinde döngü yapabilirsiniz:


```javascript
for (const num of numberGenerator()) {
console.log(num)
}
```


Bu baskılar:


```
1
2
3
```


## Geri aramalar ile eşzamanlılık

<chapterId>f3fc76ca-b3ef-54eb-a06e-501007002054</chapterId>


Şimdiye kadar, kodumuz **eşzamanlı** idi: her seferinde bir satır, sırayla çalışır. Ancak gerçek dünyada bazı şeyler zaman alır ve beklerken tüm programın duraklamasını istemeyiz.


Bu bölümde yeni bir kavramı tanıtacağız: **eşzamanlılık**. Bu, işlerin yapılma sırasını değiştirmemizi sağlar. Bu, zamanlayıcılar, kullanıcı girdisi veya diskten dosya okuma gibi şeylerle uğraşırken kullanışlıdır. JavaScript eşzamanlılık için farklı araçlar sunar.


### `setTimeout`


SetTimeout` fonksiyonu, bir fonksiyonu belli bir süre geçtikten sonra **daha sonra** çalıştırmanızı sağlar.


Örnek:


```javascript
console.log("Start")

setTimeout(
() => console.log("This runs after 2 seconds"),
2000
)

console.log("End")
```


Bu baskılar:


```
Start
End
This runs after 2 seconds
```


SetTimeout` kodun ortasında görünse de, geri kalanını engellemez. Bunun yerine, işlevi **daha sonra** çalışacak şekilde programlar ve hemen devam eder.


2000` 2000 milisaniye (yani 2 saniye) anlamına gelir.

İşte **Callbacks** ve **Promise** bölümlerinin veri manipülasyonu ve açık ek açıklamalar kullanılarak daha ayrıntılı ve yeni başlayanlara uygun bir şekilde yeniden yazılması:


### Geri aramalar


Bir **callback** sadece başka bir fonksiyona verdiğimiz bir fonksiyondur, böylece **daha sonra** çağrılabilir.


Sayıları kullanan gerçek bir örneğe bakalım. Elimizde sayılardan oluşan bir liste olduğunu ve her birini ikiye katlamak istediğimizi ve ardından ortaya çıkan "ikiye katlanmış" diziye bir işlev (geri arama) uygulamak istediğimizi, ancak bunu yavaş bir şey bekliyormuşuz gibi (internetten veri yüklemek gibi) küçük bir gecikmeden sonra yapmak istediğimizi hayal edin.


İşte bunu bir **callback** kullanarak yapan bir fonksiyon:


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


Bu fonksiyonu kullanmayı deneyelim:


```javascript
const input = [1, 2, 3]

doubleNumbers(input, function(result) {
console.log("Here is the doubled array:", result)
})
```


1 saniye sonra bu yazdırılır:


```
Here is the doubled array: [ 2, 4, 6 ]
```


**Burada neler oluyor?


1. Giriş`i ikiye katlamak istediğimiz sayıların listesi olarak iletiyoruz.

2. Ayrıca programa *ikiye katlamadan* sonra ne yapacağını söyleyen bir **geri çağırma işlevi** iletiyoruz.

3. DoubleNumbers` içinde, `setTimeout` kullanarak bir gecikme simülasyonu yaparız, ardından ikiye katlama işlemini gerçekleştiririz.

4. Bu işlem tamamlandıktan sonra, ortaya çıkan "ikiye katlanmış" dizi üzerinde geri çağırmayı çağırırız.


Bu teknik işe yarar, ancak bundan sonra **daha fazla adım** yapmak istediğinizi düşünün, örneğin küçük sayıları filtrelemek ve ardından bunları toplamak gibi. Bunun gibi daha fazla geri arama **yuvası** yapmanız gerekir:


```javascript
doubleNumbers(input, function(doubled) {
filterBigNumbers(doubled, function(filtered) {
sumNumbers(filtered, function(total) {
console.log("Final result:", total)
})
})
})
```


Bu, okunması Hard ve dağınıktır. Bu tarza **callback hell** denir ve `Promise` tam da bu durumu düzeltmek için yaratılmıştır.


## Vaatlerle Eşzamanlılık

<chapterId>30fddaca-729f-5c8d-bf86-8dfc7b3c9800</chapterId>


Bir `Promise`, **gelecekte hazır olacak** bir değeri temsil eden yerleşik bir JavaScript nesnesidir.


Bunun gibi bir Söz oluşturabiliriz:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve("It worked!") // This means everything went OK
})
```


New Promise()` kısmı vaadi oluşturur.


İçinde, iki parametreli bir fonksiyon veriyoruz:



- `resolve`, her şey başarılı olduğunda çağırdığımız bir işlevdir
- `reject`, bir şeyler ters gittiğinde çağırdığımız bir işlevdir


Yukarıdaki örnekte, `"İşe yaradı!"` mesajıyla hemen çözüyoruz.


### `.then()`


Söz verildikten **sonra** bir şey yapmak için `.then()` işlevini kullanırız:


```javascript
const promise = new Promise((resolve, reject) => {
// Do something that takes time here...

resolve(100) // This means everything went OK
})

promise.then(result => {
console.log("The result is:", result)
})
```


Bu baskılar:


```
The result is: 100
```


Resolve()` fonksiyonuna aktardığımız değer `.then()` içindeki fonksiyona `result` olarak gönderilir.


Şimdi `setTimeout` kullanarak 2 saniye süren bir görevi simüle edelim:


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


Bu işlem 2 saniye bekleyecek ve ardından yazdıracaktır:


```
Done waiting!
```


### `reject()`


Hadi **başarısız** olan bir söz yaratalım:


```javascript
const failingPromise = new Promise((resolve, reject) => {
reject("Something went wrong")
})
```


Şimdi bunun üzerinde `.then()` kullanırsak hiçbir şey olmayacaktır, çünkü `.then()` yalnızca başarıyı işler.


Hataları işlemek için `.catch()` işlevini kullanırız:


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


Bu yalnızca


```
Caught an error: Something went wrong
```


Reject()` fonksiyonuna aktarılan değer `.catch()` fonksiyonuna gönderilir.


Bazı koşullara bağlı olarak **bazen çalışan ve bazen başarısız olan** bir Söz oluşturalım.


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


Şimdi bunu çağırabilir ve her iki durumu da ele alabiliriz:


```javascript
checkNumber(5)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Bu baskılar:


```
Success: Positive number
```


Ve eğer farklı bir numarayla denersek:


```javascript
checkNumber(-1)
.then(
msg => console.log("Success:", msg)
)
.catch(
err => console.log("Failure:", err)
)
```


Yazıyor:


```
Failure: Not a positive number
```


### Promise`s kullanarak zincirleme işlemler



Daha önceki örneğimizi `Promise` kullanarak yeniden yazabiliriz ve çok daha temiz görünecektir.


İkiye katlama fonksiyonumuzun yeni bir versiyonunu yazarak başlayalım, ancak bu sefer fonksiyon bir **söz** döndürüyor:


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


Şimdi JavaScript'e sonuçla ne yapacağını söylemek için `.then()` işlevini kullanabiliriz:


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


Bu baskılar:


```
Doubled numbers: [ 2, 4, 6 ]
```


Şimdiye kadar, bu geri arama sürümüyle aynı şekilde çalışıyor, ancak şimdi kodun genişletilmesi ve okunması daha kolay.


Diyelim ki daha fazla adım eklemek istiyoruz:


1. İlk olarak, tüm sayıları iki katına çıkarın

2. Ardından, 4'ten küçük sayıları kaldırın

3. Son olarak, hepsini bir araya getirin


Her adım için bir fonksiyon yazabiliriz, hepsi de vaatleri kullanır:


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


Şimdi onları bu şekilde birbirine **zincirleyebiliriz**:


```javascript
const input = [1, 2, 3]

doubleNumbers(input)
.then(filterBigNumbers)
.then(sumNumbers)
.then(
result => console.log("Final result after all steps:", result)
)
```


Bu baskılar:


```
Final result after all steps: 10
```


Bunun ne işe yaradığını inceleyelim:


1. `doubleNumbers` diziyi ikiye katlar: `[2, 4, 6]`

2. `filterBigNumbers` ≤ 3 olan her şeyi kaldırır: `[4, 6]`

3. `sumNumbers` kalan sayıları toplar: `4 + 6 = 10`

4. Son olarak, sonucu yazdırıyoruz.


Her `.then()` kendisinden önceki adımın bitmesini bekler. Böylece iç içe geçmeden bir **eylem zinciri** oluşturabiliriz. Bu, kodu daha okunabilir ve hata ayıklamayı daha kolay hale getirir.


## Async`/`await` ile eşzamanlılık

<chapterId>6e93d29f-c8bf-5fd1-a9c9-4e794ee6cbd0</chapterId>


Promise` zincirlerinin geri arama cehenneminden kaçınmamıza nasıl yardımcı olduğunu gördük, ancak yine de birçok adım söz konusu olduğunda okuması biraz Hard olabilir.


İşte `async` ve `await` burada devreye girer. Bunlar **senkron kod gibi görünen** asenkron kod yazmamızı sağlar, bu da anlaşılmasını kolaylaştırır.


### Async` nedir?


Bir fonksiyondan önce `async` anahtar sözcüğünü yazdığınızda, JavaScript fonksiyonun dönüş değerini otomatik olarak bir Promise'e sarar.


Basit bir örnek görelim:


```javascript
async function greet() {
return "hello"
}
```


Bu işlevi çağırırsanız:


```javascript
const result = greet()
console.log(result)
```


Bunu göreceksin:


```
Promise { 'hello' }
```


Sadece bir string döndürmüş olsanız bile, JavaScript bunu sizin için bir Promise'e dönüştürür. Gerçek değeri aşağıdaki gibi `.then()` kullanarak alabilirsiniz:


```javascript
greet().then( result => console.log(result) ) // prints "hello"
```


Ya da `await` kullanabilirsiniz...


### Beklemek' nedir?


Anahtar kelime `await` JavaScript'e şunu söyler: "Bu Promise tamamlanana kadar bekle ve sonra bana sonucu ver."


Ancak `await`i yalnızca **bir asenkron fonksiyonun içinde** kullanabilirsiniz.


Örneği `await` kullanarak yeniden yazalım:


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


Şimdi sonucu normal bir değermiş gibi kullanabiliriz.


Şimdi biraz daha faydalı bir şey yapalım.


### Gecikmeyi `await` ile simüle etme


Argüman olarak bir milisaniye alan ve başka hiçbir şey yapmadan sadece bu kadar milisaniye sonra çözümleyen basit bir `wait` fonksiyonu oluşturacağız:


```javascript
function wait(ms) {
return new Promise(resolve => {
setTimeout(resolve, ms)
})
}
```


Kullanmayı deneyelim:


```javascript
async function test() {
console.log("waiting 2 seconds...")
await wait(2000)
console.log("done waiting")
}

test()
```


Bu baskılar:


```
waiting 2 seconds...
done waiting
```


'Bekle'yi "söz tamamlanana kadar burada dur, sonra devam et" olarak düşünebilirsiniz


Bu, `.then()` çağrılarını zincirlemeden eşzamansız olarak davranan **üstten alta** bir şekilde kod yazmanıza olanak tanır.


### Veri bekleniyor


Sayıları ikiye katladığımız, sonra filtrelediğimiz ve sonra topladığımız önceki örneğimizi tekrar kullanalım. Ancak bu sefer `async`/`await` kullanacağız.


Beklemeyi simüle eden ve Promise döndüren 3 fonksiyon oluşturacağız:


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


Şimdi bunları birleştirmek için bir `async` fonksiyonu yazalım:


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


Bu baskılar:


```
Final result: 10
```


Bu, zincirleme `.then()` veya iç içe geçmiş geri aramalardan çok daha kolay okunur.


Normal bir adım adım program gibi görünür, ancak yine de asenkron olarak davranır.


## Async Yineleyiciler

<chapterId>438b037d-9931-56d7-9052-7b4470f3c75b</chapterId>


Yineleyicileri** ve diziler ve diğer yinelenebilir şeyler üzerinde döngü yapmak için `for...of`u nasıl kullanabileceğimizi zaten öğrendiniz.


Peki ya üzerinde yineleme yapmak istediğimiz verilerin ulaşması zaman alıyorsa?


Bazen bir sohbetten gelen mesajlar, bir dosyadan gelen satırlar veya yavaş bir kaynaktan gelen sayılar gibi **eşzamansız** olarak gelen şeyler üzerinde döngü yapmak isteriz.


Bunu yapmak için JavaScript bize **async yineleyicileri** sunar.


### Asenkron jeneratör fonksiyonları


Bir asenkron yineleyici oluşturmanın en kolay yolu bir **asenkron üreteç işlevi** kullanmaktır.


Bu şekilde yazıyoruz:


```javascript
async function* generateNumbers() {
yield 1
yield 2
yield 3
}
```


Bu tıpkı normal bir üreteç gibi görünür, ancak önünde `async` vardır.


Artık değerleri tüketmek için `for await...of` kullanabiliriz:


```javascript
async function run() {
for await (const n of generateNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


Bu yazdırılacaktır:


```
Got number: 1
Got number: 2
Got number: 3
Done!
```


Peki normal bir jeneratörle arasındaki fark nedir?


Aradaki fark şudur: artık üretecin içinde `await` kullanabiliriz.


Tekrar bir gecikme yardımcısı yapalım:


```javascript
function wait(ms) {
return new Promise(resolve => setTimeout(resolve, ms))
}
```


Şimdi **yavaşça** sayıları verelim:


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


Kullanmayı dene:


```javascript
async function run() {
for await (const n of generateSlowNumbers()) {
console.log("Got number:", n)
}

console.log("Done!")
}

run()
```


### Neden async yineleyiciler kullanılmalı?


Async yineleyiciler şu durumlarda kullanışlıdır:



- Değerlerin hepsi aynı anda gelmez.
- Bunları teker teker, **geldiği gibi** ele almak istersiniz.
- Sözler ile çalışıyorsunuz ve temiz bir şekilde döngü yapmak istiyorsunuz.


Örneğin, bir sohbet sunucusundan mesajları tek tek yüklemek veya büyük bir dosyayı parçalar halinde indirmek istiyorsanız, async iterators size gecikmeli verilerle çalışan bir `for` döngüsü yazmanın bir yolunu sunar.


### `Symbol.asyncIterator`


Async yineleyicileri özel sınıflarda da kullanabiliriz.


İşte gecikmeli sayılar üreten bir örnek:


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


Artık daha önce olduğu gibi `for await...of` kullanabiliriz:


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


Bu, üzerinde eşzamansız olarak yinelenebilen nesneler oluşturmanıza olanak tanır


## Assignment sözdizimi şekeri

<chapterId>8b1ba7d8-ecfd-5470-b86e-73cb84ccc8b7</chapterId>


"Sözdizimi şekeri", bir şeyin ne yaptığını değiştirmeden daha kısa veya daha kolay bir şekilde yazılması anlamına gelir. Bu sadece aynı şeyi söylemenin daha güzel bir yoludur.


JavaScript, daha temiz ve daha kısa bildirimler yazmamızı sağlayan bazı yerleşik sözdizimi şekerlerine sahiptir. Bu bölümde, bir koşula göre nasıl değer atayacağımızı, değişkenleri matematikle nasıl güncelleyeceğimizi, dizilerden veya nesnelerden nasıl değer çekeceğimizi ve bunları daha basit sözdizimiyle nasıl kopyalayacağımızı veya birleştireceğimizi inceleyeceğiz.


### Üçlü Operatör


JavaScript'te, `if...else' yazmanın kısa bir yolu olan **ternary operatörünü** kullanarak bir koşula dayalı olarak bir değer atayabilirsiniz.


Yapmak yerine:


```javascript
let message

if (isMorning) {
message = "Good morning"
} else {
message = "Hello"
}
```


Yazabilirsin:


```javascript
const message = isMorning ? "Good morning" : "Hello"
```


Bu şu anlama geliyor:



- Eğer `isMorning` true ise, `"Günaydın"` kullanın
- Aksi takdirde, `"Merhaba"` kullanın


Genel form şöyledir:


```javascript
condition ? valueIfTrue : valueIfFalse
```


Diğer ifadelerin içinde de kullanabilirsiniz:


```javascript
console.log(isSunny ? "Go outside" : "Stay in")
```


Sadece **basit** kararlar için kullandığınızdan emin olun. Eğer mantık karmaşıksa, `if...else` ile devam edin.


### Alternatif Assignment Operatörleri


JavaScript, işlemlerle birlikte atamalar yapmak için **kısayol operatörlerine** sahiptir.


Normal yola bakalım:


```javascript
let counter = 1
counter = counter + 1
```


Bu şu şekilde kısaltılabilir:


```javascript
let counter = 1
counter += 1 // same as counter = counter + 1
```


İşte en yaygın olanları:


| Operator | Meaning             |
| -------- | ------------------- |
| `+=`     | add and assign      |
| `-=`     | subtract and assign |
| `*=`     | multiply and assign |
| `/=`     | divide and assign   |

Örnekler:


```javascript
let score = 10
score += 5  // now score is 15
score *= 2  // now score is 30
score -= 10 // now score is 20
```


Bunlar, bir değişkeni kendi değerini kullanarak güncellemek istediğinizde kullanışlıdır.


### Yıkım


**Destructuring** değerleri dizilerden veya nesnelerden alıp kolayca değişkenlerde saklamanızı sağlar.


#### Diziler


Diyelim ki var:


```javascript
const colors = ["red", "green", "blue"]
```


Yapmak yerine:


```javascript
const first = colors[0]
const second = colors[1]
```


Yapabilirsin:


```javascript
const [first, second] = colors
```


Bu atama:



- `first` ile `"red"` arasında
- `ikinci` ila `"Green"`


Değerleri de atlayabilirsiniz:


```javascript
const [,, third] = colors
console.log(third) // blue
```


#### Nesneler


Nesnelerden de değer çıkarabilirsiniz:


```javascript
const user = { name: "Alice", age: 30 }

const { name, age } = user
console.log(name) // Alice
console.log(age)  // 30
```


Özelliğin istediğiniz değişkenden farklı bir adı varsa, onu yeniden adlandırabilirsiniz:


```javascript
const { name: username } = user
console.log(username) // Alice
```


Destructuring, nesneler ve dizilerle çalışırken kodunuzun daha temiz olmasını sağlar.


### Yayılma Sözdizimi


Spread sözdizimi** değerleri açmak veya kopyalamak için `...` kullanır.


#### Diziler


Dizileri kopyalayabilir veya birleştirebilirsiniz:


```javascript
const a = [1, 2]
const b = [3, 4]

const both = [...a, ...b]
console.log(both) // [1, 2, 3, 4]
```


Bir diziyi de klonlayabilirsiniz:


```javascript
const original = [10, 20, 30]
const clone = [...original]
```


#### Nesneler


Aynı şeyi nesneler için de yapabilirsiniz:


```javascript
const a = { x: 1 }
const b = { y: 2 }

const merged = { ...a, ...b }
console.log(merged) // { x: 1, y: 2 }
```


Ayrıca değerleri geçersiz kılabilirsiniz:


```javascript
const user = { name: "Alice", age: 30 }
const updated = { ...user, age: 31 }

console.log(updated) // { name: "Alice", age: 31 }
```


Bu, orijinali değiştirmeden nesneleri güncellerken çok kullanışlıdır.


# NodeJS

<partId>42fe4d49-dace-5135-bb9e-b9d75034fb2a</partId>


## Node'a nasıl ulaştık

<chapterId>0da1d60c-06c9-54e6-a181-ae7dabf6e3b8</chapterId>


Bu bölümde JavaScript ve NodeJS hakkında biraz tarihsel bağlam öğreneceğiz.


Yazılımda tarihsel bağlam çok önemlidir, çünkü genellikle başkaları tarafından üretilen araçları kullanırız ve bu nedenle geçmişte onlar tarafından alınan kararlardan etkileniriz.


Bu kararların nedenini ve kullandığımız araçların nasıl bu hale geldiğini anlamak, ne yaptığımız konusunda kafamızın biraz daha az karışmasına yardımcı olacaktır.


### JavaScript'in Kökenleri


JavaScript, web sayfalarını etkileşimli hale getirmek için tasarlanmış basit bir dil olarak başladı.


1990'larda, Netscape Navigator gibi web tarayıcıları JavaScript'i ekledi, böylece geliştiriciler doğrudan tarayıcıda çalışan kod yazabildi.


Orijinal fikir, Java'nın web siteleri yapmak için temel dil olması ("Java uygulamaları" ile) ve JavaScript'in sadece küçük şeyler için olmasıydı.


Çekirdek tasarım, o sırada Netscape'te çalışan Brendan Eich tarafından 2 haftadan kısa bir sürede yapıldı.


Ancak çoğu insan Java yerine JavaScript kullanmayı tercih etti ve ayrıca Java uygulamalarının o zamanlar bazı güvenlik sorunları vardı, bu nedenle sonunda Java bir seçenek olarak bırakıldı ve JavaScript web geliştirme için fiili standart haline geldi.


### V8 motor


JavaScript, C gibi derlenmiş dillerin aksine yorumlanmış bir dildir.


Derlenmiş bir dilde yazılan kod bir ikiliye dönüştürülür ve ikili doğrudan bilgisayarın CPU'suna beslenir.


![](assets/en/6.webp)


Öte yandan, interpred diller daha kullanıcı dostu olma eğilimindedir ve makinelerin nasıl çalıştığından ("düşük seviye") ziyade insanların nasıl düşündüğüne ("yüksek seviye") daha yakındır; bu nedenle genellikle kodlarını çalıştırmak için oluşturulmuş bir sanal makineye sahiptirler.


Sanal makine, yazdığınız kod ile CPU arasında yer alan ve kodunuzu çalıştıran özel bir programdır (çünkü CPU bunu anlayamaz).


Bu, altta yatan makine hakkında çok fazla bilgi sahibi olmadan programlama yapmanızı sağlar, ancak performans açısından da bir maliyeti vardır, çünkü bilgisayar sadece sizin programınızı çalıştırmaz; programınızı çalıştıran bir programı (sanal makine) çalıştırır.


Web uygulamaları giderek daha karmaşık hale geldikçe, JavaScript'in performansını artırmaya yönelik talepler ortaya çıktı. V8 motoru, Google Chrome'da JavaScript'e güç veren yorumlayıcıdır. Google'da geliştirilmiş ve 2008 yılında piyasaya sürülmüştür.


Eski JavaScript motorları çoğunlukla geleneksel sanal makineler iken, V8 motoru bir JIT (just-in-time) derleyicisidir.


JavaScript kodu V8 motoruna aktarılır ve motor kodun bazı kısımlarını anında yerel ikili dosyalar olarak derlemeye çalışır. Bu, düşük seviyeli dillere biraz daha yakın bir performansla yüksek seviyeli bir dil deneyimine sahip olmanızı sağlar. Bu da JavaScript'i dünyanın en hızlı yüksek seviyeli dili haline getirmiştir, bir nevi "her iki dünyanın da en iyisi".


### NodeJS çalışma zamanı


Kullanımı kolay ve yürütmesi oldukça hızlı olsa da, V8'in piyasaya sürülmesinden sonra JavaScript büyük bir sınırlamaya sahip olmaya devam etti: yalnızca bir tarayıcı içinde çalışabiliyordu.


Bu neden bir sorun olsun ki?


Tarayıcılar internetteki milyonlarca farklı kaynaktan getirilen kodları çalıştırdıkları için kolayca kötü amaçlı yazılımlara maruz kalabilirler, bu nedenle işletim sisteminin geri kalanından "korumalı alana" alınmışlardır.


![](assets/en/7.webp)


JavaScript bilgisayarınızdaki dosya sistemine ve diğer yerel kaynaklara erişemezdi (en azından diğer diller gibi kolayca erişemezdi), bu nedenle bu, onunla ne tür uygulamalar oluşturabileceğiniz konusunda önemli bir sınırlamaydı.


2009 yılında Ryan Dahl, V8 motorunu tarayıcı dışında, doğrudan bilgisayarınızın yerel işletim sisteminde kullanmanıza olanak tanıyan bir çalışma zamanı olan NodeJS'yi yayınladı. Ayrıca sunucu tarafı ve komut satırı programları yazmak için yararlı olan birçok özellik ekler. Örneğin, NodeJS'yi bir web sunucusu oluşturmak, dosyaları okumak ve yazmak veya görevleri otomatikleştiren araçlar oluşturmak için kullanabilirsiniz.


![](assets/en/8.webp)


Bu kursta şimdiye kadar hem tarayıcıda hem de NodeJS'de bulunan JavaScript özelliklerini keşfettik. Bu özellikler verileri tanımlamamızı ve soyut yollarla manipüle etmemizi sağladı. Önümüzdeki birkaç derste, NodeJS'ye özgü olan ve işletim sistemiyle etkileşime girmemizi sağlayan özellikleri keşfedeceğiz.


## Komut satırı argümanları

<chapterId>960d20f3-c424-5d51-a041-ef17d2e94b6d</chapterId>


NodeJS, diğer şeylerin yanı sıra, CLI'lar (Komut Satırı Arayüzleri) oluşturmamıza olanak tanır.


Bunun için komut satırı argümanlarını almak için bir yola ihtiyacımız var, bu da Node'da yerleşik `process` nesnesi kullanılarak yapılır.


### `process`


NodeJS, mevcut çalışan programı temsil eden `process` adlı özel bir nesne sağlar.


Ortamı, geçerli çalışma dizinini incelemek ve hatta gerektiğinde programdan çıkmak için kullanabilirsiniz.


Örneğin:


```javascript
console.log(process.platform)
```


Bu, `win32`, `linux` veya `darwin` (Mac) gibi işletim sistemi platformunu yazdırır.


### `process.argv`


Terminalden bir NodeJS programı çalıştırdığınızda, kod adından sonra ekstra kelimeler (argümanlar) geçebilirsiniz. Bunlar `process.argv` içinde saklanır.


Örneğin, bu komutu çalıştırırsanız:


```
node my_script.js alpha beta
```


Argümanları şu şekilde yazdırabilirsiniz:


```javascript
console.log(process.argv)
```


Çıktı şu şekilde görünebilir:


```
[ '/path/to/node', '/path/to/my_script.js', 'alpha', 'beta' ]
```


İlk iki öğe her zaman Node yolu ve kod yolunuzdur. Komut dosyasına aktardığınız tüm ek kelimeler bundan sonra gelir.


Process.argv` dizisi, `.slice()` yöntemi kullanılarak herhangi bir dizi gibi kesilebilir, bu nedenle yalnızca geçirilen argümanları almak için şunları yapabilirsiniz


```javascript
const args = process.argv.slice(2)

console.log(args)
```


Kullanıcının ilettiği argümanlara erişmek, komut satırı uygulamaları geliştirmek için esastır.


## Modüller

<chapterId>4e1651a5-65fd-50bc-b22a-40313d5659ca</chapterId>


NodeJS gibi JavaScript çalışma zamanları genellikle her JavaScript dosyasını ayrı bir modül olarak ele alır.


Modülü bir kutu olarak düşünün. Kutunun kendi özel alanı vardır, bu nedenle içinde bildirdiğiniz değişkenler ve işlevler diğer kutulardaki kodla etkileşime girmez. Temel olarak, her modülün kendi kapsamı vardır.


Bir modül, içeriğinin bir kısmını dışa aktararak diğer modüllerin kullanımına sunabilir ve diğer modüllerin dışa aktardığı içeriği içe aktarabilir. JavaScript, farklı dosyaları birbirine bağlamak için modüller arasında içeriği dışa ve içe aktarmanıza olanak tanır.


Bir JavaScript programı genellikle birbiriyle bağlantılı birden fazla modülden oluşur.


Neden modüller kullanılmalı? Kodunuzu modüllere ayırarak, programınızı daha küçük, daha net ve yeniden kullanılabilir parçalar halinde düzenleyebilirsiniz. Her modül matematik hesaplamaları, dosyalarla çalışma veya metin biçimlendirme gibi tek bir görev türüne odaklanabilir.


### CommonJS modülleri


NodeJS'de modülleri yönetmek için kullanılan en yaygın sistem **CommonJS** olarak adlandırılır.


Bu sistemde, `module.exports` kullanarak bir modülden kodu paylaşabilir (dışa aktarabilir) ve `require()` kullanarak başka bir dosyaya yükleyebilirsiniz (içe aktarabilirsiniz).


Bir şeyi bir modülün dışında kullanılabilir hale getirmek için, onu `module.exports` öğesine atarsınız:


```javascript
const greeting = "Hello!"

module.exports = greeting
```


Burada, `"Hello!"` dizesi bu modülün dışa aktardığı şeydir.


Başka bir dosyadan dışa aktarılan kodu kullanmak için, `require()` işlevini bu dosyanın yolu ile birlikte kullanırsınız:


```javascript
const greeting = require("./greeting.js")

console.log(greeting)
```


Bu baskılar:


```
Hello!
```


Birden fazla şeyi anonim bir nesnede bir araya getirerek dışa aktarabilirsiniz, örneğin


```javascript
const greeting1 = "hello"

const greeting2 = "hi"

module.exports = {
greeting1, greeting2
}
```


CommonJS başlangıçta NodeJS tarafından benimsenen modül sistemiydi. Daha sonra ES modülleri de eklenmiştir.


### ES Modülleri


NodeJS ayrıca web geliştirmede popüler olan **ES Modülleri** adı verilen başka bir modül türünü de destekler. Bunlar `export` ve `import` anahtar kelimelerini kullanırlar.


ES modülleri tarayıcı için geliştirilmiş ve daha sonra Node'a eklenmiştir. Bunları kullanmak istiyorsanız, kullandığınız Node sürümüne bağlı olarak dosya uzantısı olarak `.js` yerine `.mjs` kullanmanız gerekebilir.


Greeting.mjs` adlı bir dosyada şunları yazıyoruz


```javascript
export const greeting = "Hello!"
```

Gördüğünüz gibi, sabiti doğrudan tanımlandığı yere aktarıyoruz


Index.mjs` adlı başka bir dosyada içe aktarıyoruz:


```javascript
import { greeting } from "./greeting.mjs"

console.log(greeting)
```


Farklı bildirimleri dosyanın farklı bölümlerinde dışa aktarabilirsiniz, örneğin


```javascript
export const num = 10

export function double (x) {
return x*2
}
```


### NodeJS standart kütüphanesi


NodeJS ayrıca birçok yerleşik modül içerir. Bunlar, NodeJS tarafından sağlanan ve dosya okuma, işletim sistemiyle çalışma veya ağa bağlanma gibi yaygın görevlere yardımcı olan hazır modüllerdir.


Örneğin, `os` modülü size işletim sisteminiz hakkında bilgi verir:


```javascript
const os = require("os")

console.log(os.platform())
```


Bu yerleşik modülleri yüklemenize gerek yoktur, NodeJS ile birlikte gelirler. Çalışma zamanının "standart kütüphanesini" oluştururlar ve çoğu Node uygulaması tarafından dosya okuma veya internet üzerinden iletişim kurma gibi şeyler yapmak için kullanılırlar.


Sonraki bölümler size bunların kullanımına ilişkin bazı faydalı örnekler gösterecektir.


## Fs` modülü

<chapterId>911e953a-35ae-5ee7-bd74-372501c32e81</chapterId>


Fs` modülü (**dosya sisteminin** kısaltması) NodeJS standart kütüphanesinin bir parçasıdır. Bilgisayarınızdaki dosyalar ve dizinlerle çalışmanıza olanak tanır: dosyaları okuyabilir, yazabilir, silebilir, yeniden adlandırabilir ve daha fazlasını yapabilirsiniz.


Bunu kullanmak için öncelikle dosyanızın en üstüne aktarmanız gerekir:


```javascript
const fs = require("fs")
```


### Senkronizasyon API'si


Fs`yi kullanmanın en basit yolu **sync** yöntemlerini kullanmaktır.


Bu yöntemler bitene kadar programı bloke eder (böylece işlem tamamlanana kadar bir sonraki kod satırı çalışmaz).


İşte bir dosyayı eşzamanlı olarak okumanın bir örneği:


```javascript
const fs = require("fs")

const data = fs.readFileSync("example.txt", "utf8")

console.log(data)
```


Eğer betiğinizle aynı dizinde `example.txt` adında bir dosya varsa, bu dosya içeriğini yazdıracaktır.


Bir dosyaya eşzamanlı olarak da yazabilirsiniz:


```javascript
const fs = require("fs")

fs.writeFileSync("output.txt", "Hello from Node!")

console.log("File written!")
```


Bu, metinle birlikte `output.txt` adlı bir dosya oluşturur (veya üzerine yazar).


İşte bu API ile yapabileceğiniz bazı yaygın işlemler:


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


Sync API basittir ve küçük komut dosyaları için iyidir, ancak iş bitene kadar programı engellediğinden, büyük dosyalarla veya bir sunucuyla çalışıyorsanız işleri yavaşlatabilir.


### Callback async API


Geri çağırma API'si** bloklama yapmaz: dosya işlemi gerçekleşirken NodeJS'nin başka şeyler yapmaya devam etmesini sağlar.


Sonucu doğrudan döndürmek yerine, işlem tamamlandığında çağrılacak bir işlev (bir **callback**) alır.


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


Şöyle olacak:



- `fs.readFile` `example.txt` dosyasını okumaya başlar.
- NodeJS beklemez, yazmış olabileceğiniz diğer kodları çalıştırmaya devam eder.
- Dosya okuma işlemi tamamlandığında geri arama çalışır:



  - Eğer bir hata varsa, `err` hatayı içerir.
  - Aksi takdirde, `data` içeriği içerir.


Bir dosyaya şu şekilde yazarsınız:


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


Aynı fikir: program dosyayı yazarken durmaz.


Bu API ile yapabileceğiniz bazı şeylere örnekler:


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


Geri arama API'si sunucular ve büyük görevler için daha iyidir, çünkü programı engellemez, ancak birçok işlemi zincirleme yaparsanız iç içe geri aramalar dağınık hale gelebilir. Bu yüzden vaat tabanlı asenkron API eklendi.


### Promise async API


Promise tabanlı API moderndir ve `.then()` ve `async/await` ile harika çalışır. Bu `fs.promises` olarak mevcuttur.


`promises` özelliğini içe aktarmanız gerekir:


```javascript
const fs = require("fs").promises
```


.then()` kullanarak:


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


Ya da daha iyisi `async/await` kullanmaktır:


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


Bir dosyaya yazma:


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


API için olağan örnek listesi:


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


Kod yazarken , genellikle başkaları tarafından yazılmış kodları kullanmanız gerekecektir; örneğin, tarihler, renkler, sunucular veya hemen hemen her şeyle çalışmanıza yardımcı olacak kütüphaneler.


Dosyaları manuel olarak indirmek ve kopyalamak yerine, bir **paket yöneticisi** kullanabilirsiniz.


Paket yöneticisi bir araçtır:



- paketleri̇ i̇ndi̇ri̇yor
- projenizin hangi paketlere ihtiyacı olduğunu takip eder
- ekibinizdeki herkesin paketlerin aynı sürümlerine sahip olduğundan emin olur


### NPM nedir


NodeJS dünyasında en popüler paket yöneticisi *Node Paket Yöneticisi* anlamına gelen **NPM**'dir.


NodeJS'yi yüklediğinizde NPM'yi otomatik olarak alırsınız.


Bunu terminalinizde çalıştırarak NPM'ye sahip olup olmadığınızı kontrol edebilirsiniz:


```
npm -v
```


Bu, sahip olduğunuz NPM sürümünü yazdırır, örneğin:


```
10.2.1
```


### Paket oluşturma


NodeJS'de bir **package** sadece içinde `package.json` dosyası bulunan bir dizindir.


Adım adım bir tane oluşturalım.


1. Projeniz için yeni bir klasör oluşturun:


```
mkdir my_project
cd my_project
```


2. Bu komutu çalıştırın:


```
npm init
```


Bu, size projenizin adı, sürümü, açıklaması vb. gibi sorular soran etkileşimli bir kurulum başlatır.


Her şeye cevap vermek istemiyorsanız ve sadece varsayılanları kabul ediyorsanız, kullanabilirsiniz:


```
npm init -y
```


Çalıştırdıktan sonra, klasörünüzde adı verilen yeni bir dosya göreceksiniz:


```
package.json
```


### `package.json`


Package.json` dosyası, projenizle ilgili meta verileri depolayan bir JSON dosyasıdır.


İşte bir örnek:


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


Birkaç önemli alan:



- `name`: paketinizin adı
- `version`: geçerli sürüm
- main`: giriş noktası dosyası (`index.js` gibi)
- `scripts`: çalıştırabileceğiniz komutlar (`npm start` gibi)
- `dependencies`: projenizin bağlı olduğu tüm paketleri listeler


### Paket yükleme


Diyelim ki terminal çıktınıza renkler eklemek için `picocolors` adlı belirli bir paketi kullanmak istiyorsunuz.


Çalıştırarak yükleyebilirsiniz:


```
npm install picocolors
```


Artık projenizde kullanabilirsiniz. Ile bir `index.js` dosyası oluşturun


```javascript
const pico = require('picocolors')

console.log(
pico.green("This text is green!")
)
```


ve çalıştırmayı deneyin. Terminal metnin renkli bir versiyonunu yazdırmalıdır.


NPM ne yaptı?



- Paketi indirdi ve `node_modules/` adlı bir alt klasörde sakladı
- package.json` dosyanıza `dependencies` altında bir girdi ekledi
- package-lock.json` dosyasını güncelledi


Package-lock.json` nedir?


### `package-lock.json`


Bu dosya NPM tarafından otomatik olarak oluşturulur.


Eğer zaten `package.json` dosyamız varsa, neden başka bir dosyaya ihtiyacımız olduğunu merak edebilirsiniz

İşte sebebi:



- package.json` sadece projenizin bir paketin hangi sürüm **aralığına** ihtiyacı olduğunu söyler.

Örnek:


```json
"dependencies": {
"picocolors": "^1.1.0"
}
```


^^1.1.0` "1.1.x ile uyumlu herhangi bir sürüm" anlamına gelir, bu nedenle esnektir.



- package-lock.json' **her bir paketin ve alt bağımlılıklarının tam sürümlerini dondurur**, böylece projenizi yükleyen herkes tam olarak aynı çalışma kurulumuna sahip olur.


Bu neden önemli?


Bir ekiple çalışıyorsanız veya projenizi bir sunucuya dağıtıyorsanız ya da gelecekte projenize geri dönecekseniz, hala aynı şekilde çalıştığından emin olmak istersiniz.

Paketler güncellendiyse ve kilit dosyası olmadan yeniden yüklerseniz, farklı davranan biraz farklı bir sürüm elde edebilirsiniz.


Projenizde `package-lock.json` dosyasını tutarak, NPM her zaman burada listelenen tam sürümleri yükleyecek ve herkesin aynı ortama sahip olmasını sağlayacaktır.


package-lock.json`, projeyi diğer makinelerde daha fazla tekrarlanabilir hale getirmek için her şeyi çok özel bir sürüme kilitler.


Ancak paketinizin birçok kişi tarafından kullanılması gerekiyorsa, NPM'nin yalnızca `package.json' dosyasını bulması ve bu dosyada izin verilen en son sürümleri otomatik olarak yüklemesine izin verilmesi için onu işlememeyi seçebilirsiniz.


Ancak bunlar daha sonra, kendi kodunuzu yayınlamaya başladığınızda endişelenmeniz gereken şeylerdir. Şimdilik, NPM'nin temellerini sadece projelerinizde diğer geliştiriciler tarafından yayınlanan kütüphaneleri bulmanızı ve kullanmanızı sağlamak için tanıttık.



## NodeJS'de Ağ Oluşturma

<chapterId>f2cabd8b-754b-5c97-8d6a-8412a9a184c7</chapterId>


NodeJS genellikle arka uç için bir dil olarak kullanılır: betiğinizi bir sunucuya dönüştürebilir ve ayrıca diğer sunuculara istekte bulunmak için kullanabilirsiniz.


Bu bölümde, bunu yapmanızı sağlayacak bazı temel ağ özelliklerini tanıtacağız.


### `fetch()`


Programınızın bir web sitesinden veya bir API'den veri indirmesini istiyorsanız, bir **HTTP isteği** yapmanız gerekir.


NodeJS'in modern sürümlerinde, yerleşik `fetch()` işlevini kullanabilirsiniz.


İşte bir API'ye GET isteği yapmanın bir örneği:


```javascript
const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
const data = await response.text()

console.log(data)
```


Bunu çalıştırdığınızda, şöyle bir şey göreceksiniz:


```
{
"userId": 1,
"id": 1,
"title": "...",
"body": "..."
}
```


İşte olanlar:


1. fetch()` bir URL alır ve bir istekte bulunur.

2. Bir `Response` nesnesine çözümlenen bir **Promise** döndürür.

3. `response.text()` yanıt gövdesini bir dize olarak okur.


Ancak geri aldığınız dize aslında JSON'dur. O da ne?


### JSON


Web API'leri ile çalışırken, veriler genellikle JavaScript Object Notation (JavaScript Nesne Gösterimi) anlamına gelen **JSON** olarak gönderilir ve alınır.


JSON, JavaScript nesnelerine çok benzeyen bir metin biçimidir. Örneğin:


```json
{
"name": "Alice",
"age": 30,
"likes": ["apples", "bananas"]
}
```


JSON` nesnesi, JavaScript'te bu veri formatıyla çalışmak için kullanılabilen yerleşik bir yardımcı programdır.


Bir JavaScript nesnesini `JSON.stringify()` kullanarak JSON dizesine dönüştürebilirsiniz:


```javascript
const user = { name: "Alice", age: 30 }

const jsonString = JSON.stringify(user)

console.log(jsonString)
```


Bu baskılar:


```
{"name":"Alice","age":30}
```


JSON metnini `JSON.parse()` kullanarak bir JavaScript nesnesine de dönüştürebilirsiniz:


```javascript
const jsonText = '{"name":"Bob","age":25}'

const obj = JSON.parse(jsonText)

console.log(obj)
```


Bu baskılar:


```
{ name: 'Bob', age: 25 }
```


Dikkatli olun: eğer dize geçerli bir JSON değilse `JSON.parse()` bir hata verecektir.


```javascript
JSON.parse("not json") // ❌ Error!
```


Bu yüzden dizenin düzgün biçimlendirildiğinden emin olun.


### `http` sunucusu


NodeJS, başka hiçbir şey yüklemeden bir web sunucusu oluşturmanıza olanak tanır.


İstemcilerden gelen istekleri işlemek ve yanıtları geri göndermek için yerleşik `http` modülünü kullanabilirsiniz.


İşte çok basit bir örnek:


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


Bu betiği çalıştırdığınızda ve tarayıcınızda `http://localhost:3000` adresini açtığınızda şunları göreceksiniz:


```
Hello from NodeJS server!
```


Kodda olan şey bu:


1. Node standart kütüphanesinden `http` sunucusunu içe aktardınız.

2. http.createServer()` bir sunucu oluşturur. Birisi her bağlandığında çalıştırılmak üzere `http.createServer()` işlevine `(req, res) => {...}` şeklinde bir geriçağırım ilettiniz.

3. Yanıta 200 durum kodu (başarılı bir işlem olduğunu gösterir) atadınız. Http durum kodları hakkında [buradan](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status) bilgi edinebilirsiniz

3. res.end()` yanıtı gönderir ve bağlantıyı sonlandırır.

4. `server.listen(3000)` sunucuyu 3000 numaralı bağlantı noktasında başlatır.


Farklı yolları veya istek türlerini işlemek için istekte `req.url` ve `req.method` öğelerini de kontrol edebilirsiniz.


Yönlendirme ile örnek:


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


Bunlar çok temel örneklerdir. Daha gelişmiş sunucular oluşturmak için, çoğu geliştirici muhtemelen [express](https://www.npmjs.com/package/express) gibi hazır bir arka uç kütüphanesi indirecektir.


## Veri işleme: arabellekler, olaylar, akışlar

<chapterId>8c9623f0-a604-51a4-8fe4-871c849d3e3b</chapterId>


Bu bölümde öncelikle üç nesne sınıfını tanıtacağız:



- i̇kili verilerin küçük parçalarını temsil eden `Buffer`
- "Olay" adı verilen sinyaller yayarak bazı adımları eşzamansız süreçle izlemek için kullanılabilen `EventEmitter`
- her seferinde bir `Buffer` olmak üzere büyük veri parçalarını işlememizi sağlayan ve olayları yayarak süreci izleyen `Stream`


Bunlar profesyonel NodeJS kodunda son derece yaygındır, bu nedenle ilk projelerinizde kullanmasanız bile, bunlarla ne zaman etkileşime girmeniz gerekeceği konusunda temel bir anlayış edinmeniz iyi olacaktır


### Tamponlar


NodeJS'de **buffer**, ikili verilerle çalışmak için kullanılan bir nesne türüdür.


Tamponu, ham baytlar için sabit boyutlu bir kap olarak düşünebilirsiniz.


Bir dizeden nasıl tampon oluşturulacağı aşağıda açıklanmıştır:


```javascript
const buf = Buffer.from("hello")
console.log(buf)
```


Bu, aşağıdaki gibi bir şey yazdırır:


```
<Buffer 68 65 6c 6c 6f>
```


Bu sayılar (`68`, `65`, `6c`, vb.) `"hello"`daki harflerin onaltılık gösterimleridir.


Bunu aşağıdaki gibi bir dizeye dönüştürebilirsiniz:


```javascript
console.log(buf.toString())
```


Bu baskılar:


```
hello
```


Ayrıca sıfırlarla dolu belirli bir boyutta bir tampon da oluşturabilirsiniz:


```javascript
const buf = Buffer.alloc(10)
console.log(buf)
```


Bu, aşağıdaki gibi bir şey yazdırır:


```
<Buffer 00 00 00 00 00 00 00 00 00 00>
```


Arabelleğe yazabilirsiniz:


```javascript
buf.write("abc")
console.log(buf)
```


Ve tek tek baytlara erişebilirsiniz:


```javascript
console.log(buf[0]) // prints the ASCII number for 'a', which is 97
```


Tamponlar, özellikle verileri çok düşük bir seviyede manipüle etmeniz gerektiğinde kullanışlıdır.


### Etkinlikler


JavaScript'te **olay**, programınızda gerçekleşen ve tepki verebileceğiniz bir şeydir.


Örneğin:



- bir dosya yüklenmeyi bitirir
- bir zamanlayıcı kapanır
- bir kullanıcı bir düğmeye tıklar
- bir ağ isteği veri döndürür


Bir **olay** sadece bir şeyin gerçekleştiğine dair bir sinyaldir ve bu olayları dinlemek ve onlara tepki vermek için kod yazabilirsiniz.


NodeJS'de birçok nesne olay yayabilir. Bu nesneler **EventEmitters** olarak adlandırılır.


İşte bir örnek:


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


Bu baskılar:


```
Hello! An event happened.
```


Şöyle bir şey var:


1. Bir `EventEmitter` nesnesi oluşturuyoruz.

2. Biz `.on("greet")` kullanarak `"greet"` olayı gerçekleştiğinde bir geri arama çalıştırmasını söylüyoruz.

3. Daha sonra `.emit()` kullanarak `"greet"` olayını tetikleriz.

4. Geri çağrımız yürütülür


Olayla birlikte veri iletebilirsiniz:


```javascript
emitter.on("greet",
(name) => console.log(`Hello, ${name}!`)
)

emitter.emit("greet", "Alice") // first argument is the type of event, second argument is the data we pass with this event
```


Bu baskılar:


```
Hello, Alice!
```


Dinleyicileri diğer etkinlikler için de kaydedebilirsiniz:


```javascript
emitter.on("goodbye", () => {
console.log("Goodbye!")
})

emitter.emit("goodbye")
```


Bir olay türüne istediğiniz kadar dinleyici ekleyebilir ve aynı yayıcıdan birçok farklı olay türünü ateşleyebilirsiniz.


NodeJS'deki birçok nesne, programın geri kalanına bir şeyler olduğunu bildirmek için olaylar yayar.



### Akarsular nedir?


Akışlar, verileri işlememize yardımcı olmak için tamponları ve olayları birleştirir.


Dosyalar, ağdan gelen veriler ve hatta uzun metinlerle çalışırken, her zaman her şeyi bir kerede belleğe yüklememiz gerekmez (veya bunu istemeyiz). Bu yavaş olabilir, hatta veri çok büyükse programı çökertebilir.


Bunun yerine, verileri geldikçe veya okundukça **azar azar** işleyebiliriz, tıpkı bardağın tamamını bir kerede içmeye çalışmak yerine pipetle su içmek gibi. Buna **akış** denir.


NodeJS'de akış, bir kaynaktan veri okumanızı veya bir hedefe **her seferinde bir parça** veri yazmanızı sağlayan bir nesnedir.


NodeJS dört ana akış türüne sahiptir:



- Okunabilir**: veri okuyabileceğiniz akışlar (bir dosyayı okumak gibi)
- Writable**: veri yazabileceğiniz akışlar (bir dosyaya yazmak gibi)
- Duplex**: hem okunabilir hem de yazılabilir akışlar
- Dönüştür**: çift yönlü akışlar gibi, ancak verileri akarken değiştirebilirler (dönüştürebilirler)


### Okunabilir akışlar


Diyelim ki işlenecek bir `bigfile.txt` dosyanız var. Dosyayı parça parça okumak için `fs` modülü ile okunabilir bir akış oluşturabilirsiniz.


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


Burada ne oluyor?


1. fs.createReadStream()` okunabilir bir akış oluşturur.

2. Dosyanın bir parçası hazır olduğunda, akış bir `data` olayı yayınlar ve bize bir veri "yığını" (bir `Buffer`) verir. Bu yığını yazdırırız.

3. Tüm dosya okunduğunda `end` olayı tetiklenir.

4. Bir hata varsa (dosyanın mevcut olmaması gibi), `error` olayı tetiklenir.


Bu şekilde, dev dosyaları hepsini bir kerede belleğe yüklemeden okuyabilirsiniz.


Verilerin insan tarafından okunabilir bir biçimde (ikili yerine) gelmesini istiyorsak, akışın kodlamasını belirtebiliriz:


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


Kod şimdi dosyayı insan tarafından okunabilir biçimde yazdıracaktır.


### Yazılabilir akışlar


Yazılabilir bir akış, verileri yığın yığın bir yere göndermenizi sağlar.


İşte bir akış kullanarak `target.txt` dosyasına yazmanın bir örneği:


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


Şöyle olacak:


1. `fs.createWriteStream()` yazılabilir bir akış oluşturur.

2. .write()` kullanarak bir metin yazıyoruz.

3. İşimiz bittiğinde, akışı kapatmak için `.end()` işlevini çağırırız.

4. Tüm veriler yazıldığında, `finish` olayı yayınlanır.

5. Bir şeyler ters giderse, `error` olayı tetiklenir.


Tıpkı okunabilir akışlar gibi, yazılabilir akışlar da büyük veriler için iyidir çünkü her şeyi aynı anda bellekte tutmaları gerekmez.


### Boru akışları


Akışlarla ilgili en güzel şeylerden biri, onları birbirine **borulayabilmenizdir: okunabilir bir akışı doğrudan yazılabilir bir akışa bağlayabilirsiniz.


```javascript
const fs = require("fs")

const readable = fs.createReadStream("bigfile.txt")
const writable = fs.createWriteStream("target.txt")

readable.pipe(writable)
```


İşte:



- Okunabilir akış `bigfile.txt` dosyasından okunur.
- Yazılabilir akış `copy.txt` dosyasına yazar.
- .pipe()`, verileri doğrudan okunabilir akıştan yazılabilir akışa gönderir.


### Çift yönlü akışlar


Çift yönlü bir akış hem okunabilir hem de yazılabilir. Bir ağ soketi buna bir örnektir: ona veri gönderebilir ve ondan veri alabilirsiniz.


İşte `net` modülünü kullanan çok basit bir örnek:


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


Bu örnekte:



- Soket` nesnesi çift yönlü bir akımdır.
- Ona `yazabilir()` ve ayrıca ondan `veri` olaylarını dinleyebilirsiniz.


### Akışları dönüştürün


Dönüşüm akışı, içinden geçen verileri de değiştiren çift yönlü bir akıştır.


Örneğin, verileri sıkıştırmak veya açmak için yerleşik `zlib` modülünü kullanabilirsiniz.


Dönüşüm akışı kullanarak bir dosyanın nasıl sıkıştırılacağı aşağıda açıklanmıştır:


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


Ve geri sıkıştırmak için:


```javascript
const readable = fs.createReadStream("bigfile.txt.gz")
const unzip = zlib.createGunzip()
const writable = fs.createWriteStream("bigfile.txt")

readable.pipe(unzip).pipe(writable)

writable.on("finish", () => {
console.log("File decompressed.")
})
```


Dönüştürme akışları sıkıştırma, şifreleme veya akış sırasında dosya formatlarını değiştirme gibi görevler için çok kullanışlıdır.


### Geri Basınç


Bazen yazılabilir bir akış veri işleme konusunda yavaştır. Bir yazılabilire işleyebileceğinden daha hızlı veri göndermeye devam edersek, sorunlarla karşılaşabiliriz. Buna **backpressure** denir.


Yazılabilir bir akış üzerinde `.write()` yöntemini çağırırsanız, akışın duraklamaya ihtiyacı olup olmadığını bildiren bir boolean döndürür; dönüş değerini aşağıdaki gibi kontrol etmeniz gerekebilir:


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


Bu, verilerin bir Okunabilirden bir Yazılabilire manuel olarak aktarılması ve geri basıncın manuel olarak yönetilmesine ilişkin açıklayıcı bir örnekti.


Genellikle, geri basıncı otomatik olarak işleyen `.pipe()` yöntemini kullanarak verileri borularız.


Bu nedenle, yalnızca herhangi bir nedenle `.write()` işlevini manuel olarak çağırdığınızda geri baskı konusunda endişelenmeniz gerekir.


## Son not

<chapterId>139e2ab8-df67-525a-85f0-5a2fa5e478f2</chapterId>


İşte bu kadar, eğer dersleri takip ettiyseniz, artık NodeJS'de bazı basit programlar yazabiliyor olmalısınız.


Tam olarak bunu yapmanızı öneririm: temel bilgileri öğrendikten sonra, birkaç kişisel proje oluşturmak pratik yapmanın ve daha iyi bir programcı olmanın en iyi yoludur.


Ne inşa ettiğiniz gerçekten önemli değil, önemli olan kodla ilgili sorunları çözmek için kendinize meydan okumanız.


Modern programlama dilleri inanılmaz derecede güçlüdür ve NodeJS muhtemelen yolculuğunuzun bu aşamasında deneyebileceğiniz en iyi araç kutusudur.


İyi şanslar!


# Son bölüm


<partId>322624d8-6fbc-11f0-a67a-5b145f10afc1</partId>


## Yorumlar & Derecelendirmeler


<chapterId>3e93ac86-6fbc-11f0-8bae-9b2ed7914843</chapterId>

<isCourseReview>true</isCourseReview>

## Sonuç


<chapterId>49b3b9b2-6fbc-11f0-9870-5f5adcd3a0eb</chapterId>


<isCourseConclusion>true</isCourseConclusion>