---
name: Boltzmann Hesaplayıcı
description: Entropi kavramını ve Boltzmann'ın nasıl kullanılacağını anlamak
---
![cover](assets/cover.webp)


***UYARI:** Samourai Wallet'in kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından KYCP.org web sitesine şu anda erişilememektedir. Python Boltzmann Calculator kodunu barındıran Gitlab da ele geçirilmiştir. Şu an itibariyle bu aracı indirmek artık mümkün değil. Ancak, kodun önümüzdeki haftalarda başkaları tarafından yeniden yayınlanması mümkündür. Bu arada, Boltzmann Hesaplayıcısının işleyişini anlamak için bu eğitimden yararlanabilirsiniz. Bu araç tarafından sağlanan göstergeler herhangi bir Bitcoin işlemi için geçerlidir ve manuel olarak da hesaplanabilir. Bu eğitimde gerekli tüm hesaplamaları sunacağım. Python aracını makinenize zaten indirdiyseniz veya bir RoninDojo kullanıyorsanız, aracı kullanmaya devam edebilir ve bu öğreticiyi her zamanki gibi takip edebilirsiniz, hala çalışıyor


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

Boltzmann Hesaplayıcı, diğer gelişmiş ölçütlerle birlikte entropi seviyesini ölçerek bir Bitcoin işlemini analiz etmek için kullanılan bir araçtır. Bir işlemin girdileri ve çıktıları arasındaki bağlantılar hakkında bilgi sağlar. Bu göstergeler, bir işlemin gizliliğinin niceliksel bir değerlendirmesini sunar ve olası hataların belirlenmesine yardımcı olur.


Bu Python aracı Samourai Wallet ve OXT ekipleri tarafından geliştirilmiştir, ancak herhangi bir Bitcoin işleminde kullanılabilir.


## Boltzmann Hesaplayıcı nasıl kullanılır?

Boltzmann Hesaplayıcısını kullanmak için iki seçeneğiniz vardır. Birincisi Python aracını doğrudan makinenize yüklemektir. Alternatif olarak, basitleştirilmiş bir kullanım platformu sunan KYCP.org (_Know Your Coin Privacy_) web sitesini tercih edebilirsiniz. RoninDojo kullanıcıları için, bu aracın zaten node'unuza entegre edildiğini unutmayın.


KYCP sitesini kullanmak oldukça kolaydır: analiz etmek istediğiniz işlem tanımlayıcısını (txid) arama çubuğuna girin ve `ENTER` tuşuna basın.

![KYCP](assets/1.webp)

Daha sonra, girdiler ve çıktılar arasındaki bağlantılar da dahil olmak üzere işlem hakkında farklı bilgiler bulacaksınız. `Deterministik bağlantılar` üzerine tıklayın.

![KYCP](assets/2.webp)

Boltzmann Hesaplayıcı göstergelerine ayrılmış sayfaya ulaşacaksınız.

![KYCP](assets/3.webp)

Aracı doğrudan RoninDojo düğümlerinden kullanmayı tercih edenler için, `RoninCLI > Samourai Toolkit > Boltzmann Calculator` üzerinden erişilebilir.


KYCP.org sitesinde olduğu gibi, Python aracı yüklendikten sonra, analiz etmek istediğiniz işlemin txid'sini yapıştırmanız yeterli olacaktır.


![KYCP](assets/7.webp)


Ardından, sonuçları almak için `ENTER` tuşuna basın.


![KYCP](assets/8.webp)


## Boltzmann Hesaplayıcısının göstergeleri nelerdir?

### Kombinasyonlar / Yorumlar:

Yazılımın hesapladığı ilk gösterge, araçta `nb kombinasyonları` veya `yorumlar` altında gösterilen toplam olası kombinasyon sayısıdır.


Bu gösterge, işlemde yer alan UTXO'ların değerlerini dikkate alarak, girdilerin çıktılarla ilişkilendirilebileceği yolların sayısını hesaplar. Başka bir deyişle, bir işlemi analiz eden harici bir gözlemcinin bakış açısından bir işlemin ortaya çıkarabileceği makul yorumların sayısını belirler.

Örneğin, Whirlpool 5x5 modeline göre yapılandırılmış bir CoinJoin `1,496` olası kombinasyon sunar: ![KYCP](assets/4.webp)

Bir Whirlpool Dalgalanma Döngüsü 8x8 CoinJoin ise `9,934,563` olası yorum sunar: ![KYCP](assets/5.webp)

Bunun aksine, 1 girdi ve 2 çıktıya sahip daha geleneksel bir işlem yalnızca tek bir yorumlama sunacaktır: ![KYCP](assets/6.webp)


### Entropi:

Hesaplanan ikinci gösterge, `Entropi` ile gösterilen bir işlemin entropisidir.


Genel kriptografi ve bilgi bağlamında entropi, bir veri kaynağı veya rastgele bir süreçle ilişkili belirsizliğin veya öngörülemezliğin nicel bir ölçüsüdür. Başka bir deyişle entropi, bilginin tahmin edilmesinin veya tahmin edilmesinin ne kadar zor olduğunu ölçmenin bir yoludur.


Zincir analizi bağlamında entropi, Shannon entropisinden türetilen ve Boltzmann aracıyla hesaplanan [LaurentMT tarafından icat edilmiştir] (https://gist.github.com/LaurentMT/e758767ca4038ac40aaf) bir göstergenin de adıdır.


Bir işlem çok sayıda olası kombinasyon sunduğunda, entropisine atıfta bulunmak genellikle daha önemlidir. Bu gösterge, analistlerin işlemin tam konfigürasyonu hakkındaki bilgi eksikliğinin ölçülmesini sağlar. Başka bir deyişle, entropi ne kadar yüksek olursa, analistler için girdiler ve çıktılar arasındaki Bitcoin hareketlerini belirleme görevi o kadar zorlaşır.


Uygulamada entropi, harici bir gözlemcinin bakış açısından, bir işlemin diğer harici veya dahili kalıpları ve sezgisel yöntemleri dikkate almaksızın yalnızca girdi ve çıktı miktarlarına dayalı olarak birden fazla olası yorum sunup sunmadığını ortaya koyar. Yüksek entropi daha sonra işlem için daha iyi gizlilik ile eş anlamlıdır.


Entropi, olası kombinasyonların sayısının ikili logaritması olarak tanımlanır. İşte kullanılan formül:

```plaintext
E: the entropy of the transaction
C: the number of possible combinations for the transaction

E = log2(C)
```


Matematikte, ikili logaritma (taban-2 logaritma) 2'nin üs alma işleminin tersine karşılık gelir. Başka bir deyişle, `x`in ikili logaritması, `x`i elde etmek için `2`nin yükseltilmesi gereken üsdür. Bu gösterge böylece bit cinsinden ifade edilir.


Whirlpool 5x5 modeline göre yapılandırılmış bir CoinJoin işlemi için entropiyi hesaplama örneğini ele alalım; bu işlem, daha önce de belirtildiği gibi, `1.496` sayıda olası kombinasyon sunmaktadır:

```plaintext
C = 1,496
E = log2(1,496)
E = 10.5469 bits
```

Dolayısıyla, bu CoinJoin işlemi `10.5469 bit`lik bir entropi gösterir ki bu çok tatmin edici olarak kabul edilir. Bu değer ne kadar yüksek olursa, işlem o kadar çok farklı yorumlamayı kabul eder ve böylece gizlilik seviyesini güçlendirir.

9,934,563` yorum içeren 8x8 CoinJoin işlemi için entropi şöyle olacaktır:

```plaintext
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bits
```


Bir girdi ve iki çıktı içeren daha geleneksel bir işlemle başka bir örnek verelim: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://Mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) Bu işlem durumunda, tek olası yorum şudur: `(In.0) > (Out.0 ; Out.1)`. Sonuç olarak, entropisi `0` olarak belirlenmiştir:

```plaintext
C = 1
E = log2(1)
E = 0 bits
```


### Verimlilik:

Boltzmann Hesaplayıcı tarafından sağlanan üçüncü gösterge `Wallet Verimliliği` olarak adlandırılmıştır. Bu gösterge, işlemin verimliliğini, aynı konfigürasyonda düşünülebilecek en uygun işlemle karşılaştırarak değerlendirir.


Bu da bizi, belirli bir işlem yapısının teorik olarak ulaşabileceği en yüksek entropiye karşılık gelen maksimum entropi kavramını tartışmaya yönlendirmektedir. İşlemin verimliliği daha sonra bu maksimum entropi ile analiz edilen işlemin gerçek entropisi karşı karşıya getirilerek hesaplanır.


Kullanılan formül aşağıdaki gibidir:

```plaintext
ER: the actual entropy of the transaction expressed in bits
EM: the maximum possible entropy for a given transaction structure expressed in bits
Ef: the efficiency of the transaction in bits

Ef = ER - EM
```


Örneğin, Whirlpool 5x5 tipi bir CoinJoin yapısı için maksimum entropi `10.5469` olarak belirlenmiştir:

```plaintext
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bits
```


Bu gösterge de yüzde olarak ifade edilir, formülü şu şekildedir:

```plaintext
CR: the actual number of possible combinations
CM: the maximum number of possible combinations with the same structure
Ef: the efficiency expressed as a percentage

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```


Dolayısıyla `%100` verimlilik, işlemin yapısına göre gizlilik potansiyelini en üst düzeye çıkardığını gösterir.


### Entropi Yoğunluğu:

Dördüncü gösterge, `Entropi Yoğunluğu` aracında belirtilen entropi yoğunluğudur. İşlemin her bir girdi veya çıktısına göre entropi hakkında bir bakış açısı sağlar. Bu gösterge, farklı boyutlardaki işlemlerin verimliliğini değerlendirmek ve karşılaştırmak için kullanışlıdır. Bunu hesaplamak için, işlemin toplam entropisini ilgili toplam girdi ve çıktı sayısına bölmeniz yeterlidir:

```plaintext
ED: the entropy density expressed in bits
E: the entropy of the transaction expressed in bits
T: the total number of inputs and outputs in the transaction

ED = E / T
```


Whirlpool 5x5 CoinJoin örneğini ele alalım:

```plaintext
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bits
```


Bir Whirlpool 8x8 CoinJoin için entropi yoğunluğunu da hesaplayalım:

```plaintext
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bits
```


### Boltzmann Skoru:

Boltzmann Hesaplayıcı tarafından sağlanan beşinci bilgi, girdiler ve çıktılar arasındaki eşleşme olasılıkları tablosudur. Bu tablo, Boltzmann skoru aracılığıyla, belirli bir girdinin belirli bir çıktı ile ilişkili olduğu koşullu olasılığı gösterir.


Bu nedenle, bir işlemdeki bir girdi ile bir çıktı arasındaki bir ilişkinin, bir dizi yorumda bu olayın olumlu gerçekleşme sayısının toplam olası gerçekleşme sayısına oranına dayanan koşullu olasılığının nicel bir ölçüsüdür.


Whirlpool CoinJoin örneğini tekrar ele alırsak, koşullu olasılıklar tablosu her bir girdi ve çıktı arasındaki bağlantı olasılığını vurgulayacak ve işlemdeki ilişkilerin belirsizliğinin nicel bir ölçüsünü sağlayacaktır:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Burada, her girdinin herhangi bir çıktı ile ilişkilendirilme şansının eşit olduğunu açıkça görebiliriz, bu da işlemin gizliliğini artırır.

Boltzmann skorunun hesaplanması, belirli bir olayın meydana geldiği yorumların sayısının mevcut yorumların toplam sayısına bölünmesini içerir. Böylece, 0 numaralı girdi ile 3 numaralı çıktıyı (`512` yorum) ilişkilendiren skoru belirlemek için aşağıdaki prosedür kullanılır:

```plaintext
Interpretations (IN.0 > OUT.3) = 512
Total Interpretations = 1496
Score = 512 / 1496 = 34%
```


Whirlpool 8x8 CoinJoin (dalgalanma döngüsü) örneğini ele alırsak, Boltzmann tablosu aşağıdaki gibi görünecektir:


|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

Ancak, tek bir girdi ve iki çıktıya sahip basit bir işlem söz konusu olduğunda durum farklıdır:


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Burada, her bir çıktının 0 numaralı girdiden kaynaklanma olasılığının `%100` olduğu görülmektedir. Dolayısıyla daha düşük bir olasılık, girdiler ve çıktılar arasındaki doğrudan bağlantıları seyrelterek daha fazla gizlilik anlamına gelir.


### Deterministik Bağlantılar:

Sağlanan altıncı bilgi, bu bağlantıların oranı ile tamamlanan deterministik bağlantıların sayısıdır. Bu gösterge, analiz edilen işlemdeki girdiler ve çıktılar arasındaki kaç bağlantının `%100` olasılıkla tartışılmaz olduğunu ortaya koymaktadır. Oran ise bu deterministik bağlantıların tüm işlem bağlantıları kümesi içindeki ağırlığına ilişkin bir perspektif sunmaktadır.

Örneğin, Whirlpool tipi bir CoinJoin işleminin deterministik bağlantıları yoktur ve bu nedenle bir gösterge ve `%0` oranı gösterir. Buna karşılık, incelenen ikinci basit işlemimizde (bir girdi ve iki çıktı ile), gösterge `2` olarak ayarlanır ve oran `%100`e ulaşır. Dolayısıyla, boş bir gösterge, girdiler ve çıktılar arasında doğrudan ve tartışılmaz bağlantıların olmaması nedeniyle mükemmel gizliliğe işaret etmektedir.


**Harici Kaynaklar:**



- Samourai üzerinde Boltzmann Kodu
- [Bitcoin İşlemleri ve Gizlilik (Bölüm I) Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Bitcoin İşlemleri ve Gizlilik (Bölüm II) Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Bitcoin İşlemleri ve Gizlilik (Bölüm III) Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- KYCP Web Sitesi
- [Laurent MT tarafından Boltzmann Senaryosuna Giriş Üzerine Medium Makalesi](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)