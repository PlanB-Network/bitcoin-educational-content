---
name: Bitcoin Programlama
goal: Sıfırdan eksiksiz bir Bitcoin kütüphanesi oluşturun ve Bitcoin'in kriptografik temellerini anlayın
objectives: 

 - Python'da sonlu alan aritmetiği ve eliptik eğri işlemlerini uygulama
 - Bitcoin işlemlerini programlı olarak oluşturma ve ayrıştırma
 - Testnet adresleri oluşturun ve işlemleri ağ üzerinden yayınlayın
 - Bitcoin'ün güvenlik modelinin altında yatan matematiksel temellere hakim olma

---
# Bitcoin'ün Senaryo ve Programlarına Bir Yolculuk


Jimmy Song tarafından verilen bu iki günlük yoğun kurs, sıfırdan eksiksiz bir Bitcoin kütüphanesi oluşturarak sizi Bitcoin'in teknik temellerinin derinliklerine götürür. Sonlu alanlar ve eliptik eğrilerin temel matematiği ile başlayarak, işlem ayrıştırma, komut dosyası yürütme ve ağ iletişimi yoluyla ilerleyeceksiniz. Jupyter not defterlerindeki uygulamalı kodlama alıştırmaları sayesinde kendi testnet adresinizi oluşturacak, işlemleri manuel olarak oluşturacak ve doğrudan ağa yayınlayacaksınız; tüm bunları yaparken Bitcoin'i güvenli ve güvenilmez kılan kriptografik ilkeler hakkında derin bir anlayış kazanacaksınız.


Yolculuğun tadını çıkarın!


+++

# Giriş


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Kursa Genel Bakış


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Sizi sonlu alan aritmetiğinden Bitcoin'nın Testnet'sinde gerçek işlemler oluşturmaya ve yayınlamaya kadar götüren yoğun bir yolculuk olan PRO 202 _**Bitcoin Programlama**_ kursuna hoş geldiniz.


Bu eğitimde, Python'da aşamalı olarak bir Bitcoin kütüphanesi oluştururken, Bitcoin'in güvenliği ve iç işleyişi hakkında tam olarak akıl yürütmek için gerekli kriptografik, protokol ve yazılım temellerini edineceksiniz. PRO 202 yaklaşımı tamamen uygulamalıdır: her kavram hemen Jupyter not defterlerinde uygulanarak teori ve kodun birbirini güçlendirmesi sağlanır.


### Bitcoin için Temel Matematiksel Kavramlar


Bu ilk bölüm vazgeçilmez matematiksel altyapıyı oluşturmaktadır. ECDSA için ön koşullar olan sonlu alan aritmetiği ve eliptik eğri işlemlerini (grup yasası, toplama, ikiye katlama, skaler çarpma...) uygulayacaksınız. Amaç iki yönlüdür: kriptografik imzaları mümkün kılan cebirsel yapıyı anlamak ve bunları manipüle etmek için güvenilir Python araçları oluşturmak.


Daha sonra ECDSA'nın bileşenlerini resmileştireceksiniz: anahtar üretimi, nokta biçimlendirme, karma, imza oluşturma ve doğrulama. Bu bölüm, uygulama ayrıntılarını ve temel güvenlik modelinin sağlamlığını vurgulayarak teoriyi doğrudan uygulamaya bağlar.


### Bitcoin İşlem İç Çalışmaları


İkinci bölümde, bir Bitcoin işleminin yapısını inceleyeceksiniz: UTXO'lar, girişler/çıkışlar, diziler, komut dosyaları, kodlamalar ve daha fazlası. İşlemleri oluşturmak, imzalamak ve doğrulamak için kod yazacak ve hash tarafından neyin neden taahhüt edildiğini kesin bir şekilde anlayacaksınız.


Daha sonra, minimal bir _Script_ yürütücüsü uygulayacak, temel işlem kodlarını gözden geçirecek ve harcama yollarını doğrulayacaksınız. Amaç, işlem davranışını denetleyebilmenizi, doğrulama hatalarını teşhis edebilmenizi ve harcama politikalarının güvenliği hakkında muhakeme yapabilmenizi sağlamaktır.


### Bitcoin Ağ İç Çalışmaları


Üçüncü bölümde, işlemleri daha geniş bir sistem içine yerleştireceksiniz: blok yapısı, başlıklar, zorluk ve Proof-of-Work mekanizması. Protokol mesajlarını, blok başlıklarını ve Merkle ağaçlarını ele alacaksınız.


Son olarak, eşler arası düğüm iletişimi, mesaj optimizasyonu ve SegWit'ün tanıtımı üzerinde çalışacaksınız.


Plan ₿ Academy ile ilgili her kursta olduğu gibi, son bölüm anlayışınızı pekiştirmek için tasarlanmış bir değerlendirme içerir. Bitcoin'nın iç işleyişini ortaya çıkarmaya ve ona güç veren kodu yazmaya hazır mısınız? Haydi başlayalım!










# Bitcoin için Temel Matematiksel Kavramlar

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Bitcoin Uygulaması için Matematik

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin Programlama Temelleri: Temel Matematiksel Yapılar


Bu kurs, Bitcoin'in kriptografik sistemlerinin arkasındaki temel matematiği son derece pratik bir iş akışına dönüştürmektedir. Kavramlar açıklanır, örneklerle gösterilir ve ardından Jupyter Notebook'ta uygulanır. Rehber fikir basittir: bir kriptografik ilkeli ancak kodladığınızda gerçekten anlarsınız. İki gün boyunca öğrenciler generate testnet adreslerini kullanacak, işlemleri oluşturacak ve yayınlayacak ve sonunda blok kaşifleri olmadan ağ ile etkileşime gireceklerdir. Tüm bunlar sonlu alanlar ve eliptik eğriler konusunda sağlam bir temel gerektirir.


### Sonlu Alanlar: Kriptografinin Aritmetik Motoru


Sonlu bir F(p) alanı, bir p asal sayısı tarafından tanımlanan ve 0 ile p-1 arasındaki elemanları içeren bir aritmetik sistemdir. Asal alanlar, sıfır olmayan her elemanın bir tersinin olmasını ve tüm işlemlerin alan içinde kalmasını sağlar. Aritmetik, toplama, çıkarma ve çarpma işlemleri için modulo p'yi kullanır. Python'un `pow(base, exp, mod)` özelliği, gerçek kriptografik işlemlerde kullanılan büyük üsler için çok önemli olan verimli modüler üs alma sağlar.


#### Çarpımsal Davranış

Sıfır olmayan herhangi bir k elemanını bir asal alanın tüm elemanlarıyla çarpmak, alanın bir permütasyonunu üretir. Bu özellik tekdüzeliği garanti eder ve yapısal zayıflıkları önleyerek asal alanları güvenli anahtar üretimi ve dijital imzalar için ideal hale getirir.


#### Bölme ve Fermat'ın Küçük Teoremi

Bölme işlemi çarpımsal tersler aracılığıyla gerçekleştirilir. Fermat'ın Küçük Teoremi şunu belirtir

n^(p-1) ≡ 1 (mod p),

yani tersi n^(p-2)'dir. Python bunu doğrudan `pow(n, -1, p)` ile destekler. Bu işlemler ECDSA ve Bitcoin'nin temel şifreleme rutinlerinde sürekli olarak görülür.


### Eliptik Eğriler: Açık Anahtar Güvenliği için Doğrusal Olmayan Yapılar


Eliptik eğriler y² = x³ + ax + b denklemini takip eder. Bitcoin, sonlu bir alan üzerinde y² = x³ + 7 olarak tanımlanan secp256k1'i kullanır. Eliptik bir eğri üzerindeki noktalar, nokta toplama altında matematiksel bir grup oluşturur. İki P ve Q noktasından çizilen bir doğru eğriyi üçüncü bir R noktasında keser; R'yi x ekseni boyunca yansıtmak P + Q'yu verir. Bu sistem birleşimseldir ve bir kimlik elemanı içerir: sonsuzdaki nokta.


Bir noktanın iki katına çıkarılması sekant doğrusu yerine teğet doğrusu kullanır ve eğim eğrinin türevinden elde edilir. Bu formüller reel sayılar üzerinden hesaplamayı içermesine rağmen, eğri sonlu bir alan üzerinde tanımlandığında (Bitcoin'te kullanılan bağlam) tamamen ayrık ve kesin hale gelirler.


### Matematikten Bitcoin Kriptografisine


Sonlu alanlar deterministik, tersine çevrilebilir aritmetik sağlar; eliptik eğriler ise k-P hesaplamanın kolay olduğu ancak tersine çevirmenin hesaplama açısından mümkün olmadığı doğrusal olmayan bir yapı sağlar. Her ikisini birleştirmek Bitcoin'nın açık/özel anahtarları, ECDSA imzaları ve işlem güvenliği için temel oluşturur. Bu temelleri anlamak, öğrencileri soyutlamalar veya harici araçlar olmadan doğrudan anahtarları, işlemleri ve imzaları uygulamaya hazırlar.


## Eliptik Eğri Kriptografisi

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Bu bölümde sonlu alanlar üzerinde tanımlanan eliptik eğriler tanıtılmakta ve neden Bitcoin'nin kriptografisinin matematiksel omurgasını oluşturdukları açıklanmaktadır. Gerçek sayılar üzerindeki eliptik eğriler pürüzsüz ve sürekli görünürken, aynı denklemleri sonlu bir alan üzerinde uygulamak ayrık, dağınık bir nokta kümesi oluşturur. Görsel farklılığa rağmen, tüm nokta ekleme formülleri, eğimler ve cebirsel kurallar tamamen aynı şekilde davranır, sadece aritmetik modüler aritmetiğe dönüşür. Bitcoin, kriptografik güvenlik için gerekli olan simetriyi ve doğrusal olmayan davranışı koruyan y² = x³ + 7 (secp256k1) eğrisini kullanır.


### Noktaların Doğrulanması ve Sonlu Alan Uygulaması


F₁₃₇ üzerinde (73,128) gibi bir noktanın doğrulanması, y² mod p'nin x³ + 7 mod p'ye eşit olduğunun kontrol edilmesini gerektirir. Bunu kodda uygulamak, sonlu alan elemanları ve eğri noktaları için sınıflar oluşturmayı içerir. Operatör aşırı yüklemesi, tüm aritmetik işlemlerin (toplama, çarpma, üs alma, bölme) otomatik olarak modulo p olarak yapılmasını sağlar. Bu soyutlamalar mevcut olduğunda, daha gelişmiş kriptografik işlemlerin yazılması ve muhakeme edilmesi kolay hale gelir.


#### Grup Özellikleri ve Nokta Ekleme

Eliptik eğri noktaları toplama işlemi altında matematiksel bir grup oluşturur. Grup kapanma, birleşme, özdeşlik (sonsuzdaki nokta) ve tersleri (x ekseni boyunca yansıma) karşılar. Geometrik yapılar bu özellikleri doğrular ve skaler çarpımı (P'nin kendisine tekrar tekrar eklenmesi) iyi tanımlanmış hale getirir. Bu grup kuralları eliptik eğri kriptografisini mümkün kılar ve tekrarlanan nokta işlemleri altında tutarlı, öngörülebilir davranış sağlar.


### Devirli Gruplar ve Ayrık Logaritma Problemi


Bir eğri üzerinde bir G üreteç noktası seçmek, generate döngüsel bir grup oluşturmamızı sağlar: G, 2G, 3G, ..., nG = 0. Noktalar, sırayla üretildiklerinde bile doğrusal olmayan ve öngörülemez görünürler. Bu öngörülemezlik ayrık logaritma probleminin temelini oluşturur: P = sG'yi hesaplamak kolaydır, ancak P'den s'yi belirlemek büyük gruplar için hesaplama açısından olanaksızdır. Bu tek yönlü fonksiyon, açık anahtar kriptografisini güvenli kılan şeydir. Skaler (özel anahtarlar) küçük harfle, noktalar (açık anahtarlar) ise büyük harfle yazılır.


#### Verimli Skaler Çarpma

SG'yi verimli bir şekilde hesaplamak için, uygulamalar çift-ve-ekleme algoritmasını kullanır: skaler'in ikili gösterimini tarar, her adımda noktayı ikiye katlar ve yalnızca bit 1 olduğunda G'yi ekler. Bu, hesaplamayı O(n) eklemeden O(log n)'ye düşürür ve 256 bit skalerlerle bile pratik kriptografik işlemlere olanak tanır.


#### Bitcoin'da secp256k1 Eğrisi


Bitcoin, p = 2²⁵⁶ - 2³² - 977 olan bir asal alan üzerinde y² = x³ + 7 ile tanımlanan secp256k1 eğrisini kullanır. G üreteç noktası, deterministik bir NUMS ("nothing up my sleeve") prosedürü kullanılarak seçilen sabit koordinatlara sahiptir. Grup mertebesi n, 2²⁵⁶'ya yakın büyük bir asaldır ve sıfır olmayan her noktanın aynı grubu oluşturmasını sağlar. 2²⁵⁶'nın boyutu (~10⁷⁷) astronomik olarak büyüktür ve özel anahtarları kaba kuvvetle zorlamayı fiziksel olarak imkansız hale getirir. Bir trilyon yıl boyunca çalışan bir trilyon süper bilgisayar bile anahtar uzayını anlamlı bir şekilde azaltmayacaktır.


### Açık Anahtarlar, Özel Anahtarlar ve SEC Serileştirme


Özel anahtar rastgele bir s skaleridir; açık anahtar ise P = sG'dir. Ayrık log problemini çözmek mümkün olmadığından, P s açığa çıkmadan paylaşılabilir. Açık anahtarlar SEC formatı kullanılarak iletim için serileştirilmelidir. Sıkıştırılmamış SEC formatı 65 bayt kullanır: önek 0x04 + x-koordinatı + y-koordinatı. Sıkıştırılmış format sadece 33 bayt kullanır: 0x02 veya 0x03 öneki (y'nin paritesine bağlı olarak) + x-koordinatı. Bitcoin başlangıçta sıkıştırılmamış anahtarlar kullanıyordu ancak şimdi verimlilik için sıkıştırılmış olanları tercih ediyor.


#### Bitcoin Address Yaratılış


Bitcoin adresleri, ham anahtarların kendileri değil, açık anahtarların hash'leridir. Bir adresi generate yapmak için, açık anahtarı SEC biçiminde serileştirin, hash160 hesaplayın (SHA-256 ve ardından RIPEMD-160), ağ önekini ekleyin (mainnet için 0x00, testnet için 0x6F), çift SHA-256 kullanarak bir sağlama toplamı hesaplayın, ilk dört sağlama toplamı baytını ekleyin ve sonucu Base58 kullanarak kodlayın. Bu kodlama belirsiz karakterleri ortadan kaldırır ve transkripsiyon hatalarını önlemek için sağlama toplamını içerir. Çok adımlı işlem hattı, bir harcama gerçekleşene kadar açık anahtarı gizler, ağ tanımlaması ekler ve insan tarafından okunabilir, hataya dayanıklı adresler sağlar.


# Bitcoin İşlem İç Çalışmaları

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin İşlem Ayrıştırma ve ECDSA İmzaları

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### ECDSA'yı Anlamak: Bitcoin'un Dijital İmza Temeli


Bitcoin, RSA'dan çok daha küçük anahtar boyutlarıyla güçlü güvenlik sunan eliptik eğri tabanlı bir imza şeması olan ECDSA'ya dayanır. Güvenliği eliptik eğri ayrık logaritma probleminden gelir: P = eG verildiğinde, P'yi hesaplamak kolaydır, ancak P'den e'yi türetmek hesaplama açısından mümkün değildir. Bu asimetri, özel anahtarları güvende tutarken açık anahtar kriptografisini mümkün kılar.


#### ECDSA İmzalarının DER Kodlaması


Bitcoin, ECDSA imzalarını DER biçimini kullanarak kodlar:


- 0x30 (sıra işaretleyici)
- uzunluk bayt
- 0x02 + uzunluk + R bayt
- 0x02 + uzunluk + S bayt


Bu, 64 baytlık bir imzayı ~71-72 bayta genişleterek ek yük getirir. Taproot, sabit boyutlu Schnorr imzalarını benimseyerek bu verimsizliği ortadan kaldırır.


### İmza Taahhütleri ve İmza Süreci


ECDSA imzaları bir taahhüt denklemine dayanır: UG + VP = KG. İmzalayan kişi sıfır olmayan U ve V değerlerini ve rastgele bir nonce K seçerek özel anahtarı ifşa etmeden bildiğini kanıtlar. Mesaj Z'ye hash edilir, rastgele bir K üretilir, R KG'nin x-koordinatıdır ve S = (Z + RE)/K. İmza (R, S) çiftidir. Güvenlik kritik olarak benzersiz, öngörülemez bir K kullanılmasına bağlıdır - K yeniden kullanılırsa veya sızdırılırsa özel anahtar tehlikeye girer. Modern uygulamalar RNG hatalarını önlemek için deterministik K üretimi (RFC 6979) kullanır.


#### İmza Doğrulama

Z, (R, S) ve açık anahtar P verildiğinde, doğrulayıcı U = Z/S ve V = R/S hesaplar, ardından UG + VP'nin x koordinatının R'ye eşit olup olmadığını kontrol eder. Bu işe yarar çünkü doğrulama cebiri KG'yi özel anahtara ihtiyaç duymadan yeniden yapılandırır. İmzaların taklit edilmesi için ayrık log probleminin çözülmesi ya da hash fonksiyonunun kırılması gerekir.


#### Schnorr İmzaları ve Tarihsel Bağlam


Schnorr imzaları matematiksel olarak daha temizdir ve birleştirme özelliklerini destekler, ancak Bitcoin piyasaya sürüldüğünde patentliydi. ECDSA daha karmaşık ve daha büyük imzalara sahip olsa da ücretsiz bir alternatif sunuyordu. Patentlerin süresinin dolmasıyla birlikte Bitcoin, Taproot aracılığıyla Schnorr imzalarını ekleyerek sabit 64 baytlık imzalar ve gelişmiş gizlilik sağladı. ECDSA eski uyumluluk için desteklenmeye devam etmektedir.



### İşlem Yapısı ve Girdiler/Çıktılar


Bir Bitcoin işlemi şunlardan oluşur:


- sürüm (4 bayt, little-endian)
- giriş listesi
- çıktı listesi
- locktime (4 bayt)


Girdiler, işlem karmaları ve çıktı indekslerine göre önceki UTXO'lara referans verir ve bir kilit açma komut dosyası (scriptSig) ve zaman kilitleri veya RBF için kullanılan bir sıra numarası içerir. Çıktılar, harcama koşullarını tanımlayan miktarı (8 bayt) ve kilitleme komut dosyasını (scriptPubKey) belirtir. Bitcoin adresleri bu komut dosyalarının temsilleridir.


#### UTXO Modeli

Bitcoin hesap bakiyeleri yerine harcanmamış çıktıları izler. UTXO'lar tamamen harcanmalıdır - kısmi harcama mümkün değildir. 100 BTC'lik bir UTXO'den 1 BTC harcamak için, bir işlem bir değişim çıktısı içermelidir. Değişim çıktısının unutulması, kalanı madenci ücretine dönüştürür.


#### İşlem Serileştirme ve Ayrıştırma


İşlemler kompakt bir ikili format kullanır. Sürüm alanından sonra, bir varint girdi sayısını kodlar. Girdiler şunları içerir:


- önceki tx hash (32 bayt)
- çıktı indeksi (4 bayt)
- scriptSig (varstr)
- dizi (4 bayt)


Çıktılar 8 baytlık bir miktar ve scriptPubKey (varstr) içerir. Locktime, işlemin ne zaman geçerli olacağını kontrol eder. Serileştirme, çoğu tamsayı için little-endian sıralamasını kullanır. Ayrıştırıcılar baytları sırayla tüketir ve girdiler, çıktılar ve komut dosyaları için özel sınıflara temsilci atar.


### Ücretler, Değişim ve Şekillendirilebilirlik


Ücretler örtülüdür:

ücret = toplam(girdi değerleri) - toplam(çıktı değerleri).

Atanmamış herhangi bir değer ücret haline gelir, bu da doğru değişiklik çıktısı yapısını gerekli kılar. SegWit'den önce, imzalar değiştirilebilirliğe izin veriyordu - S'yi N-S olarak değiştirmek farklı bir ID'ye sahip yeni bir geçerli işlem üretiyordu. Bitcoin artık düşük S kuralını uyguluyor ve SegWit imzaları txid hesaplamasından izole ederek kimlikleri kararlı hale getiriyor ve Lightning gibi ikinci katman protokollerini mümkün kılıyor.


## Bitcoin Komut Dosyası ve İşlem Doğrulama

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script, coinlerin nasıl harcanabileceğini tanımlayan küçük, yığın tabanlı bir akıllı sözleşme dilidir. Her çıktı bir scriptPubKey (kilitleme komut dosyası) ve her girdi bir scriptSig (kilit açma komut dosyası) taşır. Birlikte, harcamanın geçerli olması için "doğru" olarak değerlendirilmesi gereken bir program oluştururlar. Komut dosyası kasıtlı olarak Turing-tamamlayıcı değildir, böylece tüm yürütme yolları öngörülebilir ve ağ genelinde doğrulanması kolaydır.


### Komut Dosyası İşlemleri ve Yürütme Modeli


Kod, veri öğeleri ve işlem kodlarından oluşan bir dizidir. Veri itmeleri (imzalar, açık anahtarlar, karmalar) yığına yerleştirilirken, `OP_` ile başlayan işlem kodları yığını dönüştürür. Yürütmeden sonra, başarı için en üst yığın öğesinin sıfırdan farklı olması gerekir. Örnekler: gW-58` üst öğeyi çoğaltır, `OP_HASH160` SHA256 ve ardından RIPEMD160 uygular ve `OP_CHECKSIG` işlemin sighash'ına ve bir genel anahtara karşı bir imzayı doğrular, geçerli için 1, geçersiz için 0 iter. Ayrıştırma kuralları ham veriler (uzunluk önekli) ve işlem kodları (bayt değerine göre bakılır) arasında ayrım yapar ve küçük bir sanal makine bunları her düğümde deterministik olarak yürütür.


### P2PK ve P2PKH: Temel Ödeme Kalıpları


En eski model olan Pay-to-Public-Key (P2PK), coinleri doğrudan tam bir açık anahtara kilitler: scriptPubKey `<pubkey> OP_CHECKSIG` ve scriptSig sadece bir imzadır. Basit ancak yer açısından verimsizdir ve madeni paralar harcanmadan önce açık anahtarı açığa çıkarır.


#### P2PKH ve Adresler

Pay-to-Public-Key-Hash (P2PKH), açık anahtarın 20 baytlık bir karmasına kilitlenerek bunu geliştirir. ScriptPubKey `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG` şeklindedir ve scriptSig `<signature> <pubkey>` sağlar. Yürütme, sağlanan açık anahtarın taahhüt edilen değerle hash edildiğini kontrol eder ve ardından imzayı doğrular. Bu, harcama zamanına kadar açık anahtarı gizler, boyutu azaltır ve tanıdık "1..." ile eşleşir mainnet adres formatı.


### İşlem Doğrulama ve İmza Hashing


Bir işlemi doğrulayan bir düğüm şunları sağlamalıdır:

1) Her girdi mevcut, harcanmamış bir çıktıya referans verir.

2) Toplam girdi değeri ≥ toplam çıktı değeri (aradaki fark ücrettir).

3) Her scriptSig, başvurulan scriptPubKey'in kilidini doğru şekilde açar.


İmza doğrulama, sighash olarak adlandırılan imzalanmış tam mesajın oluşturulmasını gerektirir. Eski ECDSA için, doğrulama tüm scriptSig'leri boşaltır, geçerli girdinin scriptSig'ini karşılık gelen scriptPubKey ile değiştirir, 4 baytlık bir hash türü (genellikle `SIGHASH_ALL`) ekler ve sonucu çift hash'ler. Bu 256 bitlik değer `OP_CHECKSIG`nın kullandığı değerdir. Alternatif hash türleri (örneğin, `SINGLE`, `NONE`, `ANYONECANPAY` ile veya `ANYONECANPAY` olmadan), işlemin hangi bölümlerinin taahhüt edildiğini değiştirerek, işbirlikçi finansman veya kısmen belirtilen işlemler gibi niş kullanım durumlarını mümkün kılar, ancak pratikte nadiren kullanılırlar.


#### Kuadratik Hashing ve SegWit

Eski bir işlemdeki her girdi, tüm girdileri içeren bir yapı üzerinde kendi sighash hesaplamasını gerektirdiğinden, doğrulama süresi girdi sayısı ile dört kat artabilir. Çok girdili büyük işlemler bir zamanlar fark edilir doğrulama gecikmelerine neden oluyordu. SegWit, paylaşılan parçaları önbelleğe almak ve karmaşıklığı doğrusal zamana indirmek için sighash hesaplamasını yeniden tasarlayarak ölçeklenebilirliği artırdı ve hizmet reddi saldırılarını zorlaştırdı.


### Komut Dosyası Bulmacaları ve Güvenlik Dersleri


Komut dosyası basit "bir imza bu paraların kilidini açar" ifadesinden çok daha fazlasını ifade edebilir Script bulmacaları bunu, doğru verileri sağlayan herkesin coinleri harcayabileceği keyfi koşulları (matematik problemleri, hash preimage zorlukları ve hatta çarpışma ödülleri) kodlayarak gösterir. Bununla birlikte, yalnızca herkese açık verilere (imza olmadan) dayanan çıktılar madencilerin önden çalıştırmasına karşı savunmasızdır: mempool'da geçerli bir çözüm göründüğünde, herhangi bir madenci bunu kopyalayabilir ve ödemeyi kendilerine yönlendirebilir.


Buradan çıkarılacak pratik ders, gerçek dünyadaki sözleşmelerin multisig, timelocks veya hashlocks gibi daha karmaşık mantıklar içerse bile neredeyse her zaman imza kontrolleri içermesidir. İmzalar çözümü belirli bir tarafa bağlayarak teşvikleri korur ve başkalarının ödemeyi çalmasını önler. Script'in yığın modelini, standart kalıplarını ve ince tuzaklarını anlamak, güvenli Bitcoin akıllı sözleşmeler tasarlamak ve işlemlerin ağ üzerinde gerçekte nasıl doğrulandığına dair akıl yürütmek için gereklidir.


## İşlem Oluşturma ve Senaryoya Ödeme Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Bitcoin İşlemleri ve P2SH'ün Oluşturulması


Bitcoin işlem yapısı, teorik protokol bilgisi ile pratik uygulama arasında köprü kurar. Bir işlem, harcanacak UTXO'ları seçer, kilitleme komut dosyalarıyla çıktılar oluşturur, her girdi için imzalar oluşturur ve her şeyi düğümlerin beklediği tam formatta serileştirir. Süreç, iç çekiş üretimini, Komut Dosyası davranışını ve doğru ücret ve değişiklik işlemlerini anlamayı gerektirir.


### Temel İşlem Yapısı


Her işlem girdisi, txid ve dizine göre önceki bir çıktıya referans verir. Çıktılar satoshi cinsinden miktarları ve kilitleme senaryolarını belirtir. Toplam girdiler ve toplam çıktılar arasındaki fark ücrettir. Bir girdiyi imzalamak için işlemin değiştirilmiş bir versiyonu serileştirilir, sighash'ı hesaplanır ve özel anahtar bunu imzalar. Ortaya çıkan imza ve açık anahtar ScriptSig'i oluşturur. Her girdi imzalandıktan sonra, ham işlem ağa yayınlanabilir.


### Çoklu İmza İşlemleri


Bare multisig, m-of-n imzaları gerektirmek için `OP_CHECKMULTISIG` kullanır. Erken bir hata nedeniyle, OP_CHECKMULTISIG fazladan bir yığın öğesi tüketir ve ScriptSig'de bir başlangıç `OP_0` gerektirir. Çıplak multisig işlevseldir ancak verimsizdir: tüm açık anahtarlar on-chain olarak görünür, bu da scriptPubKey'leri büyük, pahalı ve adres olarak kodlanması zor hale getirir. Bu sınırlamalar, script-hash'e ödeme yapılmasını motive etmiştir.


#### P2SH Mimarisi

P2SH karmaşık komut dosyalarını 20 baytlık bir HASH160'ın arkasına gizler. ScriptPubKey sabittir: `OP_HASH160 <20 baytlık karma> OP_EQUAL`. Multisig, zaman kilitleri veya diğer koşulları içeren temel redeem komut dosyası yalnızca harcama yapıldığında ortaya çıkar ve yürütülür. Gönderici sadece hash'i görür, alıcı ise redeem script'ini özel olarak yönetir. Bu tasarım on-chain boyutunu azaltır, gizliliği artırır ve göndericilere yük olmadan karmaşık sözleşmelere olanak sağlar.


### P2SH Harcama ve Uygulama


Bir P2SH çıktısı harcamak için, ScriptSig gerekli kilit açma verilerini *artı* kurtarma komut dosyasının kendisini içermelidir. Doğrulama iki adımda gerçekleşir:

1) HASH160(redeem_script), scriptPubKey hash'iyle eşleşmelidir.

2) Doğrulamadan sonra, redeem komut dosyası sağlanan verilerle yürütülür.


Bir P2SH girdisi için imza oluştururken, sighash işlemi scriptPubKey yerine redeem komut dosyasını kullanır. Her imzalayanın generate geçerli imzaları için tam redeem komut dosyasına sahip olması gerekir. P2SH adresleri mainnet'da ("3..." adresleri) 0x05 ve testnet'te ("2..." adresleri) 0xC4 sürüm baytını kullanır.


#### Pratik Güvenlik Hususları


Bir redeem scriptini kaybetmek fonları kaybetmek anlamına gelir: harcama için hem özel anahtarlar hem de redeem scriptinin kendisi gereklidir. Multisig katılımcıları para yatırma işlemlerini kabul etmeden önce açık anahtarlarının doğru şekilde dahil edildiğini doğrulamalıdır. P2SH multisig, timelocks ve hashlocks gibi gelişmiş yapıları destekler, ancak betik mantığındaki hatalar fonları kalıcı olarak kilitleyebilir, bu nedenle testnet üzerinde test yapmak çok önemlidir.


P2SH, ilk harcamaya kadar harcama koşullarını gizleyerek gizliliği artırır, ancak on-chain'da redeem komut dosyası göründüğünde, kalıcı olarak görünür hale gelir. Buna rağmen, küçültülmüş boyut, geriye dönük uyumluluk ve esnek sözleşme desteğinin faydaları P2SH'ü önemli bir kilometre taşı haline getirdi ve SegWit ve Taproot gibi daha sonraki yükseltmeleri etkiledi.


# Bitcoin Ağ İç Çalışmaları

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin Blokları ve Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Bitcoin blokları işlemleri gruplandırır ve proof of work kullanarak bunları güvence altına alır. Her blok 80 baytlık bir başlık ve işlemlerin bir listesini içerir. Geçerli bir blok üretmenin yüksek enerji maliyetine rağmen, bir bloğu doğrulamak ucuzdur: tüm ~900k başlıkları depolamak sadece ~72 MB gerektirir, bu da küçük cihazların bile zincirin proof of work'sini verimli bir şekilde doğrulamasına izin verir.


### Coinbase İşlemleri ve Blok Ödülleri


Her blok, yeni bitcoin'in dolaşıma girmesinin tek yolu olan tam olarak bir Coinbase işlemi ile başlar. Sıfırlanmış bir prev-tx hash ve 0xffffffff indeksine sahiptir, bu da onu benzersiz bir şekilde tanımlar. Sübvansiyon 50 BTC'den başlar ve her 210.000 blokta bir yarıya iner (50, 25, 12,5, 6,25, 3,125, ...). Madenciler işlem ücretlerini de dahil etmektedir. 4 baytlık nonce modern ASIC'ler için çok küçük olduğundan, madenciler Merkle kökünü değiştirmek ve ek arama alanı yaratmak için Coinbase işlemindeki verileri değiştirir. BIP34, her Coinbase txid'un benzersiz olmasını sağlamak için blok yüksekliğinin Coinbase scriptSig'ine gömülmesini gerektirir.


### Blok Başlık Alanları ve Soft Fork Sinyalleşmesi


80 baytlık başlık şunları içerir:


- sürüm (4 bayt)
- önceki blok karması (32 bayt)
- Merkle kökü (32 bayt)
- zaman damgası (4 bayt)
- bit (zorluk hedefi, 4 bayt)
- nonce (4 bayt)


Sürüm numaraları BIP9 aracılığıyla bir bit alanı sinyalizasyon sistemine dönüşerek madencilerin soft-fork hazırlığını koordine etmesine olanak sağlamıştır. Zaman damgası 32 bitlik bir Unix zaman değeridir ve 2106 yılı civarında güncellenmesi gerekecektir.


#### Bit Sahası ve Hedefler

Bit alanı hedefi kompakt biçimde kodlar: hedef = katsayı × 256^(üs-3). Geçerli blok karmaları sayısal olarak bu hedefin altında olmalıdır. Karmalar little-endian tamsayılar olarak yorumlandığından, geçerli karmalar hex olarak görüntülendiğinde genellikle sonda birçok sıfırla görünür.


### Zorluk, Doğrulama ve Ayarlamalar


Zorluk, en düşük_hedef / mevcut_hedef olarak tanımlanır ve mining'nin mümkün olan en kolay zorluğa kıyasla bugün ne kadar zor olduğunu ifade eder. Doğrulama için yalnızca başlığın hash'inin hedefle karşılaştırılması gerekir; bu da mining'ye göre son derece ucuzdur.


Her 2016 bloğunda, Bitcoin zorluğu ~10 dakikalık blok aralıklarını hedefleyecek şekilde ayarlar. Ayarlama, önceki 2016 blokları için gerçek süreyi beklenen iki hafta ile karşılaştırır. Sınırlar, ayarlamaları dört kat içinde kısıtlar. Çin'in mining yasağı gibi büyük gerçek dünya olayları, hash oranı keskin bir şekilde düştüğünde ve zorluk telafi etmek için aşağı doğru ayarlandığında bu mekanizmanın esnekliğini göstermiştir.


### Blok Sübvansiyon ve Toplam Supply


H yüksekliğindeki sübvansiyon şu şekilde hesaplanır: sübvansiyon = 5_000_000_000 >> (h // 210_000). Bu, ~21 milyon BTC'lik bir toplam arza yakınsayan yarılanma çizelgesini verir. Geometrik serilerin toplanması (50 + 25 + 12,5 + ...) × 210.000 üst sınırı açıklar. Madenciler izin verilen sübvansiyondan daha azını talep edebilir ancak daha fazlasını asla talep edemezler, aksi takdirde blok geçersiz hale gelir. Sübvansiyonlar birbirini izleyen yarılanmalarda azaldıkça, işlem ücretleri madenci gelirinin ve uzun vadeli ağ güvenliğinin giderek daha önemli bir bileşeni haline gelir.


## Ağ İletişimi ve Merkle Ağaçları

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Bitcoin Ağ Mimarisi


Bitcoin'nin eşler arası ağı, düğümlerin birbirlerine güvenmeden işlemleri ve blokları aktardığı merkezi olmayan bir dedikodu sistemi olarak çalışır. Yeni düğümler, çekirdek geliştiriciler tarafından tutulan sabit kodlu DNS tohumlarıyla iletişim kurarak önyükleme yapar. Bu DNS tohumları aktif eşlerin IP'lerini döndürerek düğümlerin ağı keşfetmesini ve ardından getaddr aracılığıyla ek eşler talep etmesini sağlar. Ağ oluşturma kasıtlı olarak mutabakat açısından kritik değildir, bu nedenle mutabakat kuralları değişmediği sürece uygulamalar farklılık gösterebilir.


### Mesaj Yapısı ve El Sıkışma


Tüm Bitcoin P2P mesajları sabit bir zarf kullanır: 4 baytlık bir sihirli değer (mainnet için F9BEB4D9), 12 baytlık bir ASCII komutu, 4 baytlık little-endian yük uzunluğu, 4 baytlık bir sağlama toplamı (hash256'nın ilk 4 baytı) ve yük. Yaygın komutlar arasında version, verack, inv, getdata, tx, block, getheaders, headers, ping ve pong bulunur.


El sıkışma, bir bağlantı düğümü bir sürüm mesajı gönderdiğinde başlar. Alıcı verack ve kendi versiyonu ile cevap verir. Her iki taraf da bu iki mesajı değiş tokuş ettiğinde, bağlantı aktif olur ve düğümler envanterleri ve verileri aktarmaya başlayabilir.


### Merkle Ağaçları ve Merkle Kökleri


Bitcoin, bloktaki tüm işlemlerin taahhüdü olarak her blok başlığında 32 baytlık tek bir Merkle kökü saklar. İşlemler hashlenir (hash256), eşleştirilir, birleştirilir ve bir hash kalana kadar tekrar tekrar hashlenir. Bir seviye tek sayıya sahip olduğunda, son hash çoğaltılır. Dahili olarak, hash'ler big-endian iken, serileştirilmiş blok verileri little-endian kullanır ve ağaç yapımından önce ve sonra tersine çevirme gerektirir.


#### Merkle Kanıtları ve SPV

Merkle kanıtları, tüm bloğu indirmeden bir işlemin bir bloğa dahil olduğunu doğrulamaya izin verir. İspat, köke giden yol boyunca kardeş hash'lerden oluşur. Hafif SPV istemcileri yalnızca blok başlıklarını depolar ve bu kanıtları tam düğümlerden talep eder. Bir Merkle ağacı logaritmik olarak büyüdüğünden, binlerce işlem içeren bir bloğa dahil olduğunu kanıtlamak yalnızca birkaç yüz bayt gerektirir.


Taproot bu konsepti, harcama koşullarını bir Merklize senaryo ağacına (MAST) işleyerek genişletir ve bir Merkle kanıtı ile birlikte yalnızca yürütülen dalı ortaya çıkarır. Bu hem verimliliği hem de gizliliği artırır.


### Ağ İşlemleri ve Blok Senkronizasyonu


Düğümler işlem veya blok talep etmek için getdata'yı kullanır ve bir tür kimliği (1=tx, 2=block, 3=filtrelenmiş blok, 4=kompakt blok) artı 32 baytlık bir tanımlayıcı belirtir. Zincir senkronizasyonu için düğümler başlangıç blok karması ile getheaders gönderir ve yanıt olarak 2000 adede kadar başlık alır. Dönen her başlık 80 bayttır ve ardından sıfırlık bir kukla işlem sayısı gelir.


Alınan blokların tam olarak doğrulanması iki kontrol gerektirir:

1. Blok karması, bit alanında kodlanan hedefin altında olmalıdır.

2. Tüm işlemlerden hesaplanan Merkle kökü (uygun endianness işleme ile) başlığın köküyle eşleşmelidir.


Bitcoin'ün "güvenme, doğrula" ilkesini yansıtacak şekilde, ancak her iki koşul da başarılı olursa bir düğüm bloğu kabul eder.


## Gelişmiş Düğüm İletişimi ve Ayrılmış Tanık

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Bu oturum, gelişmiş P2P ağını Segregated Witness ile birleştirerek modern Bitcoin yazılımının SegWit'ya duyarlı işlem yapılarını kullanırken düğümlerle nasıl doğrudan etkileşime girdiğini göstermektedir. Geliştiriciler blokları almayı, ilgili işlemleri taramayı ve yalnızca ham ağ iletişimini kullanarak işlemleri oluşturmayı öğrenirler - blok kaşifleri gerekmez.


### Blok Tabanlı İşlem Alma ve Gizlilik


Cüzdanlar, scriptPubKey'leriyle eşleşen çıktılar için blokları tarayarak gelen ödemeleri tespit etmelidir. Tüm blokları almak, gizliliği, kullanıcı etkinliği hakkında güçlü sinyaller sızdıran tek tek işlemleri talep etmekten daha iyi korur. Blok talepleri bile düşük hacimli zincirlerde bilgi sızdırabilir, bu da kompakt blok filtrelerini (BIP158) gizliliği koruyan hafif istemciler için gerekli hale getirir. Filtreler yanlış pozitifler üretebilir ancak asla yanlış negatifler üretmez ve istemcilerin belirli adresleri ifşa etmeden yalnızca potansiyel olarak ilgili blokları indirmesine olanak tanır.


### Trustless Ağ Etkileşimi


Get_block` iş akışı doğru ağ kullanımını gösterir: getdata gönder, bir blok al, ardından Merkle kökünü ve proof of work'u bağımsız olarak doğrula. Bir blok yalnızca alınan başlık hash'i istenen hash ile eşleşirse ve hesaplanan Merkle kökü başlıkla eşleşirse kabul edilir. Bu, kötü niyetli eşlerin bile düğümleri değiştirilmiş verileri kabul etmeleri için kandıramamasını sağlayarak "güvenme, doğrula" ilkesini somutlaştırır.


#### Bloklardan İşlemleri Alma

Bir bloğun işlemleri, basit yineleme kullanılarak eşleşen scriptPubKey'ler için taranabilir. Üretim cüzdanları, yeni bloklar geldikçe bunu sürekli olarak gerçekleştirir ve üçüncü taraf API'lere güvenmek yerine çıktıların sahipliğini kesinlikle kriptografik doğrulama yoluyla kanıtlar.


### SegWit Hedefler ve Tasarım


Segregated Witness (SegWit), imza verilerini txid hesaplamasından kaldırarak işlem hatalarını düzeltmiştir. Bu, önceden imzalanmış güvenilir işlem zincirlerini mümkün kılmış ve Lightning Network'i pratik hale getirmiştir. SegWit ayrıca "blok ağırlığı" kullanarak blok kapasitesini artırdı: eski düğümler hala ≤1 MB blokları görürken, yükseltilmiş düğümler tanık verileri dahil 4 MB'a kadar doğrulama yapıyor. Sürümlendirilmiş şahit programları (şimdiye kadar v0-v1) gelecekteki komut dosyası türleri için yapılandırılmış bir yükseltme yolu oluşturur.


#### P2WPKH (Yerel SegWit)


P2WPKH, eski P2PKH yapısını 22 baytlık bir komut dosyası ile değiştirir: OP_0 + push20 + hash160(pubkey). Harcama, imzayı ve pubkey'i ayrı bir tanık alanına taşır.


- SegWit öncesi düğümler: "anyone-can-spend" ifadesine bakın, geçerli olarak değerlendirin.
- SegWit sonrası düğümler: OP_0 + 20 bayt karmayı tanır ve tanık verilerini kullanarak doğrular.


Bu ayrıştırma işlenebilirliği düzeltir ve ücretleri azaltır. Tanık, bir varint sayısı ve ardından imza ve pubkey kullanır.


#### P2SH-P2WPKH (Geriye Dönük Uyumlu SegWit)


Eski cüzdanların SegWit adreslerine gönderilmesine izin vermek için P2WPKH komut dosyaları P2SH'e sarılabilir.


- scriptPubKey: standart P2SH hash160(redeemScript)
- scriptSig: redeemScript (P2WPKH programı)
- tanık: imza + pubkey


Doğrulama katmanları:

1. BIP16 öncesi düğümler redeemScript'i geçerli olarak kabul eder.

2. BIP16 sonrası düğümler bunu değerlendirerek OP_0 + hash'i yığında bırakır.

3. SegWit düğümleri tam tanık doğrulaması gerçekleştirir.


#### Karmaşık Komut Dosyaları için P2WSH


P2WSH, hash160 yerine SHA256(script) işleyerek SegWit'i multisig ve gelişmiş komut dosyaları için genelleştirir. Tipik bir 2-of-3 multisig tanık yığını:


- boş eleman (CHECKMULTISIG hatası)
- sig1
- sig2
- tanık betiği (multisig betiği)


SegWit düğümleri SHA256(witnessScript)'in scriptPubKey hash'iyle eşleştiğini doğrular ve ardından yürütür. SHA256 ve 32 baytlık bir karma kullanılması P2WSH'nin P2WPKH'dan ayırt edilmesini sağlar ve güvenliği güçlendirir.


#### P2SH-P2WSH (Maksimum Uyumluluk)


Karmaşık SegWit komut dosyaları da P2SH ile sarılabilir:


- scriptSig: redeemScript (OP_0 + 32 bayt hash)
- tanık: imzalar + tanıkScript


Doğrulama, P2SH-P2WPKH'te olduğu gibi üç nesil kuraldan geçer. Bu sarmalayıcı, işlenebilirlik olmadan çoklu imzaya ihtiyaç duyan erken Lightning dağıtımları için gerekliydi. Günümüzde yerel P2WSH tercih edilse de, sarmalanmış form eski wallet sistemleri arasında uyumluluk sağlar.


### SegWit'nin Etkisi


SegWit sağlandı:


- kararlı işlem kimlikleri
- indirimli tanık verileri aracılığıyla daha düşük ücretler
- blok ağırlığı ile daha yüksek blok verimi
- eski düğümler için uyumluluk
- gW-149 ve gelecekteki uzantılar için temiz bir yükseltme yolu


Güvenilir ağ etkileşimi ile birlikte bu araçlar modern Bitcoin gelişiminin bel kemiğini oluşturmaktadır.



# Son Bölüm


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Yorumlar & Derecelendirmeler


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Sınavı


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Sonuç



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>