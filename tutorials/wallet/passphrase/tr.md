---
name: passphrase BIP39
description: passphrase'in nasıl çalıştığını anlama
---
![cover](assets/cover.webp)


## BIP39 passphrase nedir?


HD cüzdanlar tipik olarak 12 veya 24 kelimeden oluşan bir Mnemonic cümlesinden üretilir. Bu ifade çok önemlidir çünkü fiziksel ortamının (örneğin bir Hardware Wallet gibi) kaybolması durumunda bir Wallet'in tüm anahtarlarının geri yüklenmesini sağlar. Bununla birlikte, tek bir hata noktası oluşturur, çünkü ele geçirilirse, bir saldırgan tüm bitcoinleri çalabilir.


![PASSPHRASE BIP39](assets/notext/01.webp)


passphrase burada devreye girer. Serbestçe seçebileceğiniz isteğe bağlı bir paroladır ve Wallet'in güvenliğini artırmak için anahtar türetme sürecinde Mnemonic ifadesine eklenir.


![PASSPHRASE BIP39](assets/notext/02.webp)


passphrase'u Hardware Wallet'unuzun PIN kodu veya bilgisayarınızda Wallet'nize erişim kilidini açmak için kullanılan parola ile karıştırmamaya dikkat edin. Tüm bu Elements'lerin aksine, passphrase, Wallet'nizin anahtarlarının türetilmesinde rol oynar. **Bu, onsuz bitcoinlerinizi asla kurtaramayacağınız anlamına gelir.**


passphrase, anahtarların üretildiği seed'yi değiştirerek Mnemonic cümlesiyle birlikte çalışır. Böylece, birisi 12 veya 24 kelimelik ifadenizi ele geçirse bile, passphrase olmadan fonlarınıza erişemez. **Bir passphrase kullanmak esasen farklı anahtarlara sahip yeni bir Wallet yaratır. passphrase'ü değiştirmek (biraz bile olsa) farklı bir generate yaratacaktır.**


## Neden bir passphrase kullanmalısınız?


passphrase isteğe bağlıdır ve kullanıcı tarafından seçilen herhangi bir karakter kombinasyonu olabilir. passphrase kullanmak bu nedenle çeşitli avantajlar sunar. İlk olarak, fonlara erişmek için ikinci bir faktör gerektirerek (hırsızlık, evinize erişim vb.) Mnemonic ifadesinin tehlikeye atılmasıyla ilişkili tüm riskleri azaltır.


Daha sonra, meşhur "*5 dolarlık İngiliz anahtarı saldırısı*" gibi fonlarınızı çalmaya yönelik fiziksel kısıtlamalarla başa çıkmak için yem bir Wallet oluşturmak için stratejik olarak kullanılabilir. Bu senaryoda amaç, passphrase olmadan, potansiyel bir saldırganı tatmin edecek kadar az miktarda bitcoin içeren bir Wallet'e sahip olmak ve aynı zamanda gizli bir Wallet'e sahip olmaktır. Bu sonuncusu aynı Mnemonic ifadesini kullanır ancak ek bir passphrase ile güvence altına alınır.


Son olarak, HD Wallet'in seed üretiminin rastgeleliğini kontrol etmek istendiğinde bir passphrase kullanmak ilginçtir.


## İyi bir passphrase nasıl seçilir?

passphrase'in etkili olabilmesi için yeterince uzun ve rastgele olması gerekir. Tıpkı güçlü bir parolada olduğu gibi, herhangi bir kaba kuvvet saldırısını imkansız kılmak için çeşitli harfler, sayılar ve semboller içeren, olabildiğince uzun ve rastgele bir passphrase seçmenizi öneririm.


Trezor tarafından 2019 yılında yapılan bir araştırmaya göre] (https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af), seed'unuza erişimi olan ve AWS'de kiralanan üst düzey bir GPU (NVIDIA Tesla V100) kullanan bir saldırgan, 1 dolar karşılığında yaklaşık 620 milyon parolayı test edebilir. Kaba bir tahmin olarak, 2019 yetenekleriyle, 12 rastgele küçük harften oluşan bir passphrase'un kırılması ortalama **77 milyon dolara** mal olacaktır.


Ancak, kendinizi 12 karakterle sınırlamamanızı tavsiye ederim. Bunun yerine güçlü parolalar için mevcut standartları hedefleyin: 2025 yılında rakamlar, küçük ve büyük harfler ve semboller dahil olmak üzere en az 13 rastgele karakter veya yalnızca küçük ve büyük harfler kullanılıyorsa 14 karakter hedefleyin. Doğal olarak, gelecekteki gelişmeleri öngörmek ve bu çalışmalarda dikkate alınmayan insan risklerini hesaba katmak için, örneğin sembollerle birlikte 20 karakterli bir passphrase seçerek daha yüksek hedeflemenizi öneririm.


Bu passphrase'yi, Mnemonic ifadesiyle aynı şekilde düzgün bir şekilde kaydetmek de önemlidir. **Bunu kaybetmek, bitcoinlerinize erişimi kaybetmek anlamına gelir**. Bunu sadece kafanızda ezberlememenizi şiddetle tavsiye ederim, çünkü bu kayıp riskini makul olmayan bir şekilde artırır. İdeal olanı, Mnemonic cümlesinden ayrı olarak fiziksel bir ortama (kağıt veya metal) yazmaktır. Her ikisinin de aynı anda ele geçirilmesini önlemek için bu yedekleme kesinlikle Mnemonic ifadenizin tutulduğu yerden farklı bir yerde saklanmalıdır.


## Öğreticiler


Bir passphrase cihazında (Stax, Flex veya Nano) bir Ledger kurmak için bu eğiticiye başvurabilirsiniz:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

COLDCARD'da:


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

Jade Plus'ta:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Pasaportta (toplu iş-2):


https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Bir Trezor cihazında (Safe 3, Safe 5 veya Model One):


https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42