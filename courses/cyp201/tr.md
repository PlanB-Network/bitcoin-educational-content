---
name: Bitcoin Cüzdanların İç İşleyişi
goal: Bitcoin cüzdanlarına güç veren kriptografik ilkelere dalın.
objectives: 

  - Bitcoin'de kullanılan kriptografik algoritmaları anlamak için gerekli teorik kavramları tanımlayabilecektir.
  - Deterministik ve hiyerarşik bir Wallet'ün yapısını tam olarak anlamak.
  - Bir Wallet'ün yönetimiyle ilişkili risklerin nasıl belirleneceğini ve azaltılacağını bilir.
  - Hash fonksiyonlarının, kriptografik anahtarların ve dijital imzaların prensiplerini anlamak.

---

# Bitcoin Cüzdanlarının Kalbine Bir Yolculuk


CYP201 kursumuz ile deterministik ve hiyerarşik Bitcoin cüzdanlarının sırlarını keşfedin! İster düzenli bir kullanıcı ister bilginizi derinleştirmek isteyen bir meraklı olun, bu kurs hepimizin günlük olarak kullandığı bu araçların işleyişine tam bir daldırma sunuyor.


Gelişmiş güvenlik stratejilerini keşfederken Hash işlevleri, dijital imzalar (ECDSA ve Schnorr), Mnemonic ifadeleri, kriptografik anahtarlar ve alıcı adreslerinin oluşturulması mekanizmaları hakkında bilgi edinin.


Bu eğitim sizi sadece bir Bitcoin Wallet'in yapısını anlayacak bilgiyle donatmakla kalmayacak, aynı zamanda kriptografinin heyecan verici dünyasına daha derinlemesine dalmaya da hazırlayacaktır.


Açık pedagoji, 60'ın üzerinde açıklayıcı diyagram ve somut örneklerle CYP201, Wallet'ünüzün nasıl çalıştığını A'dan Z'ye anlamanızı sağlayacak, böylece Bitcoin evreninde güvenle gezinebileceksiniz. HD cüzdanların nasıl çalıştığını anlayarak UTXO'larınızın kontrolünü bugün elinize alın!


+++

# Giriş


<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>


## Kurs Tanıtımı


<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>


HD Bitcoin cüzdanlarının işleyişini derinlemesine inceleyeceğimiz CYP201 kursuna hoş geldiniz. Bu kurs, ister sıradan kullanıcılar, ister aydınlanmış meraklılar veya geleceğin uzmanları olsun, Bitcoin kullanımının teknik temellerini anlamak isteyen herkes için tasarlanmıştır.


Bu eğitimin amacı, günlük olarak kullandığınız araçlarda ustalaşmanız için size anahtarlar vermektir. Kullanıcı deneyiminizin merkezinde yer alan HD Bitcoin cüzdanları, bazen erişilebilir hale getirmeye çalışacağımız karmaşık kavramlara dayanmaktadır. Birlikte bu kavramların gizemini çözeceğiz!


Bitcoin cüzdanlarının yapımı ve işleyişinin ayrıntılarına girmeden önce, bundan sonrası için bilinmesi gereken kriptografik ilkellere ilişkin birkaç bölümle başlayacağız.

Hem cüzdanlar hem de Bitcoin protokolünün kendisi için temel olan kriptografik Hash işlevleriyle başlayacağız. Ana özelliklerini, Bitcoin'de kullanılan belirli işlevleri keşfedecek ve daha teknik bir bölümde, Hash işlevlerinin kraliçesinin işleyişi hakkında ayrıntılı bilgi edineceksiniz: SHA256.


![CYP201](assets/fr/010.webp)


Daha sonra, UTXO'larınızı güvence altına almak için her gün kullandığınız dijital imza algoritmalarının çalışmasını tartışacağız. Bitcoin iki tane kullanır: ECDSA ve Schnorr protokolü. Bu algoritmaların altında hangi matematiksel ilkellerin yattığını ve işlemlerin güvenliğini nasıl sağladıklarını öğreneceksiniz.


![CYP201](assets/fr/021.webp)


Kriptografinin bu Elements'sini iyi bir şekilde anladıktan sonra, nihayet eğitimin kalbine geçeceğiz: deterministik ve hiyerarşik cüzdanlar! İlk olarak, cüzdanlarınızı oluşturmanızı ve geri yüklemenizi sağlayan 12 veya 24 kelimeden oluşan bu diziler olan Mnemonic cümlelerine ayrılmış bir bölüm var. Bu sözcüklerin bir entropi kaynağından nasıl üretildiğini ve Bitcoin'nin kullanımını nasıl kolaylaştırdığını keşfedeceksiniz.


![CYP201](assets/fr/040.webp)


Eğitim BIP39 passphrase, seed (Mnemonic ifadesiyle karıştırılmamalıdır), ana chain code ve ana anahtarın incelenmesiyle devam edecektir. Bu Elements'in ne olduğunu, ilgili rollerini ve nasıl hesaplandıklarını ayrıntılı olarak göreceğiz.


![CYP201](assets/fr/045.webp)


Son olarak, ana anahtardan, kriptografik anahtar çiftlerinin alıcı adreslere kadar deterministik ve hiyerarşik bir şekilde nasıl türetildiğini keşfedeceğiz.


![CYP201](assets/fr/056.webp)


Bu eğitim, riskleri belirleme ve azaltma becerilerinizi geliştirirken Wallet yazılımınızı güvenle kullanmanızı sağlayacaktır. Bitcoin cüzdanlarında gerçek bir uzman olmaya hazırlanın!


Bu tablo, CYP 201 dersi kapsamında kullanılan şemaları ve teknik belgeleri daha kolay anlamanızı sağlamak için kullanılan temel İngilizce terimlerin çevirisini sunar.

| İngilizce       | Çeviri / Açıklama                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------------- |
| *pubkey hash*   | Genel anahtar karması (Bitcoin adresi oluşturmak için kullanılır).                                  |
| *public key*    | Genel anahtar (fon almak için kullanılır, özel anahtardan türetilmiştir).                           |
| *signature*     | Dijital imza (bir mesajın özel anahtar sahibinden geldiğini kanıtlayan kriptografik delil).         |
| *scriptPubKey*  | Kilitleme betiği (bir çıktının harcanma koşullarını tanımlar).                                      |
| *scriptSig*     | Kilit açma betiği (*scriptPubKey*'i karşılamak için verileri sağlar).                              |
| *Stack*         | Yığın (*Bitcoin Script* tarafından kullanılan veri yapısı).                                         |
| *input*         | İşlem girdisi (kaynak olarak kullanılan önceki bir çıktıya referans).                               |
| *output*        | İşlem çıktısı (alıcıyı ve miktarı tanımlar).                                                        |
| *transaction*   | Bitcoin işlemi (bir transferi doğrulayan giriş ve çıkışların bütünü).                               |
| *XOR*           | Mantıksal operatör "özel VEYA", bazı kriptografik şemalarda kullanılır.                            |
| *HMAC*          | Hash ve gizli anahtara dayalı mesaj kimlik doğrulama kodu.                                          |
| *ECDSA*         | Eliptik eğri dijital imza algoritması.                                                              |
| *hash*          | Hash (verinin benzersiz ve sabit parmak izi).                                                       |
| *SigHash*       | İmza karması türü (bir işlemin hangi bölümlerinin imzalandığını tanımlar).                          |
| *HD Wallet*     | Hiyerarşik deterministik cüzdan (tek bir tohumdan birden çok anahtar üretir).                       |
| *Random Number* | Rastgele sayı (güvenli özel anahtarlar üretmek için kullanılır).                                    |
| *State*         | Durum (kriptografik bir süreçteki ara değer).                                                       |
| *Entropy*       | Entropi (rastgeleliğin ölçüsü, cüzdan tohumları üretmek için kullanılır).                           |
| *Mnemonic*      | Mnemonik (bir tohumun yedeklenmesini ve geri yüklenmesini kolaylaştıran kelime dizisi).             |
| *Wordlist*      | Kelime listesi (BIP39 mnemonikleri üretmek için kullanılan önceden tanımlanmış küme).               |
| *Seed*          | Tohum (bir HD cüzdanındaki tüm anahtarların türetilmesine izin veren başlangıç değeri).             |
| *Address*       | Bitcoin adresi (fon almak için okunabilir tanımlayıcı, genel anahtardan türetilmiştir).             |
| *Leaf*          | Yaprak (türev ağacındaki terminal düğüm).                                                           |

# Hash Fonksiyonları


<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>


## Hash Fonksiyonlarına Giriş


<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>


Bitcoin'de kullanılan ilk kriptografik algoritma türü Hash işlevlerini kapsar. Bunlar protokolün farklı seviyelerinde ve aynı zamanda Bitcoin cüzdanlarında önemli bir rol oynar. Hash fonksiyonunun ne olduğunu ve Bitcoin'de ne için kullanıldığını birlikte keşfedelim.


### Hashing'in Tanımı ve Prensibi


Hashing, rastgele uzunluktaki bilgileri kriptografik bir Hash fonksiyonu aracılığıyla sabit uzunlukta başka bir bilgi parçasına dönüştüren bir işlemdir. Başka bir deyişle, bir Hash işlevi herhangi bir boyuttaki bir girdiyi alır ve onu "Hash" adı verilen sabit boyutlu bir parmak izine dönüştürür.

Hash bazen "digest", "condensate", "condensed" veya "hashed" olarak da adlandırılabilir.


Örneğin, SHA256 Hash işlevi 256 bitlik sabit uzunlukta bir Hash üretir. Dolayısıyla, rastgele uzunlukta bir mesaj olan "_PlanB_" girdisini kullanırsak, üretilen Hash aşağıdaki 256 bitlik parmak izi olacaktır:


```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```


![CYP201](assets/fr/001.webp)


### Hash İşlevlerinin Özellikleri


Bu kriptografik Hash fonksiyonları, onları Bitcoin ve diğer bilgisayar sistemleri bağlamında özellikle yararlı kılan birkaç temel özelliğe sahiptir:



- Geri döndürülemezlik (veya ön görüntü direnci)
- Kurcalamaya karşı direnç (çığ etkisi)
- Çarpışma direnci
- İkinci ön görüntü direnci


#### 1. Geri döndürülemezlik (ön görüntü direnci):


Tersinmezlik, Hash'ı girdi bilgisinden hesaplamanın kolay olduğu, ancak ters hesaplamanın, yani Hash'tan girdiyi bulmanın pratikte imkansız olduğu anlamına gelir. Bu özellik, Hash işlevlerini orijinal bilgilerden ödün vermeden benzersiz dijital parmak izleri oluşturmak için mükemmel hale getirir. Bu özellik genellikle tek yönlü fonksiyon olarak adlandırılır.


Verilen örnekte, "_PlanB_" girdisini bilerek Hash `24f1b9...` elde etmek basit ve hızlıdır. Ancak, sadece `24f1b9...` bilgisiyle "_PlanB_" mesajını bulmak imkansızdır.


![CYP201](assets/fr/002.webp)


Bu nedenle, $h = \text{Hash}(m)$ olacak şekilde bir Hash $h$ için bir ön görüntü $m$ bulmak imkansızdır, burada $\text{Hash}$ bir kriptografik Hash fonksiyonudur.


#### 2. Kurcalamaya karşı direnç (çığ etkisi)


İkinci karakteristik, **avalanche etkisi** olarak da bilinen kurcalama direncidir. Bu özellik, giriş mesajındaki küçük bir değişiklik Hash çıkışında radikal bir değişikliğe yol açarsa bir Hash fonksiyonunda gözlemlenir.


"_PlanB_" girdisi ve SHA256 fonksiyonu ile örneğimize geri dönersek, oluşturulan Hash'ün aşağıdaki gibi olduğunu gördük:


```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```


Bu kez "_Planb_" kullanarak girdide çok küçük bir değişiklik yaparsak, sadece büyük "B" harfinden küçük "b" harfine geçmek SHA256 çıktısı Hash'i tamamen değiştirir:


```text
bb038b4503ac5d90e1205788b00f8f314583c5e22f72bec84b8735ba5a36df3f
```


![CYP201](assets/fr/003.webp)


Bu özellik, Hash'nin sadece küçük bir kısmını değil, tamamını değiştirdiği için orijinal mesajdaki küçük bir değişikliğin bile hemen tespit edilebilmesini sağlar. Bu, mesajların, yazılımların ve hatta Bitcoin işlemlerinin bütünlüğünü doğrulamak için çeşitli alanlarda ilgi çekici olabilir.


#### 3. Çarpışma Direnci


Üçüncü özellik çarpışma direncidir. Bir Hash fonksiyonu, fonksiyondan aynı Hash çıktısını üreten 2 farklı mesaj bulmak hesaplama açısından imkansızsa çarpışmaya dayanıklıdır. Biçimsel olarak, $m_1$ ve $m_2$ şeklinde iki farklı mesaj bulmak zordur:


$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$


![CYP201](assets/fr/004.webp)


Gerçekte, Hash fonksiyonları için çarpışmaların olması matematiksel olarak kaçınılmazdır, çünkü girdilerin boyutu çıktıların boyutundan daha büyük olabilir. Bu Dirichlet çekmece prensibi olarak bilinir: $n$ nesne $m$ çekmeceye dağıtılmışsa ve $m < n$ ise, en az bir çekmece mutlaka iki veya daha fazla nesne içerecektir. Bir Hash fonksiyonu için bu prensip geçerlidir çünkü olası mesajların sayısı (neredeyse) sonsuzken, olası hash'lerin sayısı sonludur (SHA256 durumunda $2^{256}$).


Dolayısıyla, bu özellik Hash fonksiyonları için çarpışma olmadığı anlamına gelmez, daha ziyade iyi bir Hash fonksiyonunun çarpışma bulma olasılığını ihmal edilebilir hale getirdiği anlamına gelir. Örneğin bu özellik, çarpışmaların bulunduğu SHA-2'nin öncülleri olan SHA-0 ve SHA-1 algoritmalarında artık doğrulanmamaktadır. Bu nedenle bu fonksiyonlar artık tavsiye edilmemekte ve genellikle eski olarak kabul edilmektedir.

N$ bitlik bir Hash fonksiyonu için çarpışma direnci, doğum günü saldırısına uygun olarak $2^{\frac{n}{2}}$ mertebesindedir. Örneğin, SHA256 ($n = 256$) için, bir çarpışma bulmanın karmaşıklığı $2^{128}$ deneme mertebesindedir. Pratik anlamda bu, $2^{128}$ farklı mesajın fonksiyondan geçirilmesi durumunda bir çarpışma bulma olasılığının yüksek olduğu anlamına gelir.


#### 4. İkinci Öngörüye Direnç


İkinci ön görüntüye direnç, Hash fonksiyonlarının bir diğer önemli özelliğidir. Bir $m_1$ mesajı ve onun Hash $h$'si verildiğinde, başka bir $m_2 \neq m_1$ mesajı bulmanın hesaplama açısından olanaksız olduğunu belirtir:


$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$


Bu nedenle, ikinci ön görüntüye karşı direnç çarpışma direncine biraz benzer, ancak burada saldırı daha zordur çünkü saldırgan $m_1$ 'i özgürce seçemez.


![CYP201](assets/fr/005.webp)


### Hash Fonksiyonlarının Bitcoin'teki Uygulamaları


Bitcoin'te en çok kullanılan Hash işlevi **SHA256**'dır ("_Secure Hash Algorithm 256 bits"_). NSA tarafından 2000'lerin başında tasarlanan ve NIST tarafından standartlaştırılan bu algoritma 256 bit Hash çıktısı üretir.


Bu fonksiyon Bitcoin'un birçok alanında kullanılmaktadır. Protokol düzeyinde, bir Miner tarafından oluşturulan bir aday bloğun başlığı ile zorluk hedefi arasında kısmi bir çarpışma aramak için çift hashing uygulandığı Proof-of-Work mekanizmasında yer alır. Bu kısmi çarpışma bulunursa, aday blok geçerli hale gelir ve Blockchain'e eklenebilir.


SHA256 aynı zamanda bloklar halinde işlemlerin kaydedilmesi için kullanılan akümülatör olan Merkle Tree'in yapımında da kullanılır. Bu yapı, UTXO Setinin boyutunun azaltılmasına olanak tanıyan Utreexo protokolünde de bulunur. Ek olarak, 2021'de Taproot'ün piyasaya sürülmesiyle birlikte SHA256, diğer olası seçenekleri ifşa etmeden yalnızca bir komut dosyasında gerçekten kullanılan harcama koşullarını ortaya çıkarmaya izin veren MAST'ta (_Merkelised Alternative Script Tree_) kullanılmaktadır. Ayrıca işlem tanımlayıcılarının hesaplanmasında, paketlerin P2P ağı üzerinden iletiminde, elektronik imzalarda da kullanılmaktadır... Son olarak ve bu eğitimde özellikle ilgi çekici olan SHA256, Bitcoin cüzdanlarının oluşturulması ve adreslerin türetilmesi için uygulama düzeyinde kullanılır.


Çoğu zaman, Bitcoin'da SHA256 kullanımına rastladığınızda, bu aslında SHA256'nın art arda iki kez uygulanmasından oluşan "**HASH256**" olarak belirtilen çift Hash SHA256 olacaktır:


$$
\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))
$$


Bu çift hashing uygulaması, günümüzde tek bir SHA256 kriptografik olarak güvenli kabul edilse de, belirli potansiyel saldırılara karşı ekstra bir Layer güvenlik ekler.


Script dilinde mevcut olan ve alıcı adreslerini türetmek için kullanılan bir başka hashing işlevi de RIPEMD160 işlevidir. Bu fonksiyon 160 bitlik bir Hash üretir (dolayısıyla SHA256'dan daha kısadır). Genellikle HASH160 işlevini oluşturmak için SHA256 ile birleştirilir:


$$
\text{HASH160}(m) = \text{RIPEMD160}(\text{SHA256}(m))
$$


Bu kombinasyon generate daha kısa hash'ler için, özellikle de anahtarların hash'lerini veya komut dosyası hash'lerini temsil eden belirli Bitcoin adreslerinin oluşturulmasında ve anahtar parmak izlerinin üretilmesinde kullanılır.


Son olarak, yalnızca uygulama düzeyinde, bazen cüzdanlar için anahtar türetmede dolaylı olarak rol oynayan SHA512 işlevi de kullanılır. Bu işlev çalışma açısından SHA256'ya çok benzer; her ikisi de aynı SHA2 ailesine aittir, ancak SHA512, adından da anlaşılacağı gibi, SHA256 için 256 bit ile karşılaştırıldığında 512 bitlik bir Hash üretir. Kullanımını ilerleyen bölümlerde detaylandıracağız.


Artık bundan sonrası için hashing fonksiyonları hakkında temel bilgileri biliyorsunuz. Bir sonraki bölümde, Bitcoin'ün kalbinde yer alan SHA256 fonksiyonunun işleyişini daha ayrıntılı olarak keşfetmeyi öneriyorum. Burada tanımladığımız özelliklere nasıl ulaştığını anlamak için onu inceleyeceğiz. Bir sonraki bölüm oldukça uzun ve tekniktir, ancak eğitimin geri kalanını takip etmek için gerekli değildir. Bu nedenle, anlamakta zorluk çekiyorsanız endişelenmeyin ve doğrudan çok daha erişilebilir olacak bir sonraki bölüme geçin.


## SHA256'nın İç Çalışmaları


<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>


Daha önce hashing fonksiyonlarının Bitcoin'te kullanılmalarını haklı çıkaran önemli özelliklere sahip olduğunu görmüştük. Şimdi bu hash fonksiyonlarına bu özellikleri kazandıran iç mekanizmalarını inceleyelim ve bunu yapmak için SHA256'nın çalışmasını incelemeyi öneriyorum.


SHA256 ve SHA512 işlevleri aynı SHA2 ailesine aittir. Mekanizmaları **Merkle-Damgård yapısı** adı verilen özel bir yapıya dayanır. RIPEMD160 da bu aynı tür yapıyı kullanır.


Bir hatırlatma olarak, SHA256'ya girdi olarak rastgele boyutta bir mesajımız var ve çıktı olarak 256 bit Hash elde etmek için bunu fonksiyondan geçireceğiz.


### Girdinin ön işlemden geçirilmesi


Başlangıç olarak, $m$ girdi mesajımızı 512 bitin katı olan standart bir uzunluğa sahip olacak şekilde hazırlamamız gerekir. Bu adım, daha sonra algoritmanın düzgün çalışması için çok önemlidir.

Bunu yapmak için, dolgu bitleri adımıyla başlarız. Mesaja önce bir ayırıcı bit `1` ekliyoruz, ardından belirli sayıda `0` biti ekliyoruz. Eklenen `0` bitlerinin sayısı, bu eklemeden sonra mesajın toplam uzunluğu 448 modulo 512 ile uyumlu olacak şekilde hesaplanır. Böylece, mesajın dolgu bitleriyle birlikte uzunluğu $L$'ye eşit olur:


$$
L \equiv 448 \mod 512
$$


$\text{mod}$, modulo için, iki tamsayı arasında, birincinin ikinciye Öklidyen bölümünün kalanını döndüren matematiksel bir işlemdir. Örneğin: $16 \mod 5 = 1$. Kriptografide yaygın olarak kullanılan bir işlemdir.


Burada, dolgu adımı, bir sonraki adımda 64 bit eklendikten sonra, eşitlenmiş mesajın toplam uzunluğunun 512 bitin katı olmasını sağlar. İlk mesajın uzunluğu $M$ bit ise, eklenecek `0` bit sayısı ($N$) bu şekilde bulunur:


$$
N = (448 - (M + 1) \mod 512) \mod 512
$$


Örneğin, ilk mesaj 950 bit ise, hesaplama aşağıdaki gibi olacaktır:


$$
\begin{align*}
M & = 950 \\
M + 1 & = 951 \\
(M + 1) \mod 512 & = 951 \mod 512 \\
& = 951 - 512 \cdot \left\lfloor \frac{951}{512} \right\rfloor \\
& = 951 - 512 \cdot 1 \\
& = 951 - 512 \\
& = 439 \\
\\
448 - (M + 1) \mod 512 & = 448 - 439 \\
& = 9 \\
\\
N & = (448 - (M + 1) \mod 512) \mod 512 \\
N & = 9 \mod 512 \\
& = 9
\end{align*}
$$


Böylece, ayırıcı `1`e ek olarak 9 `0`a sahip oluruz. Böylece $M$ mesajımızdan hemen sonra eklenecek dolgu bitlerimiz şöyle olacaktır:


```text
1000 0000 00
```


Dolgu bitlerini $M$ mesajımıza ekledikten sonra, $M$ mesajının orijinal uzunluğunun ikili olarak ifade edilen 64 bitlik bir gösterimini de ekleriz. Bu, Hash fonksiyonunun bitlerin sırasına ve mesajın uzunluğuna duyarlı olmasını sağlar.


Başlangıç mesajı 950 bit olan örneğimize geri dönersek, `950` ondalık sayısını ikilik sayıya çeviririz, bu da bize `1110 1101 10` sayısını verir. Toplam 64 bit yapmak için bu sayıyı tabandaki sıfırlarla tamamlarız. Örneğimizde, bu şunu verir:


```text
0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0011 1011 0110
```


Bu dolgu boyutu bit dolgusunun ardından eklenir. Dolayısıyla, ön işlememizden sonra mesaj üç parçadan oluşur:



- Orijinal mesaj $M$;
- Bit dolgusunu oluşturmak için bir bit `1` ve ardından birkaç bit `0`;
- Boyut ile dolgu oluşturmak için $M$ uzunluğunun 64 bitlik bir gösterimi.


![CYP201](assets/fr/006.webp)


### Değişkenlerin Başlatılması


SHA256, $A$ ile $H$ arasında gösterilen ve her biri 32 bitten oluşan sekiz başlangıç durum değişkeni kullanır. Bu değişkenler, ilk sekiz asal sayının kareköklerinin kesirli kısımları olan belirli sabitlerle başlatılır. Bu değerleri daha sonra hashing işlemi sırasında kullanacağız:



- $A = 0x6a09e667$
- b = 0xbb67ae85$
- $C = 0x3c6ef372$
- $D = 0xa54ff53a$
- e = 0x510e527f$
- $F = 0x9b05688c$
- $G = 0x1f83d9ab$
- $H = 0x5be0cd19$


SHA256 ayrıca $K_0$ ile $K_{63}$ arasında gösterilen ve ilk 64 asal sayının küp köklerinin kesirli kısımları olan 64 sabit daha kullanır:


$$
K[0 \ldots 63] = \begin{pmatrix}
0x428a2f98, & 0x71374491, & 0xb5c0fbcf, & 0xe9b5dba5, \\
0x3956c25b, & 0x59f111f1, & 0x923f82a4, & 0xab1c5ed5, \\
0xd807aa98, & 0x12835b01, & 0x243185be, & 0x550c7dc3, \\
0x72be5d74, & 0x80deb1fe, & 0x9bdc06a7, & 0xc19bf174, \\
0xe49b69c1, & 0xefbe4786, & 0x0fc19dc6, & 0x240ca1cc, \\
0x2de92c6f, & 0x4a7484aa, & 0x5cb0a9dc, & 0x76f988da, \\
0x983e5152, & 0xa831c66d, & 0xb00327c8, & 0xbf597fc7, \\
0xc6e00bf3, & 0xd5a79147, & 0x06ca6351, & 0x14292967, \\
0x27b70a85, & 0x2e1b2138, & 0x4d2c6dfc, & 0x53380d13, \\
0x650a7354, & 0x766a0abb, & 0x81c2c92e, & 0x92722c85, \\
0xa2bfe8a1, & 0xa81a664b, & 0xc24b8b70, & 0xc76c51a3, \\
0xd192e819, & 0xd6990624, & 0xf40e3585, & 0x106aa070, \\
0x19a4c116, & 0x1e376c08, & 0x2748774c, & 0x34b0bcb5, \\
0x391c0cb3, & 0x4ed8aa4a, & 0x5b9cca4f, & 0x682e6ff3, \\
0x748f82ee, & 0x78a5636f, & 0x84c87814, & 0x8cc70208, \\
0x90befffa, & 0xa4506ceb, & 0xbef9a3f7, & 0xc67178f2
\end{pmatrix}
$$


### Girdinin Bölünmesi


Artık eşitlenmiş bir girdimiz olduğuna göre, şimdi SHA256 algoritmasının ana işlem aşamasına geçeceğiz: sıkıştırma fonksiyonu. Bu adım çok önemlidir, çünkü Hash fonksiyonuna bir önceki bölümde incelediğimiz kriptografik özelliklerini veren şeydir.


İlk olarak, eşitlenmiş mesajımızı (ön işleme adımlarının sonucu) her biri 512 bitlik birkaç $P$ bloğa bölerek başlarız. Eğer eşitlenmiş mesajımızın toplam boyutu $n \times 512$ bit ise, her biri 512 bitlik $n$ bloğumuz olacaktır. Her 512 bitlik blok, 64 tur ardışık işlemden oluşan sıkıştırma fonksiyonu tarafından ayrı ayrı işlenecektir. Bu blokları $P_1$, $P_2$, $P_3$... olarak adlandıralım.


### Mantıksal İşlemler


Sıkıştırma işlevini ayrıntılı olarak incelemeden önce, içinde kullanılan temel mantıksal işlemleri anlamak önemlidir. Boole cebirine dayanan bu işlemler bit seviyesinde çalışır. Kullanılan temel mantıksal işlemler şunlardır:



- **Bağlaç (VE)**: $\land$ olarak gösterilir, mantıksal bir "VE" ye karşılık gelir.
- **Ayrıklık (VEYA)**: $\lor$ olarak gösterilir, mantıksal bir "VEYA"ya karşılık gelir.
- **Olumsuzlama (DEĞİL)**: $\lnot$ olarak gösterilir, mantıksal bir "DEĞİL"e karşılık gelir.


Bu temel işlemlerden, kriptografide yaygın olarak kullanılan $\oplus$ ile gösterilen "Exclusive OR" (XOR) gibi daha karmaşık işlemleri tanımlayabiliriz.

Her mantıksal işlem, ikili giriş değerlerinin (iki işlenen $p$ ve $q$) tüm olası kombinasyonları için sonucu gösteren bir doğruluk tablosu ile temsil edilebilir.

XOR ($\oplus$) için:


| $p$ | $q$ | $p \oplus q$ |
| --- | --- | ------------ |
| 0   | 0   | 0            |
| 0   | 1   | 1            |
| 1   | 0   | 1            |
| 1   | 1   | 0            |

AND ($\land$) için:


| $p$ | $q$ | $p \land q$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

NOT ($\lnot p$) için:


| $p$ | $\lnot p$ |
| --- | --------- |
| 0   | 1         |
| 1   | 0         |

XOR işlemini bit seviyesinde anlamak için bir örnek verelim. Eğer elimizde 6 bitlik iki ikili sayı varsa:



- $a = 101100$
- $b = 001000$


Sonra:


$$

a \oplus b = 101100 \oplus 001000 = 100100


$$


Bit bit XOR uygulayarak:


| Bit Position | $a$ | $b$ | $a \oplus b$ |
| ------------ | --- | --- | ------------ |
| 1            | 1   | 0   | 1            |
| 2            | 0   | 0   | 0            |
| 3            | 1   | 1   | 0            |
| 4            | 1   | 0   | 1            |
| 5            | 0   | 0   | 0            |
| 6            | 0   | 0   | 0            |

Dolayısıyla sonuç 100100$'dır.


Mantıksal işlemlere ek olarak, sıkıştırma işlevi, algoritmadaki bitlerin yayılmasında önemli bir rol oynayacak olan bit kaydırma işlemlerini kullanır.


İlk olarak $ShR_n(x)$ olarak gösterilen mantıksal sağa kaydırma işlemi vardır, bu işlem $x$'in tüm bitlerini $n$ pozisyon sağa kaydırır ve soldaki boş bitleri sıfırlarla doldurur.


Örneğin, $x = 101100001$ (9 bit üzerinde) ve $n = 4$ için:


$$

ShR_4(101100001) = 000010110


$$


Şematik olarak, sağa kaydırma işlemi şu şekilde görülebilir:


![CYP201](assets/fr/007.webp)


SHA256'da bit manipülasyonu için kullanılan bir başka işlem de $RotR_n(x)$ olarak gösterilen ve $x$ bitlerini $n$ pozisyon sağa kaydırarak kaydırılan bitleri dizenin başına yeniden yerleştiren sağ dairesel döndürmedir.

Örneğin, $x = 101100001$ (9 bit üzerinden) ve $n = 4$ için:


$$

RotR_4(101100001) = 000110110


$$


Şematik olarak, sağ dairesel kaydırma işlemi şu şekilde görülebilir:


![CYP201](assets/fr/008.webp)


### Sıkıştırma Fonksiyonu


Temel işlemleri anladığımıza göre şimdi SHA256 sıkıştırma fonksiyonunu detaylı olarak inceleyelim.


Bir önceki adımda, girdimizi 512 bitlik birkaç $P$ parçaya böldük. Her 512 bitlik $P$ bloğu için şunlara sahibiz:



- Mesaj kelimeleri **$W_i$**: 0 ila 63 arasındaki $i$ için.
- **K_i sabitleri:** $i$ için 0'dan 63'e kadar, önceki adımda tanımlanmıştır.
- Durum değişkenleri $A, B, C, D, E, F, G, H$: bir önceki adımdaki değerlerle başlatılır.


İlk 16 kelime, $W_0$ ila $W_{15}$, işlenmiş 512 bitlik $P$ bloğundan doğrudan çıkarılır. Her $W_i$ sözcüğü bloktaki 32 ardışık bitten oluşur. Örneğin, ilk girdi parçamız $P_1$'i alırız ve onu kelime olarak adlandırdığımız daha küçük 32 bitlik parçalara böleriz.


Sonraki 48 kelime ($W_{16}$ ila $W_{63}$) aşağıdaki formül kullanılarak oluşturulur:


$$
W_i = W_{i-16} + \sigma_0(W_{i-15}) + W_{i-7} + \sigma_1(W_{i-2}) \mod 2^{32}
$$


Ile:



- $\sigma_0(x) = RotR_7(x) \oplus RotR_{18}(x) \oplus ShR_3(x)$
- $\sigma_1(x) = RotR_{17}(x) \oplus RotR_{19}(x) \oplus ShR_{10}(x)$


Bu durumda $x$, $\sigma_0(x)$ için $W_{i-15}$ ve $\sigma_1(x)$ için $W_{i-2}$ değerlerine eşittir.


512-bitlik parçamız için tüm $W_i$ kelimelerini belirledikten sonra, 64 tur gerçekleştirmekten oluşan sıkıştırma işlevine geçebiliriz.


![CYP201](assets/fr/009.webp)

0'dan 63'e kadar her $i$ turu için üç farklı türde girdimiz var. Birincisi, daha önce belirlediğimiz ve kısmen $P_n$ mesaj parçamızdan oluşan $W_i$. Sonra, 64 sabit $K_i$. Son olarak, hashing işlemi boyunca gelişecek ve her sıkıştırma fonksiyonuyla değiştirilecek olan $A$, $B$, $C$, $D$, $E$, $F$, $G$ ve $H$ durum değişkenlerini kullanıyoruz. Bununla birlikte, ilk parça $P_1$ için daha önce verilen başlangıç sabitlerini kullanırız.


Daha sonra girdilerimiz üzerinde aşağıdaki işlemleri gerçekleştiriyoruz:



- Fonksiyon $\Sigma_0$:


$$
\Sigma_0(A) = RotR_2(A) \oplus RotR_{13}(A) \oplus RotR_{22}(A)
$$



- Fonksiyon $\Sigma_1$:


$$
\Sigma_1(E) = RotR_6(E) \oplus RotR_{11}(E) \oplus RotR_{25}(E)
$$



- Fonksiyon $Ch$ ("_Choose_"):


$$
Ch(E, F, G) = (E \land F) \oplus (\lnot E \land G)
$$



- Fonksiyon $Maj$ ("_Majority_"):


$$
Maj(A, B, C) = (A \land B) \oplus (A \land C) \oplus (B \land C)
$$


Daha sonra 2 geçici değişken hesaplıyoruz:



- $temp1$:


$$
temp1 = H + \Sigma_1(E) + Ch(E, F, G) + K_i + W_i \mod 2^{32}
$$



- $temp2$:


$$
temp2 = \Sigma_0(A) + Maj(A, B, C) \mod 2^{32}
$$


Ardından, durum değişkenlerini aşağıdaki gibi güncelleriz:


$$
\begin{cases}
H = G \\
G = F \\
F = E \\
E = D + temp1 \mod 2^{32} \\
D = C \\
C = B \\
B = A \\
A = temp1 + temp2 \mod 2^{32}
\end{cases}
$$


Aşağıdaki diyagram, SHA256 sıkıştırma işlevinin az önce açıkladığımız bir turunu temsil etmektedir:


![CYP201](assets/fr/010.webp)



- Oklar veri akışını göstermektedir;
- Kutular gerçekleştirilen işlemleri temsil etmektedir;
- Etrafındaki $+$, $2^{32}$ modulo toplama işlemini temsil eder.


Bu turun yeni durum değişkenleri $A$, $B$, $C$, $D$, $E$, $F$, $G$ ve $H$ ürettiğini gözlemleyebiliriz. Bu yeni değişkenler bir sonraki tur için girdi görevi görecek ve bu da bir sonraki turda kullanılmak üzere yeni $A$, $B$, $C$, $D$, $E$, $F$, $G$ ve $H$ değişkenleri üretecektir. Bu süreç 64. tura kadar devam eder.

64 turdan sonra, durum değişkenlerinin başlangıç değerlerini 64. turun sonundaki nihai değerlere ekleyerek güncelliyoruz:


$$
\begin{cases}
A = A_{\text{initial}} + A \mod 2^{32} \\
B = B_{\text{initial}} + B \mod 2^{32} \\
C = C_{\text{initial}} + C \mod 2^{32} \\
D = D_{\text{initial}} + D \mod 2^{32} \\
E = E_{\text{initial}} + E \mod 2^{32} \\
F = F_{\text{initial}} + F \mod 2^{32} \\
G = G_{\text{initial}} + G \mod 2^{32} \\
H = H_{\text{initial}} + H \mod 2^{32}
\end{cases}
$$


Bu yeni $A$, $B$, $C$, $D$, $E$, $F$, $G$ ve $H$ değerleri bir sonraki blok olan $P_2$ için başlangıç değerleri olarak kullanılacaktır. Bu $P_2$ bloğu için aynı sıkıştırma işlemini 64 turla tekrarlarız, ardından $P_3$ bloğu için değişkenleri güncelleriz ve eşitlenmiş girdimizin son bloğuna kadar bu şekilde devam ederiz.


Tüm mesaj bloklarını işledikten sonra, $A$, $B$, $C$, $D$, $E$, $F$, $G$ ve $H$ değişkenlerinin nihai değerlerini birleştirerek hashing fonksiyonumuzun nihai 256-bit Hash'ini oluşturuyoruz:


$$

\text{Hash} = A \Vert B \Vert C \Vert D \Vert E \Vert F \Vert G \Vert H


$$


Her değişken 32 bitlik bir tamsayıdır, bu nedenle hashing işlevine mesaj girdimizin boyutu ne olursa olsun, bunların birleştirilmesi her zaman 256 bitlik bir sonuç verir.


### Kriptografik Özelliklerin Gerekçelendirilmesi


Peki ama bu işlev nasıl geri döndürülemez, çarpışmaya ve kurcalanmaya karşı dayanıklıdır?


Kurcalama direnci için bunu anlamak oldukça basittir. Hem girişe hem de sabitlere bağlı olarak kademeli olarak gerçekleştirilen o kadar çok hesaplama vardır ki, başlangıç mesajındaki en ufak bir değişiklik izlenen yolu tamamen değiştirir ve dolayısıyla Hash çıkışını da tamamen değiştirir. Çığ etkisi olarak adlandırılan şey budur. Bu özellik kısmen ara durumların her bir parça için başlangıç durumlarıyla karıştırılmasıyla sağlanır.

Daha sonra, bir kriptografik Hash fonksiyonunu tartışırken, "tersinmezlik" terimi genellikle kullanılmaz. Bunun yerine, verilen herhangi bir $y$ için $h(x) = y$ olacak şekilde bir $x$ bulmanın zor olduğunu belirten "ön görüntü direnci" hakkında konuşuyoruz. Bu ön görüntü direnci, sıkıştırma fonksiyonunda gerçekleştirilen işlemlerin cebirsel karmaşıklığı ve güçlü doğrusal olmayışının yanı sıra süreçteki belirli bilgilerin kaybı ile garanti edilir. Örneğin, bir toplama modülünün belirli bir sonucu için, birkaç olası işlenen vardır:


$$

3+2 \mod 10 = 5 \\
7+8 \mod 10 = 5 \\
5+10 \mod 10 = 5


$$


Bu örnekte, yalnızca kullanılan modulo (10) ve sonuç (5) bilindiğinde, toplama işleminde kullanılan doğru işlenenlerin hangileri olduğu kesin olarak belirlenemez. Modulo 10'un birden fazla eşleniği olduğu söylenir.


XOR işlemi için de aynı sorunla karşı karşıyayız. Bu işlem için doğruluk tablosunu hatırlayın: herhangi bir 1 bitlik çıktı, doğru değerler olma olasılığı tamamen aynı olan iki farklı giriş konfigürasyonu ile belirlenebilir. Bu nedenle, bir XOR işleminin yalnızca sonucunu bilerek, bu işlemin operandlarını kesin olarak belirleyemeyiz. XOR işlenenlerinin boyutunu artırırsak, yalnızca sonucu bilerek olası girişlerin sayısı üstel olarak artar. Dahası, XOR genellikle $\text{RotR}$ işlemi gibi sonuca daha da fazla olası yorum ekleyen diğer bit seviyesi işlemlerle birlikte kullanılır.


Sıkıştırma işlevi ayrıca $\text{ShR}$ işlemini de kullanır. Bu işlem temel bilgilerin bir kısmını kaldırır ve daha sonra bu bilgilerin geri alınması imkansızdır. Bir kez daha, bu işlemi tersine çevirmek için cebirsel bir yol yoktur. Tüm bu tek yönlü ve bilgi kayıplı işlemler sıkıştırma işlevlerinde çok sık kullanılır. Bu nedenle, belirli bir çıktı için olası girdi sayısı neredeyse sonsuzdur ve her ters hesaplama girişimi, her adımda katlanarak artacak olan çok yüksek sayıda bilinmeyenli denklemlere yol açacaktır.


Son olarak, çarpışma direnci özelliği için birkaç parametre devreye girer. Orijinal mesajın ön işlemden geçirilmesi önemli bir rol oynar. Bu ön işleme olmadan, fonksiyon üzerinde çarpışmalar bulmak daha kolay olabilir. Teorik olarak çarpışmalar mevcut olsa da (güvercin deliği ilkesi nedeniyle), Hash fonksiyonunun yapısı, yukarıda belirtilen özelliklerle birleştiğinde, bir çarpışma bulma olasılığını son derece düşük hale getirir.

Bir Hash fonksiyonunun çarpışmaya dayanıklı olması için şu hususlar gereklidir:



- Çıktı tahmin edilemez: Herhangi bir öngörülebilirlik, kaba kuvvet saldırısından daha hızlı çarpışmaları bulmak için kullanılabilir. İşlev, çıktının her bir bitinin girdiye önemsiz olmayan bir şekilde bağlı olmasını sağlar. Başka bir deyişle, işlev, nihai sonucun her bitinin 0 veya 1 olma olasılığı bağımsız olacak şekilde tasarlanmıştır, bu bağımsızlık pratikte mutlak olmasa bile.
- Karmaların dağılımı sözde rastgeledir: Bu, hash'lerin eşit olarak dağıtılmasını sağlar.
- Hash'ün boyutu önemlidir: sonuçlar için olası alan ne kadar büyük olursa, bir çarpışma bulmak o kadar zor olur.


Kriptograflar bu işlevleri, çarpışmaları bulmak için mümkün olan en iyi saldırıları değerlendirerek ve ardından bu saldırıları etkisiz hale getirmek için parametreleri ayarlayarak tasarlarlar.


### Merkle-Damgård İnşaat


SHA256'nın yapısı, bir sıkıştırma fonksiyonunun keyfi uzunluktaki mesajları işleyebilen bir Hash fonksiyonuna dönüştürülmesini sağlayan Merkle-Damgård yapısına dayanır. Bu bölümde gördüğümüz de tam olarak budur.


Ancak, bu özel yapıyı kullanan SHA1 veya MD5 gibi bazı eski Hash fonksiyonları uzunluk uzatma saldırılarına karşı savunmasızdır. Bu, bir $M$ mesajının Hash'ini ve $M$ uzunluğunu bilen bir saldırganın (mesajın kendisini bilmeden) $M$'nin ek içerikle birleştirilmesiyle oluşturulan bir $M'$ mesajının Hash'ini hesaplamasına olanak tanıyan bir tekniktir.


SHA256, aynı yapı türünü kullansa da SHA1 ve MD5'in aksine teorik olarak bu tür saldırılara karşı dirençlidir. Bu, Satoshi Nakamoto tarafından Bitcoin boyunca uygulanan çift hashing'in gizemini açıklayabilir. Bu tür bir saldırıdan kaçınmak için Satoshi çift SHA256 kullanmayı tercih etmiş olabilir:


$$

\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))


$$


Bu, Merkle-Damgård yapısıyla ilgili olası saldırılara karşı güvenliği artırır, ancak çarpışma direnci açısından hashing işleminin güvenliğini artırmaz. Dahası, SHA256 bu tür bir saldırıya karşı savunmasız olsaydı bile, Bitcoin'deki Hash işlevlerinin tüm kullanım durumları herkese açık verileri içerdiğinden ciddi bir etkisi olmazdı. Bununla birlikte, uzunluk uzatma saldırısı bir saldırgan için yalnızca hashlenmiş veriler özelse ve kullanıcı Hash işlevini bu veriler için MAC'e benzer bir kimlik doğrulama mekanizması olarak kullandıysa yararlı olabilir. Bu nedenle, çift hashing uygulaması Bitcoin'in tasarımında bir gizem olarak kalmaktadır.

Bitcoin'da yoğun olarak kullanılan SHA256 başta olmak üzere Hash işlevlerinin işleyişini ayrıntılı olarak incelediğimize göre, özellikle Wallet'inizin anahtarlarını türetmek için uygulama düzeyinde kullanılan kriptografik türetme algoritmalarına daha spesifik olarak odaklanacağız.


## Türetme için kullanılan algoritmalar


<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>


Uygulama düzeyinde Bitcoin'te, Hash işlevlerine ek olarak, başlangıç girdilerinden generate güvenli veri elde etmek için kriptografik türetme algoritmaları kullanılır. Bu algoritmalar Hash işlevlerine dayanmakla birlikte, özellikle kimlik doğrulama ve anahtar üretimi açısından farklı amaçlara hizmet ederler. Bu algoritmalar, Hash fonksiyonlarının geri döndürülemezlik, kurcalanmaya karşı direnç ve çarpışma direnci gibi bazı özelliklerini korur.


Bitcoin cüzdanlarında temel olarak 2 türetme algoritması kullanılır:



- **HMAC (_Hash-based Message Authentication Code_)**
- **PBKDF2** (_Şifre Tabanlı Anahtar Türetme İşlevi 2_)


Her birinin işleyişini ve rolünü birlikte keşfedeceğiz.


### HMAC-SHA512


HMAC, bir Hash işlevi ve bir gizli anahtar kombinasyonuna dayalı olarak bir kimlik doğrulama kodu hesaplayan bir kriptografik algoritmadır. Bitcoin, SHA512 Hash işlevini kullanan HMAC varyantı olan HMAC-SHA512'yi kullanır. Önceki bölümde SHA512'nin SHA256 ile aynı Hash işlevleri ailesinin bir parçası olduğunu, ancak 512 bitlik bir çıktı ürettiğini görmüştük.


Burada $m$ giriş mesajı ve $K$ gizli anahtar olmak üzere genel çalışma şeması verilmiştir:


![CYP201](assets/fr/011.webp)


Bu HMAC-SHA512 kara kutusunda neler olduğunu daha ayrıntılı olarak inceleyelim. HMAC-SHA512 işlevi ile:



- m$: kullanıcı tarafından seçilen keyfi büyüklükteki mesaj (ilk girdi);
- k$: kullanıcı tarafından seçilen rastgele gizli anahtar (ikinci girdi);
- k'$: Hash fonksiyon bloklarının $B$ boyutuna göre ayarlanmış $K$ anahtarı (SHA512 için 1024 bit veya 128 bayt);
- $\text{SHA512}$: SHA512 Hash işlevi;
- $\oplus$: XOR (özel veya) işlemi;
- $\Vert$: bit dizelerini uçtan uca bağlayan birleştirme operatörü;
- $\text{opad}$: 128 kez tekrarlanan $0x5c$ baytından oluşan sabit
- $\text{ipad}$: 128 kez tekrarlanan $0x36$ baytından oluşan sabit.


HMAC hesaplanmadan önce, anahtar ve sabitleri $B$ blok boyutuna göre eşitlemek gerekir. Örneğin, $K$ anahtarı 128 bayttan kısaysa, $B$ boyutuna ulaşmak için sıfırlarla doldurulur. Eğer $K$ 128 bayttan uzunsa, SHA512 kullanılarak sıkıştırılır ve 128 bayta ulaşana kadar sıfırlar eklenir. Bu şekilde $K'$ adında eşitlenmiş bir anahtar elde edilir. B$ boyutuna ulaşılana kadar $\text{opad}$ ve $\text{ipad}$ değerleri temel baytlarının ($\text{opad}$ için $0x5c$, $\text{ipad}$ için $0x36$) tekrarlanmasıyla elde edilir. Böylece, $B = 128$ bayt ile şunu elde ederiz:


$$

\text{opad} = \underbrace{0x5c5c\ldots5c}\_{128 \  \text{bytes}}


$$


Ön işleme yapıldıktan sonra, HMAC-SHA512 algoritması aşağıdaki denklemle tanımlanır:


$$

\text{HMAC-SHA512}(K,m) = \text{SHA512} \left( (K' \oplus \text{opad}) \parallel \text{SHA512} \left( (K' \oplus \text{ipad}) \parallel m \right) \right)


$$


Bu denklem aşağıdaki adımlara ayrılmıştır:



- Düzeltilmiş $K'$ anahtarını $\text{ipad}$ ile XORlayarak $\text{iKpad}$ elde edin;
- Düzeltilmiş $K'$ anahtarını $\text{opad}$ ile XORlayarak $\text{oKpad}$ elde edin;
- M$ iletisi ile $\text{iKpad}$ iletisini birleştirin.
- Hash bu sonucu SHA512 ile birleştirerek bir ara Hash $H_1$ elde eder.
- H_1$ ile $\text{oKpad}$ öğesini birleştirin.
- Nihai $H_2$ sonucunu elde etmek için bu sonucu SHA512 ile Hash.


Bu adımlar şematik olarak aşağıdaki gibi özetlenebilir:


![CYP201](assets/fr/012.webp)


HMAC, Bitcoin'te özellikle HD (Hiyerarşik Deterministik) cüzdanlarda anahtar türetme için (ilerleyen bölümlerde bundan daha ayrıntılı olarak bahsedeceğiz) ve PBKDF2'nin bir bileşeni olarak kullanılır.


### PBKDF2


PBKDF2 (_Password-Based Key Derivation Function 2_) parolaların güvenliğini artırmak için tasarlanmış bir anahtar türetme algoritmasıdır. Algoritma, bir parola ve bir kriptografik tuz üzerinde sözde rastgele bir işlev (burada HMAC-SHA512) uygular ve ardından bir çıktı anahtarı üretmek için bu işlemi belirli sayıda tekrarlar.


Bitcoin'de PBKDF2, bir Mnemonic ifadesinden ve bir passphrase'ten bir HD Wallet'in seed'unu generate yapmak için kullanılır (ancak ilerleyen bölümlerde bundan daha ayrıntılı olarak bahsedeceğiz).


PBKDF2 süreci aşağıdaki gibidir:



- m$: kullanıcının Mnemonic ifadesi;
- s$: güvenliği artırmak için isteğe bağlı passphrase (passphrase yoksa boş alan);
- $n$: fonksiyonun yineleme sayısı, bizim durumumuzda 2048'dir.


PBKDF2 işlevi yinelemeli olarak tanımlanır. Her yineleme bir öncekinin sonucunu alır, HMAC-SHA512'den geçirir ve nihai anahtarı üretmek için birbirini izleyen sonuçları birleştirir:


$$

\text{PBKDF2}(m, s) = \text{HMAC-SHA512}^{2048}(m, s)


$$


Şematik olarak PBKDF2 aşağıdaki gibi gösterilebilir:


![CYP201](assets/fr/013.webp)


Bu bölümde, Bitcoin protokolünde anahtar türetme işlemlerinin bütünlüğünü ve güvenliğini sağlamak için karma işlevlerini kullanan HMAC-SHA512 ve PBKDF2 işlevlerini inceledik. Bir sonraki bölümde, Bitcoin'de yaygın olarak kullanılan bir başka kriptografik yöntem olan dijital imzaları inceleyeceğiz.


# Dijital İmzalar


<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>


## Dijital İmzalar ve Eliptik Eğriler


<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>


Bitcoin'te kullanılan ikinci kriptografik yöntem dijital imza algoritmalarını içerir. Bunun ne anlama geldiğini ve nasıl çalıştığını inceleyelim.


### Bitcoinler, UTXO'lar ve Harcama Koşulları


Bitcoin'teki "_wallet_" terimi yeni başlayanlar için oldukça kafa karıştırıcı olabilir. Aslında, Bitcoin Wallet olarak adlandırılan şey, madeni para veya banknot tutabilen fiziksel bir Wallet'in aksine, bitcoinlerinizi doğrudan tutmayan bir yazılımdır. Bitcoinler basitçe hesap birimleridir. Bu hesap birimi, harcanmamış işlem çıktıları olan **UTXO** (_Harcanmamış İşlem Çıktıları_) ile temsil edilir. Bu çıktılar harcanmamışsa, bir kullanıcıya ait oldukları anlamına gelir. UTXO'lar, bir bakıma, bir kullanıcıya ait değişken büyüklükte bitcoin parçalarıdır.


Bitcoin protokolü dağıtıktır ve merkezi bir otorite olmadan çalışır. Bu nedenle, size ait olan avroların sadece kişisel kimliğinizle ilişkilendirildiği geleneksel bankacılık kayıtları gibi değildir. Bitcoin'de UTXO'larınız size aittir çünkü Komut Dosyası dilinde belirtilen harcama koşulları ile korunmaktadırlar. Basitleştirmek gerekirse, iki tür komut dosyası vardır: bir UTXO'i koruyan kilitleme komut dosyası (_scriptPubKey_) ve bir UTXO'in kilidini açmaya ve böylece temsil ettiği Bitcoin birimlerini harcamaya izin veren kilit açma komut dosyası (_scriptSig_).

Bitcoin'nin P2PK komut dosyalarıyla ilk çalışması, fonları kilitlemek için bir açık anahtar kullanılmasını ve bir _scriptPubKey_ içinde bu UTXO'i harcamak isteyen kişinin bu açık anahtara karşılık gelen özel anahtarla geçerli bir imza sağlaması gerektiğini belirtmeyi içerir. Bu UTXO'in kilidini açmak için, bu nedenle _scriptSig_ içinde geçerli bir imza sağlamak gerekir. Adlarından da anlaşılacağı üzere, açık anahtar Blockchain'da yayınlandığı için herkes tarafından bilinirken, özel anahtar yalnızca fonların meşru sahibi tarafından bilinir.

Bu Bitcoin'ün temel işlemidir, ancak zamanla bu işlem daha karmaşık hale gelmiştir. İlk olarak Satoshi, _scriptPubKey_'de açık anahtarın Hash'sini temsil eden bir alıcı Address kullanan P2PKH komut dosyalarını da tanıttı. Daha sonra SegWit ve ardından Taproot'in gelmesiyle sistem daha da karmaşık hale geldi. Bununla birlikte, genel prensip temelde aynı kalır: UTXO'ları kilitlemek için bir genel anahtar veya bu anahtarın bir temsili kullanılır ve bunların kilidini açmak ve böylece harcamak için karşılık gelen bir özel anahtar gereklidir.


Bu nedenle, Bitcoin işlemi yapmak isteyen bir kullanıcı, işlem üzerinde kendi özel anahtarını kullanarak bir dijital imza oluşturmalıdır. İmza diğer ağ katılımcıları tarafından doğrulanabilir. İmza geçerliyse bu, işlemi başlatan kullanıcının gerçekten de özel anahtarın sahibi olduğu ve dolayısıyla harcamak istediği bitcoinlerin sahibi olduğu anlamına gelir. Diğer kullanıcılar daha sonra işlemi kabul edebilir ve yayabilir.


Sonuç olarak, açık anahtarla kilitlenmiş bitcoinlere sahip olan bir kullanıcı, fonlarının kilidini açmaya izin veren şeyi güvenli bir şekilde saklamanın bir yolunu bulmalıdır: özel anahtar. Bitcoin Wallet tam olarak tüm anahtarlarınızı başkalarının erişimi olmadan kolayca saklamanızı sağlayacak bir cihazdır. Bu nedenle Wallet'dan çok bir anahtarlığa benzer.


Bir açık anahtar ile bir özel anahtar arasındaki matematiksel bağlantı ve bir özel anahtara sahip olunduğunun ifşa edilmeden kanıtlanması için imza atılabilmesi, bir dijital imza algoritması ile mümkün olmaktadır. Bitcoin protokolünde iki imza algoritması kullanılır: **ECDSA** (_Elliptic Curve Digital Signature Algorithm_) ve **Schnorr imza şeması**. ECDSA, başlangıcından itibaren Bitcoin'de kullanılan dijital imza protokolüdür. Schnorr, Kasım 2021'de Taproot güncellemesiyle tanıtıldığı için Bitcoin'de daha yenidir.

Bu iki algoritma mekanizmaları açısından oldukça benzerdir. Her ikisi de eliptik eğri kriptografisine dayanmaktadır. Bu iki protokol arasındaki en büyük fark imzanın yapısında ve bazı özel matematiksel özelliklerde yatmaktadır. Bu nedenle, en eskisinden başlayarak bu algoritmaların işleyişini inceleyeceğiz: ECDSA.


### Eliptik Eğri Kriptografisi


Eliptik Eğri Kriptografisi (ECC), kriptografik amaçlarla çeşitli matematiksel ve geometrik özellikleri için eliptik eğri kullanan bir dizi algoritmadır. Bu algoritmaların güvenliği, eliptik eğriler üzerindeki ayrık logaritma probleminin zorluğuna dayanır. Eliptik eğriler özellikle anahtar değişimi, asimetrik şifreleme veya dijital imza oluşturmak için kullanılır.


Bu eğrilerin önemli bir özelliği x eksenine göre simetrik olmalarıdır. Dolayısıyla, eğriyi iki farklı noktada kesen dikey olmayan herhangi bir doğru, eğriyi her zaman üçüncü bir noktada kesecektir. Ayrıca, tekil olmayan bir noktada eğriye teğet olan herhangi bir doğru, eğriyi başka bir noktada kesecektir. Bu özellikler eğri üzerindeki işlemleri tanımlamak için faydalı olacaktır.


Burada gerçek sayılar alanı üzerinde bir eliptik eğrinin gösterimi yer almaktadır:


![CYP201](assets/fr/014.webp)


Her eliptik eğri aşağıdaki formda bir denklemle tanımlanır:


$$

y^2 = x^3 + ax + b


$$


### secp256k1


ECDSA veya Schnorr kullanmak için eliptik eğrinin parametrelerini, yani eğri denklemindeki $a$ ve $b$ değerlerini seçmek gerekir. Kriptografik olarak güvenli olduğu bilinen farklı eliptik eğri standartları vardır. En bilineni NIST (_National Institute of Standards and Technology_) tarafından tanımlanan ve önerilen _secp256r1_ eğrisidir.


Buna rağmen, Bitcoin'ün mucidi olan Satoshi Nakamoto bu eğriyi kullanmamayı tercih etmiştir. Bu seçimin nedeni bilinmemektedir, ancak bazıları bu eğrinin parametrelerinin potansiyel olarak bir arka kapı içerebileceği için bir alternatif bulmayı tercih ettiğine inanmaktadır. Bunun yerine, Bitcoin protokolü standart **_secp256k1_** eğrisini kullanır. Bu eğri $a = 0$ ve $b = 7$ parametreleri ile tanımlanır. Bu nedenle denklemi şöyledir:


$$

y^2 = x^3 + 7


$$


Gerçek sayılar alanı üzerindeki grafiksel gösterimi şu şekildedir:


![CYP201](assets/fr/015.webp)


Ancak kriptografide sonlu sayı kümeleri ile çalışırız. Daha spesifik olarak, $\mathbb{F}_p$ sonlu cismi üzerinde çalışırız, bu cisim bir $p$ asal sayısının modulo tamsayılar cismidir.

**Tanım**: Asal sayı, sadece iki farklı pozitif tamsayı bölenine sahip 2'den büyük veya eşit bir doğal tamsayıdır: 1 ve kendisi. Örneğin, 7 sayısı sadece 1 ve 7 ile bölünebildiği için asal bir sayıdır. Öte yandan, 8 sayısı asal değildir çünkü 1, 2, 4 ve 8 ile bölünebilir.

Bitcoin'da sonlu alanı tanımlamak için kullanılan $p$ asal sayısı çok büyüktür. Bu sayı, alanın mertebesi (yani $\mathbb{F}_p$ içindeki Elements sayısı) kriptografik güvenliği sağlamak için yeterince büyük olacak şekilde seçilir.


Kullanılan asal sayı $p$'dir:


```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```


Ondalık gösterimde bu şuna karşılık gelir:


$$

p = 2^{256} - 2^{32} - 977


$$


Böylece, eliptik eğrimizin denklemi aslında:


$$

y^2 \equiv x^3 + 7 \mod p


$$


Bu eğrinin $\mathbb{F}_p$ sonlu alanı üzerinde tanımlandığı göz önüne alındığında, artık sürekli bir eğriye değil, ayrık bir nokta kümesine benzemektedir. Örneğin, Bitcoin'de kullanılan eğrinin çok küçük bir $p = 17$ için nasıl göründüğü aşağıda verilmiştir:


![CYP201](assets/fr/016.webp)


Bu örnekte, eğitim amaçlı olarak sonlu alanı $p = 17$ ile sınırlandırdım, ancak Bitcoin'de kullanılanın çok daha büyük, neredeyse $2^{256}$ olduğunu hayal etmek gerekir.


Eğri üzerindeki işlemlerin doğruluğunu sağlamak için sonlu bir tamsayılar modulo $p$ alanı kullanıyoruz. Aslında, reel sayılar alanı üzerindeki eliptik eğriler, hesaplama sırasında yuvarlama hatalarından kaynaklanan yanlışlıklara maruz kalırlar. Eğri üzerinde çok sayıda işlem yapılırsa, bu hatalar birikir ve nihai sonuç yanlış veya yeniden üretilmesi zor olabilir. Pozitif tam sayıların özel olarak kullanılması, hesaplamaların mükemmel doğruluğunu ve dolayısıyla sonucun tekrarlanabilirliğini sağlar.


Sonlu cisimler üzerindeki eliptik eğrilerin matematiği, tüm işlemlerin modulo $p$ ile yapılması uyarlamasıyla, reel sayılar cismi üzerindekilere benzerdir. Açıklamaları basitleştirmek için, ilerleyen bölümlerde kavramları reel sayılar üzerinde tanımlı bir eğri kullanarak göstermeye devam edeceğiz, ancak pratikte eğrinin sonlu bir cisim üzerinde tanımlı olduğunu aklımızda tutacağız.


Modern kriptografinin matematiksel temelleri hakkında daha fazla bilgi edinmek isterseniz, Plan ₿ Network'daki bu diğer kursa da başvurmanızı tavsiye ederim:


https://planb.network/courses/d2fd9fc0-d9ed-4a87-9fa3-0fdbb3937e28

## Özel Anahtardan Açık Anahtarın Hesaplanması


<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>

Daha önce görüldüğü gibi, Bitcoin'taki dijital imza algoritmaları matematiksel olarak bağlantılı bir çift özel ve açık anahtara dayanmaktadır. Bu matematiksel bağlantının ne olduğunu ve nasıl üretildiklerini birlikte inceleyelim.


### Özel Anahtar


Özel anahtar basitçe rastgele veya sözde rastgele bir sayıdır. Bitcoin durumunda, bu sayı 256 bit boyutundadır. Dolayısıyla bir Bitcoin özel anahtarı için olasılık sayısı teorik olarak $2^{256}$'dır.


**Not**: "Sözde rastgele sayı", gerçekten rastgele bir sayının özelliklerine yakın özelliklere sahip olan ancak deterministik bir algoritma tarafından üretilen bir sayıdır.


Ancak pratikte secp256k1 eliptik eğrimiz üzerinde sadece $n$ farklı nokta vardır, burada $n$ eğrinin $G$ jeneratör noktasının mertebesidir. Bu sayının neye karşılık geldiğini daha sonra göreceğiz, ancak geçerli bir özel anahtarın $1$ ile $n-1$ arasında bir tamsayı olduğunu hatırlayın, $n$'nin $2^{256}$'ya yakın ancak biraz daha küçük bir sayı olduğunu bilin. Bu nedenle, Bitcoin'de özel anahtar olmak için geçerli olmayan bazı 256-bit sayılar vardır, özellikle de $n$ ile $2^{256}$ arasındaki tüm sayılar. Rastgele sayının (özel anahtar) üretilmesi $k \geq n$ gibi bir $k$ değeri üretirse, geçersiz kabul edilir ve yeni bir rastgele değer üretilmelidir.


Bu nedenle bir Bitcoin özel anahtarı için olasılık sayısı yaklaşık $n$'dir, bu da 1.158 \times 10^{77}$'e yakın bir sayıdır. Bu sayı o kadar büyüktür ki, rastgele bir özel anahtar seçerseniz, başka bir kullanıcının özel anahtarına denk gelmeniz istatistiksel olarak neredeyse imkansızdır. Ölçek hakkında bir fikir vermesi açısından, Bitcoin'teki olası özel anahtarların sayısı, gözlemlenebilir evrendeki tahmini atomların sayısına yakın bir büyüklüktedir.


İlerleyen bölümlerde göreceğimiz gibi, günümüzde Bitcoin'te kullanılan özel anahtarların çoğu rastgele üretilmemekte, kendisi de sözde rastgele olan bir Mnemonic cümlesinden deterministik olarak türetilmektedir (bu 12 veya 24 kelimelik ünlü cümledir). Bu bilgi ECDSA gibi imza algoritmalarının kullanımı için bir şey değiştirmez, ancak Bitcoin'teki popülerleşmemize yeniden odaklanmamıza yardımcı olur.


Açıklamanın geri kalanında, özel anahtar küçük harf $k$ ile gösterilecektir.


### Açık Anahtar


Açık anahtar eliptik eğri üzerinde $K$ büyük harfi ile gösterilen bir noktadır ve $k$ özel anahtarından hesaplanır. Bu $K$ noktası eliptik eğri üzerinde $(x, y)$ koordinat çifti ile temsil edilir, her koordinat $\mathbb{F}_p$ sonlu cismini tanımlayan asal sayı olan $p$ modülünde bir tam sayıdır.

Uygulamada, sıkıştırılmamış bir açık anahtar 520 bit (veya 65 bayt) ile temsil edilir ve uç uca yerleştirilmiş iki 256 bitlik sayıya ($x$ ve $y$) karşılık gelir ve önünde 8 bitlik $0x04$ öneki bulunur.


Ancak, sadece eğri üzerindeki noktamızın apsisini $x$ ve $y$'nin paritesini gösteren bir bayt tutarak açık anahtarı sadece 33 bayt (264 bit) kullanarak sıkıştırılmış bir biçimde temsil etmek de mümkündür. Bu sıkıştırılmış açık anahtar olarak bilinir. Bu eğitimin son bölümlerinde bu konu hakkında daha fazla konuşacağım. Ancak hatırlamanız gereken şey $K$ açık anahtarının $x$ ve $y$ ile tanımlanan bir nokta olduğudur.


Açık anahtarımıza karşılık gelen $K$ noktasını hesaplamak için, eliptik eğriler üzerinde skaler çarpma işlemini kullanırız, bu işlem $G$ üreteç noktasının tekrarlanan bir toplama işlemi ($k$ kez) olarak tanımlanır:


$$

K = k \cdot G


$$


nerede?



- k$ özel anahtardır ($1$ ile $n-1$ arasında rastgele bir tamsayı);
- g$, Bitcoin ağının tüm katılımcıları tarafından kullanılan eliptik eğrinin üreteç noktasıdır;
- $\cdot$ eliptik eğri üzerinde $G$ noktasının kendisine $k$ kez eklenmesine eşdeğer olan skaler çarpımı temsil eder.


Bu $G$ noktasının Bitcoin'deki tüm açık anahtarlar için ortak olması, aynı özel anahtarın $k$ bize her zaman aynı açık anahtarı $K$ vereceğinden emin olmamızı sağlar:


![CYP201](assets/fr/017.webp)


Bu işlemin temel özelliği tek yönlü bir fonksiyon olmasıdır. Özel anahtar $k$ ve üreteç noktası $G$ bilinerek açık anahtar $K$'yı hesaplamak kolaydır, ancak yalnızca açık anahtar $K$ ve üreteç noktası $G$ bilinerek özel anahtar $k$'yı hesaplamak pratikte imkansızdır. K$ ve $G$'den $k$'yı bulmak, eliptik eğriler üzerinde ayrık logaritma problemini çözmek anlamına gelir ki bu matematiksel olarak zor bir problemdir ve etkin bir algoritması bilinmemektedir. Günümüzün en güçlü hesap makineleri bile bu problemi makul bir sürede çözememektedir.


![CYP201](assets/fr/018.webp)


### Eliptik Eğriler Üzerinde Noktaların Toplanması ve İkiye Katlanması


Eliptik eğriler üzerinde toplama kavramı geometrik olarak tanımlanır. Eğri üzerinde $P$ ve $Q$ olmak üzere iki nokta varsa, $P + Q$ işlemi $P$ ve $Q$ noktalarından geçen bir doğru çizilerek hesaplanır. Bu doğru zorunlu olarak eğriyi üçüncü bir $R'$ noktasında kesecektir. Daha sonra toplama işleminin sonucu olan $R$ noktasını elde etmek için bu noktanın x eksenine göre ayna görüntüsünü alırız:


$$

P + Q = R


$$


Grafiksel olarak bu durum aşağıdaki gibi gösterilebilir:


![CYP201](assets/fr/019.webp)


Bir noktanın iki katına çıkarılması, yani $P + P$ işlemi için, eğriye $P$ noktasından teğet çizeriz. Bu teğet eğriyi başka bir $S'$ noktasında keser. Daha sonra bu noktanın x eksenine göre ayna görüntüsünü alarak ikiye katlamanın sonucu olan $S$ noktasını elde ederiz:


$$

2P = S


$$


Grafiksel olarak bu şu şekilde gösterilir:


![CYP201](assets/fr/020.webp)


Bu toplama ve ikiye katlama işlemlerini kullanarak, bir noktanın $kP$ olarak gösterilen bir $k$ tamsayısı ile skaler çarpımını, tekrarlanan ikiye katlama ve toplama işlemleri yaparak gerçekleştirebiliriz.


Örneğin, $k = 4$ özel anahtarını seçtiğimizi varsayalım. İlişkili açık anahtarı hesaplamak için şunları yaparız:


$$

K = k \cdot G = 4G


$$


Grafiksel olarak bu, bir dizi toplama ve iki katına çıkarma işlemine karşılık gelir:



- G$'yi iki katına çıkararak $2G$'yi hesaplayın.
- $2G$'yi iki katına çıkararak $4G$'yi hesaplayın.


![CYP201](assets/fr/021.webp)


Örneğin, $3G$ noktasını hesaplamak istiyorsak, önce $G$ noktasını ikiye katlayarak $2G$ noktasını hesaplamalı, ardından $G$ ve $2G$ noktalarını toplamalıyız. G$ ve $2G$ noktalarını toplamak için, bu iki noktayı birleştiren doğruyu çizmek, bu doğru ile eliptik eğrinin kesişimindeki tek $-3G$ noktasını elde etmek ve ardından $3G$ noktasını $-3G$ noktasının tersi olarak belirlemek yeterlidir.


Alacağız:


$$

G + G = 2G


$$


$$

2G + G = 3G


$$


Grafiksel olarak bu durum aşağıdaki gibi gösterilebilir:


![CYP201](assets/fr/022.webp)


### Tek Yönlü Fonksiyon


Bu işlemler sayesinde, bir özel anahtardan bir açık anahtar türetmenin neden kolay olduğunu, ancak tersinin pratikte imkansız olduğunu anlayabiliriz.


Basitleştirilmiş örneğimize geri dönelim. Özel anahtar $k = 4$ olsun. İlişkili açık anahtarı hesaplamak için şunu yaparız:


$$
K = k \cdot G = 4G
$$


Böylece $k$ ve $G$'yi bilerek $K$ açık anahtarını kolayca hesaplayabiliyoruz.


Şimdi, eğer birisi yalnızca $K$ açık anahtarını biliyorsa, ayrık logaritma problemiyle karşı karşıya kalır: $K = k \cdot G$ olacak şekilde $k$ bulmak. Bu problem zor olarak kabul edilir çünkü eliptik eğriler üzerinde bunu çözecek etkili bir algoritma yoktur. Bu, ECDSA ve Schnorr algoritmalarının güvenliğini sağlar.


Elbette, $k = 4$ olan bu basitleştirilmiş örnekte, olasılık sayısı düşük olduğu için $k$'yı deneme yanılma yoluyla bulmak mümkün olacaktır. Ancak pratikte $k$ 256 bitlik bir tamsayıdır, bu da olasılık sayısını astronomik derecede büyük yapar (yaklaşık 1.158 \times 10^{77}$). Bu nedenle, kaba kuvvetle $k$ değerini bulmak mümkün değildir.


## Özel Anahtar ile İmzalama


<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>


Artık bir özel anahtardan bir açık anahtarı nasıl türeteceğinizi bildiğinize göre, bu anahtar çiftini harcama koşulu olarak kullanarak bitcoin alabilirsiniz. Peki bunları nasıl harcayabilirsiniz? Bitcoinleri harcamak için, UTXO'inize ekli _scriptPubKey_'in kilidini açmanız ve gerçekten meşru sahibi olduğunuzu kanıtlamanız gerekecektir. Bunu yapmak için, başlangıçta $K$'yı hesaplamak için kullanılan özel anahtarı $k$ kullanarak _scriptPubKey_'de bulunan açık anahtar $K$ ile eşleşen bir imza $s$ üretmelisiniz. Dolayısıyla dijital imza, iddia ettiğiniz açık anahtarla ilişkili özel anahtara sahip olduğunuzun reddedilemez bir kanıtıdır.


### Eliptik Eğri Parametreleri


Bir dijital imza gerçekleştirmek için, tüm katılımcılar öncelikle kullanılan eliptik eğrinin parametreleri üzerinde anlaşmalıdır. Bitcoin durumunda, **secp256k1** parametreleri aşağıdaki gibidir:


Tarafından tanımlanan $\mathbb{Z}_p$ sonlu cismi:


$$
p = 2^{256} - 2^{32} - 977
$$


```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```


p$, $2^{256}$'dan biraz daha küçük çok büyük bir asal sayıdır.


Tarafından tanımlanan $\mathbb{Z}_p$ üzerinde $y^2 = x^3 + ax + b$ eliptik eğrisi:


$$
a = 0, \quad b = 7
$$


Üreteç noktası veya başlangıç noktası $G$:


```text
G = 0x0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
```


Bu sayı sadece $G$ noktasının apsisini veren sıkıştırılmış formdur. Baştaki `02` öneki, bu apsise $x$ sahip iki değerden hangisinin üretme noktası olarak kullanılacağını belirler.

G$'nin $n$ mertebesi (mevcut noktaların sayısı) ve $h$ kofaktörü:


```text
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
```


n$, $p$'den biraz daha küçük çok büyük bir sayıdır.


$$
h=1
$$


h$ kofaktör ya da alt grup sayısıdır. Oldukça karmaşık olduğu için bunun neyi temsil ettiğini burada detaylandırmayacağım ve Bitcoin durumunda $1$'a eşit olduğu için dikkate almamıza gerek yok.


Tüm bu bilgiler herkese açıktır ve tüm katılımcılar tarafından bilinir. Bu sayede kullanıcılar dijital imza oluşturabilir ve bunu doğrulayabilir.


### ECDSA ile İmza


ECDSA algoritması, bir kullanıcının özel anahtarını kullanarak bir mesajı imzalamasına olanak tanır, öyle ki ilgili açık anahtarı bilen herkes, özel anahtar hiç açıklanmadan imzanın geçerliliğini doğrulayabilir. Bitcoin bağlamında, imzalanacak mesaj kullanıcı tarafından seçilen _sighash_ değerine bağlıdır. İşlemin hangi kısımlarının imza kapsamında olduğunu belirleyecek olan bu _sighash_'tir. Bir sonraki bölümde bu konu hakkında daha fazla konuşacağım.


generate ECDSA imzası için adımlar aşağıda verilmiştir:


İlk olarak, imzalanması gereken mesajın Hash'ünü ($e$) hesaplarız. Böylece $m$ mesajı, genellikle SHA256 veya Bitcoin durumunda çift SHA256 olmak üzere bir kriptografik Hash fonksiyonundan geçirilir:


$$
e = \text{HASH}(m)
$$


Ardından, bir Nonce hesaplayacağız. Kriptografide Nonce basitçe rastgele ya da sözde rastgele bir şekilde üretilen ve yalnızca bir kez kullanılan bir sayıdır. Yani, bu anahtar çifti ile her yeni dijital imza yapıldığında, farklı bir Nonce kullanmak çok önemli olacaktır, aksi takdirde özel anahtarın güvenliğini tehlikeye atacaktır. Bu nedenle, $1 \leq r \leq n-1$ olacak şekilde rastgele ve benzersiz bir $r$ tamsayısı belirlemek yeterlidir; burada $n$ eliptik eğrinin $G$ üretme noktasının mertebesidir.


Daha sonra, eliptik eğri üzerinde $(x_R, y_R)$ koordinatlarına sahip $R$ noktasını hesaplayacağız, öyle ki


$$
R = r \cdot G
$$


R$ noktasının apsis değerini ($x_R$) çıkarıyoruz. Bu değer imzanın ilk kısmını temsil eder. Ve son olarak, $s$ imzasının ikinci kısmını bu şekilde hesaplıyoruz:


$$
s = r^{-1} \left( e + k \cdot x_R \right) \mod n
$$


nerede?



- r^{-1}$ , $r$ modulo $n$ 'nin modüler tersidir, yani $r \cdot r^{-1} \equiv 1 \mod n$ olacak şekilde bir tamsayıdır;
- k$ kullanıcının özel anahtarıdır;
- e$ mesajın Hash'sıdır;
- n$ eliptik eğrinin $G$ jeneratör noktasının mertebesidir.


İmza basitçe $x_R$ ve $s$ değerlerinin birleştirilmesinden oluşur:


$$
\text{SIG} = x_R \Vert s
$$


### ECDSA İmzasının Doğrulanması


Bir $(x_R, s)$ imzasını doğrulamak için, $K$ açık anahtarını ve eliptik eğrinin parametrelerini bilen herkes bu şekilde ilerleyebilir:


İlk olarak, $x_R$ ve $s$ değerlerinin $[1, n-1]$ aralığında olduğunu doğrulayın. Bu, imzanın eliptik grubun matematiksel kısıtlamalarına uymasını sağlar. Eğer durum böyle değilse, doğrulayıcı imzayı hemen geçersiz olarak reddeder.


Ardından, mesajın Hash'sini hesaplayın:


$$
e = \text{HASH}(m)
$$


S$'nin $n$ modülündeki modüler tersini hesaplayın:


$$
s^{-1} \mod n
$$


Bu şekilde iki skaler değeri $u_1$ ve $u_2$ hesaplayın:


$$
\begin{align*}
u_1 &= e \cdot s^{-1} \mod n \\
u_2 &= x_R \cdot s^{-1} \mod n
\end{align*}
$$


Ve son olarak, eliptik eğri üzerindeki $V$ noktasını hesaplayın, öyle ki:


$$
V = u_1 \cdot G + u_2 \cdot K
$$


İmza ancak $x_V \equiv x_R \mod n$ ise geçerlidir; burada $x_V$, $V$ noktasının $x$ koordinatıdır. Aslında, $u_1 \cdot G$ ve $u_2 \cdot K$ birleştirilerek, imza geçerliyse imza sırasında kullanılan $R$ noktasına karşılık gelmesi gereken bir $V$ noktası elde edilir (modulo $n$).


### Schnorr Protokolü ile İmza


Schnorr imza şeması, ECDSA'ya birçok avantaj sunan bir alternatiftir. P2TR kod kalıpları ile 2021'den ve Taproot'un piyasaya sürülmesinden bu yana Bitcoin'de kullanılması mümkün olmuştur. ECDSA gibi, Schnorr şeması da bir mesajın özel anahtar kullanılarak imzalanmasına izin verir, öyle ki imza ilgili açık anahtarı bilen herkes tarafından doğrulanabilir.

Schnorr durumunda, ECDSA ile tamamen aynı eğri aynı parametrelerle kullanılır. Ancak, açık anahtarlar ECDSA'ya kıyasla biraz farklı temsil edilir. Aslında, sadece eliptik eğri üzerindeki noktanın $x$ koordinatı ile belirtilirler. Sıkıştırılmış açık anahtarların 33 bayt ile temsil edildiği ECDSA'nın aksine (ön ek baytı $y$ paritesini gösterir), Schnorr yalnızca $K$ noktasının $x$ koordinatına karşılık gelen 32 baytlık açık anahtarlar kullanır ve varsayılan olarak $y$'nin çift olduğu varsayılır. Bu basitleştirilmiş gösterim imzaların boyutunu azaltır ve doğrulama algoritmalarında belirli optimizasyonları kolaylaştırır.

O halde açık anahtar $K$ noktasının $x$ koordinatıdır:


$$
\text{pk} = K_x
$$


generate imzasının ilk adımı mesajı Hash'ye dönüştürmektir. Ancak ECDSA'dan farklı olarak, bu işlem başka değerlerle yapılır ve farklı bağlamlarda çakışmaları önlemek için etiketli bir Hash işlevi kullanılır. Etiketli bir Hash fonksiyonu basitçe Hash fonksiyonunun girdilerine mesaj verisinin yanında rastgele bir etiket eklemeyi içerir.


![CYP201](assets/fr/023.webp)


Mesaja ek olarak, açık anahtar $K_x$'in $x$ koordinatı ve Nonce $r$'den hesaplanan $R = r \cdot G$ noktası (Nonce'ün yeniden kullanımıyla ilgili güvenlik açıklarını önlemek için özel anahtardan ve mesajdan deterministik olarak hesaplanan, her imza için benzersiz bir tamsayıdır) da etiketli fonksiyona aktarılır. Tıpkı açık anahtarda olduğu gibi, Nonce $R_x$ noktasının yalnızca $x$ koordinatı noktayı tanımlamak için tutulur.


Bu hashing işleminin sonucu $e$ olarak not edilir ve "challenge" olarak adlandırılır:


$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$


Burada, $\text{Hash}$ SHA256 Hash işlevidir ve $\text{``BIP0340/challenge''}$ hashing için özel etikettir.


Son olarak, $s$ parametresi özel anahtar $k$, Nonce $r$ ve meydan okuma $e$'den aşağıdaki gibi hesaplanır:


$$
s = (r + e \cdot k) \mod n
$$


Bu durumda imza basitçe $R_x$ ve $s$ çiftidir.


$$
\text{SIG} = R_x \Vert s
$$


### Schnorr İmzasının Doğrulanması


Bir Schnorr imzasının doğrulanması ECDSA imzasının doğrulanmasından daha basittir. Burada $(R_x, s)$ imzasını $K_x$ açık anahtarı ve $m$ mesajı ile doğrulamak için gerekli adımlar verilmiştir.

İlk olarak, $K_x$ değerinin $p$ değerinden küçük geçerli bir tamsayı olduğunu doğruluyoruz. Eğer durum buysa, $K_y$ çift olacak şekilde eğri üzerindeki ilgili noktayı buluyoruz. Ayrıca $\text{SIG}$ imzasını bölerek $R_x$ ve $s$ değerlerini çıkarıyoruz. Daha sonra $R_x < p$ ve $s < n$ (eğrinin mertebesi) olup olmadığını kontrol ediyoruz.

Daha sonra, $e$ meydan okumasını imzayı atanla aynı şekilde hesaplarız:


$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$


Ardından, bu şekilde eğri üzerinde bir referans noktası hesaplıyoruz:


$$
R' = s \cdot G - e \cdot K
$$


Son olarak, $R'_x = R_x$ olduğunu doğrularız. Eğer iki x-koordinatı eşleşirse, $(R_x, s)$ imzası gerçekten de $K_x$ açık anahtarıyla geçerlidir.


### Bu neden işe yarıyor?


İmzalayan kişi $s = r + e \cdot k \mod n$ olarak hesaplamıştır, bu nedenle $R' = s \cdot G - e \cdot K$ orijinal $R$ noktasına eşit olmalıdır, çünkü:


$$
s \cdot G = (r + e \cdot k) \cdot G = r \cdot G + e \cdot k \cdot G
$$


K = k \cdot G$ olduğundan, $e \cdot k \cdot G = e \cdot K$ olur. Böylece:


$$
R' = r \cdot G = R
$$


Bu nedenle, elimizde:


$$
R'_x = R_x
$$


### Schnorr imzalarının avantajları


Schnorr imza şeması, Bitcoin için orijinal ECDSA algoritmasına göre çeşitli avantajlar sunar. İlk olarak, Schnorr anahtarların ve imzaların toplanmasına izin verir. Bu, birden fazla açık anahtarın tek bir anahtarda birleştirilebileceği anlamına gelir.


![CYP201](assets/fr/024.webp)


Ve benzer şekilde, birden fazla imza tek bir geçerli imzada toplanabilir. Böylece, çok imzalı bir işlem durumunda, bir dizi katılımcı tek bir imza ve tek bir birleştirilmiş açık anahtar ile imzalayabilir. Her düğümün yalnızca tek bir imzayı doğrulaması gerektiğinden, bu durum ağ için depolama ve hesaplama maliyetlerini önemli ölçüde azaltır.


![CYP201](assets/fr/025.webp)


Dahası, imza birleştirme gizliliği artırır. Schnorr ile çok imzalı bir işlemi standart tek imzalı bir işlemden ayırt etmek imkansız hale gelir. Bu homojenlik, Wallet parmak izlerini tanımlama becerisini sınırladığı için zincir analizini daha zor hale getirir.


Son olarak Schnorr, toplu doğrulama imkanı da sunar. Birden fazla imzayı aynı anda doğrulayarak, düğümler özellikle çok sayıda işlem içeren bloklar için verimlilik kazanabilir. Bu optimizasyon, bir bloğu doğrulamak için gereken süreyi ve kaynakları azaltır.

Ayrıca Schnorr imzaları, ECDSA ile üretilen imzaların aksine değiştirilebilir değildir. Bu, bir saldırganın geçerli bir imzayı değiştirerek aynı mesaj ve aynı açık anahtar için başka bir geçerli imza oluşturamayacağı anlamına gelir. Bu güvenlik açığı daha önce Bitcoin'da mevcuttu ve özellikle Lightning Network'in güvenli bir şekilde uygulanmasını engelliyordu. ECDSA için 2017 yılında SegWit softfork ile çözülmüştür ve bu çözüm imzaların değiştirilebilirliğini önlemek için işlemlerden ayrı bir veritabanına taşınmasını içermektedir.


### Satoshi neden ECDSA'yı seçti?


Gördüğümüz gibi, Satoshi başlangıçta Bitcoin'de dijital imzalar için ECDSA'yı uygulamayı seçmiştir. Ancak Schnorr'un birçok açıdan ECDSA'dan daha üstün olduğunu da gördük ve bu protokol Claus-Peter Schnorr tarafından 1989 yılında, Bitcoin'nin icadından 20 yıl önce oluşturuldu.


Satoshi'nın neden bunu seçmediğini gerçekten bilmiyoruz, ancak olası bir hipotez, bu protokolün 2008 yılına kadar patent altında olmasıdır. Bitcoin bir yıl sonra, Ocak 2009'da oluşturulmuş olsa da, o sırada Schnorr imzaları için açık kaynaklı bir standardizasyon mevcut değildi. Belki de Satoshi, açık kaynaklı yazılımlarda zaten yaygın olarak kullanılan ve test edilen ve birkaç tanınmış uygulamaya sahip olan ECDSA'yı kullanmanın daha güvenli olduğunu düşündü (özellikle Bitcoin core'te 2015 yılına kadar kullanılan OpenSSL kütüphanesi, daha sonra 0.10.0 sürümünde libsecp256k1 ile değiştirildi). Ya da belki de bu patentin 2008 yılında sona ereceğinin farkında değildi. Her halükarda, en olası hipotez bu patent ve ECDSA'nın kanıtlanmış bir geçmişe sahip olması ve uygulanmasının daha kolay olmasıyla ilgili görünüyor.


## Sighash bayrakları


<chapterId>231c41a2-aff2-4655-9048-47b6d2d83d64</chapterId>


Önceki bölümlerde gördüğümüz gibi, dijital imzalar genellikle bir girdinin senaryosunun kilidini açmak için kullanılır. İmzalama sürecinde, örneklerimizde $m$ mesajı ile belirtilen imzalı verinin hesaplamaya dahil edilmesi gerekir. Bu veri bir kez imzalandıktan sonra imzayı geçersiz kılmadan değiştirilemez. Aslında, ister ECDSA ister Schnorr için olsun, imza doğrulayıcı hesaplamasına aynı $m$ mesajını dahil etmelidir. İmzalayan tarafından başlangıçta kullanılan $m$ mesajından farklıysa, sonuç yanlış olacak ve imza geçersiz sayılacaktır. Bu durumda bir imzanın belirli verileri kapsadığı ve bir şekilde yetkisiz değişikliklere karşı koruduğu söylenir.


### Sighash bayrağı nedir?


Bitcoin'nin özel durumunda, $m$ mesajının işleme karşılık geldiğini gördük. Ancak gerçekte durum biraz daha karmaşıktır. Aslında, sighash bayrakları sayesinde, işlem içinde imza tarafından kapsanacak veya kapsanmayacak belirli verileri seçmek mümkündür.

Bu nedenle "sighash flag" her girdiye eklenen bir parametredir ve bir işlemin ilgili imza tarafından kapsanan bileşenlerinin belirlenmesini sağlar. Bu bileşenler girdiler ve çıktılardır. Böylece sighash bayrağının seçimi, işlemin hangi girdilerinin ve hangi çıktılarının imza tarafından sabitlendiğini ve hangilerinin imzayı geçersiz kılmadan değiştirilebileceğini belirler. Bu mekanizma, imzaların işlem verilerini imzalayanın niyetine göre işlemesine olanak tanır.


Açıkçası, işlem Blockchain üzerinde onaylandıktan sonra, kullanılan sighash bayraklarından bağımsız olarak değişmez hale gelir. Sighash bayrakları aracılığıyla değişiklik yapma olasılığı imzalama ve onaylama arasındaki süreyle sınırlıdır.


Genel olarak, Wallet yazılımı bir işlem oluştururken girdilerinizin sighash bayrağını manuel olarak değiştirme seçeneği sunmaz. Varsayılan olarak `SIGHASH_ALL` ayarlıdır. Şahsen, bu değişikliğin Interface kullanıcısı tarafından yapılmasına izin veren sadece Sparrow wallet'u biliyorum.


### Bitcoin'deki mevcut sighash bayrakları nelerdir?


Bitcoin'te her şeyden önce 3 temel sighash bayrağı vardır:



- `SIGHASH_ALL` (`0x01`): İmza, işlemin tüm girdileri ve tüm çıktıları için geçerlidir. Böylece işlem tamamen imza kapsamına girer ve artık değiştirilemez. sIGHASH_ALL` günlük işlemlerde, bir işlemin değiştirilemeden yapılmak istendiği durumlarda en sık kullanılan sighash'tır.


![CYP201](assets/fr/026.webp)


Bu bölümdeki tüm diyagramlarda, turuncu renk imzanın kapsadığı Elements'ü temsil ederken, siyah renk kapsamayanları göstermektedir.



- sIGHASH_NONE` (`0x02`): İmza tüm girdileri kapsar ancak çıktıların hiçbirini kapsamaz, böylece imzadan sonra çıktıların değiştirilmesine izin verir. Somut olarak, bu boş bir çeke benzer. İmzalayan kişi girdilerdeki UTXO'ların kilidini açar ancak çıktılar alanını tamamen değiştirilebilir bırakır. Böylece bu işlemi bilen herkes istediği çıktıyı ekleyebilir, örneğin girdiler tarafından tüketilen fonları toplamak için bir alıcı Address belirleyebilir ve ardından bitcoinleri geri almak için işlemi yayınlayabilir. Girdilerin sahibinin imzası, yalnızca girdileri kapsadığı için geçersiz kılınmayacaktır.


![CYP201](assets/fr/027.webp)



- `SIGHASH_SINGLE` (`0x03`): İmza, tüm girdilerin yanı sıra imzalanan girdinin indeksine karşılık gelen tek bir çıktıyı da kapsar. Örneğin, imza #0 numaralı girdinin _scriptPubKey_ kilidini açıyorsa, #0 numaralı çıktıyı da kapsar. İmza, artık değiştirilemeyen diğer tüm girdileri de korur. Ancak, imzanın kapsadığı tek çıktı olan #0 çıktısının değiştirilmemesi koşuluyla, herhangi biri imzayı geçersiz kılmadan ek bir çıktı ekleyebilir.


![CYP201](assets/fr/028.webp)


Bu üç sighash bayrağına ek olarak, `SIGHASH_ANYONECANPAY` (`0x80`) değiştiricisi de vardır. Bu değiştirici, üç yeni sighash bayrağı oluşturmak için temel bir sighash bayrağı ile birleştirilebilir:



- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): İmza, işlemin tüm çıktılarını içerirken tek bir girdiyi kapsar. Bu birleşik sighash bayrağı, örneğin bir kitle fonlaması işleminin oluşturulmasına olanak tanır. Organizatör, Address ve hedef miktar ile çıktıyı hazırlar ve her yatırımcı daha sonra bu çıktıyı finanse etmek için girdiler ekleyebilir. Çıktıyı karşılamak için girdilerde yeterli fon toplandığında, işlem yayınlanabilir.


![CYP201](assets/fr/029.webp)



- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): İmza, herhangi bir çıktı taahhüt etmeden tek bir girdiyi kapsar;


![CYP201](assets/fr/030.webp)



- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): İmza, tek bir girdinin yanı sıra bu girdiyle aynı indekse sahip çıktıyı da kapsar. Örneğin, imza 3 numaralı girdinin _scriptPubKey_ kilidini açarsa, 3 numaralı çıktıyı da kapsar. İşlemin geri kalanı, hem diğer girdiler hem de diğer çıktılar açısından değiştirilebilir kalır.


![CYP201](assets/fr/031.webp)


### Yeni Sighash Bayrakları Ekleme Projeleri


Şu anda (2024), Bitcoin'de yalnızca önceki bölümde sunulan sighash bayrakları kullanılabilir durumdadır. Ancak, bazı projeler yeni sighash bayraklarının eklenmesini düşünmektedir. Örneğin, Christian Decker ve Anthony Towns tarafından önerilen BIP118, iki yeni sighash bayrağı getirmektedir: sIGHASH_ANYPREVOUT` ve `SIGHASH_ANYPREVOUTANYSCRIPT` (_AnyPrevOut = "Any Previous Output"_).


Bu iki sighash bayrağı Bitcoin'de ek bir olasılık sunacaktır: işlemin herhangi bir özel girdisini kapsamayan imzalar oluşturmak.


![CYP201](assets/fr/032.webp)


Bu fikir ilk olarak Joseph Poon ve Thaddeus Dryja tarafından Lightning White Paper'da formüle edilmiştir. Yeniden adlandırılmadan önce, bu sighash bayrağı `SIGHASH_NOINPUT` olarak adlandırılıyordu.

Bu sighash bayrağı Bitcoin'a entegre edilirse, sözleşmelerin kullanılmasını sağlayacaktır, ancak aynı zamanda bir UTXO'in Ownership'unun ortaklaşa nasıl yönetileceğini tanımlayan ikinci katmanlar için genel bir protokol olan Eltoo'nun uygulanması için zorunlu bir ön koşuldur. Eltoo, Yıldırım kanallarının durumunu, yani açılış ve kapanış arasında müzakere etme mekanizmalarıyla ilgili sorunları çözmek için özel olarak tasarlanmıştır.


Lightning Network hakkındaki bilgilerinizi derinleştirmek için CYP201 kursunun ardından Fanis Michalakis tarafından verilen ve konuyu ayrıntılı olarak ele alan LNP201 kursunu şiddetle tavsiye ederim:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Bir sonraki bölümde, Bitcoin Wallet'inizin temelindeki Mnemonic ifadesinin nasıl çalıştığını keşfetmeyi öneriyorum.


# Mnemonic cümlesi


<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>


## Bitcoin cüzdanlarının evrimi


<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>


Artık Hash işlevlerinin ve dijital imzaların işleyişini keşfettiğimize göre, Bitcoin cüzdanlarının nasıl çalıştığını inceleyebiliriz. Amaç, Bitcoin'de bir Wallet'un nasıl oluşturulduğunu, nasıl ayrıştırıldığını ve onu oluşturan farklı bilgi parçalarının ne için kullanıldığını açıklamak olacaktır. Wallet mekanizmalarının bu şekilde anlaşılması, güvenlik ve gizlilik açısından Bitcoin kullanımınızı geliştirmenize olanak sağlayacaktır.


Teknik ayrıntılara girmeden önce, "Bitcoin Wallet" ile ne kastedildiğini açıklığa kavuşturmak ve faydasını anlamak önemlidir.


### Bitcoin Wallet nedir?


Fiziksel banknotları ve madeni paraları saklamanıza olanak tanıyan geleneksel cüzdanların aksine, bir Bitcoin Wallet kendi başına bitcoin "içermez". Aslında, bitcoinler depolanabilecek fiziksel veya dijital bir formda mevcut değildir, ancak Bitcoin sisteminde **UTXOs** (_Unspent Transaction Outputs_) şeklinde gösterilen hesap birimleri ile temsil edilir.


Böylece UTXO'lar, _scriptPubKey_'lerinin karşılanması koşuluyla harcanabilecek çeşitli boyutlardaki bitcoin parçalarını temsil eder. Bir kullanıcı bitcoinlerini harcamak için UTXO ile ilişkili _scriptPubKey_'in kilidini açan bir _scriptSig_ sağlamalıdır. Bu kanıt genellikle _scriptPubKey_'de bulunan açık anahtara karşılık gelen özel anahtardan üretilen bir dijital imza aracılığıyla yapılır. Dolayısıyla, kullanıcının güvenliğini sağlaması gereken en önemli unsur özel anahtardır.

Bir Bitcoin Wallet'un rolü tam olarak bu özel anahtarları güvenli bir şekilde yönetmektir. Gerçekte, rolü geleneksel anlamda bir Wallet'dan ziyade bir anahtar zincirine daha çok benzemektedir.


### JBOK Cüzdanlar


Bitcoin'de kullanılan ilk cüzdanlar, bağımsız olarak ve aralarında herhangi bir bağlantı olmadan üretilen özel anahtarları bir araya getiren JBOK (_Just a Bunch Of Keys_) cüzdanlarıydı. Bu cüzdanlar, her bir özel anahtarın Address alan benzersiz bir Bitcoin'in kilidini açabildiği basit bir model üzerinde çalışıyordu.


![CYP201](assets/fr/033.webp)


Birden fazla özel anahtar kullanılmak istenirse, Wallet'i barındıran cihazda sorun olması durumunda fonlara erişimi sağlamak için çok sayıda yedekleme yapmak gerekiyordu. Tek bir özel anahtar kullanılıyorsa, tek bir yedekleme yeterli olduğundan bu Wallet yapısı yeterli olabilir. Ancak, bu bir sorun teşkil eder: Bitcoin'te, her zaman aynı özel anahtarın kullanılmaması şiddetle tavsiye edilir. Aslında, bir özel anahtar benzersiz bir Address ile ilişkilidir ve Bitcoin alıcı adresleri normalde tek seferlik kullanım için tasarlanmıştır. Her para aldığınızda, generate yeni bir boş Address kullanmalısınız.


Bu kısıtlama, Bitcoin'nin gizlilik modelinden kaynaklanmaktadır. Aynı Address'nın tekrar kullanılması, harici gözlemcilerin Bitcoin işlemlerini izlemesini kolaylaştırır. Bu nedenle, alıcı bir Address'nın yeniden kullanılması kesinlikle önerilmez. Bununla birlikte, birden fazla adrese sahip olmak ve işlemlerimizi kamuya açık bir şekilde ayırmak için birden fazla özel anahtarı yönetmek gerekir. JBOK cüzdanları söz konusu olduğunda, bu, yeni anahtar çiftleri kadar çok sayıda yedekleme oluşturmak anlamına gelir; bu, kullanıcılar için hızla karmaşık ve bakımı zor hale gelebilecek bir görevdir.


Bitcoin'un gizlilik modeli hakkında daha fazla bilgi edinmek ve gizliliğinizi koruma yöntemlerini keşfetmek için Plan ₿ Network hakkındaki BTC204 kursumu da takip etmenizi öneririm:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### HD Cüzdanlar


Address JBOK cüzdanlarının sınırlandırılması için daha sonra yeni bir Wallet yapısı kullanılmıştır. 2012 yılında Pieter Wuille, HD (Hiyerarşik Deterministik) cüzdanları tanıtan BIP32 ile bir iyileştirme önerdi. Bir HD Wallet'nin prensibi, tüm özel anahtarları deterministik ve hiyerarşik bir şekilde seed adı verilen tek bir bilgi kaynağından türetmektir. Bu seed, Wallet oluşturulduğunda rastgele oluşturulur ve Wallet'nin tüm özel anahtarlarının yeniden oluşturulmasına olanak tanıyan benzersiz bir yedek oluşturur. Böylece kullanıcı, Address'in yeniden kullanılmasını önlemek ve gizliliğini korumak için çok sayıda özel anahtarı generate yapabilirken, Wallet'sinin seed aracılığıyla yalnızca tek bir yedeğini alması gerekir.


![CYP201](assets/fr/034.webp)


HD cüzdanlarında anahtar türetme, farklı Wallet yazılımları arasında fon yönetimini ve birlikte çalışabilirliği kolaylaştırmak için anahtarların türetme alt uzaylarında düzenlenmesine olanak tanıyan ve her alt uzayın daha da alt bölümlere ayrılabildiği hiyerarşik bir yapıya göre gerçekleştirilir. Günümüzde bu standart Bitcoin kullanıcılarının büyük çoğunluğu tarafından benimsenmiştir. Bu nedenle ilerleyen bölümlerde detaylı olarak inceleyeceğiz.


### BIP39 Standardı: Mnemonic İfadesi


BIP32'ye ek olarak BIP39, yedeklemeyi ve kullanıcılar tarafından okunabilirliği kolaylaştırmak için seed formatını bir Mnemonic cümlesi olarak standartlaştırır. Kurtarma cümlesi veya 24 kelimelik cümle olarak da adlandırılan Mnemonic cümlesi, Wallet'in seed'unu güvenli bir şekilde kodlayan önceden tanımlanmış bir listeden alınan bir dizi kelimedir.


Mnemonic ifadesi kullanıcı için yedeklemeyi büyük ölçüde basitleştirir. Wallet'i barındıran cihazın kaybolması, hasar görmesi veya çalınması durumunda, sadece bu Mnemonic ifadesinin bilinmesi Wallet'in yeniden oluşturulmasına ve onun tarafından güvence altına alınan tüm fonlara erişimin geri kazanılmasına olanak tanır.


İlerleyen bölümlerde, anahtar türetme mekanizmaları ve farklı olası hiyerarşik yapılar da dahil olmak üzere HD cüzdanlarının iç işleyişini inceleyeceğiz. Bu, Bitcoin'deki fonların güvenliğinin dayandığı kriptografik temelleri daha iyi anlamanızı sağlayacaktır. Ve başlamak için, bir sonraki bölümde, Wallet'ünüzün temelindeki entropinin rolünü keşfetmemizi öneriyorum.


## Entropi ve Rastgele Sayılar


<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>

Modern HD cüzdanları, tüm generate anahtar setini deterministik olarak Wallet'e dönüştürmek için "entropi" adı verilen tek bir başlangıç bilgisine dayanır. Bu entropi, Wallet'in güvenliğini kısmen belirleyen sözde rastgele bir sayıdır.


### Entropinin Tanımı


Entropi, kriptografi ve bilgi bağlamında, bir veri kaynağı veya rastgele bir süreçle ilişkili belirsizliğin veya öngörülemezliğin nicel bir ölçüsüdür. Kriptografik sistemlerin güvenliğinde, özellikle de anahtarların ve rastgele sayıların üretilmesinde önemli bir rol oynar. Yüksek entropi, üretilen anahtarların yeterince öngörülemez olmasını ve bir saldırganın anahtarı tahmin etmek için tüm olası kombinasyonları denediği kaba kuvvet saldırılarına karşı dirençli olmasını sağlar.


Bitcoin bağlamında, entropi generate'yi seed yapmak için kullanılır. Bir HD Wallet oluşturulurken, Mnemonic ifadesinin inşası, kendisi de bir entropi kaynağından türetilen rastgele bir sayıdan yapılır. İfade daha sonra UTXO'larda harcama koşulları oluşturmak için deterministik ve hiyerarşik bir şekilde generate çoklu özel anahtarlar için kullanılır.


### Entropi Üretme Yöntemleri


Bir HD Wallet için kullanılan başlangıç entropisi genellikle 128 bit veya 256 bittir:



- 128 bit entropi, **12 kelimelik** bir Mnemonic ifadesine karşılık gelir;
- 256 bit entropi, **24 kelimelik** bir Mnemonic ifadesine karşılık gelir.


Çoğu durumda, bu rastgele sayı Wallet yazılımı tarafından bir PRNG (_Pseudo-Random Number Generator_) kullanılarak otomatik olarak üretilir. PRNG'ler, bir başlangıç durumundan rastgele bir sayıya yaklaşan özelliklere sahip, ancak gerçekte bir sayı olmayan generate sayı dizileri için kullanılan bir algoritma kategorisidir. İyi bir PRNG, çıktı tekdüzeliği, öngörülemezlik ve tahmin saldırılarına karşı direnç gibi özelliklere sahip olmalıdır. Gerçek rastgele sayı üreteçlerinin (TRNG'ler) aksine, PRNG'ler deterministik ve tekrarlanabilirdir.


![CYP201](assets/fr/035.webp)


Bir alternatif de entropiyi manuel olarak generate oluşturmaktır, bu daha iyi kontrol sağlar ancak aynı zamanda çok daha risklidir. HD Wallet'niz için entropiyi kendiniz oluşturmamanızı şiddetle tavsiye ederim.


Bir sonraki bölümde, rastgele bir sayıdan 12 veya 24 kelimelik bir Mnemonic ifadesine nasıl geçtiğimizi göreceğiz.


## Mnemonic İfadesi


<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>

"Mnemonic cümlesi", "seed cümlesi", "kurtarma cümlesi", "gizli cümle" veya "24 kelimelik cümle" olarak da adlandırılan seed cümlesi, genellikle 12 veya 24 kelimeden oluşan ve entropiden üretilen bir dizidir. Bir HD Wallet'ün tüm anahtarlarını deterministik olarak türetmek için kullanılır. Bu, bu ifadeden, generate'in tüm özel ve açık anahtarlarını deterministik olarak Bitcoin Wallet oluşturmak ve sonuç olarak onunla korunan fonlara erişmek mümkün olduğu anlamına gelir. Mnemonic ifadesinin amacı, bitcoinlerin hem güvenli hem de kullanımı kolay bir şekilde yedeklenmesi ve kurtarılması için bir araç sağlamaktır. BIP39 standardı ile 2013 yılında tanıtılmıştır.


Entropiden Mnemonic ifadesine nasıl geçileceğini birlikte keşfedelim.


### Checksum


Entropiyi bir Mnemonic ifadesine dönüştürmek için önce entropinin sonuna bir sağlama toplamı (veya "kontrol toplamı") eklenmelidir. Bu sağlama toplamı, yanlışlıkla herhangi bir değişiklik yapılmadığını doğrulayarak verinin bütünlüğünü sağlayan kısa bir bit dizisidir.


Sağlama toplamını hesaplamak için, SHA256 Hash işlevi entropiye uygulanır (sadece bir kez; bu, Bitcoin'de çift Hash yerine tek bir SHA256 Hash'in kullanıldığı nadir durumlardan biridir). Bu işlem 256 bitlik bir Hash üretir. Sağlama toplamı bu Hash'in ilk bitlerinden oluşur ve uzunluğu aşağıdaki formüle göre entropinin uzunluğuna bağlıdır:


$$
\text{CS} = \frac{\text{ENT}}{32}
$$


burada $\text{ENT}$ bit cinsinden entropi uzunluğunu ve $\text{CS}$ bit cinsinden sağlama toplamı uzunluğunu temsil eder.


Örneğin, 256 bitlik bir entropi için, Hash'un ilk 8 biti sağlama toplamını oluşturmak üzere alınır:


$$
\text{CS} = \frac{256}{32} = 8 \text{ bits}
$$


Sağlama toplamı hesaplandıktan sonra, $\text{ENT} olarak belirtilen genişletilmiş bir bit dizisi elde etmek için entropi ile birleştirilir \Vert \text{CS}$ ("concatenate" uç uca eklemek anlamına gelir).


![CYP201](assets/fr/036.webp)


### Entropi ve Mnemonic İfadesi Arasındaki Uyum


Mnemonic cümlesindeki kelime sayısı, aşağıdaki tabloda gösterildiği gibi başlangıç entropisinin boyutuna bağlıdır:



- $\text{ENT}$: entropinin bit cinsinden boyutu;
- $\text{CS}$: sağlama toplamının bit cinsinden boyutu;
- $w$: son Mnemonic cümlesindeki kelime sayısı.


$$
\begin{array}{|c|c|c|c|}
\hline
\text{ENT} & \text{CS} & \text{ENT} \Vert \text{CS} & w \\
\hline
128 & 4 & 132 & 12 \\
160 & 5 & 165 & 15 \\
192 & 6 & 198 & 18 \\
224 & 7 & 231 & 21 \\
256 & 8 & 264 & 24 \\
\hline
\end{array}
$$


Örneğin, 256 bit entropi için sonuç $\text{ENT} \Vert \text{CS}$ 264 bittir ve 24 kelimelik bir Mnemonic cümlesi verir.


### İkili Dizinin Mnemonic İfadesine Dönüştürülmesi


Bit dizisi $\text{ENT} \Vert \text{CS}$ daha sonra 11 bitlik segmentlere bölünür. Her 11 bitlik segment, ondalık sayıya dönüştürüldükten sonra, bir kelimenin [BIP39 tarafından standartlaştırılan 2048 kelimelik bir listede] konumunu belirleyen 0 ile 2047 arasında bir sayıya karşılık gelir (https://github.com/Planb-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf).


![CYP201](assets/fr/037.webp)


Örneğin, 128 bitlik bir entropi için sağlama toplamı 4 bittir ve dolayısıyla toplam dizi 132 bittir. Bu dizi 11 bitlik 12 bölüme ayrılmıştır (turuncu bitler sağlama toplamını belirtir):


![CYP201](assets/fr/038.webp)


Her segment daha sonra listedeki bir kelimeyi temsil eden bir ondalık sayıya dönüştürülür. Örneğin, `01011010001` ikili segmenti ondalık olarak `721`e eşdeğerdir. Listenin indekslemesine (0'dan değil 1'den başlar) uyum sağlamak için 1 ekleyerek, bu, listedeki "_focus_" olan `722` kelime sırasını verir.


![CYP201](assets/fr/039.webp)


Bu yazışma 12 kelimelik bir cümle elde etmek için 12 segmentin her biri için tekrarlanır.


![CYP201](assets/fr/040.webp)


### BIP39 Kelime Listesinin Özellikleri


BIP39 kelime listesinin bir özelliği de hiçbir kelimenin ilk dört harfinin başka bir kelimeyle aynı sırayı paylaşmamasıdır. Bu, Mnemonic ifadesini kaydetmek için her kelimenin sadece ilk dört harfini yazmanın yeterli olduğu anlamına gelir. Bu, özellikle metal bir destek üzerine kazımak isteyenler için yerden tasarruf etmek açısından ilginç olabilir.


2048 kelimeden oluşan bu liste çeşitli dillerde mevcuttur. Bunlar basit çeviriler değil, her dil için farklı kelimelerdir. Ancak, diğer dillerdeki versiyonlar genellikle Wallet yazılımı tarafından desteklenmediğinden, İngilizce versiyona bağlı kalmanız şiddetle tavsiye edilir.


### Mnemonic İfadeniz İçin Hangi Uzunluğu Seçmelisiniz?


Mnemonic ifadenizin en uygun uzunluğunu belirlemek için, sağladığı gerçek güvenlik göz önünde bulundurulmalıdır. 12 kelimelik bir ifade 128 bit güvenlik sağlarken, 24 kelimelik bir ifade 256 bit sunar.


Ancak, ifade düzeyinde güvenlikteki bu fark Bitcoin Wallet'in genel güvenliğini artırmaz, çünkü bu ifadeden türetilen özel anahtarlar yalnızca 128 bit güvenlikten faydalanır. Aslında, daha önce gördüğümüz gibi, Bitcoin özel anahtarları $1$ ile $n-1$ arasında değişen rastgele sayılardan üretilir (veya rastgele bir kaynaktan türetilir), burada $n$ secp256k1 eğrisinin $G$ üreteç noktasının mertebesini temsil eder, bu sayı $2^{256}$'dan biraz daha azdır. Dolayısıyla bu özel anahtarların 256 bit güvenlik sunduğu düşünülebilir. Bununla birlikte, güvenlikleri, eliptik eğriler üzerinde ayrık logaritma (_ECDLP_) matematik problemi tarafından belirlenen bir zorluk olan, ilişkili açık anahtardan özel bir anahtar bulmanın zorluğunda yatmaktadır. Bugüne kadar, bu sorunu çözmek için en iyi bilinen algoritma, bir anahtarı kırmak için gereken işlem sayısını boyutunun kareköküne indiren Pollard'ın rho algoritmasıdır.


Bitcoin'de kullanılanlar gibi 256 bitlik anahtarlar için Pollard'ın rho algoritması karmaşıklığı $2^{128}$ işlemine indirir:


$$

O(\sqrt{2^{256}}) = O(2^{128})


$$


Bu nedenle, Bitcoin'te kullanılan bir özel anahtarın 128 bit güvenlik sunduğu düşünülmektedir.


Sonuç olarak, 24 kelimelik bir ifade seçmek Wallet için ek koruma sağlamaz, çünkü türetilen anahtarlar yalnızca 128 bit güvenlik sunuyorsa ifadede 256 bit güvenlik anlamsızdır. Bu prensibi açıklamak için, iki kapılı bir eve sahip olmak gibi: eski bir ahşap kapı ve güçlendirilmiş bir kapı. Bir hırsızlık durumunda, güçlendirilmiş kapı hiçbir işe yaramayacaktır, çünkü davetsiz misafir ahşap kapıdan geçecektir. Burada da benzer bir durum söz konusudur.


Bu nedenle, 128 bit güvenlik sunan 12 kelimelik bir ifade, bitcoinlerinizi herhangi bir hırsızlık girişimine karşı korumak için şu anda yeterlidir. Dijital imza algoritması daha büyük anahtarlar kullanacak ya da ECDLP dışında bir matematiksel probleme dayanacak şekilde değişmediği sürece, 24 kelimelik bir ifade gereksiz olmaya devam edecektir. Dahası, daha uzun bir ifade yedekleme sırasında kayıp riskini artırır: iki kat daha kısa bir yedeklemenin yönetimi her zaman daha kolaydır.


Daha ileri gitmek ve bir test Mnemonic ifadesini manuel olarak nasıl generate yapacağınızı somut olarak öğrenmek için bu öğreticiyi keşfetmenizi tavsiye ederim:


https://planb.network/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

Bu Mnemonic ifadesinden Wallet'un türetilmesine devam etmeden önce, bir sonraki bölümde, türetme sürecinde rol oynadığı ve Mnemonic ifadesiyle aynı seviyede olduğu için size BIP39 passphrase'yi tanıtacağım.


## passphrase


<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>


Daha önce gördüğümüz gibi, HD cüzdanları tipik olarak 12 veya 24 kelimeden oluşan bir Mnemonic cümlesinden üretilir. Bu ifade çok önemlidir çünkü fiziksel cihazının (örneğin bir Hardware Wallet gibi) kaybolması durumunda bir Wallet'ün tüm anahtarlarının geri yüklenmesini sağlar. Bununla birlikte, tek bir hata noktası oluşturur, çünkü ele geçirilirse, bir saldırgan tüm bitcoinleri çalabilir. İşte bu noktada BIP39 passphrase devreye girmektedir.


### BIP39 passphrase nedir?


passphrase, Wallet'in güvenliğini artırmak için anahtar türetme sürecinde Mnemonic ifadesine eklenen, özgürce seçebileceğiniz isteğe bağlı bir paroladır.


Dikkatli olun, passphrase, Hardware Wallet'unuzun PIN kodu veya bilgisayarınızda Wallet'nize erişim kilidini açmak için kullanılan parola ile karıştırılmamalıdır. Tüm bu Elements'lerin aksine, passphrase, Wallet'nizin anahtarlarının türetilmesinde rol oynar. **Bu, onsuz bitcoinlerinizi asla kurtaramayacağınız anlamına gelir.**


passphrase, anahtarların üretildiği seed'yi değiştirerek Mnemonic ifadesiyle birlikte çalışır. Böylece, birisi 12 veya 24 kelimelik ifadenizi ele geçirse bile, passphrase olmadan fonlarınıza erişemez. Bir passphrase kullanmak esasen farklı anahtarlara sahip yeni bir Wallet oluşturur. passphrase'ün (birazcık bile) değiştirilmesi generate'i farklı bir Wallet haline getirecektir.


![CYP201](assets/fr/041.webp)


### Neden bir passphrase kullanmalısınız?


passphrase isteğe bağlıdır ve kullanıcı tarafından seçilen herhangi bir karakter kombinasyonu olabilir. Bir passphrase kullanmak bu nedenle çeşitli avantajlar sunar. Her şeyden önce, fonlara erişmek için ikinci bir faktör gerektirerek (hırsızlık, evinize erişim vb.) Mnemonic ifadesinin tehlikeye atılmasıyla ilişkili tüm riskleri azaltır.


Daha sonra, meşhur "_$5 ingiliz anahtarı saldırısı_" gibi fonlarınızı çalmak için fiziksel kısıtlamalarla karşılaşmak üzere bir yem Wallet oluşturmak için stratejik olarak kullanılabilir. Bu senaryoda fikir, gizli bir Wallet'e sahipken, potansiyel bir saldırganı tatmin edecek kadar az miktarda bitcoin içeren bir passphrase olmadan bir Wallet'e sahip olmaktır. Bu sonuncusu aynı Mnemonic ifadesini kullanır ancak ek bir passphrase ile güvence altına alınmıştır.

Son olarak, HD Wallet'in seed üretiminin rastgeleliğini kontrol etmek istendiğinde bir passphrase kullanımı ilginçtir.


### İyi bir passphrase nasıl seçilir?


passphrase'in etkili olabilmesi için yeterince uzun ve rastgele olması gerekir. Güçlü bir parolada olduğu gibi, herhangi bir kaba kuvvet saldırısını imkansız kılmak için mümkün olduğunca uzun ve rastgele, çeşitli harfler, sayılar ve semboller içeren bir passphrase seçmenizi öneririm.


Bu passphrase'u, Mnemonic ifadesiyle aynı şekilde düzgün bir şekilde kaydetmek de önemlidir. **Bunu kaybetmek, bitcoinlerinize erişimi kaybetmek anlamına gelir**. Kaybetme riskini makul olmayan bir şekilde artırdığı için bunu sadece ezbere hatırlamamanızı şiddetle tavsiye ederim. İdeal olanı, Mnemonic cümlesinden ayrı bir fiziksel ortama (kağıt veya metal) yazmaktır. Her ikisinin de aynı anda ele geçirilmesini önlemek için bu yedekleme kesinlikle Mnemonic ifadenizin saklandığı yerden farklı bir yerde saklanmalıdır.


![CYP201](assets/fr/042.webp)


Aşağıdaki bölümde, Wallet'ünüzün temelindeki bu iki Elements'nin - Mnemonic ifadesi ve passphrase - UTXO'larınızı kilitleyen _scriptPubKey_ içinde kullanılan anahtar çiftlerini türetmek için nasıl kullanıldığını keşfedeceğiz.


# Bitcoin Cüzdanlarının Oluşturulması


<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>


## seed ve Ana Anahtarın Oluşturulması


<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>


Mnemonic cümlesi ve isteğe bağlı passphrase oluşturulduktan sonra, Bitcoin HD Wallet türetme süreci başlayabilir. Mnemonic cümlesi ilk olarak Wallet'nin tüm anahtarlarının temelini oluşturan bir seed'e dönüştürülür.


![CYP201](assets/fr/043.webp)


### HD Wallet'nin seed'ü


BIP39 standardı seed'yi bir HD Wallet'nın tüm anahtarlarının türetilmesi için başlangıç noktası olarak hizmet eden 512 bitlik bir dizi olarak tanımlar. seed, daha önce bölüm 3.3'te tartıştığımız **PBKDF2** algoritması (_Şifre Tabanlı Anahtar Türetme Fonksiyonu 2_) kullanılarak Mnemonic cümlesinden ve olası passphrase'ten türetilir. Bu türetme fonksiyonunda aşağıdaki parametreleri kullanacağız:



- m$ : Mnemonic ifadesi;
- p$ : seed'un güvenliğini artırmak için kullanıcı tarafından seçilen isteğe bağlı bir passphrase. Eğer passphrase yoksa bu alan boş bırakılır;
- $\text{PBKDF2}$ : $\text{HMAC-SHA512}$ ve $2048$ yinelemeli türetme işlevi;
- $s$: 512-bit Wallet seed.

Seçilen Mnemonic cümle uzunluğu ne olursa olsun (132 bit veya 264 bit), PBKDF2 işlevi her zaman 512 bitlik bir çıktı üretecektir ve bu nedenle seed her zaman bu boyutta olacaktır.


### PBKDF2 ile seed Türetme Şeması


Aşağıdaki denklem seed'in Mnemonic ifadesinden ve passphrase'dan türetilmesini göstermektedir:


$$
s = \text{PBKDF2}_{\text{HMAC-SHA512}}(m, p, 2048)
$$


![CYP201](assets/fr/044.webp)


seed'in değeri böylece Mnemonic ifadesinin ve passphrase'un değerinden etkilenir. passphrase değiştirildiğinde farklı bir seed elde edilir. Ancak, aynı Mnemonic ifadesi ve passphrase ile, PBKDF2 deterministik bir fonksiyon olduğu için her zaman aynı seed üretilir. Bu, aynı anahtar çiftlerinin yedeklerimiz aracılığıyla geri alınabilmesini sağlar.


**Not:** Yaygın dilde, "seed" terimi genellikle dilin yanlış kullanımı nedeniyle Mnemonic ifadesine atıfta bulunur. Gerçekten de, passphrase'nin yokluğunda, biri basitçe diğerinin kodlanmasıdır. Ancak, gördüğümüz gibi, cüzdanların teknik gerçekliğinde, seed ve Mnemonic ifadeleri gerçekten de iki ayrı Elements'tür.


Artık seed'imizi elde ettiğimize göre, Bitcoin Wallet'mizin türetilmesine devam edebiliriz.


### Ana Anahtar ve Ana chain code


seed elde edildikten sonra, HD Wallet'in türetilmesindeki bir sonraki adım, ana özel anahtarın ve Wallet'imizin 0 derinliğini temsil edecek olan ana chain code'nin hesaplanmasını içerir.


Ana özel anahtarı ve ana chain code'ü elde etmek için HMAC-SHA512 işlevi, tüm Bitcoin kullanıcıları için aynı olan sabit bir anahtar "_Bitcoin Seed_" kullanılarak seed'ya uygulanır. Bu sabit, anahtar türetmelerinin Bitcoin'e özgü olmasını sağlamak için seçilmiştir. İşte Elements:



- $\text{HMAC-SHA512}$: türetme işlevi;
- $s$: 512-bit Wallet seed;
- $\text{"Bitcoin seed"}$: tüm Bitcoin cüzdanları için ortak türetme sabiti.


$$

\text{output} = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)


$$


Dolayısıyla bu fonksiyonun çıktısı 512 bittir. Daha sonra 2 parçaya bölünür:



- Geriye kalan 256 bit **ana özel anahtarı** oluşturur;
- Sağ 256 bit **master chain code**'i oluşturur.


Matematiksel olarak bu iki değer, $k_M$ ana özel anahtar ve $C_M$ ana chain code olmak üzere aşağıdaki gibi yazılabilir:


$$
k_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[:256]}
$$


$$
C_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[256:]}
$$


![CYP201](assets/fr/045.webp)


### Ana Anahtar ve chain code'ün Rolü


Ana özel anahtar, tüm türetilmiş özel anahtarların (çocuklar, torunlar, torun çocukları, vb.) üretileceği ana anahtar olarak kabul edilir. Türetme hiyerarşisinde sıfır seviyesini temsil eder.


Öte yandan ana chain code, bazı potansiyel saldırılara karşı koymak amacıyla çocuklar için anahtar türetme sürecine ek bir entropi kaynağı ekler. Ayrıca, HD Wallet'te her anahtar çiftinin kendisiyle ilişkilendirilmiş benzersiz bir chain code'ü vardır ve bu da bu çiftten çocuk anahtarları türetmek için kullanılır, ancak bunu ilerleyen bölümlerde daha ayrıntılı olarak tartışacağız.


Aşağıdaki Elements ile HD Wallet'in türetilmesine devam etmeden önce, bir sonraki bölümde size genellikle ana anahtarla karıştırılan genişletilmiş anahtarları tanıtmak istiyorum. Nasıl yapıldıklarını ve Bitcoin Wallet'de nasıl bir rol oynadıklarını göreceğiz.


## Genişletilmiş Anahtarlar

<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>


Genişletilmiş bir anahtar basitçe bir anahtarın (özel veya genel) ve ilişkili chain code'un birleştirilmesidir. Bu chain code alt anahtarların türetilmesi için gereklidir, çünkü bu olmadan bir üst anahtardan alt anahtarları türetmek mümkün değildir, ancak bu süreci bir sonraki bölümde daha ayrıntılı olarak keşfedeceğiz. Dolayısıyla bu genişletilmiş anahtarlar, alt anahtarları türetmek için gerekli tüm bilgilerin bir araya getirilmesini sağlar ve böylece bir HD Wallet içinde hesap yönetimini basitleştirir.


![CYP201](assets/fr/046.webp)


Genişletilmiş anahtar iki bölümden oluşur:


- Özel veya genel anahtarın yanı sıra ilişkili chain code'i de içeren yük;
- Yazılımlar arasında birlikte çalışabilirliği kolaylaştırmak ve kullanıcının anlamasını geliştirmek için çeşitli bilgi parçaları olan meta veriler.


### Genişletilmiş Anahtarlar Nasıl Çalışır?

Genişletilmiş anahtar bir özel anahtar içerdiğinde, genişletilmiş özel anahtar olarak adlandırılır. Bu anahtar `prv` tanımlayıcısını içeren önekiyle tanınır. Özel anahtara ek olarak, genişletilmiş özel anahtar ayrıca ilişkili chain code'yi de içerir. Bu tür genişletilmiş anahtar ile her tür alt özel anahtar türetmek mümkündür. Bu nedenle, eliptik eğriler üzerindeki noktaların eklenmesi ve iki katına çıkarılmasıyla, alt açık anahtarların türetilmesine de izin verir.


Genişletilmiş anahtar bir özel anahtar değil de bir açık anahtar içeriyorsa, bu anahtar genişletilmiş açık anahtar olarak adlandırılır. Bu anahtar `pub` tanımlayıcısını içeren önekiyle tanınır. Açıkçası, anahtara ek olarak, ilişkili chain code'ü de içerir. Genişletilmiş özel anahtardan farklı olarak, genişletilmiş açık anahtar yalnızca "normal" alt açık anahtarların türetilmesine izin verir (yani "sertleştirilmiş" alt anahtarları türetemez). Bu "normal" ve "sertleştirilmiş" niteleyicilerinin ne anlama geldiğini bir sonraki bölümde göreceğiz.


Her durumda, genişletilmiş açık anahtar alt özel anahtarların türetilmesine izin vermez. Bu nedenle, bir kişinin bir `xpub`a erişimi olsa bile, ilgili özel anahtarlara erişimi olmayacağı için ilgili fonları harcayamayacaktır. Yalnızca ilişkili işlemleri gözlemlemek için alt genel anahtarları türetebilirler.


Aşağıda, aşağıdaki gösterimi benimseyeceğiz:


- $K_{\text{PAR}}$: bir üst açık anahtar;
- k_{\text{PAR}}$: bir üst özel anahtar;
- c_{\text{PAR}}$: bir ebeveyn chain code;
- $C_{\text{CHD}}$: bir çocuk chain code;
- $K_{\text{CHD}}^n$: normal bir alt açık anahtar;
- $k_{\text{CHD}}^n$: normal bir alt özel anahtar;
- $K_{\text{CHD}}^h$: sertleştirilmiş bir alt açık anahtar;
- $k_{\text{CHD}}^h$: sertleştirilmiş bir alt özel anahtar.


![CYP201](assets/fr/047.webp)


### Genişletilmiş Anahtarın Oluşturulması


Genişletilmiş bir anahtar aşağıdaki gibi yapılandırılmıştır:


- **Sürüm**: Anahtarın niteliğini tanımlamak için sürüm kodu (`xprv`, `xpub`, `yprv`, `ypub`...). Bu bölümün sonunda `x`, `y` ve `z` harflerinin neye karşılık geldiğini göreceğiz.
- **Derinlik**: HD Wallet'da ana anahtara göre hiyerarşik seviye (ana anahtar için 0).
- **Üst Parmak İzi**: Yükte bulunan anahtarı türetmek için kullanılan ana açık anahtarın HASH160 Hash'sinin ilk 4 baytı.
- **Dizin Numarası**: Kardeş anahtarlar arasında, yani aynı üst anahtarlara sahip aynı türetme düzeyindeki tüm anahtarlar arasında çocuğun tanımlayıcısı.
- **chain code**: Alt anahtarları türetmek için benzersiz bir 32 baytlık kod.
- **Anahtar**: Özel anahtar (boyut için önüne 1 bayt eklenir) veya genel anahtar.
- **Sağlama toplamı**: HASH256 işlevi (çift SHA256) ile hesaplanan bir sağlama toplamı da eklenir, bu da genişletilmiş anahtarın iletimi veya depolanması sırasında bütünlüğünün doğrulanmasına olanak tanır.


Bu nedenle, genişletilmiş bir anahtarın tam biçimi sağlama toplamı olmadan 78 bayt ve sağlama toplamıyla birlikte 82 bayttır. Daha sonra kullanıcılar tarafından kolayca okunabilecek bir gösterim üretmek için Base58'e dönüştürülür. Base58 formatı *Legacy* alıcı adresleri için kullanılan formatla aynıdır (*SegWit* öncesi).


| Element           | Description                                                                                                        | Size      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ | --------- |
| Version           | Indicates whether the key is public (`xpub`, `ypub`) or private (`xprv`, `zprv`), as well as the version of the extended key | 4 bytes   |
| Depth             | Level in the hierarchy relative to the master key                                                                  | 1 byte    |
| Parent Fingerprint| The first 4 bytes of HASH160 of the parent public key                                                              | 4 bytes   |
| Index Number      | Position of the key in the order of children                                                                       | 4 bytes   |
| Chain Code        | Used to derive child keys                                                                                          | 32 bytes  |
| Key               | The private key (with a 1-byte prefix) or the public key                                                          | 33 bytes  |
| Checksum          | Checksum to verify integrity                                                                                       | 4 bytes   |

Özel anahtara yalnızca bir bayt eklenirse, bunun nedeni sıkıştırılmış açık anahtarın özel anahtardan bir bayt daha uzun olmasıdır. Özel anahtarın başına `0x00` olarak eklenen bu ek bayt, boyutlarını eşitler ve ister açık ister özel anahtar olsun, genişletilmiş anahtarın yükünün aynı uzunlukta olmasını sağlar.


### Genişletilmiş Anahtar Önekleri

Az önce gördüğümüz gibi, genişletilmiş anahtarlar hem genişletilmiş anahtarın sürümünü hem de doğasını belirten bir önek içerir. Pub` notasyonu genişletilmiş bir açık anahtara atıfta bulunduğunu gösterir ve `prv` notasyonu genişletilmiş bir özel anahtarı belirtir. Genişletilmiş anahtarın tabanındaki ek harf, takip edilen standardın Legacy, SegWit v0, SegWit v1 vb. olup olmadığını belirtmeye yardımcı olur.

Burada kullanılan öneklerin ve anlamlarının bir özeti bulunmaktadır:


| Base 58 Prefix  | Base 16 Prefix  | Network | Purpose             | Associated Scripts  | Derivation            | Key Type     |
| --------------- | --------------- | ------- | ------------------- | ------------------- | --------------------- | ------------ |
| `xpub`          | `0488b21e`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | public       |
| `xprv`          | `0488ade4`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | private      |
| `tpub`          | `043587cf`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | public       |
| `tprv`          | `04358394`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | private      |
| `ypub`          | `049d7cb2`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | public       |
| `yprv`          | `049d7878`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | private      |
| `upub`          | `049d7cb2`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | public       |
| `uprv`          | `044a4e28`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | private      |
| `zpub`          | `04b24746`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | public       |
| `zprv`          | `04b2430c`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | private      |
| `vpub`          | `045f1cf6`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | public       |
| `vprv`          | `045f18bc`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | private      |


### Genişletilmiş Anahtarın Elements Detayları


Genişletilmiş bir anahtarın iç yapısını daha iyi anlamak için, örnek olarak bir tane alalım ve parçalara ayıralım. İşte genişletilmiş bir anahtar:



- **Base58**'de:


```text
xpub6CTNzMUkzpurBWaT4HQoYzLP4uBbGJuWY358Rj7rauiw4rMHCyq3Rfy9w4kyJXJzeFfyrKLUar2rUCukSiDQFa7roTwzjiAhyQAdPLEjqHT
```



- Onaltılık olarak**:**


```text
0488B21E036D5601AD80000000C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A89303772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF50658051F067C3A
```


Bu genişletilmiş anahtar birkaç farklı Elements'ye ayrılır:


1.**Sürüm**: `0488B21E`


İlk 4 bayt sürümdür. Burada, Mainnet üzerinde *Legacy* veya *SegWit v1* türetme amacına sahip genişletilmiş bir açık anahtara karşılık gelir.


2.**Derinlik**: `03`


Bu alan anahtarın HD Wallet içindeki hiyerarşik seviyesini gösterir. Bu durumda, `03` derinliği bu anahtarın ana anahtarın üç seviye altında olduğu anlamına gelir.


3.**Ebeveyn parmak izi**: `6D5601AD`


Bunlar, bu `xpub`ı türetmek için kullanılan ana açık anahtarın HASH160 Hash'sının ilk 4 baytıdır.


4.**İndeks numarası**: `80000000`


Bu indeks, anahtarın ebeveyninin çocukları arasındaki konumunu gösterir. 0x80` ön eki, anahtarın sertleştirilmiş bir şekilde türetildiğini gösterir ve geri kalanı sıfırlarla doldurulduğundan, bu anahtarın olası kardeşleri arasında ilk olduğunu gösterir.


5.**chain code**: `C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A893`


6.**Genel Anahtar**: `03772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF5065805`


7.**Checksum**: 1F067C3A`


Sağlama toplamı, diğer her şeyin Hash'inin (çift SHA256) ilk 4 baytına karşılık gelir.


Bu bölümde, iki farklı alt anahtar türü olduğunu keşfettik. Ayrıca bu alt anahtarların türetilmesi için bir anahtara (özel ya da genel) ve onun chain code'una ihtiyaç duyulduğunu öğrendik. Bir sonraki bölümde, bu farklı anahtar türlerinin doğasını ve bunların ana anahtarlarından ve chain code'dan nasıl türetileceğini ayrıntılı olarak inceleyeceğiz.



## Çocuk Anahtar Çiftlerinin Türetilmesi

<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>


Bitcoin HD cüzdanlarında alt anahtar çiftlerinin türetilmesi, bu çiftleri dallar aracılığıyla farklı gruplar halinde düzenlerken çok sayıda anahtar üretilmesine olanak tanıyan hiyerarşik bir yapıya dayanır. Bir üst çiftten türetilen her bir alt çift, bitcoinleri kilitlemek için doğrudan bir *scriptPubKey* içinde kullanılabilir ya da bir anahtar ağacı oluşturmak için generate daha fazla alt anahtar için bir başlangıç noktası olarak kullanılabilir.


Tüm bu türetmeler, derinlik seviyesi 0'daki ilk ebeveynler olan ana anahtar ve ana chain code ile başlar. Bunlar bir bakıma Wallet anahtarlarınızın Adem ve Havva'sı, türetilmiş tüm anahtarların ortak atalarıdır.


![CYP201](assets/fr/048.webp)


Bu deterministik türetmenin nasıl çalıştığını inceleyelim.


### Çocuk Anahtarı Türevlerinin Farklı Türleri


Bir önceki bölümde kısaca değindiğimiz gibi, alt anahtarlar iki ana türe ayrılır.


- **Normal alt anahtarlar** ($k_{\text{CHD}}^n, K_{\text{CHD}}^n$): Bunlar genişletilmiş genel anahtardan ($K_{\text{PAR}}$) veya genişletilmiş özel anahtardan ($k_{\text{PAR}}$), önce genel anahtarın türetilmesiyle elde edilir.
- **Sertleştirilmiş alt anahtarlar** ($k_{\text{CHD}}^h, K_{\text{CHD}}^h$): Bunlar yalnızca genişletilmiş özel anahtardan ($k_{\text{PAR}}$) türetilebilir ve bu nedenle yalnızca genişletilmiş açık anahtara sahip olan gözlemciler tarafından görünmez.


Her alt anahtar çifti 32 bitlik bir **indeks** ile tanımlanır (hesaplamalarımızda $i$ olarak adlandırılır). Normal anahtarlar için indeksler $0$ ile $2^{31}-1$ arasında değişirken, sertleştirilmiş anahtarlar için olanlar $2^{31}$ ile $2^{32}-1$ arasında değişir. Bu sayılar türetme sırasında kardeş anahtar çiftlerini ayırt etmek için kullanılır. Aslında, her ebeveyn anahtar çifti birden fazla alt anahtar çifti türetebilmelidir. Aynı hesaplamayı ana anahtarlardan sistematik olarak uygulayacak olsaydık, elde edilen tüm kardeş anahtarlar aynı olurdu ki bu da arzu edilen bir durum değildir. Bu nedenle dizin, türetme hesaplamasını değiştirerek her bir kardeş çiftin farklılaştırılmasına olanak tanıyan bir değişken sunar. Belirli protokollerde ve türetme standartlarında özel kullanım dışında, genellikle ilk alt anahtarı `0` indeksiyle, ikincisini `1` indeksiyle türeterek başlarız ve bu böyle devam eder.


### HMAC-SHA512 ile Türetme Süreci


Her bir alt anahtarın türetilmesi, Bölüm 2'de Hash işlevleri hakkında tartıştığımız HMAC-SHA512 işlevine dayanmaktadır. İki girdi alır: üst chain code $C_{\text{PAR}}$ ve üst anahtarın (istenen alt anahtarın türüne bağlı olarak $K_{\text{PAR}}$ açık anahtarı ya da $k_{\text{PAR}}$ özel anahtarı) dizinle birleştirilmesi. HMAC-SHA512'nin çıktısı 512 bitlik bir dizidir ve iki bölüme ayrılmıştır:


- İlk 32 bayt (veya $h_1$) yeni alt çifti hesaplamak için kullanılır.
- Son 32 bayt (veya $h_2$) alt çift için yeni chain code $C_{\text{CHD}}$ olarak işlev görür.


Tüm hesaplamalarımızda, HMAC-SHA512 fonksiyonunun çıktısını $\text{Hash}$ olarak göstereceğim.


![CYP201](assets/fr/049.webp)


#### Üst Özel Anahtardan Alt Özel Anahtarın Türetilmesi


Üst özel anahtar $k_{\text{CHD}}$'den alt özel anahtar $k_{\text{PAR}}$ türetmek için, sertleştirilmiş veya normal anahtar istenmesine bağlı olarak iki senaryo mümkündür.


Bir **normal alt anahtar** ($i < 2^{31}$) için $\text{Hash}$ hesaplaması aşağıdaki gibidir:


$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}},  k_{\text{PAR}} \cdot G \Vert i)
$$


Bu hesaplamada, HMAC işlevimizin iki girdi aldığını gözlemliyoruz: önce ana chain code ve ardından dizinin ana özel anahtarla ilişkili açık anahtarla birleştirilmesi. Burada ana açık anahtar kullanılmaktadır çünkü biz sertleştirilmiş değil normal bir alt anahtar türetmek istiyoruz.

Şimdi elimizde 64 baytlık bir $\text{Hash}$ var ve bunu her biri 32 baytlık 2 parçaya böleceğiz, $h_1$ ve $h_2$:



$$

\text{hash} = h_1 \Vert h_2

$$



$$
h_1 = \text{hash}_{[:32]} \quad, \quad h_2 = \text{hash}_{[32:]}
$$


Alt özel anahtar $k_{\text{CHD}}^n$ daha sonra aşağıdaki gibi hesaplanır:


$$
k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n
$$


Bu hesaplamada, $\text{parse256}(h_1)$ işlemi $\text{Hash}$'in ilk 32 baytının 256 bitlik bir tamsayı olarak yorumlanmasından oluşur. Bu sayı daha sonra ana özel anahtara eklenir, hepsi de dijital imzalarla ilgili 3. bölümde gördüğümüz gibi eliptik eğrinin sırası içinde kalmak için modulo $n$ olarak alınır. Bu nedenle, normal bir alt özel anahtar türetmek için, HMAC-SHA512 işlevinin girdilerinde hesaplama temeli olarak ana açık anahtar kullanılsa da, hesaplamayı sonuçlandırmak için her zaman ana özel anahtara sahip olmak gerekir.


Bu alt özel anahtardan, ECDSA veya Schnorr uygulayarak ilgili açık anahtarı türetmek mümkündür. Bu şekilde, eksiksiz bir anahtar çifti elde ederiz.


Daha sonra, $\text{Hash}$ ifadesinin ikinci kısmı, yeni türettiğimiz alt anahtar çifti için chain code olarak yorumlanır:


$$
C_{\text{CHD}} = h_2
$$


Burada genel türetmenin şematik bir gösterimi yer almaktadır:


![CYP201](assets/fr/050.webp)


Sertleştirilmiş bir alt anahtar için ($i \geq 2^{31}$), $\text{Hash}$ hesaplaması aşağıdaki gibidir:



$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, 0x00 \Vert k_{\text{PAR}} \Vert i)
$$


Bu hesaplamada, HMAC işlevimizin iki girdi aldığını gözlemliyoruz: önce ana chain code ve ardından dizinin ana özel anahtarla birleştirilmesi. Burada ana özel anahtar kullanılmaktadır çünkü sertleştirilmiş bir alt anahtar türetmek istiyoruz. Ayrıca, anahtarın başına `0x00` değerine eşit bir bayt eklenir. Bu işlem anahtarın uzunluğunu sıkıştırılmış bir açık anahtarın uzunluğuna eşitler.

Şimdi elimizde 64 baytlık bir $\text{Hash}$ var ve bunu her biri 32 baytlık 2 parçaya böleceğiz, $h_1$ ve $h_2$:

$$

\text{hash} = h_1 \Vert h_2

$$



$$
h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]
$$


Alt özel anahtar $k_{\text{CHD}}^h$ daha sonra aşağıdaki gibi hesaplanır:


$$
k_{\text{CHD}}^h = \text{parse256}(h_1) + k_{\text{PAR}} \mod n
$$


Daha sonra, $\text{Hash}$'in ikinci kısmını, az önce türettiğimiz alt anahtar çifti için chain code olarak yorumluyoruz:


$$
C_{\text{CHD}} = h_2
$$


Burada genel türetmenin şematik bir gösterimi yer almaktadır:


![CYP201](assets/fr/051.webp)


Normal türetmenin ve sertleştirilmiş türetmenin şu farkla aynı şekilde çalıştığını görebiliriz: normal türetmenin HMAC işlevine girdi olarak ana açık anahtarı kullanırken, sertleştirilmiş türetmenin ana özel anahtarı kullanması.


#### Bir üst açık anahtardan bir alt açık anahtar türetme


Yalnızca ana açık anahtar $K_{\text{PAR}}$ ve ilişkili chain code $C_{\text{PAR}}$'ı, yani genişletilmiş bir açık anahtarı biliyorsak, alt açık anahtarları $K_{\text{CHD}}^n$ türetmek mümkündür, ancak yalnızca normal (sertleştirilmemiş) alt anahtarlar için. Bu prensip özellikle bir Bitcoin Wallet'deki bir hesabın hareketlerinin `xpub'dan (*sadece izle*) izlenmesine izin verir.


Bu hesaplamayı gerçekleştirmek için $\text{Hash}$'i $i < 2^{31}$ indeksi ile hesaplayacağız (normal türetme):


$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, K_{\text{PAR}} \Vert i)
$$


Bu hesaplamada, HMAC işlevimizin iki girdi aldığını gözlemliyoruz: önce ana chain code, ardından dizinin ana açık anahtarla birleştirilmesi.


Şimdi elimizde 64 baytlık bir $\text{Hash}$ var ve bunu her biri 32 baytlık 2 parçaya böleceğiz, $h_1$ ve $h_2$:



$$

\text{hash} = h_1 \Vert h_2

$$



$$

h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]

$$


Alt açık anahtar $K_{\text{CHD}}^n$ daha sonra aşağıdaki gibi hesaplanır:


$$
K_{\text{CHD}}^n = \text{parse256}(h_1) \cdot G + K_{\text{PAR}}
$$


Eğer $\text{parse256}(h_1) \geq n$ (eliptik eğrinin mertebesi) veya $K_{\text{CHD}}^n$ sonsuzdaki nokta ise, türetme geçersizdir ve başka bir indeks seçilmelidir.


Bu hesaplamada, $\text{parse256}(h_1)$ işlemi $\text{Hash}$'ın ilk 32 baytının 256 bitlik bir tamsayı olarak yorumlanmasını içerir. Bu sayı, $G$ üreteç noktasından toplama ve iki katına çıkarma yoluyla eliptik eğri üzerinde bir nokta hesaplamak için kullanılır. Bu nokta daha sonra normal çocuk açık anahtarını elde etmek için ana açık anahtara eklenir. Dolayısıyla, normal bir çocuk açık anahtarı türetmek için yalnızca ebeveyn açık anahtarı ve ebeveyn chain code gereklidir; ebeveyn özel anahtarı, daha önce gördüğümüz çocuk özel anahtarının hesaplanmasının aksine, bu sürece asla dahil olmaz.


Ardından, çocuk chain code basitçe:


$$
C_{\text{CHD}} = h_2
$$


Burada genel türetmenin şematik bir gösterimi yer almaktadır:


![CYP201](assets/fr/052.webp)


### Çocuk açık ve özel anahtarları arasındaki yazışmalar


Ortaya çıkabilecek bir soru, bir ebeveyn açık anahtarından türetilen normal bir çocuk açık anahtarının, ilgili ebeveyn özel anahtarından türetilen normal bir çocuk özel anahtarına nasıl karşılık gelebileceğidir. Bu bağlantı, eliptik eğrilerin özellikleri tarafından tam olarak sağlanır. Aslında, normal bir alt açık anahtar türetmek için HMAC-SHA512 aynı şekilde uygulanır, ancak çıktısı farklı şekilde kullanılır:


- **Normal alt özel anahtar**: $k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n$
- **Normal alt açık anahtar**: $K_{\text{CHD}}^n = \text{parse256}(h_1) \cdot G + K_{\text{PAR}}$


Eliptik eğri üzerindeki toplama ve ikiye katlama işlemleri sayesinde her iki yöntem de tutarlı sonuçlar üretir: alt özel anahtardan türetilen açık anahtar, doğrudan üst açık anahtardan türetilen alt açık anahtarla aynıdır.


### Türetme türlerinin özeti


Özetlemek gerekirse, olası farklı türetme türleri şunlardır:


$$
\begin{array}{|c|c|c|c|}
\hline
\rightarrow & \text{PAR} & \text{CHD} & \text{n/h} \\
\hline
k_{\text{PAR}} \rightarrow k_{\text{CHD}} & k_{\text{PAR}} & \{ k_{\text{CHD}}^n, k_{\text{CHD}}^h \} & \{ n, h \} \\
k_{\text{PAR}} \rightarrow K_{\text{CHD}} & k_{\text{PAR}} & \{ K_{\text{CHD}}^n, K_{\text{CHD}}^h \} & \{ n, h \} \\
K_{\text{PAR}} \rightarrow k_{\text{CHD}} & K_{\text{PAR}} & \times & \times \\
K_{\text{PAR}} \rightarrow K_{\text{CHD}} & K_{\text{PAR}} & K_{\text{CHD}}^n & n \\
\hline
\end{array}
$$


Şimdiye kadar bir HD Wallet'nin temel Elements'unu oluşturmayı öğrendiniz: Mnemonic ifadesi, seed ve ardından ana anahtar ve ana chain code. Ayrıca bu bölümde alt anahtar çiftlerinin nasıl türetileceğini de keşfettiniz. Bir sonraki bölümde, bu türetmelerin Bitcoin cüzdanlarında nasıl düzenlendiğini ve *scriptPubKey* ve *scriptSig*'de kullanılan anahtar çiftlerinin yanı sıra alıcı adreslerini somut olarak elde etmek için hangi yapının izleneceğini inceleyeceğiz.


## Wallet Yapısı ve Türetme Yolları

<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>


Bitcoin'daki HD cüzdanlarının hiyerarşik yapısı, anahtar çiftlerinin çeşitli şekillerde düzenlenmesine olanak tanır. Buradaki fikir, ana özel anahtardan ve ana chain code'ten çeşitli derinlik seviyeleri türetmektir. Eklenen her seviye, bir üst anahtar çiftinden bir alt anahtar çiftinin türetilmesine karşılık gelir.


Zaman içinde, farklı BIP'ler bu türetme yolları için standartlar getirerek farklı yazılımlar arasında kullanımlarını standartlaştırmayı amaçlamıştır. Bu bölümde, bu standartlara göre HD cüzdanlarındaki her bir türetme seviyesinin anlamını keşfedeceğiz.


### Bir HD Wallet'nin Türetilmesinin Derinlikleri


Türetme yolları, ana anahtarı ve ana chain code'i temsil eden derinlik 0'dan UTXO'ları kilitlemek için kullanılan adresleri türetmek için alt düzey katmanlara kadar değişen derinlik katmanlarına göre düzenlenmiştir. BIP'ler (*Bitcoin İyileştirme Teklifleri*) her bir Layer için standartları tanımlar ve bu da farklı Wallet yönetim yazılımları arasındaki uygulamaların uyumlaştırılmasına yardımcı olur.


Bu nedenle türetme yolu, bir ana anahtardan alt anahtarları türetmek için kullanılan indisler dizisini ifade eder.


**Derinlik 0: Ana Anahtar (BIP32)**


Bu derinlik Wallet'ün ana özel anahtarına ve ana chain code'ye karşılık gelir. M/$ gösterimi ile temsil edilir.


**Derinlik 1: Amaç (BIP43)**


Amaç, türetmenin mantıksal yapısını belirler. Örneğin, bir P2WPKH Address 1. derinlikte $/84'/$ değerine sahipken (BIP84'e göre), bir P2TR Address $/86'/$ değerine sahip olacaktır (BIP86'ya göre). Bu Layer, BIP numaralarına karşılık gelen indeks numaralarını göstererek cüzdanlar arasındaki uyumluluğu kolaylaştırır.


Başka bir deyişle, ana anahtar ve ana chain code'e sahip olduğunuzda, bunlar bir alt anahtar çifti türetmek için bir üst anahtar çifti görevi görür. Bu türetmede kullanılan dizin, örneğin Wallet'ın SegWit v0 tipi komut dosyalarını kullanması amaçlanıyorsa $/84'/$ olabilir. Bu anahtar çifti daha sonra 1. derinliktedir. Rolü bitcoinleri kilitlemek değil, sadece türetme hiyerarşisinde bir yol noktası olarak hizmet etmektir.


**Derinlik 2: Para Birimi Türü (BIP44)**


Derinlik 1'deki anahtar çiftinden, derinlik 2'deki anahtar çiftini elde etmek için yeni bir türetme gerçekleştirilir. Bu derinlik, Bitcoin hesaplarının aynı Wallet içindeki diğer kripto para birimlerinden ayırt edilmesini sağlar.


Çoklu para birimi cüzdanları arasında uyumluluğu sağlamak için her para biriminin benzersiz bir endeksi vardır. Örneğin, Bitcoin için indeks $/0'/$ (veya onaltılık gösterimde `0x80000000`) şeklindedir. Para birimi endeksleri, sertleştirilmiş türetmeyi sağlamak için $2^{31}$ ile $2^{32}-1$ aralığında seçilir.


Size başka örnekler vermek gerekirse, işte bazı para birimlerinin endeksleri:


- gW-444 bitcoinleri için $1'$ (`0x80000001`);
- litecoin için $2'$ (`0x80000002`);
- ethereum için $60'$ (`0x8000003c`)...


**Derinlik 3: Hesap (BIP32)**


Her bir Wallet, $2^{31}$'den itibaren numaralandırılan ve 3. derinlikte ilk hesap için $/0'/$, ikincisi için $/1'/$ ve bu şekilde devam eden birkaç hesaba bölünebilir. Genel olarak, genişletilmiş bir `xpub` anahtarına atıfta bulunulduğunda, bu türetme derinliğindeki anahtarlara atıfta bulunulur.


Bu farklı hesaplara ayırma isteğe bağlıdır. Kullanıcılar için Wallet'nın organizasyonunu basitleştirmeyi amaçlar. Uygulamada, genellikle varsayılan olarak ilk hesap olmak üzere yalnızca bir hesap kullanılır. Bununla birlikte, bazı durumlarda, farklı kullanımlar için anahtar çiftlerini açıkça ayırt etmek istenirse, bu yararlı olabilir. Örneğin, bu türetme derinliğinden tamamen farklı anahtar gruplarıyla aynı seed'den kişisel bir hesap ve profesyonel bir hesap oluşturmak mümkündür.


**Derinlik 4: Zincir (BIP32)**


Derinlik 3'te tanımlanan her hesap daha sonra iki zincir halinde yapılandırılır:


- **Dış zincir**: Bu zincirde, "genel" adresler olarak bilinen adresler türetilir. Bu alıcı adresler, harici işlemlerden gelen (yani size ait olmayan UTXO'ların tüketiminden kaynaklanan) UTXO'ları kilitlemek için tasarlanmıştır. Basitçe söylemek gerekirse, bu harici zincir bitcoin almak istendiğinde kullanılır. Wallet yazılımınızda "*al*" seçeneğine tıkladığınızda, size sunulan her zaman harici zincirden bir Address'dir. Bu zincir $/0/$ indeksi ile türetilmiş bir anahtar çifti ile temsil edilir.
- **İç zincir (değişim)**: Bu zincir, size ait UTXO'ların tüketiminden gelen bitcoinleri kilitleyen adresleri almak, başka bir deyişle adresleri değiştirmek için ayrılmıştır. $/1/$ indeksi ile tanımlanır.


**Derinlik 5: Address Endeksi (BIP32)**


Son olarak, derinlik 5, Wallet'deki türetmenin son adımını temsil eder. Teknik olarak sonsuza kadar devam etmek mümkün olsa da, mevcut standartlar burada durmaktadır. Bu son derinlikte, UTXO'ları kilitlemek ve kilidini açmak için gerçekten kullanılacak anahtar çiftleri türetilir. Her bir indeks kardeş anahtar çiftleri arasında ayrım yapılmasını sağlar: böylece ilk alıcı Address $/0/$ indeksini, ikincisi $/1/$ indeksini kullanır ve bu böyle devam eder.


![CYP201](assets/fr/053.webp)


### Türetme Yollarının Gösterimi


Türetme yolu, her bir seviyeyi eğik çizgi ($/$) ile ayırarak yazılır. Böylece her eğik çizgi bir üst anahtar çiftinin ($k_{\text{PAR}}$, $K_{\text{PAR}}$, $C_{\text{PAR}}$) bir alt anahtar çiftine ($k_{\text{CHD}}$, $K_{\text{CHD}}$, $C_{\text{CHD}}$) türetildiğini gösterir. Her derinlikte belirtilen sayı, bu anahtarı ebeveynlerinden türetmek için kullanılan dizine karşılık gelir. Bazen dizinin sağına yerleştirilen kesme işareti ($'$) sertleştirilmiş bir türetmeyi gösterir ($k_{\text{CHD}}^h$, $K_{\text{CHD}}^h$). Bazen bu kesme işareti $h$ ile değiştirilir. Kesme işareti veya $h$ olmadığında, bu normal bir türetmedir ($k_{\text{CHD}}^n$, $K_{\text{CHD}}^n$).

Önceki bölümlerde gördüğümüz gibi, sertleştirilmiş anahtar dizinleri $2^{31}$ veya onaltılık olarak `0x80000000` değerinden başlar. Bu nedenle, bir türetme yolunda bir dizinin ardından kesme işareti geldiğinde, HMAC-SHA512 işlevinde kullanılan gerçek değeri elde etmek için $2^{31}$ belirtilen sayıya eklenmelidir. Örneğin, türetme yolu $/44'/$ belirtiyorsa, gerçek dizin şu şekilde olacaktır:

$$

i = 44 + 2^{31} = 2\,147\,483\,692

$$


Onaltılık sayı olarak bu `0x8000002C`dir.


Türetme yollarının ana prensiplerini anladığımıza göre, şimdi bir örnek verelim! İşte Address alan bir Bitcoin için türetme yolu:



$$

m / 84' / 0' / 1' / 0 / 7

$$


Bu örnekte:


- $84'$ P2WPKH (SegWit v0) standardını gösterir;
- $0'$ Mainnet üzerindeki Bitcoin para birimini gösterir;
- 1'$ Wallet'daki ikinci hesaba karşılık gelmektedir;
- $0$ Address'ın harici zincirde olduğunu gösterir;
- $7$ bu hesabın 8. harici Address'ini gösterir.


### Türetme yapısının özeti


| Depth | Description        | Standard Example                  |
| ----- | ------------------ | --------------------------------- |
| 0     | Master Key         | $m/$                              |
| 1     | Purpose            | $/86'/$ (P2TR)                    |
| 2     | Currency           | $/0'/$ (Bitcoin)                  |
| 3     | Account            | $/0'/$ (First account)            |
| 4     | Chain              | $/0/$ (external) or $/1/$ (change)|
| 5     | Address Index      | $/0/$ (first address)             |

Bir sonraki bölümde, Bitcoin core'de yakın zamanda tanıtılan ve bir Bitcoin Wallet'ün yedeklenmesini basitleştiren bir yenilik olan "*çıktı komut dosyası tanımlayıcılarının*" ne olduğunu keşfedeceğiz.


## Çıktı komut dosyası tanımlayıcıları

<chapterId>e4f1c2d3-9b8a-4d3e-8f2a-7b6c5d4e3f2a</chapterId>

Genellikle Mnemonic ifadesinin tek başına bir Wallet'e erişimi kurtarmak için yeterli olduğu söylenir. Gerçekte işler biraz daha karmaşıktır. Bir önceki bölümde HD Wallet'in türetme yapısına baktık ve bu sürecin oldukça karmaşık olduğunu fark etmiş olabilirsiniz. Türetme yolları yazılıma kullanıcının anahtarlarını türetmek için hangi yönü takip etmesi gerektiğini söyler. Ancak, bir Bitcoin Wallet kurtarılırken, bu yollar bilinmiyorsa, Mnemonic ifadesi tek başına yeterli değildir. Ana anahtarın ve ana chain code'in elde edilmesini sağlar, ancak daha sonra alt anahtarlara ulaşmak için kullanılan dizinlerin bilinmesi gerekir.


Teorik olarak, sadece Mnemonic'umuzun Wallet ifadesini değil, aynı zamanda kullandığımız hesaplara giden yolları da kaydetmek gerekir. Pratikte, standartlara uyulması koşuluyla, bu bilgiler olmadan alt anahtarlara yeniden erişim sağlamak çoğu zaman mümkündür. Her bir standardı tek tek test ederek bitcoinlere yeniden erişim sağlamak genellikle mümkündür. Ancak bu garanti değildir ve özellikle yeni başlayanlar için karmaşıktır. Ayrıca, script türlerinin çeşitlenmesi ve daha karmaşık konfigürasyonların ortaya çıkmasıyla, bu bilgilerin tahmin edilmesi zorlaşabilir, böylece bu veriler özel bilgilere dönüşebilir ve kaba kuvvetle kurtarılması zorlaşabilir. Bu nedenle yakın zamanda bir yenilik tanıtıldı ve favori Wallet yazılımınıza entegre edilmeye başlandı: *çıkış komut dosyası tanımlayıcıları*.


### "Descriptor" nedir?


"*output script descriptors*" ya da kısaca "*descriptors*", bir çıktı komut dosyasını (*scriptPubKey*) tam olarak tanımlayan ve belirli bir komut dosyasıyla ilişkili işlemleri takip etmek için gerekli tüm bilgileri sağlayan yapılandırılmış ifadelerdir. Wallet yapısının ve kullanılan adres türlerinin standartlaştırılmış ve eksiksiz bir tanımını sunarak HD cüzdanlarındaki anahtarların yönetimini kolaylaştırırlar.


Tanımlayıcıların ana avantajı, bir Wallet'yı geri yüklemek için gerekli tüm bilgileri tek bir dizede (kurtarma ifadesine ek olarak) kapsülleme yeteneklerinde yatmaktadır. Bir Descriptor'ü ilişkili Mnemonic ifadeleriyle birlikte kaydederek, özel anahtarları hiyerarşideki konumlarını tam olarak bilerek geri yüklemek mümkün hale gelir. Yedeklemesi başlangıçta daha karmaşık olan Multisig cüzdanları için, Descriptor her bir faktörün `xpub`ını içerir, böylece bir sorun olması durumunda adresleri yeniden oluşturma imkanı sağlar.


### Descriptor'nin inşası


Bir Descriptor birkaç Elements'dan oluşur:


- Pk` (*Pay-to-PubKey*), `pkh` (*Pay-to-PubKey-Hash*), `wpkh` (*Pay-to-Witness-PubKey-Hash*), `sh` (*Pay-to-Script-Hash*) gibi komut dosyası işlevleri, wsh` (*Pay-to-Witness-Script-Hash*), `tr` (*Pay-to-Taproot*), `multi` (*Multisignature*) ve `sortedmulti` (*Sıralanmış anahtarlarla çoklu imza*);
- Türetme yolları, örneğin, türetilmiş bir hesap yolunu ve belirli bir ana anahtar parmak izini gösteren `[d34db33f/44h/0h/0h]`;
- Onaltılık genel anahtarlar veya genişletilmiş genel anahtarlar (`xpub`) gibi çeşitli biçimlerdeki anahtarlar;
- Descriptor'ün bütünlüğünü doğrulamak için Hash işaretinden önce gelen bir sağlama toplamı.


Örneğin, bir P2WPKH (SegWit v0) Wallet için bir Descriptor şöyle görünebilir:


```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7nr4
```


Bu Descriptor'da, `wpkh` türetme işlevi bir komut dosyası türünü *Pay-to-Witness-Public-Key-Hash* belirtir. Bunu içeren türetme yolu takip eder:


- `cdeab12f`: ana anahtar parmak izi;
- `84h`: SegWit v0 adresleri için tasarlanmış bir BIP84 amacının kullanıldığını gösterir;
- `0h`: bu da Mainnet üzerinde bir BTC para birimi olduğunu gösterir;
- `0h`: Wallet'te kullanılan belirli hesap numarasını ifade eder.


Descriptor ayrıca bu Wallet'te kullanılan genişletilmiş açık anahtarı da içerir:


```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```


<0;1>/*` notasyonu Descriptor'nın generate adreslerini hem harici zincirden (`0`) hem de dahili zincirden (`1`) alabileceğini gösterir. Yolun sonundaki joker karakter (`*`), ister harici ister dahili adresler olsun, sırayla tüm sertleştirilmemiş ("*sertleştirilmemiş*") alt anahtarların bu konumdan türetilebileceği anlamına gelir. Bu sözdizimi, Address tespiti için Wallet'a özgü bir mekanizmanın parçası olan *boşluk sınırı* kavramını doğrudan ima etmez, ancak burada yalnızca bu konumdaki tüm olası türetmelerin dikkate alındığını belirtmeye yarar.


Son olarak, `#jy0l7nr4` Descriptor'ün bütünlüğünü doğrulamak için sağlama toplamını temsil eder.


Artık Bitcoin'de HD cüzdanların çalışması ve anahtar çiftlerinin türetilmesi süreci hakkında her şeyi biliyorsunuz. Ancak, son bölümlerde, alıcı adreslerin oluşturulmasına değinmeden kendimizi özel ve açık anahtarların oluşturulmasıyla sınırladık. Bu tam olarak bir sonraki bölümün konusu olacak!


## Alıcı Adresleri

<chapterId>ca80a89d-f8da-4e09-8c35-43179b65bced</chapterId>


Alıcı adresleri, yeni oluşturulan UTXO'ları kilitlemek için *scriptPubKey* içine yerleştirilmiş bilgi parçalarıdır. Basitçe söylemek gerekirse, bir Address bitcoin almaya yarar. Önceki bölümlerde incelediklerimizle bağlantılı olarak bunların işleyişini inceleyelim.


### Bitcoin Adreslerinin Komut Dosyalarındaki Rolü


Daha önce açıklandığı gibi, bir işlemin rolü Ownership bitcoinlerini girdilerden çıktılara aktarmaktır. Bu süreç, UTXO'ları girdi olarak tüketirken, çıktı olarak yeni UTXO'lar oluşturmayı içerir. Bu UTXO'lar, fonların kilidini açmak için gerekli koşulları tanımlayan komut dosyaları tarafından güvence altına alınır.


Bir kullanıcı bitcoin aldığında, gönderen bir UTXO oluşturur ve bunu bir *scriptPubKey* ile kilitler. Bu komut dosyası, UTXO'in kilidini açmak için gerekli kuralları içerir ve genellikle gerekli imzaları ve açık anahtarları belirtir. Bu UTXO'i yeni bir işlemde harcamak için, kullanıcı istenen bilgileri bir *scriptSig* aracılığıyla sağlamalıdır. *ScriptPubKey* ile birlikte *scriptSig*'in yürütülmesi "true" veya `1` döndürmelidir. Bu koşul yerine getirilirse, UTXO yeni bir *scriptPubKey* tarafından kilitlenen yeni bir UTXO oluşturmak için harcanabilir ve bu böyle devam eder.


![CYP201](assets/fr/054.webp)


Alıcı adresleri tam olarak *scriptPubKey* içinde bulunur. Ancak, bunların kullanımı benimsenen komut dosyası standardına bağlı olarak değişir. Burada, kullanılan standarda göre *scriptPubKey* içinde bulunan bilgilerin ve *scriptPubKey* kilidini açmak için *scriptSig* içinde beklenen bilgilerin bir özet tablosu bulunmaktadır.


| Standard           | *scriptPubKey*                                              | *scriptSig*                     | *redeem script*     | *witness*                                |
| ------------------ | ----------------------------------------------------------- | ------------------------------- | ------------------- | ---------------------------------------- |
| P2PK               | `<pubkey> OP_CHECKSIG`                                      | `<signature>`                   |                     |                                          |
| P2PKH              | `OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG` | `<signature> <public key>`      |                     |                                          |
| P2SH               | `OP_HASH160 <scriptHash> OP_EQUAL`                          | `<data pushes> <redeem script>` | Arbitrary data     |                                          |
| P2WPKH             | `0 <pubKeyHash>`                                            |                                 |                     | `<signature> <public key>`               |
| P2WSH              | `0 <witnessScriptHash>`                                     |                                 |                     | `<data pushes> <witness script>`         |
| P2SH-P2WPKH        | `OP_HASH160 <redeemScriptHash> OP_EQUAL`                    | `<redeem script>`               | `0 <pubKeyHash>`    | `<signature> <public key>`               |
| P2SH-P2WSH         | `OP_HASH160 <redeemScriptHash> OP_EQUAL`                    | `<redeem script>`               | `0 <scriptHash>`    | `<data pushes> <witness script>`         |
| P2TR (key path)    | `1 <public key>`                                            |                                 |                     | `<signature>`                            |
| P2TR (script path) | `1 <public key>`                                            |                                 |                     | `<data pushes> <script> <control block>` |

*Kaynak: Bitcoin core PR inceleme kulübü, 7 Temmuz 2021 - Gloria Zhao*


Bir betikte kullanılan işlem kodları, bilgiyi işlemek ve gerekirse karşılaştırmak veya test etmek için tasarlanmıştır. Aşağıdaki gibi bir P2PKH betiği örneğini ele alalım:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```


Bu bölümde göreceğimiz gibi, `<pubKeyHash>` aslında UTXO'i kilitlemek için kullanılan alıcı Address'nin yükünü temsil eder. Bu *scriptPubKey*'in kilidini açmak için, *scriptSig* içeren bir *scriptSig* sağlamak gerekir:


```text
<signature> <public key>
```


Kod dilinde yığın, kod yürütme sırasında Elements'u geçici olarak depolamak için kullanılan bir *LIFO* ("*Last In, First Out*") veri yapısıdır. Her kod işlemi, Elements'un eklenebildiği (*push*) veya kaldırılabildiği (*pop*) bu yığını manipüle eder. Kodlar ifadeleri değerlendirmek, geçici değişkenleri saklamak ve koşulları yönetmek için yığını kullanır.


Az önce örnek olarak verdiğim komut dosyasının yürütülmesi bu süreci takip eder:



- Elimizde *scriptSig*, *scriptPubKey* ve yığın var:


![CYP201](assets/fr/055.webp)



- *scriptSig* yığına itilir:


![CYP201](assets/fr/056.webp)



- oP_DUP`, *scriptSig* içinde sağlanan açık anahtarı yığın üzerinde çoğaltır:


![CYP201](assets/fr/057.webp)



- oP_HASH160`, az önce çoğaltılan açık anahtarın Hash değerini döndürür:


![CYP201](assets/fr/058.webp)



- oP_PUSHBYTES_20 <pubKeyHash>` *scriptPubKey* içinde bulunan Bitcoin Address'i yığına iter:


![CYP201](assets/fr/059.webp)



- `OP_EQUALVERIFY` hashlenmiş açık anahtarın sağlanan alıcı Address ile eşleştiğini doğrular:


![CYP201](assets/fr/060.webp)


oP_CHECKSIG` açık anahtarı kullanarak *scriptSig* içinde bulunan imzayı kontrol eder. Bu işlem kodu esasen bu eğitimin 3. bölümünde açıkladığımız gibi bir imza doğrulaması gerçekleştirir:



![CYP201](assets/fr/061.webp)



- Yığında `1` kalırsa, komut dosyası geçerlidir:


![CYP201](assets/fr/062.webp)


Dolayısıyla, özetlemek gerekirse, bu komut dosyası, dijital imza yardımıyla, bu UTXO'nın Ownership'ünü talep eden ve onu harcamak isteyen kullanıcının, bu UTXO'nın oluşturulması sırasında kullanılan alıcı Address ile ilişkili özel anahtara gerçekten sahip olduğunu doğrulamaya izin verir.


### Farklı Bitcoin adres türleri


Bitcoin'un gelişimi boyunca, birkaç standart senaryo modeli eklenmiştir. Bunların her biri farklı bir Address alma türü kullanır. İşte bugüne kadar mevcut olan ana senaryo modellerine genel bir bakış:


**P2PK (*Pay-to-PubKey*)**:


Bu betik modeli Bitcoin'in ilk sürümünde Satoshi Nakamoto tarafından tanıtılmıştır. P2PK betiği bitcoinleri doğrudan ham bir açık anahtar kullanarak kilitler (dolayısıyla bu modelde Address alınmaz). Yapısı basittir: bir açık anahtar içerir ve fonların kilidini açmak için karşılık gelen bir dijital imza gerektirir. Bu komut dosyası "*Legacy*" standardının bir parçasıdır.


**P2PKH (*Pay-to-PubKey-Hash*)**:


P2PK gibi, P2PKH betiği de Bitcoin'in lansmanında tanıtıldı. Selefinden farklı olarak, doğrudan ham açık anahtarı kullanmak yerine açık anahtarın Hash'sını kullanarak bitcoinleri kilitler. Daha sonra *scriptSig* alıcı Address ile ilişkili açık anahtarı ve geçerli bir imzayı sağlamalıdır. Bu modele karşılık gelen adresler `1` ile başlar ve *base58check* ile kodlanır. Bu komut dosyası aynı zamanda "*Legacy*" standardına aittir.


**P2SH (*Pay-to-Script-Hash*)**:


2012 yılında BIP16 ile tanıtılan P2SH modeli, *scriptPubKey* içinde rastgele bir komut dosyasının Hash'unun kullanılmasına izin verir. "*redeemscript*" olarak adlandırılan bu karma komut dosyası, fonların kilidini açmak için gerekli koşulları içerir. P2SH ile kilitlenmiş bir UTXO'yi harcamak için, orijinal *redeemscript*'un yanı sıra bunu doğrulamak için gerekli verileri içeren bir *scriptSig* sağlamak gerekir. Bu model özellikle eski multisig'ler için kullanılır. P2SH ile ilişkili adresler `3` ile başlar ve *base58check* ile kodlanır. Bu betik aynı zamanda "*Legacy*" standardına aittir.


**P2WPKH (*Pay-to-Witness-PubKey-Hash*)**:


Bu betik de bir açık anahtarın Hash'sını kullanarak bitcoinleri kilitlediği için P2PKH'ye benzer. Ancak P2PKH'den farklı olarak *scriptSig*, "*Witness*" adlı ayrı bir bölüme taşınmıştır. İmza ve açık anahtarı içeren kümeyi belirtmek için bu bazen "*scriptWitness*" olarak adlandırılır. Her bir SegWit girdisinin kendine ait bir *scriptWitness* vardır ve *scriptWitnesses* koleksiyonu işlemin *Witness* alanını oluşturur. İmza verilerinin bu hareketi, SegWit güncellemesiyle getirilen bir yeniliktir ve özellikle ECDSA imzaları nedeniyle işlemlerin değiştirilebilirliğini önlemeyi amaçlamaktadır.

P2WPKH adresleri *bech32* kodlamasını kullanır ve her zaman `bc1q` ile başlar. Bu tür bir kod, sürüm 0 SegWit çıktılarına karşılık gelir.


**P2WSH (*Pay-to-Witness-Script-Hash*)**:


P2WSH modeli de Ağustos 2017'de SegWit güncellemesiyle tanıtıldı. P2SH modeline benzer şekilde, bir komut dosyasının Hash'sini kullanarak bitcoinleri kilitler. Temel fark, imzaların ve komut dosyalarının işleme nasıl dahil edildiğinde yatmaktadır. Bu tür bir komut dosyası ile kilitlenen bitcoinleri harcamak için, alıcının *witnessScript* (P2SH'teki *redeemscript* ile eşdeğer) adı verilen orijinal komut dosyasını ve bu *witnessScript*'i doğrulamak için gerekli verileri sağlaması gerekir. Bu mekanizma, multisig gibi daha karmaşık harcama koşullarının uygulanmasına olanak sağlar.


P2WSH adresleri *bech32* kodlamasını kullanır ve her zaman `bc1q` ile başlar. Bu betik aynı zamanda sürüm 0 SegWit çıktılarına da karşılık gelir.


**P2TR (*Pay-to-Taproot*)**:


P2TR modeli, Kasım 2021'de Taproot'in uygulanmasıyla birlikte tanıtılmıştır. Kriptografik anahtar toplama için Schnorr protokolünün yanı sıra MAST (*Merkelized Alternative Script Tree*) adı verilen alternatif senaryolar için bir Merkle Tree'ye dayanmaktadır. Harcama koşullarının kamuya açık olduğu (makbuzda veya harcamada) diğer senaryo türlerinden farklı olarak P2TR, karmaşık senaryoların tek ve görünür bir açık anahtarın arkasına gizlenmesine olanak tanır.


Teknik olarak, bir P2TR betiği bitcoinleri $Q$ olarak gösterilen benzersiz bir Schnorr açık anahtarına kilitler. Bu $Q$ anahtarı aslında $P$ açık anahtarı ile $M$ açık anahtarının bir toplamıdır ve ikincisi *scriptPubKey* listesinin Merkle Root'sinden hesaplanır. Bu tür bir komut dosyası ile kilitlenen Bitcoinler iki şekilde harcanabilir:


- P$ açık anahtarı için bir imza yayınlayarak (*anahtar yolu*).
- Merkle Tree'de bulunan komut dosyalarından birini (*komut dosyası yolu*) yerine getirerek.


P2TR, bitcoinlerin benzersiz bir açık anahtarla, tercih edilen birkaç komut dosyasıyla veya her ikisiyle aynı anda kilitlenmesine izin verdiği için büyük esneklik sunar. Bu Merkle Tree yapısının avantajı, işlem sırasında yalnızca kullanılan harcama komut dosyasının açığa çıkması, ancak diğer tüm alternatif komut dosyalarının gizli kalmasıdır.


![CYP201](assets/fr/063.webp)


P2TR, sürüm 1 SegWit çıktılarına karşılık gelir; bu da P2TR girdilerinin imzalarının *scriptSig* içinde değil, işlemin *Witness* bölümünde saklandığı anlamına gelir. P2TR adresleri *bech32m* kodlamasını kullanır ve `bc1p` ile başlar, ancak yapıları için bir Hash işlevi kullanmadıkları için oldukça benzersizdirler. Aslında, doğrudan meta verilerle basitçe biçimlendirilmiş $Q$ açık anahtarını temsil ederler. Bu nedenle, P2PK'ya yakın bir komut dosyası modelidir.


Şimdi teoriyi ele aldığımıza göre, uygulamaya geçelim! Bir sonraki bölümde, bir çift anahtardan hem bir SegWit v0 Address hem de bir SegWit v1 Address türetmeyi öneriyorum.


## Address Türetme

<chapterId>3ebdc750-4135-4881-b07e-08965941b93e</chapterId>


Örneğin bir HD Wallet'ün 5. derinliğinde bulunan bir çift anahtardan bir alıcı Address'nin nasıl generate yapılacağını birlikte inceleyelim. Bu Address daha sonra bir Wallet yazılımında bir UTXO'ü kilitlemek için kullanılabilir.


Bir Address oluşturma süreci benimsenen komut dosyası modeline bağlı olduğundan, iki özel duruma odaklanalım: P2WPKH'da bir SegWit v0 Address ve P2TR'de bir SegWit v1 Address oluşturmak. Bu iki adres türü günümüzde kullanımların büyük çoğunluğunu kapsamaktadır.


### Açık Anahtar Sıkıştırma


Uygun indeksleri kullanarak ana anahtardan derinlik 5'e kadar tüm türetme adımlarını gerçekleştirdikten sonra, $K = k \cdot G$ ile bir çift anahtar ($k$, $K$) elde ederiz. Bu açık anahtarı P2PK standardı ile fonları kilitlemek için olduğu gibi kullanmak mümkün olsa da, buradaki amacımız bu değil. Bunun yerine, ilk örnekte Address'da ve daha sonra başka bir örnek için P2TR'de bir P2WPKH oluşturmayı hedefliyoruz.


İlk adım açık anahtar $K$'yı sıkıştırmaktır. Bu süreci iyi anlamak için öncelikle 3. bölümde ele alınan bazı temel bilgileri hatırlayalım.

Bitcoin'de bir açık anahtar, eliptik bir eğri üzerinde bulunan bir $K$ noktasıdır. Bu nokta $(x, y)$ şeklinde gösterilir, burada $x$ ve $y$ noktanın koordinatlarıdır. Sıkıştırılmamış haliyle bu açık anahtar 520 bit büyüklüğündedir: önek için 8 bit (başlangıç değeri `0x04`), $x$ koordinatı için 256 bit ve $y$ koordinatı için 256 bit.

Ancak, eliptik eğriler x eksenine göre bir simetri özelliğine sahiptir: belirli bir $x$ koordinatı için, $y$ için yalnızca iki olası değer vardır: $y$ ve $-y$. Bu iki nokta x ekseninin her iki tarafında yer alır. Başka bir deyişle, $x$ değerini biliyorsak, eğri üzerindeki tam noktayı belirlemek için $y$ değerinin çift mi yoksa tek mi olduğunu belirtmemiz yeterlidir.


![CYP201](assets/fr/064.webp)


Bir açık anahtarı sıkıştırmak için yalnızca 256 bitlik $x$ kodlanır ve $y$ paritesini belirtmek için bir önek eklenir. Bu yöntem açık anahtarın boyutunu başlangıçtaki 520 bit yerine 264 bite düşürür. 0x02` öneki $y$'nin çift olduğunu, `0x03` öneki ise $y$'nin tek olduğunu gösterir.


İyi anlamak için sıkıştırılmamış gösterimde ham bir açık anahtarla bir örnek verelim:


```text
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```


Eğer bu anahtarı ayrıştırırsak:


   - Önek: `04`;
   - $x$: `678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6`;
   - $y$: `49f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f`


Y$'nin son onaltılık karakteri `f`dir. 10 tabanında, `f = 15` tek sayıya karşılık gelir. Bu nedenle, $y$ tektir ve bunu belirtmek için önek `0x03` olacaktır.


Sıkıştırılmış açık anahtar olur:


```text
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```

Bu işlem ECDSA'ya dayalı tüm senaryo modelleri için geçerlidir, yani Schnorr kullanan P2TR hariç hepsi için geçerlidir. Schnorr durumunda, 3. bölümde açıklandığı gibi, ECDSA'nın aksine $y$ paritesini belirtmek için bir önek eklemeden yalnızca $x$ değerini koruruz. Bu, tüm anahtarlar için benzersiz bir paritenin keyfi olarak seçilmesiyle mümkün olmaktadır. Bu, açık anahtarlar için gereken depolama alanında küçük bir azalma sağlar.

### Bir SegWit v0 (bech32) Address türetilmesi


Artık sıkıştırılmış açık anahtarımızı elde ettiğimize göre, bundan Address alan bir SegWit v0 türetebiliriz.


İlk adım, HASH160 Hash işlevini sıkıştırılmış açık anahtara uygulamaktır. HASH160, birbirini izleyen iki Hash işlevinin bir bileşimidir: SHA256 ve ardından RIPEMD160:



$$

\text{HASH160}(K) = \text{RIPEMD160}(\text{SHA256}(K))

$$


İlk olarak anahtarı SHA256'dan geçiriyoruz:


```text
SHA256(K) = C489EBD66E4103B3C4B5EAFF462B92F5847CA2DCE0825F4997C7CF57DF35BF3A
```


Ardından sonucu RIPEMD160 üzerinden geçiririz:


```text
RIPEMD160(SHA256(K)) = 9F81322CC88622CA4CCB2A52A21E2888727AA535
```


Address'un yükü olarak adlandırılan şeyi oluşturan 160 bitlik bir Hash açık anahtarı elde ettik. Bu yük, Address'un merkezi ve en önemli kısmını temsil eder. Ayrıca UTXO'ları kilitlemek için *scriptPubKey* içinde kullanılır.


Ancak, bu yükü insanlar tarafından daha kolay kullanılabilir hale getirmek için meta veri eklenir. Bir sonraki adım, bu Hash'nin ondalık olarak 5 bitlik gruplar halinde kodlanmasını içerir. Bu ondalık dönüşüm, SegWit sonrası adresler tarafından kullanılan *bech32*'ye dönüştürme için faydalı olacaktır. Böylece 160 bitlik ikili Hash 5 bitlik 32 gruba bölünmüş olur:



$$

\begin{array}{|c|c|}
\hline
\text{5 bits} & \text{Decimal} \\
\hline
10011 & 19 \\
11110 & 30 \\
00000 & 0 \\
10011 & 19 \\
00100 & 4 \\
01011 & 11 \\
00110 & 6 \\
01000 & 8 \\
10000 & 16 \\
11000 & 24 \\
10001 & 17 \\
01100 & 12 \\
10100 & 20 \\
10011 & 19 \\
00110 & 6 \\
01011 & 11 \\
00101 & 5 \\
01001 & 9 \\
01001 & 9 \\
01010 & 10 \\
00100 & 4 \\
00111 & 7 \\
10001 & 17 \\
01000 & 8 \\
10001 & 17 \\
00001 & 1 \\
11001 & 25 \\
00111 & 7 \\
10101 & 21 \\
00101 & 5 \\
00101 & 5 \\
10101 & 21 \\
\hline
\end{array}

$$

Yani, elimizde:


```text
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
```


Hash 5 bitlik gruplar halinde kodlandıktan sonra Address'e bir sağlama toplamı eklenir. Bu sağlama toplamı, Address'ün yükünün depolanması veya iletimi sırasında değiştirilmediğini doğrulamak için kullanılır. Örneğin, bir Wallet yazılımının alıcı bir Address girerken yazım hatası yapmadığınızdan emin olmasını sağlar. Bu doğrulama olmadan, yanlışlıkla yanlış bir Address'e bitcoin gönderebilirsiniz, bu da ilgili genel veya özel anahtara sahip olmadığınız için kalıcı bir fon kaybına neden olabilir. Bu nedenle, sağlama toplamı insan hatalarına karşı bir korumadır.


Eski Bitcoin *Legacy* adresleri için sağlama toplamı basitçe Address Hash'un başından HASH256 fonksiyonu ile hesaplanıyordu. SegWit ve *bech32* formatının kullanılmaya başlanmasıyla birlikte artık BCH kodları (*Bose, Ray-Chaudhuri ve Hocquenghem*) kullanılmaktadır. Bu hata düzeltme kodları veri dizilerindeki hataları tespit etmek ve düzeltmek için kullanılır. Küçük değiĢiklikler olsa bile, iletilen bilginin hedefine bozulmadan ulaĢmasını sağlarlar. BCH kodları SSD'ler, DVD'ler ve QR kodları gibi birçok alanda kullanılmaktadır. Örneğin, bu BCH kodları sayesinde, kısmen gizlenmiş bir QR kodu yine de okunabilir ve çözülebilir.


Bitcoin bağlamında, BCH kodları, *Legacy* adresleri için kullanılan basit Hash işlevlerine kıyasla boyut ve hata algılama yeteneği arasında daha iyi bir uzlaşma sunar. Ancak, Bitcoin'de BCH kodları düzeltme için değil sadece hata tespiti için kullanılır. Bu nedenle, Wallet yazılımı hatalı bir Address alımını işaret edecek ancak otomatik olarak düzeltmeyecektir. Bu sınırlama kasıtlıdır: otomatik düzeltmeye izin vermek hata algılama kapasitesini azaltacaktır.


BCH kodları ile sağlama toplamını hesaplamak için birkaç Elements hazırlamamız gerekir.


- **HRP (*İnsan Tarafından Okunabilir Parça*)**: Bitcoin Mainnet için HRP `bc`dir;


HRP, her bir karakter iki parçaya ayrılarak genişletilmelidir:


- HRP'nin karakterlerinin ASCII olarak alınması:
 - `b`: `01100010`
 - `c`: `01100011`
- En anlamlı 3 bitin ve en az anlamlı 5 bitin çıkarılması:
  - en anlamlı 3 bit: `011` (ondalık olarak 3)
  - en anlamlı 3 bit: `011` (ondalık olarak 3)
  - en az anlamlı 5 bit: `00010` (ondalık olarak 2)
  - en az anlamlı 5 bit: `00011` (ondalık olarak 3)


İki karakter arasında `0` ayıracı ile HRP uzantısı bu şekilde olur:


```text
03 03 00 02 03
```



- **Tanık sürümü**: SegWit sürüm 0 için bu `00`dür;



- **Yük**: Hash genel anahtarının ondalık değerleri;



- **Sağlama toplamı için rezervasyon**: Dizinin sonuna 6 sıfır `[0, 0, 0, 0, 0]` ekliyoruz.


Sağlama toplamını hesaplamak için programa girmek üzere birleştirilen tüm veriler aşağıdaki gibidir:


```text
HRP = 03 03 00 02 03
SEGWIT v0 = 00
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
CHECKSUM = 00 00 00 00 00 00

INPUT = 03 03 00 02 03 00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 00 00 00 00 00 00
```


Sağlama toplamının hesaplanması oldukça karmaşıktır. Polinom sonlu alan aritmetiği içerir. Bu hesaplamayı burada detaylandırmayacağız ve doğrudan sonuca geçeceğiz. Örneğimizde, ondalık olarak elde edilen sağlama toplamı şöyledir:


```text
10 16 11 04 13 18
```


Şimdi aşağıdaki Elements'u sırayla birleştirerek alıcı Address'ü oluşturabiliriz:


- **SegWit sürümü**: `00`
- **Yük**: Açık anahtar Hash
- **Sağlama toplamı**: Önceki adımda elde edilen değerler (`10 16 11 04 13 18`)


Bu bize ondalık olarak verir:


```text
00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 10 16 11 04 13 18
```


Ardından, her ondalık değer aşağıdaki dönüşüm tablosu kullanılarak *bech32* karakterine eşlenmelidir:



$$

\begin{array}{|c|c|c|c|c|c|c|c|c|}
\hline
& 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\hline
+0 & q & p & z & r & y & 9 & x & 8 \\
\hline
+8 & g & f & 2 & t & v & d & w & 0 \\
\hline
+16 & s & 3 & j & n & 5 & 4 & k & h \\
\hline
+24 & c & e & 6 & m & u & a & 7 & l \\
\hline
\end{array}

$$


Bu tabloyu kullanarak bir değeri _bech32_ karakterine dönüştürmek için, ilk sütunda ve ilk satırda toplandığında istenen sonucu veren değerleri bulun. Ardından, karşılık gelen karakteri alın. Örneğin, `19` ondalık sayısı `n` harfine dönüştürülecektir, çünkü $19 = 16 + 3$.


Tüm değerlerimizi eşleştirerek aşağıdaki Address'ü elde ederiz:


```
qn7qnytxgsc3v5nxt9ff2y83g3pe84ff42stydj
```


Geriye kalan tek şey, Bitcoin Mainnet için bir Address olduğunu belirten HRP `bc`yi ve tam alıcı Address'ü elde etmek için `1` ayırıcısını eklemektir:


```
bc1qn7qnytxgsc3v5nxt9ff2y83g3pe84ff42stydj
```


Bu _bech32_ alfabesinin özelliği, özellikle insanlar tarafından girilmesi veya okunması sırasında benzer karakterler arasındaki görsel karışıklığı önlemek için `1`, `b`, `i` ve `o` hariç tüm alfanümerik karakterleri içermesidir.


Özetlemek gerekirse, türetme süreci şu şekildedir:


![CYP201](assets/fr/065.webp)


Bir çift anahtardan Address alan bir P2WPKH (SegWit v0) bu şekilde türetilir. Şimdi P2TR (SegWit v1 / Taproot) adreslerine geçelim ve bunların üretim sürecini keşfedelim.


### SegWit v1 (bech32m) Address'nin türetilmesi


Taproot adresleri için oluşturma süreci biraz farklıdır. Gelin buna birlikte bakalım!


Açık anahtar sıkıştırma adımından itibaren ECDSA'ya kıyasla ilk fark ortaya çıkar: Bitcoin'te Schnorr için kullanılan açık anahtarlar yalnızca apsisleriyle ($x$) temsil edilir. Bu nedenle, ön ek yoktur ve sıkıştırılmış anahtar tam olarak 256 bittir.

Önceki bölümde gördüğümüz gibi, bir P2TR betiği bitcoinleri $Q$ ile belirtilen benzersiz bir Schnorr açık anahtarına kilitler. Bu $Q$ anahtarı iki açık anahtarın bir toplamıdır: $P$, ana dahili açık anahtar ve $M$, _scriptPubKey_ listesinin Merkle Root'sından türetilen bir açık anahtardır. Bu tür bir komut dosyası ile kilitlenen bitcoinler iki şekilde harcanabilir:



- P$ açık anahtarı için bir imza yayınlayarak (_key path_);
- Merkle Tree'de bulunan komut dosyalarından birini (_script path_) yerine getirerek.


Gerçekte, bu iki anahtar gerçekten "birleştirilmiş" değildir Bunun yerine $P$ anahtarı $M$ anahtarı tarafından değiştirilir. Kriptografide, bir açık anahtarı "ince ayarlamak", bu anahtarı "ince ayar" adı verilen bir toplama değeri uygulayarak değiştirmek anlamına gelir Bu işlem, değiştirilen anahtarın orijinal özel anahtar ve ince ayar ile uyumlu kalmasını sağlar. Teknik olarak ince ayar, ilk açık anahtara eklenen skaler bir $t$ değeridir. Eğer $P$ orijinal açık anahtar ise, ince ayarlanmış anahtar şu hale gelir:



$$

P' = P + t \cdot G

$$


Burada $G$ kullanılan eliptik eğrinin üretecidir. Bu işlem, kullanımına izin veren kriptografik özellikleri korurken orijinal anahtardan türetilmiş yeni bir açık anahtar üretir.


Alternatif komut dosyaları eklemeniz gerekmiyorsa (yalnızca _anahtar yolu_ üzerinden harcama yaparak), yalnızca Wallet'nizin 5. derinliğinde bulunan açık anahtar üzerine kurulmuş bir generate Taproot Address oluşturabilirsiniz. Bu durumda, yapının gerekliliklerini yerine getirmek için _script path_ için harcanamayan bir komut dosyası oluşturmak gerekir. Daha sonra $t$ ince ayarı, dahili açık anahtar $P$ üzerinde etiketlenmiş bir Hash işlevi olan **`TapTweak`** uygulanarak hesaplanır:



$$

t = \text{H}_{\text{TapTweak}}(P)

$$


nerede?



- $\text{H}_{\text{TapTweak}}$, `TapTweak` etiketiyle etiketlenmiş bir SHA256 Hash işlevidir. Etiketli bir Hash işlevinin ne olduğunu bilmiyorsanız, sizi bölüm 3.3'e bakmaya davet ediyorum;
- p$, yalnızca $x$ koordinatını kullanarak sıkıştırılmış 256 bit biçiminde temsil edilen dahili genel anahtardır.


Taproot açık anahtarı $Q$ daha sonra eliptik eğri üreteci $G$ ile çarpılan ince ayar $t$'nin dahili açık anahtar $P$'ye eklenmesiyle hesaplanır:



$$

Q = P + t \cdot G

$$


Taproot açık anahtarı $Q$ elde edildiğinde, karşılık gelen alıcı Address'yi generate yapabiliriz. Diğer formatların aksine, Taproot adresleri açık anahtarın bir Hash'u üzerine kurulmaz. Bu nedenle, $Q$ anahtarı ham bir şekilde doğrudan Address'ye eklenir.


Başlangıç olarak, sıkıştırılmış bir açık anahtar elde etmek için $Q$ noktasının $x$ koordinatını çıkarırız. Bu yük üzerinde, SegWit v0 adreslerinde olduğu gibi BCH kodları kullanılarak bir sağlama toplamı hesaplanır. Ancak, Taproot adresleri için kullanılan program biraz farklıdır. Gerçekten de, SegWit ile _bech32_ formatının tanıtılmasından sonra, bir hata keşfedildi: bir Address'un son karakteri bir `p` olduğunda, bu `p`den hemen önce `q` eklemek veya kaldırmak sağlama toplamını geçersiz kılmaz. Bu hatanın SegWit v0 üzerinde bir sonucu olmamasına rağmen (boyut kısıtlaması sayesinde), gelecekte bir sorun teşkil edebilir. Bu nedenle bu hata Taproot adresleri için düzeltilmiştir ve yeni düzeltilmiş format "_bech32m_" olarak adlandırılmıştır.


Taproot Address, $Q$'nun $x$ koordinatının _bech32m_ formatında aşağıdaki Elements ile kodlanmasıyla oluşturulur:



- **HRP (_İnsan Tarafından Okunabilir Bölüm_)**: ana Bitcoin ağını belirtmek için `bc`;
- **Sürüm**: gW-637 / SegWit v1'i belirtmek için `1`;
- **Sağlama toplamı**.


Bu nedenle nihai Address şu formata sahip olacaktır:


```
bc1p[Qx][checksum]
```


Öte yandan, dahili ortak anahtarla (_script path_) harcama yapmanın yanı sıra alternatif komut dosyaları eklemek isterseniz, alınan Address'in hesaplanması biraz farklı olacaktır. Alternatif komut dosyalarının Hash'ünü ince ayar hesaplamasına dahil etmeniz gerekecektir. Taproot'de, Merkle Tree'ın sonunda bulunan her alternatif komut dosyası "yaprak" olarak adlandırılır.


Farklı alternatif komut dosyaları yazıldıktan sonra, bunları bazı meta verilerle birlikte etiketlenmiş bir Hash işlevi olan `TapLeaf` üzerinden ayrı ayrı geçirmeniz gerekir:



$$

\text{h}_{\text{leaf}} = \text{H}_{\text{TapLeaf}} (v \Vert sz \Vert S)

$$


Ile:



- $v$: kod sürüm numarası (Taproot için varsayılan `0xC0`);
- $sz$: _CompactSize_ biçiminde kodlanmış betiğin boyutu;
- $S$: senaryo.


Farklı komut dosyası karmaları ($\text{h}_{\text{leaf}}$) önce leksikografik sıraya göre sıralanır. Daha sonra bunlar çiftler halinde birleştirilir ve `TapBranch` etiketli bir Hash fonksiyonundan geçirilir. Bu işlem, adım adım Merkle Tree oluşturmak için yinelemeli olarak tekrarlanır:

$$

\text{h}_{\text{branch}} = \text{H}_{\text{TapBranch}}(\text{h}_{\text{leaf1}} \Vert \text{h}_{\text{leaf2}})

$$


Daha sonra, Merkle Tree kökünü elde edene kadar sonuçları ikişer ikişer birleştirerek ve her adımda `TapBranch` etiketli Hash işlevinden geçirerek devam ediyoruz:


![CYP201](assets/fr/066.webp)


Merkle Root $h_{\text{root}}$ hesaplandıktan sonra, ince ayarı hesaplayabiliriz. Bunun için, Wallet $P$'nin dahili açık anahtarını $h_{\text{root}}$ kökü ile birleştirir ve ardından tümünü etiketli Hash işlevi `TapTweak` üzerinden geçiririz:



$$

t = \text{H}_{\text{TapTweak}}(P \Vert h_{\text{root}})

$$


Son olarak, daha önce olduğu gibi, Taproot açık anahtarı $Q$, dahili açık anahtar $P$'nin $t$ ile üreteç noktası $G$'nin çarpımına eklenmesiyle elde edilir:



$$

Q = P + t \cdot G

$$

Ardından, Address'ün oluşturulması, bazı ek meta verilerle birlikte yük olarak ham açık anahtar $Q$ kullanılarak aynı süreci izler.


Ve işte bu kadar! CYP201 kursunun sonuna geldik. Bu kursu faydalı bulduysanız, aşağıdaki değerlendirme bölümünde iyi bir puan vermek için birkaç dakikanızı ayırabilirseniz çok minnettar olurum. Ayrıca sevdiklerinizle veya sosyal ağlarınızda paylaşmaktan çekinmeyin. Son olarak, bu kurs için diplomanızı almak istiyorsanız, değerlendirme bölümünden hemen sonra final sınavına girebilirsiniz.

# Son Bölüm

<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>


## Yorumlar & Derecelendirmeler

<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>

<isCourseReview>true</isCourseReview>

## Final Sınavı

<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>

<isCourseExam>true</isCourseExam>

## Sonuç

<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

<isCourseConclusion>true</isCourseConclusion>