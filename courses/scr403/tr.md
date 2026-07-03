---
name: Simplicity'yi Derinlemesine İncelemek
goal: Simplicity'nin tasarım felsefesine, tip sistemine ve tam yaşam döngüsüne hâkim olmak
objectives:
  - Tam bir dili oluşturan üç temel bileşim yöntemini ve dokuz kombinatörü anlamak
  - Simplicity'nin minimal tip sisteminden Boole mantığı, aritmetik ve SHA-256 inşa etmek
  - Failure ve Reader yan etkilerinin gerçek blockchain etkileşimini nasıl mümkün kıldığını kavramak
  - Simplicity programlarının nasıl Taproot adreslerine dönüştüğünü ve tanık verisiyle nasıl harcandığını öğrenmek
---

# Simplicity'yi Derinlemesine İncelemek

Blockstream Research'te Simplicity'nin yaratıcısı olan [Dr. Russell O'Connor](https://r6.ca/) tarafından yazılan beş bölümlük eksiksiz ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) makale serisine dayanan, Simplicity dilinin ardındaki teori ve tasarım kararlarına derin bir bakış. Bu kurs, Simplicity'nin nasıl yazılacağını değil, *neden* bu şekilde tasarlandığını açıklar.

Kurs, Dr. O'Connor'ın makalelerini takip ederek hesaplamaları birleştirmenin üç temel yolunu, minimal tip sistemini ve onun tamlık teoremini, pratik veri tiplerinin ve aritmetiğin ilk ilkelerden inşasını, blockchain etkileşimi için yan etkilerin dikkatli biçimde dahil edilmesini ve nihayet programların adreslere nasıl taahhüt edilip zincir üzerinde nasıl harcandığını ele alır.

+++

# Giriş

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Kursa genel bakış

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

SCR403 — Simplicity'yi Derinlemesine İncelemek kursuna hoş geldiniz!

Bu kurs, [Blockstream](https://blockstream.com/) bünyesinde Altyapı Teknolojileri Geliştiricisi olan ve Simplicity'nin yaratıcısı [Dr. Russell O'Connor](https://r6.ca/) tarafından yazılan **"Delving Simplicity"** makale serisine dayanır. Özgün makaleler [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) forumunda yayımlanmıştır ve bu kurs için birincil kaynak materyali oluşturur. Bu eğitim içeriğini mümkün kılan öncü çalışmaları için kendisine minnettarız.

### Ne öğreneceksiniz

Bu kurs, Temmuz 2025'te [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) üzerinde etkinleştirilen yeni nesil betik dili Simplicity'nin ardındaki tasarım felsefesini ve matematiksel temelleri inceler. Beş bölümlük eksiksiz makale serisini takip eder ve iki ana içerik bölümünde yapılandırılmıştır:

1. **Simplicity'nin Temelleri** — Blockchain hesaplamasının neden temelde farklı bir dil gerektirdiği, işlemleri birleştirmenin üç yolu (sıralı, paralel, koşullu) ve matematiksel olarak tam bir dil oluşturan dokuz çekirdek kombinatör
2. **Veri Tiplerinden Programlara** — İlk ilkelerden Boole mantığı, aritmetik ve SHA-256 inşa etmek; blockchain etkileşimini mümkün kılan Failure ve Reader yan etkilerini anlamak; ve programların Commitment Merkle Root'lar aracılığıyla Taproot adreslerine nasıl taahhüt edildiğini ve tanık verisiyle nasıl harcandığını öğrenmek

### Ön koşullar

Bu, **uzman düzeyinde** bir kurstur (yaklaşık 10 saat). Şunlar konusunda rahat olmalısınız:
- Temel Bitcoin betik kavramları (işlem doğrulamasının ne yaptığı)
- Temel programlama kavramları (tipler, fonksiyonlar, bileşim)
- Matematiksel gösterime biraz aşinalık yararlıdır ancak şart değildir. Her şeyi ilerledikçe tanıtıyoruz

### Temel kaynaklar

- **Özgün makaleler**: Delving Bitcoin üzerinde Dr. Russell O'Connor tarafından yazılan ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary)
- **Simplicity deposu**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — kaynak kodu ve Rocq biçimsel ispatları
- **Resmî web sitesi**: [simplicity-lang.org](https://simplicity-lang.org/) — dokümantasyon ve SimplicityHL referansı
- **Blockstream blogu**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — teknik genel bakış

Bitcoin mühendisliğinin en zarif parçalarından birine dalmaya hazır mısınız? Başlayalım!

## Simplicity nedir?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Bu kursa Simplicity geçmişi olmadan geliyorsanız, derinlere dalmadan önce bu bölüm size yön verecek.

### Kısaca Simplicity

Simplicity, bugün Liquid Network üzerinde çalışan **Bitcoin'e özgü bir akıllı sözleşme dilidir**. İlk olarak 2012 civarında Dr. Russell O'Connor tarafından tasarlanmış ve 2017 tarihli *Simplicity: A New Language for Blockchains* makalesinde ayrıntılandırılmıştır; yıllar süren biçimsel doğrulama ve geliştirmenin ardından Temmuz 2025'te Liquid Network üzerinde etkinleştirilmiştir.

Turing-tam, yüksek seviyeli bir sözleşme dili olan Ethereum Solidity'sinden farklı olarak Simplicity kasıtlı biçimde minimaldir. Şunlara sahiptir:
- **Üç tip oluşturucu** (birim, toplam, çarpım)
- **Dokuz kombinatör** (temel işlemler ve bileşim kuralları)
- **Döngü yok, özyineleme yok, dinamik bellek yok**

Yalnızca bu ilkel öğelerden, Boole mantığından tam SHA-256 hash'lemeye kadar işlem doğrulaması için ihtiyaç duyduğunuz her hesaplamayı inşa edebilirsiniz.

### Bugün Simplicity ile ne yapabilirsiniz?

Simplicity hâlihazırda Liquid Network üzerinde gerçek uygulamaları çalıştırıyor. En dikkat çekeni, kullanıcıların USDt'yi teminat olarak kullanarak L-BTC üzerinde call opsiyonları alıp sattığı, oracle gerektirmeyen bir opsiyon piyasası olan [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/)tir (altta yatan sözleşme put opsiyonlarını da destekler). Diğer canlı Simplicity projeleri arasında SideSwap'in [Swaption](https://swaption.io/) ürünü (opsiyonlar) ve Resolvr tarafından geliştirilen açık kaynak [Deadcat](https://github.com/Resolvr-io/deadcat) (tahmin piyasaları) bulunur. DeFi'nin ötesinde Simplicity, Bitcoin Script'te imkânsız veya güvensiz olacak kasalar, covenant'lar ve karmaşık multisig şemaları gibi gelişmiş harcama koşullarını mümkün kılar.

### Bu kurs nedir — ve ne değildir

Bu, uygulamalı bir kodlama eğitimi **değildir**. Burada Simplicity programları yazmayacaksınız. Aradığınız buysa şunlara bakın:
- [simplicity-lang.org](https://simplicity-lang.org/) — resmî dokümantasyon ve yüksek seviyeli SimplicityHL dili
- [Simplicity GitHub deposu](https://github.com/BlockstreamResearch/simplicity) — referans uygulama, örnekler ve Rocq ispatları
- Başlamak üzerine [Blockstream blog yazısı](https://blog.blockstream.com/en-simplicity-github/)

Bu kursun konusu **şudur**: Simplicity'nin tasarımının ardındaki **felsefi ve teknik tercihler**. Bu dil neden bu şekilde oluşturuldu? Neden yalnızca dokuz kombinatör? Neden özyineleme yok? Tip sisteminin Gentzen'in sequent calculus'uyla bağlantılı olması neden önemlidir?

Bunu, araba sürmeyi öğrenmekten ziyade **motorun neden bu şekilde inşa edildiğini anlamak** olarak düşünün.

### Bu kurs kimler için?

Bu kurs şunlar için idealdir:
- Kod yazmadan önce Simplicity'nin temellerini anlamak isteyen **protokol geliştiricileri**
- Biçimsel doğrulama ve tip kuramsal yaklaşımla ilgilenen **Bitcoin araştırmacıları**
- Sequent calculus ile blockchain hesaplaması arasındaki bağlantıyı merak eden **bilgisayar bilimcileri**
- Liquid'in betik yeteneklerini yüzeysel anlayışın ötesinde kavramak isteyen **ileri düzey bitcoin kullanıcıları**

"Toplam tipleri", "kombinatörler" veya "sequent calculus" gibi terimler sizin için tamamen yeniyse endişelenmeyin; her şeyi sıfırdan açıklıyoruz. Ancak yoğun ve matematiksel bir yolculuğa hazır olun.

### Makalelerden kursa

Dr. O'Connor'ın özgün "Delving Simplicity" serisi beş teknik makale olarak yapılandırılmıştır. Bu kurs, o materyali, yol boyunca anlayışınızı sınayacak quizlerle birlikte ilerlemeli bir öğrenme yoluna yeniden düzenler ve açıklamalar ekler. Fikirler, tanımlar ve ispatlar ona aittir; biz formatı yapılandırılmış eğitim için uyarladık.

# Simplicity'nin Temelleri

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Hesaplamaları Birleştirmenin Temel Yolları

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Simplicity artık Liquid Network üzerinde etkinleştirildiğine göre, Simplicity dilinin felsefesine ve tasarımına derinlemesine dalmak istiyorum.

Bitcoin'in işlem doğrulaması, sıradan programlama dili tasarımından belirgin ölçüde farklı bir uygulamadır. Blok alanı maliyeti yüksek olduğundan programların kompakt olması gerekir. Bitcoin işlemlerindeki programlar yalnızca tek bir girdi üzerinde yürütülür ve herkes programı aynı girdi üzerinde yürütür. Ayrıca işlemi yetkilendiren taraf, hesaplamanın sonucunu önceden bilir: işlemin geçerli olduğunu.

Tipik olarak yetkilendiren taraf, işlemin geçerliliğine tanıklık eden tanık verisini türetmek için çok daha pahalı hesaplamalar çalıştırır; blockchain üzerinde çalışan programların ise tanık verisinin geçerliliğini kontrol etmesi gerekir. Geçerliliği kontrol etmek çoğu zaman geçerliliği ispatlamaktan çok daha ucuzdur.

Simplicity'yi bu tür benzersiz dil tasarımı zorluklarını göz önünde bulundurarak tasarladık. Örneğin Simplicity, yürütülmeyen dalların budanmasını ve blockchain üzerinde görünmemesini gerektirir. Ön işleme adımları, Simplicity programının boyutunda (yaklaşık) doğrusal zaman karmaşıklığı sergileyecek şekilde dikkatle tasarlanmıştır. Yürütme modelinin ayrıntılarının konsensüs açısından kritik hâle gelmemesi için, kodu önceden belirlenmiş bir biçimde yürütmeden hesaplanamayan "gas" yerine statik analiz kullanılır. Yürütme sırasında dinamik bellek ayırma yoktur. Ve benzeri.

Simplicity'nin tasarım ayrıntılarına dalmadan önce, bu seriye yeni işlevsellik oluşturmak için temel yapı taşlarını birleştirmenin genel yolları üzerine biraz programlama felsefesiyle başlamak istiyorum.

### Bileşim

Bitcoin gibi bir blockchain için programlanabilir işlemler dili tasarlandığını varsayalım. Özellikle, programlar yalnızca işlem verilerine ve girdilerin UTXO verilerine erişebilir; yürütme yalnızca işlem geçerliliğini belirler (bu da yürütme sonucunun önbelleğe alınmasına olanak tanır). Diyelim ki temel hesaplamalar yapmak, işlemden veri okumak ve/veya işlemek ve imza doğrulamak gibi çeşitli görevleri yerine getirebilen bir temel işlemler kümesiyle başlanıyor. Her işlem bir tür girdi (muhtemelen boş) tüketir ve bir tür çıktı döndürür. Bu temel işlemleri daha karmaşık işlemler hâline getirmenin yolları nelerdir?

### Sıralı Bileşim

![Sıralı Bileşim](assets/en/001.webp)

En temel bileşim yöntemi sıralı bileşimdir. İki temel işlemimiz varsa ve birinin çıktı veri tipi diğerinin girdi veri tipiyle eşleşiyorsa, bu iki işlemi yeni bir bileşik işlemde birleştirebiliriz. Bu yeni işlem, bu iki temel işlemi sırayla çalıştırır; ilk işlemin girdisini girdi olarak alır, bu ilk işlemin çıktısını ikinci işlemin girdisine geçirir ve nihayet ikinci işlemin çıktısını döndürür.

Elbette kendimizi yalnızca temel işlemleri birleştirmekle sınırlamamız gerekmez. Artık bazı bileşik işlemlerimiz olduğuna göre, bunları da fonksiyonel bileşim kullanarak birleştirebiliriz.

Matematikte bu sıralı bileşim çoğu zaman yalnızca "bileşim" olarak adlandırılır ve bunun şeyleri bileştirmenin tek yolu olduğu düşünülebilir. Ancak işlemleri bileştirmenin başka yolları da vardır.

### Paralel Bileşim

![Paralel Bileşim](assets/en/002.webp)

İki işlemimiz olduğunu varsayalım; bunlar temel veya karmaşık işlemler olabilir ve ikisi de aynı tipte girdiyi alır. Bu iki işlemi bileştirmenin ikinci temel yolu, ikisini de aynı girdi üzerinde yürütmektir. Buna paralel bileşim denir ve çıktı tipi, özgün işlemlerin çıktılarının tiplerinin "çarpımı"dır ve iki çıktının çiftini içerir.

Buna "paralel" bileşim dense de ve iki işlem ilke olarak paralel yürütülebilse de, paralel yürütme operasyonel bir gereklilik değildir. Paralel bileşimi, önce bir işlemi sonra ikinci işlemi yürüterek "sıralı" biçimde uygulayabiliriz. Çıktı aynı olduğu sürece paralel bileşimin nasıl uygulandığının ayrıntılarıyla ilgilenmeyiz.

### Koşullu Bileşim

![Koşullu Bileşim](assets/en/003.webp)

Koşullu bileşim, paralel bileşimin dualidir. Bu durumda aynı çıktıyı üreten iki işlemimiz vardır ve bunları yürütülecek olanı seçerek bileştiririz. Bu bileşik işlemin girdisi, özgün işlemlerin girdilerinin tiplerinin "toplamı" veya "etiketli birleşimi"dir. Bu örnekte "Left" veya "Right" etiketi, girdinin verisindeki tek bir bittir; hangi veri tipinin taşındığını ve dolayısıyla iki işlemden hangisinin yürütülebileceğini belirler.

Girdi iki özdeş tipin toplamı olduğunda bile koşullu bileşim aynı şekilde çalışır. Toplam tipi yine bir etiket içerir ve bu etiketin değeri iki işlemden hangisinin yürütüleceğini belirler.

### Bitcoin Script'te Bileşim

Bu üç tür bileşimi çeşitli programlama dillerinde gerçekleştirmenin birçok yolu vardır. Bitcoin Script'te sıralı bileşim, iki rutinin birleştirilmesiyle (yaklaşık olarak) gerçekleştirilir (Bitcoin Script'in birleştirmeli programlama dili olarak adlandırılmasının nedeni budur), çünkü bir rutinin çıktısı, sonraki rutin tarafından tüketilmek üzere stack üzerinde bırakılır. Paralel bileşim, iki rutinin aynı girdi üzerinde çalıştırılabilmesi için stack'i manipüle eden çoğaltma ve takas işlemlerinin kullanımıyla elde edilir. Tiplerin "çarpımı" dediğimiz şey tipik olarak birden çok stack öğesi kullanılarak gerçekleştirildiğinden işler tamamen basit değildir. Umarım genel fikri görebilirsiniz.

Koşullu bileşim ise elbette stack üzerindeki değere göre dallanan `OP_IF` ile gerçekleştirilir. Bu durumda en üstteki stack öğesi etiket rolünü oynar ve genellikle stack üzerindeki sonraki öğe veya öğeler, etiketin değerine bağlı olarak farklı "tiplerde" olur. Her durum için stack öğesi tipleri, `OP_IF` içindeki dallardan yalnızca biri tarafından işlenmeye uygun olabilir. Ancak `OP_ENDIF` noktasına ulaştıktan sonra stack öğeleri tutarlı bir "tipte" olmalıdır; böylece kalan betik daha önce hangi dalın alındığından bağımsız olarak ilerleyebilir.

### Simplicity'de Bileşim

Simplicity'yi, bu üç bileşim biçimini doğrudan uygulayan kombinatörlerle tasarladık. Çarpım ve toplam tipleriyle ilişkili diğer temel işlemleri destekleyen birkaç kombinatörle birlikte çekirdek Simplicity dili, herhangi bir sonlu hesaplamayı ifade etmeye yeterli dokuz kombinatörden oluşur. Bunu bir sonraki bölümde daha ayrıntılı ele alacağız.

### Dördüncü Bir Bileşim Türü

Bitirmeden önce, Bilgisayar Biliminde bulunan en az bir bileşim türü daha olduğunu belirtmeliyiz: "özyinelemeli bileşim". Özyinelemeli bileşimde bir işlem birden çok kez yinelenir.

Bitcoin Script'in özyinelemeli bileşimi desteklemediğini ve benzer şekilde, Simplicity'nin tasarımından sınırsız özyinelemeyi açıkça hariç tuttuğumuzu unutmayın. Tezimiz, sınırsız yinelemeli hesaplamanın birden çok işlem üzerinde hesaplama yapan recursive covenant'lar kullanılarak daha iyi uygulandığıdır. Bu, kullanıcıların blok alanı ve standardness kısıtlarından kaçınmasını ve işlem maliyetlerini daha iyi öngörmesini sağlar.

Bununla birlikte, Simplicity'nin delegasyon özelliğini kötüye kullanarak sınırsız özyinelemeli bileşime benzeyen bir şey sağlama yolları vardır; bunu bu serinin ilerleyen kısımlarında tartışabiliriz.

### Sonuç

Temel işlemleri karmaşık işlemlere dönüştürmek için üç ana bileşim biçimini gözden geçirdik:

- sıralı bileşim
- paralel bileşim
- koşullu bileşim

Bu bileşim biçimlerinin Bitcoin Script'te nasıl gerçekleştirildiğini tartıştık ve bunların Simplicity dilinin tasarımını nasıl etkilediğine işaret ettik. Dördüncü bileşim türü olan özyinelemeli bileşimin hem Simplicity'den hem de Bitcoin Script'ten özellikle hariç tutulduğunu belirttik.

Bir sonraki bölümde Simplicity dilinin çekirdeğini oluşturan dokuz kombinatörü, bunların bu üç bileşim biçimini doğrudan gerçekleştirmeye nasıl hizmet ettiğini ve bunun herhangi bir sonlu hesaplamayı tanımlamak için nasıl tam bir dil oluşturduğunu açıklayacağız.

## Simplicity'nin Kombinatör Tamlığı

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

Bu bölümde çekirdek Simplicity dilini tanıtıyor ve dilin tam olduğunu, yani herhangi bir sonlu hesaplamanın onun içinde ifade edilebildiğini gösteriyoruz.

### Simplicity Tipleri

Simplicity üç temel tip kurucusunu destekler. Çarpım tipi `A × B` paralel bileşim çıktılarını temsil ederken, toplam tipi `A + B` (etiketli birleşim) koşullu bileşim girdilerini ele alır. Üçüncü tip birim tipidir.

### Birim Tipi

`𝟙` veya `ONE` ile gösterilen birim tipi tam olarak bir değer içerir: boş demet `⟨⟩` veya `()`. Bu sıfır bitlik veri tipi bilgi taşımaz.

### Toplam Tipi

Bir toplam tipi `A + B`, "sol" veya "sağ" olduğunu gösteren etiketlerle iki tipi birleştirir. Değerler, sol etiketli değerler için `σᴸ(a)` veya `inl(a)`, sağ etiketli değerler için `σᴿ(b)` veya `inr(b)` olarak yazılır. Etiketler, özdeş tipler birleştirilirken bile ayrı kalır.

#### Boole Tipi

`𝟚` veya `TWO` ile gösterilen `𝟙 + 𝟙` tipi, iki değeri olan bir bitlik tipi temsil eder. Konvansiyon gereği `σᴸ⟨⟩` false/sıfırı, `σᴿ⟨⟩` ise true/biri temsil eder.

### Çarpım Tipi

Çarpım tipleri `A × B`, `⟨a, b⟩` veya `(a, b)` olarak yazılan değer çiftleri içerir. `𝟚 × 𝟚` tipi dört değere sahiptir; bunlar `𝟚 + 𝟚` içindeki dört değerden farklıdır.

### Çekirdek Simplicity İfadeleri

İşlemler `f : A ⊢ B` olarak gösterilir; bu, girdi tipinin `A` ve çıktı tipinin `B` olduğu anlamına gelir. Simplicity "first-order"dır — fonksiyon tipleri yoktur.

### İki Temel İşlem

Çekirdek dil iki temel işlem sağlar:

**Kimlik (`iden`).** Kimlik işlemi girdisini değiştirmeden geçirir:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Birim (`unit`).** Birim işlemi girdisini atar ve boş demeti döndürür:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Bunlar, tip başına bir işlem olacak şekilde aileler oluşturur.

### Üç Bileşim Kombinatörü

Sıralı bileşim `comp f g` kullanır (`f ⨾ g` veya `f >>> g` olarak yazılır):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Paralel bileşim `pair f g` kullanır (`f ▵ g` veya `f &&& g` olarak yazılır):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Koşullu bileşim, dalların paylaşılan `C` ortamına erişmesini sağlayan `case f g : (A + B) × C ⊢ D` kullanır:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Koşullu bileşim neden yalnızca bir dal seçen daha basit bir `copair f g : A + B ⊢ C` yerine bu biçimi — paylaşılan bir ortam `C` ile eşlenmiş bir toplamı — alır? Çünkü yalın bir `copair`, **dağıtımı** ifade edemez: paylaşılan bir girdiyi hangi dal alınırsa o dala iten `dist : (A + B) × C ⊢ A × C + B × C` fonksiyonunu. Simplicity, ortam `C`yi doğrudan `case` içine yerleştirerek tek bir kombinatörden hem koşullu bileşimi *hem de* dağıtımı elde eder — çekirdek dili dokuz kombinatörde tutan temel tasarım kararlarından biri budur.

### Dört Kombinatör Daha

Çarpım tüketimi `take` ve `drop` kullanır:

**take** sol öğeyi çıkarır:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** sağ öğeyi çıkarır:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Toplam üretimi `injl` ve `injr` kullanır:

**injl** sol etiketle sarar:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** sağ etiketle sarar:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Dokuz Çekirdek Kombinatör

Toplamda Simplicity tam olarak dokuz çekirdek kombinatöre sahiptir:

| Kombinatör | Amaç |
|---|---|
| `iden` | Girdiyi olduğu gibi geçirir |
| `unit` | Girdiyi atar |
| `comp` | Sıralı bileşim |
| `pair` | Paralel bileşim |
| `case` | Koşullu bileşim |
| `take` | Çarpımdan solu çıkarır |
| `drop` | Çarpımdan sağı çıkarır |
| `injl` | Toplamın soluna enjekte eder |
| `injr` | Toplamın sağına enjekte eder |

### Simplicity ve Sequent Calculus

Simplicity'nin tasarımı, Gentzen'in sequent calculus'unun konjonktif-disjonktif parçasından türetilir. Daha kesin olarak, sequent calculus'un *fonksiyonel yorumunun* bir varyantıdır; bu yorumun kendisi doğal çıkarım ile lambda calculus arasındaki Curry-Howard karşılıklılığına benzer. Kombinatör kuralları "öncüllerde sonuçlardan daha küçük tipler" sergiler; bu da Simplicity'nin soyut stack makinesi yorumlayıcısı olan Bit Machine'in yürütme sırasında veri kopyalamayı en aza indirmesine olanak tanır.

### Değerler İfade Değildir

Simplicity ifadeleri değerleri değil işlemleri belirtir. `scribe b : A ⊢ B` gösterimi, her zaman `b` değerini döndüren benzersiz bir ifadeyi temsil eder; bir kombinatör olmaktan ziyade gösterim kolaylığı sağlar. Bu, Bitcoin Script'te `OP_1` gibi işlemlerin değerleri doğrudan ifade etmek yerine stack'e itmesine benzer.

### Simplicity'nin Tamlık Teoremi

Dokuz kombinatörün tamamı elimizdeyken, bir şeyin eksik olmadığını — bu dokuzun gerçekten yeterli olduğunu — nasıl biliriz? Simplicity Tamlık teoremi buna cevap verir: (sonlu) Simplicity tipleri arasındaki herhangi bir fonksiyon için, onu gösteren bir Simplicity ifadesi vardır. İspat yapıcıdır — ifadenin nasıl inşa edileceğini gösterir:

1. **Girdiyi ayrıştırın**: İç içe `case` ifadeleri kullanarak, herhangi bir tipteki herhangi bir girdiyi bileşen bitlerine tamamen ayırın
2. **Bir arama tablosu inşa edin**: Her olası girdi için, karşılık gelen çıktıyı üretmek üzere `scribe` kullanın
3. **Birleştirin**: İç içe case'ler ve scribe'lar birlikte fonksiyonu uygulayan dev bir arama tablosu oluşturur

Bu teorem Rocq ispat yardımcısında (eski adıyla Coq) biçimsel olarak doğrulanmıştır. İspat resmî Simplicity deposunun parçasıdır ve doğruluğu makine tarafından kontrol edilmiştir.

Tamlık teoremi, Simplicity'nin dokuz kombinatörünün (sonlu) Simplicity tipleri arasındaki herhangi bir fonksiyonu ifade edebileceğini garanti etse de, arama tablosu inşasından çıkan ifadeler pratik olmayacak kadar büyüktür. 256 bitlik girdiler üzerinde bir fonksiyon, 2²⁵⁶ girişli bir arama tablosu gerektirir. Bu nedenle sonraki bölümler, her şeyi arama tabloları üzerinden kaba kuvvetle yapmak yerine hesaplamaların yapısından yararlanan verimli ifadeler inşa etmeye odaklanır.

### Sonuç

Simplicity'nin çekirdek dili, herhangi bir sonlu hesaplamayı mümkün kılan bir tip sistemi ve kombinatörler içerir. Tamlık teoremi ifade gücünü garanti etse de, genel inşadan çıkan ifadeler pratik olmayacak kadar büyüktür. Pratik Simplicity geliştirme, kısa ifadeler için hesaplama yapısından yararlanmayı içerir. Sonraki bölümler veri yapılarını, işlem etkileşimlerini ve ek kombinatörleri inceler.

# Veri Tiplerinden Programlara

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Veri Tipleri İnşa Etmek

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

Önceki bölümlerde, Simplicity'nin çekirdek kombinatör kümesinin herhangi bir sonlu saf hesaplamayı uygulamak için yeterli olduğunu gösterdik. Bu bölüm, tıpkı bilgisayarların mantık kapılarından inşa edilmesi gibi, bu ilkel öğelerden pratik veri yapılarının ve hesaplamaların nasıl inşa edileceğini gösterir.

### Boole Mantığı

`𝟚` ile gösterilen Boole tipi, `𝟙 + 𝟙`e eşittir ve iki değere sahiptir: `σᴸ⟨⟩` (false) ve `σᴿ⟨⟩` (true). Çekirdek kombinatörler kullanılarak Boole mantık operatörleri inşa edilebilir.

#### And İşlemi

Mantıksal `and : 𝟚 × 𝟚 ⊢ 𝟚` işlemi iki bit alır ve bir bit döndürür. Uygulama ilk bit üzerinde dallanır: false ise false döndürür; aksi hâlde ikinci biti döndürür.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

`⟨false, false⟩` ile test:

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

`⟨true, true⟩` ile test:

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### Diğer Mantık İşlemleri

`not` işlemi bir yardımcı kombinatör gerektirir:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

Başlangıçtaki `iden ▵ unit : A ⊢ A × 𝟙`, girdiye boş bir "ortam" ekleyerek `case` kombinatörünün uygulanmasını sağlar. İki dalda `take` kullanılması, `f` veya `g`yi yürütmek için bu boş ortamı düşürür.

Diğer Boole mantık işlemleri:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bit Toplayıcılar

Bir "half-adder" iki bit alır ve bunları toplar; bir taşıma biti ve toplam biti olmak üzere iki bitlik çıktı üretir.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

Bir "full-adder" üç bit toplar ve iki bitlik çıktı üretir. Girdi iç içe demet `(𝟚 × 𝟚) × 𝟚` kullanır.

İç içe demetler için kompakt gösterim kullanılır:

- `O f` ifadesi `take f`yi belirtir
- `I f` ifadesi `drop f`yi belirtir
- `H` ifadesi `iden`ı belirtir

Örneğin `I O H`, orta değeri çıkaran `drop (take iden) : A × (B × C) ⊢ B` anlamına gelir. Gösterim ikili rakamları çağrıştırır: iç içe demetleri ikili ağaçlar olarak düşündüğümüzde, gösterim ağaç konumlarının ters çevrilmiş ikili rakamlarını temsil eder. Bu ifadeler Simplicity için De Bruijn indeksleri oluşturur.

**Not:** `I`, `O` ve `H` gösterimi yalnızca tamamen `take`, `drop` ve `iden`dan oluşan alt ifadelere uygulanır.

Full-adder, iki half-adder'ı bileştirir ve taşıma bitlerinin mantıksal `or`unu alır:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

İlk satırda, `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` half-adder'ı ilk iki bit üzerinde çalıştırır ve son biti saklar.

İkinci satırda, `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` ilk biti (ilk half-adder'ın carry-out'u) saklar ve half-adder'ı son iki bit üzerinde çalıştırır.

Son satırda, `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` ilk iki bitin (iki half-adder'ın carry-out'ları) mantıksal OR'unu alır ve ikinci half-adder'ın sum-out bitini döndürür.

Bu, Simplicity programlamasını gösterir: `I`, `O` ve `H` gösterimini veri bitlerine referans vermek için kullanmak, sıralı bileşim aracılığıyla diğer fonksiyonları çağırmak için uygun "ortamlar" oluşturmak.

Kullanıcılar düşük seviyeli işlemleri doğrudan tanımlamaz. Bu serinin ilerleyen kısımlarında yaygın fonksiyonları uygulayan standart kütüphane jet'leri tartışılır. Son kullanıcıların Bitcoin Script'e benzer şekilde doğrudan Simplicity'de program yazması beklenmez. Bunun yerine SimplicityHL gibi daha yüksek seviyeli diller Simplicity kodu üretir; alt ifade "ortamlarını" yönetir ve adlandırılmış değişkenleri uygun `take` ve `drop` dizilerine çevirir.

### Vektörler

Sabit uzunluklu vektörler, `A` tipinin yinelenmiş çarpımları oluşturularak tanımlanır:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Bunlar `A^2`, `A^4`, `A^8` vb. olarak yazılabilir.

Vektörler yalnızca ikinin kuvvetleri olan uzunluklar için tanımlanır. Diğer kuvvetler parantezleme konvansiyonları seçmeyi gerektirir.

`f : A ⊢ B` ifadesi verildiğinde, tekrarlanan eşleme onu sabit uzunluklu vektörler üzerine "eşler":

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

`f : A × B ⊢ B` fonksiyonu verildiğinde, sabit uzunluklu vektörler üzerinde yineleme veya "katlama":

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Birçok varyasyon vardır. `f : A × B ⊢ C` verildiğinde, eşlenmiş vektörler üzerinde `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ` ile "zip" yapılır. `f : (A × B) × C ⊢ C` verildiğinde, eşlenmiş vektörler üzerinde `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C` ile katlama yapılır. `map` ve `fold-right`ı birleştirmek biriktiren kombinatörler oluşturur: `f : A × C ⊢ C × B`, `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ` verir. Çok daha fazla varyant mümkündür.

#### Çok bitli Kelimeler

Bir bit vektörü çok bitli tamsayılar verir. Örneğin `𝟚³²`, 32 bitlik bir word tipidir. `𝟚²⁵⁶`, hash'ler ve kriptografik işlemler için uygun 256 bitlik bir word tipidir.

Full-adder kullanılarak, vektör işlemlerinin bir varyantı çok bitli word'ler üzerinde bir "ripple carry adder" tanımlar:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n`, iki n bitlik ikili sayı ve bir bitlik carry-input alır; bir bitlik carry-out bayrağı ve n bitlik toplam döndürür.

#### SHA-256

Çok bitli word'ler üzerinde aritmetik işlemler — çıkarma, çarpma, bölme — ve mantıksal AND, OR, XOR gibi bit düzeyinde mantıksal işlemler özyinelemeli tanımlanıp bunlar tekrar tekrar birleştirilerek, SHA-256'nın blok sıkıştırma fonksiyonu bile inşa edilebilir:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

SHA-256 sıkıştırması, Rocq ispat yardımcısı (eski adıyla Coq) içinde Simplicity kullanılarak biçimsel olarak tanımlanmıştır; `sha256-hash-block` uygulamasının doğru olduğuna dair biçimsel bir ispatla birlikte.

Sıkıştırma ham Simplicity olarak çok yavaş çalışır. Jet'ler SHA-256 sıkıştırması gibi yaygın fonksiyonları yerel olarak yürütür. Saf Simplicity uygulamaları jet'ler için biçimsel şartnameler olarak hizmet eder.

### Option Tipleri

Option tipleri, birim tipiyle toplam alınmasından doğar:

```
Option A ≔ 𝟙 + A
```

`Option A` tipi `A?` veya `𝕊 A` (`𝕊` "ardıl" anlamına gelir) olarak yazılabilir. Fonksiyonlar option tipleri üzerinde eşlenir:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

bind gibi monadik kombinatörler tanımlanabilir:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Değişken Uzunluklu Buffer'lar

"Buffer"lar, kısmen doldurulmuş vektörler için tiplerdir:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

`Xᑉ⁸` tipi `(1 + X⁴) × ((1 + X²) × (1 + X))` olarak açılır. Bunu bir polinom olarak ele alıp açmak `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷` verir. Tip olarak yorumlandığında, boş demet dahil X'in 7'ye kadar tüm olası demetlerinin toplamını temsil eder. Bu tam olarak uzunluğu 8'den küçük listelerin tipidir.

Vektörlerde olduğu gibi, buffer'lar üzerinde de eşleme ve katlama işlemleri tanımlanabilir. Stack işlemleri arasında `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` ve `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?` bulunur. `push-<n` buffer'a bir öğe ekler ve taşma olursa tam bir vektör döndürür. `pop-<n` bir öğeyi kaldırır; daha küçük buffer'ı ve kaldırılan öğeyi döndürür, özgün buffer boşsa isteğe bağlı olarak hiçbir şey döndürmez.

`push-<n` tanımı özyinelemeli olarak:

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

Ham Simplicity belirli karmaşıklık düzeylerinin ötesinde takip edilmesi zor hâle gelir. Son kullanıcılar bu idiomatik ifadeleri üreten SimplicityHL gibi daha yüksek seviyeli diller kullanır.

### Sonuç

Bu bölüm, bitlerden mantıksal işlemlerin nasıl inşa edileceğini gösterdi. Bunlardan bit düzeyinde aritmetik ortaya çıktı ve yürütme hakkında akıl yürütmeyi mümkün kıldı. Vektör tipleri geliştirildi; aritmetik tanımı için çok bitli word'ler üzerinde yineleme gösterildi. Devamında, SHA-256 ve Schnorr imza doğrulaması gibi kriptografik işlemler yalnızca Simplicity kombinatörleri kullanılarak tanımlanabilir — bunların hepsi gerçekten Simplicity kullanılarak tanımlanmıştır.

Bu bölüm, Simplicity'de inşa edilebilecek tüm olası veri tipleri ve işlemler için kapsamlı bir rehber değildir; fakat Simplicity'nin kısıtları içinde pratik işlevselliğe ulaşmayı gösterir. Sonlu sınırlı tiplere rağmen yararlı vektörler, buffer tipleri ve bu yapılar üzerinde yineleyen işlemler tanımlanabilir.

Gerçek standart kütüphane işlem şartnameleri buradaki tanımlardan biraz farklıdır. Örneğin full-adder iki half-adder yerine 3 yönlü XOR ve "majority" mantık fonksiyonu kullanır.

Pratikte Simplicity programları aritmetik ve kriptografik işlemler için jet'ler kullanır. Ancak jet'ler yalnızca ifadelerin yerini alır. Buffer'lar ve vektörler üzerinde yineleyen kombinatörler jet'lerle değiştirilemez ve gerçek Simplicity programlarında görünür. Son kullanıcılar bunları doğrudan kullanmak yerine, bu tür ifadeleri üreten SimplicityHL gibi daha yüksek seviyeli diller kullanır.

Özyinelemeli tanımlanan kombinatörler ifade boyutunda üstel büyüyor gibi görünür. Bu sorun değildir. Serileştirme sırasında ifadeler ağaçlar yerine DAG'ler (directed acyclic graph'ler) olarak kodlanır. Gerçek temsil yalnızca doğrusal büyür.

Şimdiye kadar yalnızca saf hesaplamalar ele alındı. İşlem imzalama gibi görevlerde işlem verisiyle etkileşim, imzalar geçersizse programların başarısız olabilmesi için bir yol gerektirir. Bir sonraki bölüm Simplicity'deki yan etkileri tartışır.

## İki Yan Etki

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

Önceki bölümlerde, Simplicity'nin çekirdek kombinatör kümesini kullanarak bazı veri yapılarının ve hesaplamaların nasıl inşa edileceğini gösterdik. Belirttiğimiz gibi, çekirdek kombinatörler herhangi bir sonlu saf hesaplamayı uygulamak için yeterlidir. Bu şu soruyu doğurur: daha ne başarılabilir? İfadelerimize ek yan etkiler ekleyebiliriz.

İfadeler için çeşitli olası yan etki türleri vardır: durum güncelleme, log'a yazma, istisna fırlatma, bir ortamdan okuma, continuation çağırma vb. Simplicity'de mevcut yan etkiler uygulamaya bağlı olacaktır.

Bitcoin ve Liquid uygulamaları için şu anda iki yan etkimiz vardır: istisnanın tipinin `𝟙` olduğu bir istisna etkisi olan Failure etkisi ve işlem ortamındaki verilere erişilmesini sağlayan Reader etkisi. Çekirdek kombinatörlerimiz "saf"tır; yan etkileri yoktur. Ancak jet'ler yan etkileri olan yeni ilkel işlemler sunabilir.

### Etkili Jet'ler

Bu kursun ilerleyen kısımlarında jet'ler hakkında daha fazla konuşacağız; ancak burada yan etkilerini göstermek için birkaç örnek jet tanıtıyoruz.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙`, x-only pubkey, 256 bitlik mesaj ve Schnorr imzası alan ve hiçbir şey döndürmeyen bir ifade için jet'tir! Tipine göre bir `unit` ile aynı davranması gerekir. Fark, jet'in yan etkisindedir: imza doğrulaması başarısız olursa, unit tipinde bir istisna fırlatılarak tüm hesaplama iptal edilir. Bu Failure etkisidir.

#### Verify

`verify : 𝟚 ⊢ 𝟙`, Failure etkisini ifade etmek için yalın bir jet'tir. `verify`ın girdisi `false` ise, bir istisna fırlatılarak tüm hesaplama iptal edilir. Girdi `true` ise hiçbir şey döndürülmez, ancak hesaplama devam edebilir.

#### İşlem Hash'leri

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` sabit bir fonksiyon gibi görünür, çünkü yalnızca bir olası girdi değeri vardır: boş demet. Ancak bu jet işlem ortamından okur ve Bitcoin Script'in imza doğrulamasında kullanılan `SIGHASH_ALL` mesaj özetine benzer bir işlem verisi hash'i üretir. Bu, Reader etkisinin bir örneğidir: döndürülen değer, jet'in içinde yürütüldüğü işlem ortamına bağlıdır. İmzalar için özel mesaj özetleri oluşturmaya yardımcı olmak amacıyla işlem ortamı verisinin çeşitli alt kümelerini hash'leyen başka birçok hashing jet'i vardır.

#### İçgözlem Jet'leri

`input-sequence : 𝟚³² ⊢ 𝟚³²?`, bir girdi indeksi alan ve o girdi için işlemin sequence number'ını döndüren, indeks sınır dışıysa isteğe bağlı olarak hiçbir şey döndürmeyen bir fonksiyondur. Yine çıktı değeri, girdi indeksinin saf bir fonksiyonu değildir; bunun yerine işlem, çıktı değerini belirlemek için işlem ortamına erişmek amacıyla Reader etkisini kullanır. İşlem ortamı verisinin çeşitli parçalarını döndüren başka birçok içgözlem jet'i vardır.

### Etkileri Sınıflandırmak

Tüm yan etkiler eşit yaratılmamıştır. Bazı yan etkiler diğerlerinden daha düzgün davranır. Etkileri, program dönüşümlerine ne kadar elverişli olduklarına göre sınıflandırabiliriz.

#### Komütatif Etkiler

Komütatif etki, iki ifadenin çıktılarını takas ettiğinizde, ifadenin etkisini değiştirmeden ifadelerin kendilerini de güvenle takas edebildiğiniz etkidir. `swap = I H ▵ O H : A × B ⊢ B × A`yı düşünün. Yan etkileri olan her `f` ve `g` ifadesi için `f ▵ g ⨾ swap = g ▵ f` ise, etkiler komütatiftir.

Ortamdan işlem verisi okumak komütatif bir etkidir; çünkü ortamdan okumanın sonucu, okumayı hangi sırayla yürüttüğümüzden bağımsız olarak aynıdır.

Genel olarak, istisna fırlatmak komütatif bir etki değildir. `f` bir `e₁` istisnası ve `g` başka bir `e₂` istisnası fırlatırsa, `f` ve `g` çiftinden hangi istisnanın fırlatılacağı bunların hangi sırayla yürütüldüğüne bağlıdır.

Ancak yalnızca unit tipli bir istisnanın fırlatılabildiği Failure etkisinin özel durumunda etki komütatiftir. `f` veya `g`den hangisi istisna fırlatırsa fırlatsın, ortaya çıkan istisna aynı olacaktır; çünkü yalnızca bir olası istisna değeri vardır.

#### İdempotent Etkiler

İdempotent etki, bir ifadenin çıktısını çoğalttığınızda, ifadenin etkisini değiştirmeden ifadenin kendisini de güvenle çoğaltabildiğiniz etkidir. `dup = iden ▵ iden : A ⊢ A × A`yı düşünün. Yan etkileri olan her `f` için `f ⨾ dup = dup ⨾ f ▵ f` ise, etkiler idempotenttir.

Ortamdan işlem verisi okumak idempotent bir etkidir. İstisna fırlatmak da idempotent bir etkidir. Çoğaltılmış iki ifadeden yalnızca biri yürütülecek olsa bile, `dup ⨾ f ▵ f` tarafından fırlatılan herhangi bir istisna, `f ⨾ dup` tarafından fırlatılan istisnayla aynı olacaktır.

Ancak log'a yazmak idempotent olmayabilir; çünkü etkiyi çoğaltmak log mesajının iki kez görünmesine neden olur. Bununla birlikte, log bir mesaj _listesi_ yerine bir mesaj _kümesi_nden oluşuyorsa, etki idempotent (ve komütatif) olur; çünkü kümeye ekleme işleminin kendisi idempotenttir.

#### Birimsel Etkiler

Birimsel etki, bir ifadenin çıktısını attığınızda, ifadenin etkilerini değiştirmeden ifadenin kendisini de güvenle atabildiğiniz etkidir. Yan etkileri olan her `f` için her zaman `f ⨾ unit = unit` ise, etkileriniz birimseldir.

Ortamdan veri okumak, az sayıdaki birimsel etki türünden biridir. İşlem verisini ortamdan okumanın sonucu atılırsa, okumayı yapan tüm ifade atılabilir.

Failure etkisi birimsel değildir. `f` bir istisna fırlatırsa `f ⨾ unit` de fırlatır; hesaplama iptal edilmeden önce `unit` kombinatörüne ulaşamaz bile. Öte yandan, `unit` açıkça herhangi bir istisna fırlatmaz; bu nedenle `f ⨾ unit` ve `unit`in etkileri farklı olur.

Özetlemek gerekirse, yukarıda tartışılan etkilerin bu üç özellik karşısındaki durumu şöyledir:

| Etki | Komütatif | İdempotent | Birimsel |
| --- | :---: | :---: | :---: |
| Reader (işlem ortamı) | ✓ | ✓ | ✓ |
| Failure (unit tipli istisna) | ✓ | ✓ | ✗ |
| Writer (küme olarak log) | ✓ | ✓ | ✗ |
| Genel istisnalar (keyfi tip) | ✗ | ✓ | ✗ |

### Simplicity'de İzin Verilen Etkiler

Bir etki türü ne kadar iyi davranan özelliklere sahipse, Simplicity optimizer'ının o etkileri kullanan programları dönüştürmek için o kadar fazla alanı olur. İdeal olarak yalnızca üç özelliğin tamamına sahip etkileri — komütatif, idempotent ve birimsel — kabul ederdik. Bu, bir optimizer'ın istediği her tür program dönüşümünü gerçekleştirmesine olanak tanırdı. Ancak üç özelliğin tamamını sağlayan tek etki, bir ortamdan okumadır.

Bunun yerine Simplicity etkilerinin komütatif ve idempotent olmasını talep ederiz. Simplicity'de kullandığımız iki etki de, Failure etkisi ve Reader etkisi, komütatif ve idempotenttir. Bu, Simplicity kodu üzerinde büyük bir optimizasyon sınıfının gerçekleştirilmesine olanak tanır.

Ancak yukarıda açıklanan "discard" dönüşümüne, yani `f ⨾ unit`i `unit` ile değiştirme girişimine veya benzer herhangi bir dönüşüme, `f` bir Failure etkisi üretebiliyorsa izin verilmez. Gerçekten de, `f`nin bir `bip0340-verify` assertion'ı içerdiğini hayal edin. Bu kontrolü optimize ederek ortadan kaldırmaya çalışmak felaket olurdu.

### Yan Etkilere Neden Hiç İzin Verilsin?

Simplicity neden yan etkilere hiç izin veriyor? Her programın tüm işlemi girdi olarak alıp bir işlemin geçerli olup olmadığına karar veren bir Boole çıktısı döndürmesi daha iyi olmaz mıydı?

#### Toplu Doğrulama

Failure etkisine sahip olmamızın nedenlerinden biri, Schnorr imzalarının [toplu doğrulama](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) işlemini desteklemektir. Toplu doğrulamada, birçok bireysel Schnorr imza kontrolü, tek bir imza kontrolü bile başarısız olursa tüm toplu doğrulama başarısız olacak şekilde bir araya toplanır.

Bu toplu doğrulama prosedürü, her imzayı tek tek doğrulamaya kıyasla verimliliği artırır. Dezavantajı, toplu doğrulama başarısız olursa hangi belirli imza kontrolünün veya kontrollerinin başarısız olduğunu öğrenmememizdir.

Failure yan etkisini kullanarak `bip0340-verify`, bir imza kontrolü başarısız olursa tüm işlemin başarısız olmasını sağlar. `bip0340-verify` bunun yerine başarı veya başarısızlık için bir Boole tipi olan `𝟚` döndürseydi, başarısız bir imza kontrolü yine de betiğin başarılı olduğu bir dala yol açabilirdi. Böyle bir durumda belirli imzanın geçerli olup olmadığını bilmemiz gerekirdi ve dolayısıyla toplu doğrulama avantajından yararlanamazdık.

#### Önceden Hesaplanmış İşlem Verisi

Erken Bitcoin Script'te bir sorun, imzalar için mesaj özetleri oluşturmakta kullanılan hashing fonksiyonunun işlem boyutunda doğrusal olmasıydı. Tipik olarak her girdi imza doğrulaması için en az bir mesaj özeti oluşturur; bu nedenle toplam hashing miktarı işlem boyutunda kareseldi.

Bu sorun, Segwit'te ve Bitcoin Script'in daha sonraki yinelemelerinde, mesaj özetlerinin imza kontrolü başına sabit zamanda hesaplanabilecek şekilde yeniden tanımlanmasıyla giderildi. Bu, işlem verilerinin hash'lerini bir kez önceden hesaplayan ve ardından her girdinin sighash hesaplamaları tarafından paylaşılan `PrecomputedTransactionData`ya sahip olmaya dayanır. Simplicity'nin işlem hashing jet'leri, jet'lerin sabit zamanda çalışmasını sağlamak için aynı tür önceden hesaplanmış işlem verilerine dayanır.

`sig-all-hash`in Reader etkisini kullanmadığını varsayalım. Diyelim ki bir şekilde işlem ortamı için bir Simplicity tipi inşa etmeyi başardık. Buna `TxEnv` diyelim; böylece `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` jet'in tipi olsun. Böyle bir tanım, `sig-all-hash` jet'inin yalnızca içinde bulunduğu işlemin değil, herhangi bir işlemin hash'ini hesaplayabilmesini gerektirirdi. Simplicity programları verilen `TxEnv`yi kopyalayıp değiştirilmiş bir kopyasını `sig-all-hash`e geçirebilirdi. Böyle bir durumda `sig-all-hash`, `PrecomputedTransactionData`ya dayanamazdı ve `sig-all-hash`in bu sürümüne geçirilen işlem verisi ne olursa olsun yine doğrusal zaman gereksinimine geri dönerdik.

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶`, işlem verisine erişmek için Reader etkisini kullandığından, _yalnızca_ sabit bir işlem ortamına erişim elde eder. Bu nedenle jet'in uygulaması güvenle `PrecomputedTransactionData` kullanabilir ve sabit zamanda çalışabilir.

### Girdiler Arası İmza Toplama

Ne Liquid ne de Bitcoin şu anda [girdiler arası imza toplama](https://hrf.org/latest/cisa-research-paper/) desteklemese de, zamanı geldiğinde Simplicity'nin bununla uyumlu olabileceğini kontrol etmek istiyoruz.

Ayrıntılar henüz çalışılmamış olsa da, yarım toplamanın bir Writer etkisi kullanılarak uygulanacağını hayal ediyoruz. Yani `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` gibi bir tipe sahip yeni bir jet, açık anahtar, mesaj özeti ve bir Schnorr imzasının `r`-bileşenini (bir Schnorr imzası bir `r`-bileşeni ve bir `s`-bileşeninden oluşur) alır ve yürütmeye devam etmeden önce bunu bir işlem log'una yazar. Ardından, işlemin başka bir yerinde veya işlemle birlikte, yarı-toplanmış tüm Schnorr imzaları için toplanmış bir `s`-bileşeni sağlanır. İşlem yalnızca, log'lanan tüm anahtarlar, mesajlar ve `r`-bileşenleri için böyle bir toplanmış `s`-bileşeni sağlandığında geçerli olur.

Simplicity'nin gereksinimlerini karşılamak için bu Writer etkisinin idempotent ve komütatif olması gerekir. Bu, writer log'u anahtar, mesaj, `r`-bileşeni demetlerinden oluşan bir küme olarak ele alınarak sağlanabilir. Bu işe yarar çünkü küme işlemleri idempotent ve komütatiftir. Log'u değerler kümesi olarak ele almak, yarım toplama doğrulama algoritmasıyla uyumlu olurdu.

### Sonuç

Bu bölümde Simplicity'nin yapabileceği hesaplamalara yan etkiler eklemeye baktık. Çeşitli etki türlerini, farklı program dönüşümleri açısından ne kadar iyi davrandıklarına göre sınıflandırdık. Simplicity'nin etkilerini komütatif ve idempotent olanlarla sınırlamaya karar verdik.

Bitcoin ve Liquid uygulamaları için kullandığımız iki etki, işlem ortamına erişmek için Reader etkisi ve programı iptal edip başarısız kılmak için Failure etkisidir. Bazı jet'ler, bu tür yan etkilerin ortaya çıkabildiği ilkel işlemleri kullanır.

Failure etkisi bir Simplicity programının çıktısını belirler: program ya başarısız olur ve işlemi geçersiz kılar ya da program başarılı olur. Reader etkisi ise bir Simplicity programına bir tür girdi sağlar: işlem verisini içeren ortam. Ancak Simplicity programlarına dijital imzalar gibi başka girdiler de sağlamamız gerekir.

Bir sonraki bölümde Simplicity programlarının ne olduğuna, bunların adreslere nasıl dönüştürüldüğüne ve imzalar gibi diğer girdileri Simplicity programlarına nasıl eklediğimize bakacağız.

## Programlar ve Adresler

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

Önceki bölümde Simplicity'de kullanılan iki yan etkiyi açıkladık: bir programın başarısını veya başarısızlığını belirleyen Failure etkisi ve işlem ortamına erişim sağlayan Reader etkisi. Şimdi pratik soruya dönüyoruz: Bir Simplicity programı tam olarak nedir ve blockchain üzerinde nasıl bir adrese dönüşür?

### Simplicity Programları

Bir Simplicity programı, `𝟙 ⊢ 𝟙` tipinde bir Simplicity ifadesi olarak tanımlanır. Bu tip imzası, programın anlamlı bir girdi almadığı (yalnızca birim değer) ve anlamlı bir çıktı üretmediği (yalnızca birim değer) anlamına gelir. Reader etkisi işlem ortamı girdisini yakalarken, Failure etkisi başarı veya başarısızlığı belirtir. Bu etkiler, Simplicity tiplerinin kendisi yerine I/O'yu ele alır.

### Commitment Merkle Root

Tam programları zincir üzerinde depolamak yerine Bitcoin taahhütler kullanır — bu, Pay-to-Script-Hash'ten (P2SH) uzanan bir pratiktir. Simplicity bir Commitment Merkle Root (CMR) kullanır.

Her kombinatör, şu kalıptan türetilmiş bir SHA-256 etiketi alır: `Simplicity␟Commitment␟[identifier]`; burada `␟`, ASCII kodu 31'i (unit separator) temsil eder.

Her etiket, aşağıda listelenen karşılık gelen ön imge string'inin SHA-256 hash'idir:

| Kombinatör | Etiket ön imgesi (ASCII string) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

Bir Simplicity ifadesi daha sonra, her kombinatör için argümanlarının CMR'leriyle birlikte etiketli bir SHA-256 midstate hesaplanarak özyinelemeli biçimde 256 bitlik bir CMR'ye hash'lenir (ifade `e`nin CMR'si için `#ᶜ(e)`, bayt birleştirme için `∥` yazın):

| Kombinatör | CMR kuralı |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

İkili kombinatörler (`comp`, `pair`, `case`) iki çocuğun CMR'lerini birleştirir; tekli kombinatörler (`take`, `drop`, `injl`, `injr`) tek çocuklarının CMR'sini 32 baytlık `0x00` padding'den sonra birleştirir; nullary yapraklar (`iden`, `unit`) ise yalnızca etiketlerini hash'ler. İki konvansiyon bunu hesaplamayı ucuz tutar: SHA-256 midstate'leri kullanılır; böylece **her ifade en fazla bir SHA-256 sıkıştırma fonksiyonu çağrısı gerektirir** (sabit etiketlere kadar olan midstate'in önceden hesaplandığı varsayılırsa) ve tek argümanlı kurucular argümanlarını 32 baytlık `0x00` padding ile öne alır; bu da isteyen uygulamalar için biraz ek ön hesaplamaya olanak tanır.

`unit` kombinatörü için — argüman alt ifadeleri olmayan nullary bir kurucu — bu kural `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` olarak özelleşir; burada `tag_unit = SHA-256(Simplicity␟Commitment␟unit)`tir (etiket iki kez beslenir). Önemsiz `unit` programı için ortaya çıkan CMR şudur:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Kritik olarak, CMR Simplicity ifadelerinin tiplerine taahhüt etmez; bunun yerine harcama sırasında tip çıkarımına dayanır.

### Adresler

Adresler, `0xbe` TapLeaf sürümü altında taahhüt edilen CMR'lerle BIP-0341'in Taproot mekanizmasını kullanır. Süreç şunları içerir:

1. Sürüm baytını, CMR uzunluğunu ve CMR'nin kendisini birleştiren bir TapLeaf etiketli hash'i hesaplamak
2. Bir iç açık anahtarı tweak etmek (anahtar harcama yolu istenmediğinde bir NUMS noktası kullanarak)
3. bech32m formatına dönüştürmek
4. Uygun checksum'ları eklemek

Anahtar harcama yolu istenmediğinde, iç açık anahtar bir **NUMS** ("Nothing-Up-My-Sleeve") noktası olarak ayarlanır: hiç kimsenin ayrık logaritmasını bilmediği kasıtlı olarak seçilmiş bir eğri noktası — başka bir deyişle, karşılık gelen özel anahtarı olmayan bir nokta. Hiç kimse bunun için imza üretemeyeceğinden, anahtar harcama yolu ispatlanabilir biçimde kullanılamaz ve çıktı *yalnızca* taahhüt edilen Simplicity betik yolu üzerinden harcanabilir. Gerçek bir uygulamada bu NUMS noktası, BIP-0341'in önerdiği gibi rastgeleleştirilmelidir; böylece anahtar harcama yolu olmayan çıktılar sıradan Taproot çıktılarından ayırt edilemez (bir gizlilik faydası).

#### Simplicity'den Adrese

Mümkün olan en basit program için tüm türetmeyi adım adım inceleyelim: her zaman başarılı olan bir no-op, `unit : 𝟙 ⊢ 𝟙`.

**1. Kombinatör etiketi.** Önce `unit` etiketini hesaplayın:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Programın CMR'sini elde etmek için etiketi iki kez besleyin:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf hash'i.** CMR'nin önüne Simplicity'nin TapLeaf sürümü `0xbe` ve CMR uzunluğu `0x20`yi (32 bayt) ekleyin, ardından Elements TapLeaf etiketli hash'ini alın (etiketli hash `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)` şeklindedir):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Yalnızca bu tek yaprak olduğundan TapBranch yoktur; dolayısıyla bu hash zaten TapTree köküdür.

**4. TapTweak.** Anahtar harcama yolu istemediğimiz için, iç anahtar olarak BIP-0341 NUMS noktasını kullanır ve onu TapTree köküyle tweak ederiz:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Çıktı anahtarı.** İç anahtarı eğri üzerinde tweak edin, `output_pk = lift_x(internal_pk) ⊕ t·G` (eliptik eğri aritmetiği burada özetlenmiştir); bu, x-only çıktı anahtarı `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`u verir.

**6. Bech32m adresi.** X-only çıktı anahtarını encode edin, bir `p` öneki ekleyin (SegWit v1 tanık sürümü karakteri), Liquid-testnet human-readable öneki `tex1`i ekleyin ve Bech32m checksum'ını sonuna iliştirin. Nihai adres şudur:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

Bu çok işti — ancak bunun büyük kısmı Simplicity tarafından değil, Taproot'un kendisi tarafından zorunlu kılınır.

### Tanık İfadeleri

Yeni bir kombinatör tipi, Simplicity programlarına girdi yokluğu sorununu ele alır: tanık ifadesi. `witness` kombinatörü, imza verisinin ve diğer tanık materyalinin programlara entegre edilmesine izin verir.

```
      w : B
-----------------
witness w : A ⊢ B
```

Tanık ifadesinin semantiği basittir: girdisini yok sayar ve yalnızca `w` değerini (herhangi bir Simplicity tipinde olabilir) döndürür; yani `⟦witness w⟧(a) = w`. Bu **yeni bir ifade gücü eklemez** — tamlık teoremine göre Simplicity zaten böyle herhangi bir sabit fonksiyonu inşa edebilir (önceki bölümlerdeki `scribe` makrosunu hatırlayın). `witness` kombinatörünün amacı tamamen **CMR**'sinde yatar: `w` değeri ifadenin CMR'sinden **hariç tutulur**; böylece adres `w` bilinmeden önce hesaplanabilir ve `w` harcama zamanında sağlanır.

Bu tasarım tercihi budamayı destekler — yürütülmeyen koşullu dalların, ilişkili tanık ifadeleri dahil olmak üzere zincir üzerinde açıklanması gerekmez. Bir dal budandığında, doğrulayıcının budanmış alt ağacın gerçek içeriğine değil yalnızca CMR'sine ihtiyacı vardır.

### Tanık Değerleri

Bir tanık ifadesinin daha genel bir Simplicity ifadesini değil de yalnızca bir *değeri* tutabilmesi bir sınırlama gibi görünebilir. Ancak UTXO tabanlı blockchain programları yalnızca bir kez yürütülür. Bir witness düğümüne bütün bir alt ifade geçirmeye gerek yoktur: kullanıcı bu alt ifadeyi zincir dışında kendisi çalıştırabilir ve aynı sonucu elde etmek için çıktısını tanık değerine yazabilir.

(Bu kursun ilerleyen kısmında, argüman olarak bütün bir Simplicity ifadesi alan bir tanık ifadesine oldukça benzeyen `disconnect` kombinatörüyle karşılaşacağız.)

Alternatif bir tasarım, tüm tanık verilerini en üst seviyedeki Simplicity programına argüman olarak beslerdi. Tanık ifadeleri iki nedenle tercih edilir. Birincisi, **budama**: `case` ifadelerinin yürütülmeyen dalları zincir üzerinde asla açıklanmaz ve bu dalların içindeki tüm tanık ifadeleri de onlarla birlikte budanır. İkincisi, **yerellik**: tanık ifadeleri, her tanık değerini programın en üst seviyedeki girdisinden aşağı taşımak yerine, tam olarak kullanıldığı yere yerleştirmemizi sağlar.

### Tip Çıkarımı

CMR'ler tiplere taahhüt etmediği için tip sistemi harcama sırasında yeniden inşa edilir. Simplicity'nin tip çıkarımı algoritması, kombinatör yapısına dayanarak her alt ifade için minimal tipleri belirler. Daha kesin olarak, çıkarım her alt ifadenin *principal* (en genel) tipini hesaplar; serbest kalan tip değişkenleri daha sonra birim tipi `𝟙` olarak örneklenir ve bu, program için benzersiz, minimal bir tip verir.

### Sonuç

Bu bölümde Simplicity programlarının `𝟙 ⊢ 𝟙` tipinde ifadeler olduğunu ortaya koyduk, Commitment Merkle Root'ların her kombinatörün etiketli SHA-256 hash'lerinden nasıl oluşturulduğunu açıkladık ve CMR'lerin BIP-0341 Taproot aracılığıyla zincir üzerindeki adreslere nasıl dönüştürüldüğünü gösterdik. Tanık ifadelerini, adres oluşturma zamanında değerlerine taahhüt etmeden, imza verisi ve diğer girdileri harcama zamanında sağlama mekanizması olarak tanıttık.

# Final Bölümü

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## İncelemeler ve Puanlar

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Final Sınavı

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Sonuç

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
