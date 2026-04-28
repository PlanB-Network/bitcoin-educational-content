---
name: Bitcoin ile Rust'i Öğrenme
goal: Bitcoin kodlama ile Rust geliştirme becerilerinizi ilerletin
objectives: 

  - Rust Diline alışmak
  - Bitcoin'i geliştirmek için neden Rust kullanıldığını anlayın
  - Lightning SDK'nın temelini alın

---

# Bitcoin Üreticileri için Bir Rust Keşif Gezisi



Fulgur' Ventures tarafından Ekim 2023'te düzenlenen bir seminer sırasında çekilen bu uygulamalı kursta, gerçek Bitcoin odaklı bileşenler ve mini projeler oluşturarak Rust becerilerinizi geliştireceksiniz. Rust temellerini, Rust'un neden Bitcoin geliştirme için kullanıldığını (bellek güvenliği, performans ve güvenli eşzamanlılık) ve ödeme özellikleri oluşturmak için Lightning SDK ile nasıl başlayacağınızı ele alacağız.


Bölümler boyunca temel Rust kalıplarını (sahiplik, yaşam süreleri, özellikler, async) uygulayacak, Bitcoin ilkelleri (anahtarlar, işlemler, komut dosyası oluşturma) ile çalışacak ve Lightning kavramlarını (düğümler, kanallar, faturalar) aşamalı olarak entegre edeceksiniz.


Temel programlamaya aşinalık yardımcı olsa da, önceden Rust veya Bitcoin geliştirme kesinlikle gerekli değildir. Kurs, başlangıç seviyesine uygun olmakla birlikte Bitcoin'e geçen mühendisler için de yeterince pratiktir.


+++

# Giriş

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Kursa genel bakış

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Giriş**


SDK'larla ilgili bu yeni başlayan dostu programlama kursuna hoş geldiniz. Bu eğitimde, Rust'nın temellerini öğrenecek, ardından Bitcoin programlamaya uygulanan Rust'ya odaklanacak ve SDK'ları kullanan bazı kullanım örnekleriyle bitireceksiniz.


Fulgure Venture tarafından geçtiğimiz Ekim ayında Toskana'da düzenlenen canlı seminerin bir parçası olan eğitimin videoları şimdilik sadece İngilizce olarak sunulacak. Bu eğitim sadece ilk haftaya odaklanacaktır. İkinci yarı RGB'ye yöneliktir ve RGB kursunda bulunabilir.


https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Bu eğitim size Rust ve çeşitli SDK'ları kullanarak Lightning Network üzerinde programlama becerilerinizi geliştirme fırsatı verir. Lightning Network'e özgü geliştirmeye dalmak isteyen sağlam bir programlama geçmişine sahip geliştiriciler için tasarlanmıştır. Rust'nin temellerini, neden Bitcoin geliştirme için uygun olduğunu öğrenecek ve ardından özel SDK'ları kullanarak uygulamalı uygulamaya geçeceksiniz.


**Bölüm 2: Rust** ile kod yazmayı öğrenin

Bu bölümde, bir dizi aşamalı bölüm aracılığıyla Rust temellerini keşfedeceksiniz. Rust kodu yazmayı, özelliklerini anlamayı ve yedi ayrıntılı bölüm boyunca temel özelliklerinde ustalaşmayı öğreneceksiniz. Bu modül, Rust'ün neden Bitcoin geliştirme için tercih edilen bir dil olduğunu anlamak için gereklidir.


**Bölüm 3: Rust & Bitcoin**

Burada, Rust'nin Bitcoin geliştirme için neden uygun bir seçim olduğunu derinlemesine inceleyeceğiz. Hata modeli, UniFFI aracı ve asenkron özellikler hakkında bilgi edineceksiniz - bunların hepsi sağlam ve güvenli yazılım oluşturmanın temel unsurlarıdır.


**Bölüm 4: SDK'lar ile LNP/BP geliştirme**

Breez SDK ve Lipa için Greenlight gibi çeşitli SDK'ları kullanarak LN düğümlerini nasıl geliştireceğinizi öğreneceksiniz. Bitcoin ve Lightning geliştirmeyi basitleştirmek için tasarlanmış kütüphaneleri kullanarak Lightning Network uygulamalarını nasıl uygulayacağınızı göreceksiniz.


Lightning Network becerilerinizi Rust ile geliştirmeye hazır mısınız? Hadi başlayalım!

# Rust kitabı ile kod yazmayı öğrenin

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Rust'e Giriş

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

### Rustup ile Rust'yı Kurma ve Yönetme


Rust ile yolculuğunuza başlarken, ilk adım uygun bir geliştirme ortamı kurmayı içerir. Rust'yi kurmak için en yaygın olarak önerilen yaklaşım, farklı projeler ve platformlar arasında kurulum ve güncellemeleri yöneten bir araç zinciri yönetim sistemi olan Rustup'tır.


Rustup bir yükleyiciden çok daha fazlasıdır; Rust geliştirme ortamınız için kapsamlı bir yönetim aracı olarak işlev görür. Rustup ile, Android geliştirme için ARM64 veya desteklemeniz gerekebilecek diğer mimariler gibi farklı platformlar için ek derleme hedeflerini kolayca yükleyebilirsiniz. Araç ayrıca Rust güncellemelerini sorunsuz bir şekilde yönetir, bu da Rust'in yaklaşık altı haftada bir yeni bir kararlı sürüm yayınladığı göz önüne alındığında özellikle değerlidir. En son sürüme güncellemeniz gerektiğinde, basit bir `rustup update` komutu her şeyi otomatik olarak halleder.


Rustup'ı kurarken, ilgili güvenlik modelini anlamaya değer. Kurulum işlemi, taşıma katmanı kriptografik güvenliği sağlayan HTTPS üzerinden resmi Rust web sitesinden bir komut dosyası indirir ve çalıştırır. Rustup ve Cargo tarafından indirilen paketler güvenilir kaynaklardan (crates.io ve resmi Rust altyapısı) gelir ve HTTPS şifrelemesinden yararlanır. Bu yaklaşım çoğu geliştirme senaryosu için güvenli olsa da, sıkı güvenlik politikalarına sahip bazı kuruluşlar, dağıtımın kendi paket imzalama altyapısı aracılığıyla ek bir güven katmanı sağlayan Linux dağıtımlarının paket yöneticisi aracılığıyla Rust'u yüklemeyi tercih edebilir. Öğrenme ve genel geliştirme amaçları için Rustup, Rust ekosisteminde iyi kurulmuş ve yaygın olarak güvenilen bir araçtır.


Çoğu geliştirme senaryosu için, resmi Rust web sitesinde sağlanan kurulum betiğini çalıştırarak Rustup'ı kurabilirsiniz. Yükleyici sizden farklı araç zinciri seçenekleri arasından seçim yapmanızı isteyecektir, kararlı araç zinciri çoğu kullanıcı için önerilen seçimdir. Kurulum, yönetici ayrıcalıkları gerektirmeden ev dizininizde gerçekleşir ve hemen kullanım için gerekli tüm ortam değişkenlerini ayarlar.


### Rust Araç Zincirlerini ve Bileşenlerini Anlama


Rust'nin geliştirme ekosistemi, eksiksiz bir programlama ortamı sağlamak için birlikte çalışan birkaç temel bileşenden oluşur. Bu bileşenleri anlamak, Rust geliştirme sürecinde daha etkili bir şekilde ilerlemenize ve ortaya çıkan sorunları gidermenize yardımcı olur.


Rustc` olarak bilinen Rust derleyicisi, Rust araç zincirinin çekirdeğini oluşturur. Teorik olarak Rust programlarını derlemek için doğrudan `rustc` kullanabilseniz de, geliştirme çalışmalarının çoğu Rust'ün paket yöneticisi ve derleme sistemi olan Cargo'ya dayanır. Cargo, JavaScript ekosistemindeki npm'e benzer şekilde çalışır, bağımlılıkları yönetir, derlemeleri koordine eder ve yaygın geliştirme görevleri için uygun komutlar sağlar. Cargo build` veya `cargo run` gibi komutları çalıştırdığınızda, Cargo derleme sürecini düzenler, bağımlılık çözümlemesini yönetir ve genel proje yapısını yönetir.


Clippy, kodunuzu analiz eden ve iyileştirmeler için öneriler sunan bir linterdir. Temel sözdizimi denetleyicilerinin aksine Clippy, Rust deyimlerini anlar ve belirli görevleri yerine getirmek için daha deyimsel yollar önerebilir. Bu araç, Rust'ün en iyi uygulamalarını öğrenmeye ve daha sürdürülebilir kod yazmaya yardımcı olur.


Rust araç zinciri ayrıca kapsamlı dokümantasyon araçları ve resmi Rust dokümantasyon web sitesinden erişilebilen standart kütüphane dokümantasyonu içerir. Bu dokümantasyon, standart kütüphane fonksiyonları, türleri ve modülleri hakkında ayrıntılı bilgi sağlayarak geliştirme sırasında vazgeçilmez bir referans görevi görür. Dokümantasyon, sadece fonksiyonların ne işe yaradığını değil, aynı zamanda bunları programlarınızda nasıl etkili bir şekilde kullanacağınızı anlamanıza yardımcı olan kapsamlı örnekler ve açıklamalar içerir.


Rust birden fazla sürüm kanalını destekler: kararlı, beta ve gecelik. Kararlı kanal, üretim kullanımı için uygun, kapsamlı bir şekilde test edilmiş sürümler sağlar. Beta kanalı bir sonraki kararlı sürümün önizlemesini sunar, öncelikle resmi sürümden önce son testler için kullanılır. Nightly kanalı, yeni Rust yeteneklerini denemek için yararlı olabilecek, aktif geliştirme aşamasındaki deneysel özellikleri içerir, ancak bu özellikler gelecekteki sürümlerde değişebilir veya kaldırılabilir.


### Cargo ile Rust Projeleri Oluşturma ve Yönetme


Modern Rust geliştirme, proje oluşturma, bağımlılık yönetimi ve derleme sürecini kolaylaştıran Cargo etrafında toplanır. Dizinleri ve dosyaları manuel olarak oluşturmak yerine, Cargo, generate'e mantıklı varsayılanlarla eksiksiz bir proje yapısı için `cargo new` komutunu sağlar.


Cargo new project_name` ile yeni bir proje oluşturduğunuzda, Cargo standart bir dizin yapısı kurar, "Hello, world!" programı ile temel bir `main.rs` dosyası oluşturur, bir Git deposunu başlatır ve proje yapılandırması için bir `Cargo.toml` dosyası oluşturur. Cargo.toml` dosyası, projeniz için merkezi yapılandırma noktası olarak hizmet eder, projeniz hakkında meta veriler içerir ve kodunuzun gerektirdiği tüm bağımlılıkları listeler.


Cargo, günlük geliştirme çalışmaları için birkaç temel komut sağlar. Cargo build` komutu projenizi ve bağımlılıklarını derleyerek `target` dizininde çalıştırılabilir dosyalar oluşturur. Geliştirme sırasında hızlı yineleme için `cargo run` komutu derleme ve yürütmeyi tek bir adımda birleştirir. Cargo check` komutu, son çalıştırılabilir dosyayı oluşturmadan tüm derleme kontrollerini gerçekleştirir, bu da kodunuzun doğru derlendiğini doğrulamak istediğinizde tam bir derlemeden önemli ölçüde daha hızlı olmasını sağlar.


Üretim dağıtımı için kod hazırlarken, `--release` bayrağı optimizasyonları etkinleştirir ve hata ayıklama onaylarını kaldırır. Sürüm derlemeleri daha hızlı çalışır ve daha küçük yürütülebilir dosyalar üretir, ancak derlenmesi daha uzun sürer ve yararlı hata ayıklama bilgilerini kaldırır. Derleyici, sürüm derlemeleri sırasında çeşitli optimizasyonlar uygular ve tamsayı taşması tespiti gibi çalışma zamanı kontrollerini devre dışı bırakır, bu da performansı artırır ancak hata ayıklama derlemelerinde bulunan bazı güvenlik garantilerini ortadan kaldırır.


### Değişkenler, Değişebilirlik ve Rust'nin Güvenlik Felsefesi


Rust değişken yönetimi konusunda çoğu dilden farklı bir yaklaşım benimser. Varsayılan olarak, Rust'deki tüm değişkenler değişmezdir, yani değerleri ilk atamadan sonra değiştirilemez. Bu tasarım kararı, beklenmedik durum değişikliklerinden kaynaklanan yaygın programlama hatalarını önlemeyi amaçlamaktadır.


Let x = 5` kullanarak bir değişken bildirdiğinizde, bu değişken varsayılan olarak değişmez hale gelir. Daha sonra değerini değiştirmeye yönelik herhangi bir girişim derleme hatasıyla sonuçlanacaktır. Bu değişmezlik gereksinimi, geliştiricileri durum değişikliklerinin gerçekten ne zaman gerekli olduğu konusunda dikkatli düşünmeye zorlar ve kod davranışını daha öngörülebilir hale getirir. Birçok programlama hatası değişkenlerin beklenmedik şekilde değişmesinden kaynaklanır ve Rust'nin varsayılan değişmezliği bu sorunları önlemeye yardımcı olur.


Bir değişkenin değerini gerçekten değiştirmeniz gerektiğinde, Rust `mut` anahtar sözcüğünü kullanarak değişebilirliğin açıkça beyan edilmesini gerektirir: `let mut x = 5`. Bu açık bildirim, hem derleyiciye hem de diğer geliştiricilere programın yürütülmesi sırasında bu değişkenin değerinin değişebileceğine dair açık bir sinyal görevi görür. Değişebilirliğin açıkça beyan edilmesi gerekliliği, her değişken için değişebilirliğin gerçekten gerekli olup olmadığının dikkatle değerlendirilmesini teşvik eder.


Rust ayrıca, önceki bir değişkenle aynı ada sahip yeni bir değişken bildirmenize olanak tanıyan gölgelemeyi de destekler. Mutasyondan farklı olarak gölgeleme, aynı ada sahip tamamen yeni bir değişken oluşturarak önceki değişkeni etkili bir şekilde gizler. Bu teknik, bir dizeyi bir sayıya ayrıştırmak ve ardından bu sayıyı daha fazla işlemek gibi birden fazla adımla veri dönüştürürken özellikle yararlıdır. Gölgeleme ile, her adımda değişkenin türünü değiştirirken dönüşüm süreci boyunca tutarlı bir değişken adını koruyabilirsiniz.


Gölgeleme ve mutasyon arasındaki ayrım, tür değişiklikleri göz önünde bulundurulduğunda önem kazanır. Gölgeleme ile, yeni bir değişken oluşturduğunuz için bir değişkenin hem değerini hem de türünü değiştirebilirsiniz. Mutasyon ile, yeni bir değişken oluşturmak yerine mevcut bir değişkeni değiştirdiğiniz için aynı türü korurken yalnızca değeri değiştirebilirsiniz.


```rust
// Shadowing: creating new variables with the same name
let amount = "100000";           // amount is a &str (string slice)
let amount = amount.parse::<u64>().unwrap();  // amount is now u64
let amount = amount * 100;       // amount is still u64, new value

// Mutation: modifying the same variable
let mut balance = 50000_u64;
balance = balance + amount;      // OK: same type, different value
// balance = "empty";            // ERROR: cannot change type with mutation

// Practical example: processing a Bitcoin amount input
let user_input = "  0.001 ";                    // &str with whitespace
let user_input = user_input.trim();            // &str, whitespace removed
let satoshis: u64 = (user_input.parse::<f64>().unwrap() * 100_000_000.0) as u64;
println!("Amount in satoshis: {}", satoshis);  // 100000
```


### Veri Tipleri ve Tip Sistemi Temelleri


Rust, her değerin derleme zamanında bilinen iyi tanımlanmış bir tipe sahip olması gereken güçlü, statik bir tip sistemi uygular. Bu, dinamik olarak tiplendirilmiş dillere kıyasla kısıtlayıcı görünse de, Rust'in tip çıkarım yetenekleri, tipleri nadiren açıkça belirtmeniz gerektiği anlamına gelir. Derleyici genellikle değeri nasıl kullandığınıza bağlı olarak uygun türü belirleyebilir.


Ancak, bazı durumlar açık tür ek açıklamaları gerektirir. Dizeleri çeşitli sayısal türlere dönüştürebilen `parse()` gibi genel işlevleri kullanırken, derleyicinin hangi belirli türü istediğinizi bilmesi gerekir. Bu durumlarda, iki nokta üst üste sözdizimini kullanarak tür ek açıklamaları sağlarsınız: "let guess: u32 = "42".parse().expect("Not a number!")`.


Rust'nın skaler tipleri arasında tamsayılar, kayan noktalı sayılar, booleanlar ve karakterler bulunur. Tamsayı tip sistemi, bellek kullanımı ve performans özellikleri üzerinde hassas kontrol sağlar. Tamsayı tipleri sistematik olarak adlandırılır: i̇şaretli tamsayılar için `i8`, `i16`, `i32`, `i64` ve `i128` ve işaretsiz tamsayılar için `u8`, `u16`, `u32`, `u64` ve `u128`. Sayılar bit genişliğini gösterir, böylece bellek kullanımı ve değer aralıkları hemen anlaşılır hale gelir.


Isize` ve `usize` türleri, hedef mimarinize uyum sağladıkları için özel bir ilgiyi hak etmektedir. 64 bit sistemlerde bu tipler 64 bit genişliğindeyken, 32 bit sistemlerde 32 bit genişliğindedir. Bu tipler genellikle dizi indeksleme ve bellek ofsetleri için kullanılır, çünkü hedef mimarinin doğal kelime boyutuyla eşleşerek verimli işaretçi aritmetiği ve bellek işlemleri sağlarlar.


Rust, ondalık, onaltılık (`0x`), sekizlik (`0o`) ve ikili (`0b`) biçimler dahil olmak üzere tamsayı değişmezlerini yazmak için birden fazla yol sağlar. Ayrıca, `1000000` yerine `1_000_000` yazmak gibi okunabilirliği artırmak için sayısal değişmezler içinde herhangi bir yerde alt çizgi kullanabilirsiniz. Alt çizgilerin değer üzerinde bir etkisi yoktur, ancak büyük sayıları daha okunabilir hale getirebilir.


Rust'deki kayan nokta türleri basittir: tek hassasiyetli için `f32` ve çift hassasiyetli kayan nokta sayıları için `f64`. F64` türü, daha yüksek hassasiyeti ve modern işlemcilerin 64 bit kayan nokta işlemlerini 32 bit işlemler kadar verimli bir şekilde gerçekleştirebilmesi nedeniyle genellikle tercih edilir.


### Bileşik Tipler ve Veri Organizasyonu


Rust, skaler türlerin ötesinde, birden fazla değeri bir arada gruplayan bileşik türler sağlar. Tuple'lar, farklı türlerdeki değerleri tek bir bileşik değerde birleştirmenize olanak tanır. Parantez kullanarak tuple'lar oluşturursunuz ve her bir öğenin türünü belirtebilirsiniz: `let tup: (i32, f64, u8) = (500, 6.4, 1)`.


Tuple'lar, tek tek değerleri ayıklamanıza olanak tanıyan yıkımı destekler: `let (x, y, z) = tup`. Bu sözdizimi, tuple'ın bileşenlerinden üç ayrı değişken oluşturur. Alternatif olarak, eleman indeksi ile nokta gösterimini kullanarak tuple elemanlarına doğrudan erişebilirsiniz: `tup.0`, `tup.1`, `tup.2`.


```rust
// Creating a tuple with different types
let transaction: (&str, u64, bool) = ("abc123", 50000, true);

// Destructuring: extract all values at once
let (txid, amount, confirmed) = transaction;
println!("Transaction {} for {} sats", txid, amount);

// Dot notation: access individual elements by index
println!("Confirmed: {}", transaction.2);  // true

// Practical example: function returning multiple values
fn parse_utxo(data: &str) -> (String, u32, u64) {
// Returns (txid, output_index, value_in_sats)
("a]1b2c3".to_string(), 0, 100000)
}

let (txid, vout, value) = parse_utxo("raw_data");
println!("UTXO {}:{} = {} sats", txid, vout, value);
```


Rust'taki diziler, türlerinin bir parçası haline gelen sabit bir boyuta sahip oldukları için diğer birçok dildeki dizilerden veya listelerden önemli ölçüde farklıdır. Beş tamsayıdan oluşan bir dizi `[i32; 5]` türüne sahiptir, burada noktalı virgül eleman türünü dizi uzunluğundan ayırır. Bu tür düzeyindeki boyut bilgisi, derleyicinin sınır denetimi yapmasını ve dizileri alan işlevlerin tam olarak kaç öğe beklemeleri gerektiğini bilmelerini sağlar.


Dizileri, tüm öğeleri açıkça listeleyerek başlatabilirsiniz: 1, 2, 3, 4, 5]` veya tekrarlanan değerlere sahip diziler için bir kısaltma sözdizimi kullanarak: `[3; 5]`, tümü 3 değerine sahip beş elemanlı bir dizi oluşturur. Bu kısaltma, tamponları başlatmak veya varsayılan değerlere sahip diziler oluşturmak için kullanışlıdır.


Dizi erişimi çoğu dilde olduğu gibi köşeli ayraç gösterimini kullanır, ancak Rust hem derleme zamanı hem de çalışma zamanı sınır denetimi sağlar. Derleyicinin doğrulayabileceği sabit bir indeksle bir diziye eriştiğinizde, derleme zamanında sınır dışı erişimi yakalayacaktır. Çalışma zamanında belirlenen dinamik indeksler için Rust, geçersiz bir indekse erişmeye çalışırsanız programın paniklemesine neden olacak ve bellek güvenliği ihlallerini önleyecek sınır denetimleri ekler.



## Ownership ve Rust'te Bellek Güvenliği

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


### Rust'ün Bellek Yönetimine Benzersiz Yaklaşımını Anlama


Bu bölüm Rust'in en önemli kavramlarından birini ele almaktadır. Önceki kavramlar diğer dillerden gelen programcılara tanıdık gelebilirken, sahiplik Rust'in çöp toplama olmadan bellek güvenliğini çözme yaklaşımıdır.


Rust, C ve C++ gibi düşük seviyeli dilleri rahatsız eden bellekle ilgili hataları önlemek gibi temel bir hedefle tasarlanmıştır. Bu sorunlar arasında belleğe serbest bırakıldıktan sonra erişildiği use-after-free hataları ve programların tahsis edilen bellek sınırlarının dışına yazıldığı tampon taşmaları yer almaktadır. Bu sorunlara yönelik geleneksel çözümler, Rust'nın ortadan kaldırmaya çalıştığı ödünleşimleri içermektedir. Java ve Go gibi üst düzey diller bellek güvenliğini, otomatik bir sürecin kullanılmayan belleği periyodik olarak tanımladığı ve serbest bıraktığı çöp toplama yoluyla çözmektedir. Bununla birlikte, çöp toplayıcılar performans ek yükü getirir ve program yürütme sırasında öngörülemeyen duraklamalara neden olabilir, bu da onları tutarlı performansın kritik olduğu sistem programlama için uygun hale getirmez.


Rust bellek güvenliğini öncelikle derleme zamanında gerçekleştirilen statik analiz yoluyla sağlar. Derleyici kaynak kodu inceler ve çoğu bellek işleminin çöp toplama gerektirmeden güvenli olup olmadığını belirleyebilir. Çalışma zamanında hesaplanan indekslerle dizi erişimi gibi statik olarak doğrulanamayan durumlar için Rust, tanımlanmamış davranışa izin vermek yerine panikleyen sınır kontrolleri ekler. Bu yaklaşım, başlangıçta kapsamlı statik analiz için tasarlanmamış dillere uyarlanmış olan C ve C++ için mevcut statik analizörlerden temel olarak farklıdır. Rust'nin söz dizimi ve dil kuralları, kapsamlı derleme zamanı doğrulamasını mümkün kılmak için sıfırdan hazırlanmıştır ve bir program başarıyla derlendiğinde, tanımlanmamış davranış sergilemek yerine ya güvenli bir şekilde çalışmasını ya da tahmin edilebilir bir şekilde paniklemesini sağlar.


### Ownership Sistemi: Kurallar ve İlkeler


Rust'in bellek güvenliği garantilerinin temel taşı, bir programın yürütülmesi boyunca belleğin nasıl yönetileceğini düzenleyen sahiplik sistemidir. Ownership, derleyicinin her zaman uyguladığı üç temel kural üzerinde çalışır:


1. Rust'deki her değerin bir sahibi vardır (değeri tutan bir değişken)

2. Aynı anda yalnızca bir sahibi olabilir

3. Sahip kapsam dışına çıktığında, değer düşürülür


Rust'deki kapsamlar, fonksiyon gövdelerinde, koşul bloklarında veya açıkça oluşturulmuş kapsam bloklarında genellikle küme parantezleriyle tanımlanır. Bir kapsam içinde bir değişken tanımlandığında, bu kapsam değişkenin değerinin sahibi olur. Değişken kapsamın ömrü boyunca erişilebilir ve geçerli kalır, ancak yürütme kapsamdan ayrılır ayrılmaz, sahip olunan tüm değişkenler dropping adı verilen bir işlemle otomatik olarak temizlenir.


Bu otomatik temizleme, Rust'ün drop mekanizması aracılığıyla gerçekleştirilir; burada dil, kapsam dışına çıkan değişkenler için dolaylı olarak bir drop işlevi çağırır. Temel tipler için bu basitçe belleğin yeniden kullanıma uygun olarak işaretlendiği anlamına gelir. Kaynakları yöneten daha karmaşık tipler için, özel drop uygulamaları dosya tutamaçlarını kapatmak veya ağ bağlantılarını serbest bırakmak gibi ek temizleme işlemleri gerçekleştirebilir. C++'ın RAII'sinden (Resource Acquisition Is Initialization) ödünç alınan bu model, programcının açık temizleme koduna ihtiyaç duymadan kaynakların her zaman düzgün bir şekilde serbest bırakılmasını sağlar.


### Ownership'ün Taşınması ve Bellek Düzeni


Sahipliğin değişkenler arasında nasıl aktarıldığını anlamak, bellek düzeni ve kopyalama davranışı açısından basit tipler ile karmaşık tipler arasındaki farkı incelemeyi gerektirir. Tamsayılar, booleanlar ve kayan noktalı sayılar gibi basit tipler derleme zamanında sabit, bilinen bir boyuta sahiptir ve verimli bir şekilde kopyalanabilir. Bir tamsayı değişkenini diğerine atadığınızda, Rust değerin tam ve bağımsız bir kopyasını oluşturarak her iki değişkenin de herhangi bir sahiplik endişesi olmadan aynı anda var olmasını sağlar.


Dizeler gibi karmaşık tipler, dinamik olarak tahsis edilen belleği yönettikleri için farklı bir zorluk oluştururlar. Rust'daki bir String, yığında depolanan üç bileşenden oluşur: yığın tarafından tahsis edilen karakter verilerine bir işaretçi, dizenin geçerli uzunluğu ve tahsis edilen arabelleğin toplam kapasitesi. Bu yapı, dizelerin sınırları hakkında bilgi sahibi olurken verimli bir şekilde büyümelerini ve küçülmelerini sağlar. Bir String değişkenini diğerine atadığınızda, Rust bir seçimle karşı karşıya kalır: sadece yığın tabanlı yapıyı kopyalayabilir (aynı yığın verilerine iki işaretçi oluşturarak) veya tüm yığın verilerinin derin bir kopyasını gerçekleştirebilir.


Rust'nin varsayılan davranışı kopyalama yerine sahipliği taşımak, heap verilerini kaynak değişkenden hedef değişkene aktarmak ve kaynağı geçersiz kılmaktır. Bu yaklaşım, birden fazla değişkenin aynı heap belleğini değiştirebileceği veya değişkenler kapsam dışına çıktığında aynı belleğin birden fazla kez serbest bırakılabileceği tehlikeli senaryoyu önler. Taşıma işlemi, potansiyel olarak büyük yığın verilerini değil, yalnızca küçük yığın tabanlı yapıyı kopyaladığı için verimlidir ve tek sahiplik sağlayarak bellek güvenliğini korur.


### Referanslar ve Borçlanma


Sahiplik hareketleri güvenlik sağlarken, bir değeri sahiplik aktarımı yapmadan birden fazla yerde kullanmanız gerektiğinde kısıtlayıcı olabilir. Rust bu sorunu, fonksiyonların ve değişkenlerin sahiplik almadan verilere geçici olarak erişmesine olanak tanıyan ödünç alma yoluyla çözer. Ampersand operatörü kullanılarak oluşturulan bir referans, sahipliği orijinal değişkende bırakırken bir değere salt okunur erişim sağlar.


Referanslar, fonksiyonların verileri tüketmeden üzerinde işlem yapmasını sağlayarak, aynı değerin bir program boyunca birden çok kez kullanılmasını mümkün kılar. Bir fonksiyona bir referans ilettiğinizde, veriyi geçici olarak ödünç vermiş olursunuz ve asıl sahibinin tam kontrolü yeniden kazanabilmesi için fonksiyonun referansı geri vermesi gerekir. Bu ödünç alma metaforu, erişimin geçici doğasını yansıtır: tıpkı bir arkadaşınıza sahipliğini koruyarak bir kitap ödünç vermeniz gibi, referanslar da orijinal sahiplik ilişkisini korurken geçici erişime izin verir.


Değiştirilebilir referanslar, ödünç alınan verilerin değiştirilmesine izin vermek için bu kavramı genişletir, ancak güvenliği korumak için katı kısıtlamalar vardır. Rust, herhangi bir zamanda bir veri parçasına yalnızca bir değiştirilebilir referansa izin vererek, bir programın birden fazla bölümünün aynı anda aynı belleği değiştirebileceği veri yarışlarını önler. Ayrıca, aynı veriye aynı anda hem değiştirilebilir hem de değiştirilemez referanslar veremezsiniz, çünkü bu durum kodun veriyi sabit kabul ederken diğer kodun aktif olarak değiştirdiği durumlara yol açabilir. Bu kurallar derleme zamanında uygulanır ve diğer sistem programlama dillerini rahatsız eden eşzamanlılık hatalarının tüm sınıflarını ortadan kaldırır.


```rust
fn main() {
let mut wallet_balance: u64 = 100_000; // 100,000 satoshis

// Immutable borrow: read the balance
let balance_ref = &wallet_balance;
println!("Current balance: {} sats", balance_ref);
// balance_ref goes out of scope here

// Mutable borrow: update the balance
let balance_mut = &mut wallet_balance;
*balance_mut += 50_000; // Receive payment
println!("After deposit: {} sats", balance_mut);
// balance_mut goes out of scope here

// Function that borrows immutably
fn display_balance(balance: &u64) {
println!("Balance check: {} sats", balance);
}

// Function that borrows mutably
fn deduct_fee(balance: &mut u64, fee: u64) {
*balance -= fee;
}

display_balance(&wallet_balance);
deduct_fee(&mut wallet_balance, 1_000);
println!("After fee: {} sats", wallet_balance); // 149,000
}
```


### Dize Türleri ve Dilimleri


Rust, farklı bellek yönetimi stratejilerini ve kullanım durumlarını yansıtan string değişmezleri ve String türü arasında ayrım yapar. Dize değişmezleri doğrudan derlenmiş ikili dosyaya gömülür ve değişmez dize verilerinin bir görünümünü temsil eden &str (dize dilimi) türüne sahiptir. Bu değişmezler, çalışma zamanı tahsisi gerektirmedikleri için verimlidir, ancak program kodunun bir parçası oldukları için değiştirilemezler.


Buna karşın String türü dinamik olarak ayrılan belleği yönetir ve çalışma zamanında büyüyebilir, küçülebilir ve değiştirilebilir. String::from() veya benzer yöntemleri kullanarak bir değişmezden bir String oluşturabilirsiniz, bu da yığın belleği ayırır ve değişmezin içeriğini kopyalar. Bu ayrım, Rust'in hem performans (mümkün olduğunda değişmezleri kullanma) hem de esneklik (değişiklik gerektiğinde String kullanma) için optimize edilmesini sağlar.


Dize dilimleri (&str), verileri kopyalamadan dizelerin bölümleriyle çalışmak için güçlü bir soyutlama sağlar. Bir dilim, dize verilerinin başlangıcına bir işaretçi ve alt dizelere verimli bir şekilde başvurmanıza olanak tanıyan bir uzunluk içerir. Dilim sözdizimi, dizenin hangi bölümüne başvurulacağını belirtmek için aralıklar (örneğin, &s[0..5]) kullanır. Dilimler referans olduklarından, ödünç alma kurallarına tabidirler ve dilimler mevcutken temel dizenin değiştirilmesini önlerler. Bu derleme zamanı uygulaması, orijinal dize serbest bırakıldıktan veya değiştirildikten sonra geçersiz belleğe erişmek gibi yaygın hataları önler.


### Diziler, Vektörler ve Genel Dilimler


Dilim kavramı, dizelerin ötesinde herhangi bir öğe dizisine kadar uzanır ve hem sabit boyutlu dizilerle hem de dinamik vektörlerle çalışmak için birleşik bir yol sağlar. Rust'deki dizilerin uzunlukları türlerinde kodlanmıştır (örneğin, beş adet 32 bit tamsayıdan oluşan bir dizi için [i32; 5]), bu da onları derleme zamanı boyut garantileri gerektiren durumlar için uygun hale getirir. Dizileri kabul eden işlevler, tam uzunluk gereksinimlerini uygulayabilir, bu da tam olarak boyutlandırılmış girdilere ihtiyaç duyan kriptografik işlevler gibi işlemler için yararlıdır.


Dilimler (&[T]) daha esnek bir alternatif sunar ve altta yatan depolamadan bağımsız olarak herhangi bir bitişik öğe dizisinin görünümünü temsil eder. Dizilerden, vektörlerden veya diğer dilimlerden dilimler oluşturabilirsiniz ve aynı dilim, kullanım ömrü boyunca farklı veri bölümlerine başvurabilir. Bu esneklik, dilimleri, belirli depolama mekanizmasını veya tam boyutu önemsemeden dizileri işlemesi gereken işlevler için ideal hale getirir.


Sahipli tipler (String, Vec<T>) ve ödünç alınan dilim karşılıkları (&str, &[T]) arasındaki ilişki Rust boyunca tutarlı bir model izler. Sahip olunan tipler belleklerini yönetir ve değiştirilebilirken, dilimler bu verilerin bölümlerine verimli, salt okunur erişim sağlar. Bu tasarım, ödünç alma sistemi aracılığıyla Rust'ün güvenlik garantilerini korurken, hem esnek (dilimler aracılığıyla çeşitli girdi türlerini kabul eden) hem de verimli (gereksiz kopyalamadan kaçınan) API'ler sağlar.



## Yapılar, Karmaşık Veri Türleri Oluşturma

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

Rust'teki yapılar, diğer programlama dillerindeki sınıflara benzer şekilde karmaşık veri türleri oluşturmak için temel görevi görür. Birbiriyle ilişkili verileri, farklı türlerde birden fazla alan içerebilen tek ve uyumlu bir birim halinde gruplandırmanıza olanak tanırlar. Bir yapıyı tanımlamak için sözdizimi basit bir model izler: `struct` anahtar sözcüğünü ve ardından yapı adını kullanırsınız, ardından her alanın türünü belirtmek için iki nokta üst üste sözdizimi kullanarak alanları küme parantezleri içinde tanımlarsınız.


Rust, derleyicinin uyarılar yoluyla uygulayacağı yapılar için belirli adlandırma kurallarını izler. Yapı adları CamelCase (PascalCase olarak da bilinir) kullanırken, yapı içindeki alan adları alt çizgi ile snake_case kullanmalıdır. Bu kural, Rust kod tabanları arasında tutarlılığın korunmasına yardımcı olur ve kodu diğer geliştiriciler için daha okunabilir hale getirir.


Yapıların örneklerini oluşturmak, yapının adını ve ardından alan atamalarını içeren küme parantezlerini kullanarak tüm alanlar için değerler belirtmenizi gerektirir. Bir yapı örneğine sahip olduğunuzda, örneğin değiştirilebilir olarak bildirilmesi koşuluyla, nokta gösterimini kullanarak tek tek alanlara erişebilir ve bunları değiştirebilirsiniz. Bu nokta gösterimi, işaretçiler ve doğrudan nesneler için farklı operatörler kullanabileceğiniz C++ gibi dillerin aksine, Rust'da tutarlı bir şekilde çalışır.


### Kurucu İşlevler ve Alan Kısayolları


Rust, bazı nesne yönelimli diller gibi yerleşik kuruculara sahip değildir, ancak aynı amaca hizmet etmek için yapı örneklerini döndüren işlevler oluşturabilirsiniz. Bu kurucu fonksiyonlar tipik olarak bazı veya tüm alanlar için parametre alır ve diğerleri için varsayılan değerleri ayarlayabilir. Bu tür fonksiyonları yazarken, Rust kullanışlı bir steno sağlar: eğer bir parametre bir yapı alanıyla aynı isme sahipse, alan ismini `field: value` formatında tekrarlamak yerine sadece bir kez yazabilirsiniz.


Yapı örnekleri, struct güncelleme sözdizimi kullanılarak mevcut örneklerden değerler kopyalanarak da oluşturulabilir. Bu özellik, yalnızca değiştirmek istediğiniz alanları belirtirken, diğer tüm alanların mevcut bir örnekten kopyalanmasıyla yeni bir örnek oluşturmanıza olanak tanır. Ancak, bu işlem Rust'in sahiplik kurallarını takip eder, bu da Kopyalanmayan türlerin kaynak örnekten taşınacağı ve potansiyel olarak orijinal örneğin parçalarını daha sonra kullanılamaz hale getireceği anlamına gelir. Derleyici bu kısmi taşımaları akıllıca izler ve taşınan alanlara erişimi engellerken taşınmayan alanları kullanmaya devam etmenizi sağlar.


### Tuple Yapıları ve Birim Yapıları


Rust, isim yerine indeksle erişilen isimsiz alanlara sahip yapılar olan tuple yapılarını destekler. Bunlar basit sarmalayıcı tipler için veya bir yapıya ihtiyaç duyduğunuzda ancak adlandırılmış alanlara gerek duymadığınızda kullanışlıdır. Tuple yapı alanlarına, ilk alan için `.0`, ikinci alan için `.1` gibi nokta gösterimini ve ardından alan indeksini kullanarak erişirsiniz. Bu yaklaşım, tek bir değeri saran veya adların gereksiz olabileceği birkaç yakın ilişkili değer içeren yapılar için iyi çalışır.


Birim yapıları, yapıların en basit biçimini temsil eder; hiçbir veri içermezler. Bu başlangıçta anlamsız görünse de, birim yapıları Rust'ın özellik sistemi ile çalışırken değerli hale gelir, çünkü herhangi bir veri depolamadan davranışları uygulayabilirler. Bu boş yapılar, daha gelişmiş Rust modellerinde işaretleyici veya yer tutucu görevi görür.


### Yöntemler ve İlişkili Fonksiyonlar


Yapılar, uygulama blokları aracılığıyla davranış eklediğinizde ek işlevsellik kazanır. Yapı adının ardından `impl` anahtar sözcüğünü kullanarak, yapınızın örnekleri üzerinde çalışan yöntemler tanımlayabilirsiniz. Metotlar, ilk parametre olarak `self` alan fonksiyonlardır; bu parametre, metodun örnekle ne yapması gerektiğine bağlı olarak sahip olunan bir değer (`self`), değişmez bir referans (`&self`) veya değişebilir bir referans (`&mut self`) olabilir.


Self` parametre tipinin seçimi, metodun sahiplikle ilgili davranışını belirler. Self` alan metotlar sahiplik almadan örnekten okuyabilir, bu da onları yapıyı değiştirmeyen işlemler için uygun hale getirir. &mut self` alan metotlar, çağıranın sahipliğini korumasına izin verirken örneği değiştirebilir. Self` değerini alan metotlar örneği tüketir, bu da yapıyı başka bir şeye dönüştüren işlemler için veya metot bu örnek üzerindeki son işlemi temsil ettiğinde uygundur.


İlişkili fonksiyonlar, bir uygulama bloğu içinde tanımlanan ve parametre olarak `self` almayan fonksiyonlardır. Bunlar diğer dillerdeki statik yöntemlere benzer ve genellikle türle ilgili kurucular veya yardımcı işlevler olarak kullanılır. İlişkili fonksiyonları çift iki nokta üst üste sözdizimini (`Type::function_name()`) kullanarak çağırırsınız, bu da onları örnekler üzerinde çağrılan yöntemlerden açıkça ayırır.


```rust
// Define a struct for a Lightning invoice
struct Invoice {
payment_hash: String,
amount_msat: u64,
description: String,
expiry_secs: u32,
}

impl Invoice {
// Associated function (constructor) - no self parameter
fn new(payment_hash: String, amount_msat: u64, description: String) -> Self {
Invoice {
payment_hash,
amount_msat,
description,
expiry_secs: 3600, // default 1 hour
}
}

// Method with &self - read-only access
fn amount_sats(&self) -> u64 {
self.amount_msat / 1000
}

// Method with &mut self - can modify the instance
fn extend_expiry(&mut self, additional_secs: u32) {
self.expiry_secs += additional_secs;
}

// Method with self - consumes the instance
fn into_payment_request(self) -> String {
format!("lnbc{}n1p{}", self.amount_msat, self.payment_hash)
}
}

fn main() {
// Use associated function to create instance
let mut invoice = Invoice::new(
"abc123".to_string(),
100_000_000, // 100,000 sats in millisats
"Coffee payment".to_string(),
);

println!("Amount: {} sats", invoice.amount_sats());
invoice.extend_expiry(1800); // Add 30 minutes

let request = invoice.into_payment_request();
// invoice is now consumed, cannot be used anymore
println!("Payment request: {}", request);
}
```


#### Numaralandırmalar: Seçeneklerin ve Varyantların Modellenmesi


Rust'deki numaralandırmalar, diğer birçok dildeki enum'lardan daha fazla yeteneğe sahiptir. Adlandırılmış sabitlerin basit kümelerini temsil edebilirken, Rust enum'ları her bir varyant içinde veri de taşıyabilir, bu da onları bir değerin birkaç farklı tür veya durumdan biri olabileceği durumları modellemek için uygun hale getirir. Her enum değişkeni, hiç veri içermeyenden adlandırılmış alanlara sahip karmaşık yapılara kadar farklı türde ve miktarda veri içerebilir.


Enum varyantlarına veri ekleme yeteneği, diğer dillerde bulunan birçok yaygın programlama hatasını ortadan kaldırır. Bir tip göstergesi ve ilişkili veriler için ayrı değişkenler tutmak yerine (ki bu değişkenler kolayca tutarsız hale gelebilir) Rust enum'ları tip bilgisini verinin kendisiyle bir araya getirir. Bu tasarım, verilerin her zaman varyantla eşleşmesini sağlayarak çalışma zamanı hatalarına yol açabilecek uyumsuzlukları önler.


Enum varyantları çeşitli biçimlerde veri içerebilir: basit bayraklar için veri yok, isimsiz alanlar için tuple benzeri veri veya isimli alanlarla struct benzeri veri. Hatta her bir varyant için en uygun formu seçerek bu stilleri tek bir enum içinde karıştırabilirsiniz. Bu esneklik, enum'ları farklı durumların farklı bilgiler gerektirdiği karmaşık etki alanı kavramlarını modellemek için uygun hale getirir.


#### Seçenek Türü: Devamsızlığı Güvenle Ele Almak


Rust'ün en önemli enumlarından biri, mevcut olabilecek veya olmayabilecek değerleri temsil eden `Option<T>`'dir. Bu enumun iki çeşidi vardır: T tipinde bir değer içeren `Some(T)` ve bir değerin yokluğunu temsil eden `None`. Option türü, Rust'ün diğer birçok dili rahatsız eden null pointer sorunlarına çözümü olarak hizmet eder ve geliştiricileri değerlerin eksik olabileceği durumları açıkça ele almaya zorlar.


Option türlerini kullanmak kodunuzu daha sağlam hale getirir, çünkü derleyici değerlerin hem varlığını hem de yokluğunu ele almanızı gerektirir. Potansiyel olarak eksik bir değeri, önce var olup olmadığını kontrol etmeden yanlışlıkla kullanamazsınız. Bu açık işleme, diğer programlama dillerinde yaygın hata kaynakları olan null pointer istisnalarını ve benzer çalışma zamanı hatalarını önler.


Option türü, Rust'ün kalıp eşleştirme sistemiyle bütünleşerek her iki durumu da ele almanıza olanak tanır. Unwrap_or()` gibi yöntemler, geri dönüş varsayılanlarıyla değerleri ayıklamak için uygun yollar sağlarken, `map()` ve `and_then()` gibi yöntemler isteğe bağlı değerlerle çalışmak için işlevsel programlama kalıpları sağlar.


### Eşleştirme İfadeleri ile Desen Eşleştirme


Match` ifadeleri aracılığıyla kalıp eşleştirme, enum'lar ve diğer veri türleriyle çalışmak için bir yol sağlar. Bir eşleşme ifadesi bir değeri inceler ve değerin hangi desenle eşleştiğine bağlı olarak farklı kodlar yürütür. Her kalıp, eşleşen değerin parçalarını ilgili kod bloğunda kullanılabilecek değişkenlere bağlayarak değeri yeniden yapılandırabilir.


Eşleştirme ifadeleri kapsamlı olmalıdır, yani eşleştirilen tür için mümkün olan her durumu ele almalıdır. Bu gereklilik, belirli durumların yanlışlıkla işlenmeden bırakılması durumunda oluşabilecek hataları önler. Her durumu açıkça ele almak istemediğinizde, kalan tüm durumları yakalamak için joker karakter kalıbını (`_`) kullanabilir veya değere erişmeniz gerekiyorsa işlenmemiş durumları bir değişkene bağlayabilirsiniz.


If let` yapısı, yalnızca belirli bir kalıbı önemsediğinizde eşleşmeye daha özlü bir alternatif sağlar. Bu sözdizimi özellikle Seçenek türleriyle çalışırken veya yalnızca bir değer belirli bir enum varyantıyla eşleşiyorsa kod çalıştırmak istediğinizde kullanışlıdır. If let` yapısı, kalıbın eşleşmediği durumlar için bir `else` cümlesi içerebilir, bu da onu basit kalıp eşleştirme senaryolarını ele almanın kolaylaştırılmış bir yolu haline getirir.


#### Koleksiyonlar: Veri Gruplarını Yönetme


Rust'in standart kütüphanesi, ilgili veri gruplarını yönetmek için çeşitli koleksiyon türleri sağlar. Bu koleksiyonlar geneldir, yani her türden öğeyi saklayabilirler ve bellek yönetimini otomatik olarak gerçekleştirirler. En yaygın kullanılan koleksiyonlar sıralı listeler için vektörler, anahtar-değer ilişkileri için hash eşlemeleri ve metin verileri için dizelerdir.


#### Vektörler: Dinamik Diziler


Vektörler, programın yürütülmesi sırasında boyutu değişebilen, büyütülebilir dizileri temsil eder. Sabit boyutlu dizilerin aksine, vektörler heap üzerinde bellek ayırır ve gerektiğinde genişleyebilir veya daralabilir. Derleyicinin vektörün ne tür öğeler içereceğini bilmesi gerektiğinden, boş bir vektörle başlarken bir vektör oluşturmak genellikle açık tür açıklaması gerektirir.


Vektörler, her biri farklı güvenlik özelliklerine sahip öğelere erişmek için birden fazla yol sağlar. Dizin gösterimi (`vec[0]`) doğrudan erişim sağlar, ancak dizin sınırların dışındaysa panik yapar. Get()` yöntemi bir `Option` döndürerek sınır dışı erişimi zarif bir şekilde ele almanızı sağlar. Bu yaklaşımlar arasındaki seçim, dizinin geçerli olduğunu garanti edip edemeyeceğinize veya olası hataları ele almanız gerekip gerekmediğine bağlıdır.


Rust'nın ödünç alma kuralları vektörler için geçerlidir ve yaygın bellek güvenliği sorunlarını önler. Bir vektör elemanına referans tutuyorsanız, bu referans kapsam dışına çıkana kadar vektörü değiştiremezsiniz. Bu, yeni elemanlar itmek veya vektörü temizlemek gibi vektör işlemlerinden sonra referansların ayrılmış belleği işaret edebileceği durumları önler.


#### Hash Haritaları: Anahtar-Değer Depolama


Hash eşlemeleri, ilişkili anahtarlarına göre değerleri hızlı bir şekilde arayabileceğiniz verimli anahtar-değer depolaması sağlar. Hem anahtarlar hem de değerler herhangi bir türde olabilir, ancak anahtarlar karma ve eşitlik karşılaştırması için gerekli özellikleri uygulamalıdır. Hash eşlemeleri, değerler Copy özelliğini uygulamadığı sürece eklenen değerlerin sahipliğini alır.


Hash eşlemeleri değer eklemek ve güncellemek için çeşitli yöntemler sunar. Temel `insert()` yöntemi mevcut değerlerin üzerine yazarken, `entry()` daha esnek bir ekleme mantığı sağlar. Giriş API, değerleri yalnızca zaten mevcut değillerse eklemenize veya mevcut değerleri mevcut durumlarına göre güncellemenize olanak tanır. Bu API, oluşumları saymak veya çalışan toplamları korumak gibi modeller için kullanışlıdır.


Hash eşlemelerinden değerler alınırken, istenen anahtar mevcut olmayabileceğinden `get()` yöntemi bir `Option` döndürür. Kopya türleri için `Option<&T>`den `Option<T>`ye dönüştürmek için `copied()` ve anahtarlar eksik olduğunda varsayılan değerler sağlamak için `unwrap_or()` gibi yöntemleri kullanabilirsiniz.


### Dize İşleme ve Unicode


Rust'deki dizeler UTF-8 kodludur, bu da tam Unicode desteği sağlar ancak basit ASCII dizelerine kıyasla karmaşıklık getirir. String` türü sahip olunan, büyütülebilir metin verilerini temsil ederken, dize dilimleri (`&str`) dize verilerine ödünç alınmış görünümler sağlar. Bu türler arasında gerektiği gibi dönüşüm yapabilirsiniz; dize dilimleri genellikle hem sahip olunan dizeleri hem de dize değişmezlerini kabul etmek için işlev parametreleri için kullanılır.


Dize manipülasyonu, metin ekleme, birden fazla değeri birlikte biçimlendirme ve alt dizeleri ayıklama yöntemlerini içerir. Push_str()` yöntemi sahiplik almadan dize dilimleri eklerken, `format!` makrosu birden fazla bileşenden dize oluşturmak için esnek bir yol sağlar. Dize dizinleriyle çalışırken, çalışma zamanı paniklerinden kaçınmak için UTF-8 karakter sınırlarına uymaya dikkat etmelisiniz.


Karakter karakter güvenli işleme için, dizeler Unicode skaler değerleri için `chars()` ve ham bayt erişimi için `bytes()` gibi yineleyici yöntemleri sağlar. Bu yineleyiciler UTF-8 kodlamasını doğru şekilde işleyerek çok baytlı karakterleri yanlışlıkla bölmemenizi sağlar. Bu yaklaşım, özellikle karmaşık Unicode karakterleri içerebilen uluslararası metinlerle çalışırken manuel indekslemeden daha güvenli ve daha güvenilirdir.



## Rust'ün İki Kategorili Hata İşleme Sistemi

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

Rust, çoğu programlama diline kıyasla hata işleme konusunda temelde farklı bir yaklaşım benimser. Birçok dil öncelikli olarak istisnalara dayanırken, Rust iki farklı hata kategorisi arasında ayrım yapar ve her bir türün ele alınması için özel mekanizmalar sağlar. Bu bölüm, Rust'ün hem program yürütmesini sonlandıran kurtarılamaz hataları hem de programların zarif bir şekilde çalışmaya devam etmesini sağlayan kurtarılabilir hataları kapsayan kapsamlı hata işleme sistemini incelemektedir.


### Telafi Edilemeyen Hatalar ve Panik


Kurtarılamayan hatalar, programın güvenli bir şekilde kurtarılamayacağı tutarsız veya beklenmedik bir duruma girdiği durumları temsil eder. Bunlar arasında bir diziye sınırların dışında erişilmesi, bellek güvenliğini ihlal eden işlemlerin denenmesi veya temel program mantığı hatalarını gösteren koşullarla karşılaşılması gibi senaryolar yer alır. Bu tür hatalar oluştuğunda, uygun yanıt daha fazla bozulma veya tanımlanmamış davranış riskine girmek yerine programı derhal sonlandırmaktır.


Rust'te kurtarılamayan hatalar paniği tetikler ve bu da programın kontrollü bir şekilde çökmesine neden olur. Sonlandırmadan önce Rust, paniğin tam olarak nerede meydana geldiğini gösteren ayrıntılı bir yığın izi sağlamak için çağrı yığını boyunca geri yürüdüğü çözme adı verilen bir işlem gerçekleştirir. Bu çözme işlemi, geliştiricilerin hata ayıklama sırasında sorunun kaynağını belirlemelerine yardımcı olur. Performans açısından kritik uygulamalar veya gömülü sistemler için, çözme işlemini devre dışı bırakabilir ve Rust'i bir panik oluştuğunda hemen sonlandıracak şekilde yapılandırabilirsiniz, ancak bu, daha hızlı sonlandırma için hata ayıklama bilgilerinden ödün verir.


Özel bir mesajla birlikte `panic!` makrosunu kullanarak paniği açıkça tetikleyebilirsiniz. Bir panik oluştuğunda, hangi iş parçacığının paniklediğini ve ilgili mesajı gösteren bir çıktı görürsünüz. RUST_BACKTRACE` ortam değişkeninin ayarlanması, paniğe yol açan çağrı yığınının tamamını göstererek ek hata ayıklama bilgileri sağlar. Örneğin, yalnızca üç öğe içeren bir vektörün 99. öğesine erişmeye çalışmak, hataya neden olan işlev çağrılarının tam sırasını gösteren bir geri izleme ile birlikte "index out of bounds" mesajıyla bir panik generate olacaktır.


### Sonuç ile Kurtarılabilir Hatalar


Kurtarılabilir hatalar, programların sonlandırılmadan zarif bir şekilde ele alabileceği beklenen hata koşullarını temsil eder. Örnekler arasında mevcut olmayan bir dosyayı açmaya çalışmak, ağ bağlantısı hataları veya geçersiz kullanıcı girdisi yer alır. Bu durumlar için Rust, başarısız olabilecek işlemleri açıkça temsil eden ve geliştiricileri hem başarı hem de başarısızlık durumlarını ele almaya zorlayan `Result` enumunu sağlar.


Sonuç` enumu iki değişkenle tanımlanır: `T` tipinde bir değer içeren başarılı işlemler için `Ok(T)` ve `E` tipinde bir hata içeren başarısızlıklar için `Err(E)`. Bu tasarım, olası başarısızlıkların göz ardı edilemeyeceğinden emin olmak için Rust'in tip sistemini kullanır. Başarısız olabilecek fonksiyonlar bir `Result` döndürür ve çağıran kod, tipik olarak `match` ifadeleriyle desen eşleştirme kullanarak hem başarı hem de hata durumlarını açıkça ele almalıdır.


Bir `Result<File, std::io::Error>` döndüren `File::open` fonksiyonunu düşünün. Bir dosyayı açarken, başarılı olursa bir `File` nesnesi veya işlem başarısız olursa bir `std::io::Error` alırsınız. Her durumu uygun şekilde ele almak için bu sonucu eşleştirebilirsiniz. Başarı durumunda dosya işlemlerine devam edebilir, hata durumunda ise dosyayı oluşturmayı deneyebilir, alternatif bir yaklaşım deneyebilir veya hatayı çağıran koda iletebilirsiniz. Bu açık işleme, programınızın beklenmedik bir şekilde çökmek yerine hata kurtarma konusunda bilinçli kararlar almasını sağlar.


### Hata İşleme Kalıpları ve Kısayolları


Açık kalıp eşleştirme hata işleme üzerinde tam kontrol sağlarken, Rust yaygın hata işleme kalıpları için çeşitli kolaylık yöntemleri sunar. Unwrap` yöntemi bir `Result`tan başarı değerini çıkarır, ancak bir hata oluşursa panik yapar, bu da hızlı prototip oluşturma veya bir işlemin başarılı olacağından emin olduğunuz durumlar için kullanışlıdır. Expect` yöntemi de benzer şekilde çalışır, ancak özel bir panik mesajı sağlamanıza olanak tanıyarak işler ters gittiğinde hata ayıklamayı kolaylaştırır.


Daha esnek hata işleme için, `unwrap_or_else` gibi yöntemler, bir hata oluştuğunda çalışan bir kapatma sağlayarak özel kurtarma mantığını etkinleştirmenize olanak tanır. Her adım için farklı hata işleme stratejileri ile bir dosyayı açmaya çalışmak ve mevcut değilse oluşturmak gibi karmaşık senaryoları işlemek için bu işlemleri birbirine zincirleyebilirsiniz.


Soru işareti operatörü (`?`), Rust programlarında yaygın olan hata yayılımı için kısa bir sözdizimi sağlar. Bir `Sonuç` türüne `?` eklediğinizde, başarılı değerleri otomatik olarak çözer ve hataları geçerli işlevden hemen döndürür. Bu operatör yalnızca `Result` türlerini döndüren fonksiyonlarda kullanılabilir ve hataların çağrı yığınında düzgün bir şekilde yayılmasını sağlar. ? operatörü, açık hata yayılımı semantiğini korurken ayrıntılı eşleşme ifadelerini ortadan kaldırarak hata işleme kodunu çok daha okunabilir hale getirir.


```rust
use std::fs::File;
use std::io::{self, Read};

// Custom error type for wallet operations
#[derive(Debug)]
enum WalletError {
FileNotFound,
InvalidFormat,
InsufficientFunds,
}

// Function returning Result for recoverable errors
fn load_wallet_balance(path: &str) -> Result<u64, WalletError> {
// Simulate reading from file
let balance_str = "150000"; // Would normally read from file
balance_str
.parse::<u64>()
.map_err(|_| WalletError::InvalidFormat)
}

// Using the ? operator for clean error propagation
fn send_payment(amount: u64) -> Result<String, WalletError> {
let balance = load_wallet_balance("wallet.dat")?; // Propagates error if it fails

if balance < amount {
return Err(WalletError::InsufficientFunds);
}

Ok(format!("Sent {} sats, remaining: {}", amount, balance - amount))
}

fn main() {
// Handle the Result explicitly
match send_payment(50_000) {
Ok(msg) => println!("Success: {}", msg),
Err(WalletError::InsufficientFunds) => println!("Error: Not enough funds"),
Err(WalletError::FileNotFound) => println!("Error: Wallet file not found"),
Err(WalletError::InvalidFormat) => println!("Error: Corrupted wallet file"),
}

// Or use unwrap_or_else for custom fallback
let result = send_payment(200_000)
.unwrap_or_else(|e| format!("Payment failed: {:?}", e));
println!("{}", result);
}
```


### Hata Yayılımı ve Fonksiyon Tasarımı


Hata yayılımı, Rust hata işlemede temel bir kavramdır ve fonksiyonların hataları yerel olarak ele almak yerine çağrı yığınına aktarmasına olanak tanır. Başarısız olabilecek fonksiyonlar tasarlarken, çağıranlara hataları nasıl ele alacaklarına karar verme esnekliği sağlamak için `Result` tipleri döndürmelisiniz. Bu yaklaşım, çağrı zincirindeki her fonksiyonun hataları yerel olarak ele alabileceği veya kurtarma kararları vermek için daha fazla içeriğe sahip olan daha üst düzey koda aktarabileceği birleştirilebilir hata işlemeyi teşvik eder.


Soru işareti operatörü hata yayılımını basitleştirir. Başarısız olma ihtimali olan her işlem için ayrıntılı eşleşme ifadeleri yazmak yerine, işlemleri `?` işleçleriyle birbirine zincirleyebilir ve oluşan hataları otomatik olarak yayarken başarı yolunu işleyen okunabilir bir kod oluşturabilirsiniz. Bu model o kadar yaygındır ki, birçok Rust işlevi özellikle `?` operatörüyle iyi çalışacak şekilde tasarlanmıştır ve kod tabanınız boyunca akıcı hata işleme olanağı sağlar.


Panikleme ile hata döndürme arasında karar verirken, çağıran kodun hatadan makul bir şekilde kurtulup kurtulamayacağını göz önünde bulundurun. Hata bir programlama hatasını veya kurtarılamaz bir sistem durumunu temsil ediyorsa paniklemek uygundur. Ancak, hata, çağıran kodun bağlama bağlı olarak farklı şekilde ele alabileceği beklenen bir durumsa, bir `Sonuç` döndürmek daha iyi esneklik ve birleştirilebilirlik sağlar.


### En İyi Uygulamalar ve Tasarım Hususları


Rust'te etkili hata işleme, ne zaman panik yapılacağı ve ne zaman hata döndürüleceği konusunda dikkatli olunmasını gerektirir. Geçerli olduğunu bildiğiniz kodlanmış verilere erişmek gibi programlama hatalarını veya doğru programlarda asla oluşmaması gereken durumları temsil eden durumlar için panikleri kullanın. Örneğin, doğru olduğunu doğruladığınız sabit kodlanmış bir IP adresi dizesini ayrıştırmak için, işlemin neden asla başarısız olmaması gerektiğini açıklayan açıklayıcı bir mesajla birlikte `expect` güvenle kullanılabilir.


Kullanıcı kontrollü girdi veya harici sistem etkileşimleri için paniğe kapılmak yerine her zaman `Sonuç` türlerini döndürmeyi tercih edin. Kullanıcılar hata yapar, dosyalar silinir ve ağ bağlantıları başarısız olur - bunlar iyi tasarlanmış programların incelikle ele alması gereken normal durumlardır. Bu durumlar için hata döndürerek, çağıran kodun uygun kurtarma stratejilerini uygulamasına izin verirsiniz; bu, ister kullanıcıdan farklı bir girdi istemek, ister varsayılan değerlere geri dönmek veya yardımcı hata mesajları görüntülemek olsun.


Geçersiz durumların programınıza yayılmasını önlemek için yapım sırasında doğrulamayı zorunlu kılan özel türler oluşturmayı düşünün. Örneğin, programınız belirli bir aralıktaki sayıları gerektiriyorsa, yapım sırasında girdiyi doğrulayan ve geçersiz örnekler oluşturmanın hiçbir yolunu sağlamayan bir sarmalayıcı tür oluşturun. Bu yaklaşım, geçersiz durumları temsil edilemez hale getirerek tüm hata sınıflarını ortadan kaldırmak için Rust'ün tip sistemini kullanır ve kod tabanınız boyunca çalışma zamanı hata denetimi ihtiyacını azaltır.


## Fonksiyonel Programlama Özellikleri, Kapanışlar ve Akıllı İşaretçiler


<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

Rust saf bir fonksiyonel programlama dili olmamakla birlikte, fonksiyonel programlama paradigmalarından esinlenen özellikler içermektedir. Bu özellikler, geliştiricilerin kapanışlar ve yineleyiciler gibi kavramlardan yararlanarak kısa ve öz kod yazmalarını sağlar. Rust, veri işleme ve geri arama mekanizmaları için esnek araçlar sağlamak üzere bu işlevsel öğeleri içerir.


Rust'daki fonksiyonel programlama özellikleri, dilin temel ilkeleri olan bellek güvenliği ve sıfır maliyetli soyutlamaları korur. Kapanışları ve yineleyicileri kullandığınızda, ifade için performanstan ödün vermezsiniz - Rust derleyicisi, geleneksel döngü tabanlı yaklaşımlarla karşılaştırılabilir verimli makine kodu üretmek için bu yapıları optimize eder.


### Kapanışları Anlamak


Rust'deki Closure'lar, çevrelerindeki değişkenleri yakalayabilen anonim fonksiyonlardır. Diğer programlama dillerinde bunlar genellikle lambda fonksiyonları olarak adlandırılır. Kapanışların temel özelliği, çevrelerini "kapatma" yetenekleridir, yani kapanışın tanımlandığı kapsamda var olan değişkenlere erişebilir ve bunları kullanabilirler.


Closure'ların sözdiziminde parametreleri tanımlamak için parantezler yerine boru karakterleri (`|`) kullanılır. Parametreleri olmayan bir closure için `||` yazarsınız ve parametreleri olan closure'lar için bunları `|x, y|` gibi borular arasında listelersiniz. Closure gövdesi tek bir ifadeden oluşuyorsa, küme parantezlerini atlayarak sözdizimini çok kısa hale getirebilirsiniz.


Müşteri tercihlerine göre özel tişörtler veren bir tişört şirketinin bu pratik örneğini düşünün. Bir müşteri favori rengini belirtmişse, o rengi alır; aksi takdirde, varsayılan olarak en çok stoklanan rengi alır. Kapanışları kullanarak bu mantık şu hale gelir: user_preference.unwrap_or_else(|| self.most_stocked())`. Self.most_stocked()` closure'u yalnızca gerektiğinde varsayılan değeri sağlar ve `self` öğesine kendi ortamından erişebilir.


### Kapanış Türü Çıkarsaması ve Esneklik


Rust'in closure'larla ilgili en kullanışlı özelliklerinden biri otomatik tip çıkarımıdır. Parametre türlerini ve dönüş türlerini açıkça belirtmeniz gereken normal fonksiyonların aksine, closure'lar genellikle bu türleri bağlamdan çıkarabilir. Derleyici closure'un nasıl kullanıldığını analiz eder ve uygun tipleri otomatik olarak belirler. Ancak, bir closure belirli türlerle çağrıldığında, bu türler o closure örneği için sabit hale gelir.


Kapanışları tıpkı diğer değerler gibi değişkenlerde saklayabilirsiniz, bu da onları dilde birinci sınıf vatandaş yapar. Bir değişkene bir closure atadığınızda, daha sonra parantez kullanarak onu çağırabilirsiniz: let my_closure = |x| x + 1; let result = my_closure(5);`. Bu esneklik, closure'ları fonksiyonlara argüman olarak aktarmanıza, fonksiyonlardan döndürmenize ve veri yapılarında kullanmanıza olanak tanır.


Derleyici türleri çıkaramıyorsa veya açık olmak istiyorsanız, fonksiyonlara benzer sözdizimi kullanarak kapanış parametrelerine ve dönüş türlerine açıklama ekleyebilirsiniz: `|x: i32| -> i32 { x + 1 }`. Bu açık yazım bazen derleyicinin türleri doğru şekilde çözümlemek için ek bilgiye ihtiyaç duyduğu karmaşık senaryolarda gereklidir.


### Ortam Değişkenlerini Yakalama


Closure'lar değişkenleri ortamlarından üç farklı şekilde yakalayabilir: değişmez referansla, değiştirilebilir referansla veya sahiplik alarak. Rust derleyicisi, en az ayrıcalık ilkesini izleyerek, closure'unuzun ihtiyaçlarını karşılayan en kısıtlayıcı yakalama yöntemini otomatik olarak belirler.


Bir closure yalnızca bir değeri okumaya ihtiyaç duyduğunda, değişmez referansla yakalar. Bu, closure tanımlandıktan ve çağrıldıktan sonra orijinal değişkenin erişilebilir kalmasını sağlar. Örneğin, bir listeyi yazdıran bir closure, listeyi değişmez bir şekilde ödünç alır ve closure çalıştırıldıktan sonra listeyi kullanmaya devam etmenize olanak tanır.


Bir closure'un yakalanan bir değişkeni değiştirmesi gerekiyorsa, değişebilir referansla yakalaması gerekir. Bu durumda, hem yakalanan değişken hem de closure'un kendisi mutable olarak bildirilmelidir. Closure daha sonra yakalanan değişkeni değiştirebilir, ancak ödünç alma kuralları hala geçerlidir - mutable closure varken bu değişkene başka referanslar veremezsiniz.


En kısıtlayıcı yakalama yöntemi, yakalanan değişkenleri closure içine taşıyan sahiplik alma yöntemidir. Bu, iş parçacıkları oluştururken olduğu gibi, kapanışın değişkenlerin orijinal olarak tanımlandığı kapsamı aşabileceği durumlarda gereklidir. Closure parametrelerinden önce `move` anahtar sözcüğünü kullanarak sahiplik yakalamayı zorlayabilirsiniz: `move |x| { /* closure body */ }`. İş parçacıkları, sonlanabilecek ve değişkenlerini bırakabilecek diğer iş parçacıklarından güvenli bir şekilde ödünç alamayacağından, iş parçacığı güvenliği için bu çok önemlidir.


### Kapanış Özellikleri ve İşlev Türleri


Rust, kapanışları üç temel özelliğe sahip bir özellik sistemi aracılığıyla temsil eder: `FnOnce`, `FnMut` ve `Fn`. Bu özellikler, kapanışların nasıl çağrılabileceğini ve yakalanan değişkenlerle neler yapabileceklerini tanımlayan bir hiyerarşi oluşturur.


fnOnce` tüm closure'ların uyguladığı en temel özelliktir. En az bir kez çağrılabilen kapanışları temsil eder. Bazı kapanışlar, özellikle de yakalanan değerleri taşıyan veya bir şekilde tüketen kapanışlar, yakalanan verileri yürütme sırasında yok ettikleri veya taşıdıkları için yalnızca bir kez çağrılabilir.


fnMut`, birden çok kez çağrılabilen ve yakaladıkları ortamı değiştirebilen kapanışları temsil eder. Bu kapanışlar değişkenleri değiştirilebilir referansla yakalar ve bunları birden fazla çağrı boyunca değiştirebilir. Ödünç alma kuralları, bir `FnMut` kapanışı etkin olduğunda, yakalanan değişkenlerine özel değiştirilebilir erişime sahip olmasını sağlar.


fn` en kısıtlayıcı özelliktir ve yakalanan ortamlarını değiştirmeden birden çok kez çağrılabilen kapanışları temsil eder. Bu kapanışlar yalnızca değişmez referansla yakalanır ve Rust'in güvenlik garantilerini ihlal etmeden eşzamanlı olarak çağrılabilir. Bir kapanış `Fn` özelliğini uygularsa, otomatik olarak `FnMut` ve `FnOnce` özelliğini de uygular, çünkü mutasyon olmadan birden çok kez çağrılabilir olmak, mutasyonla çağrılabilir olmak ve bir kez çağrılabilir olmak anlamına gelir.


### Yineleyicilerle Çalışma


Rust'deki yineleyiciler, veri dizilerini işlemek için bir yol sağlar. Tembeldirler, yani siz verileri gerçekten yineleyen yöntemleri çağırarak onları tüketene kadar herhangi bir iş yapmazlar. Bu tembel değerlendirme, ara koleksiyonlar oluşturmadan işlemlerin verimli bir şekilde zincirlenmesine olanak tanır.


Iterator` özelliği, yineleyicinin ne verdiğini temsil eden ilişkili bir `Item` türü ve `Option<Self::Item>` döndüren bir `next` yöntemi ile temel işlevselliği tanımlar. Next` `None` döndürdüğünde, yineleyici tükenir. Bu tasarım, yineleyicilerin hem sonlu hem de potansiyel olarak sonsuz dizileri güvenli bir şekilde temsil etmesini sağlar.


Ödünç yineleme için `iter()`, değiştirilebilir ödünç yineleme için `iter_mut()` ve yinelemeyi tüketmek için `into_iter()` gibi yöntemleri kullanarak koleksiyonlardan yineleyiciler oluşturabilirsiniz. Bu yöntemler arasındaki seçim, öğeleri değiştirmeniz gerekip gerekmediğine ve orijinal koleksiyonu tüketmek isteyip istemediğinize bağlıdır.


### Yineleyici Uyarlayıcıları ve Tüketicileri


Yineleyici uyarlayıcıları, bir yineleyiciyi diğerine dönüştürerek işlemleri birbirine zincirlemenize olanak tanıyan yöntemlerdir. Yaygın uyarlayıcılar arasında her bir öğeyi dönüştürmek için `map`, bir yüklem temelinde öğeleri seçmek için `filter` ve indeks eklemek için `enumerate` bulunur. Bu adaptörler tembeldir - tüketilene kadar herhangi bir iş yapmazlar.


Map` yöntemi her öğeye bir kapanış uygulayarak onu başka bir şeye dönüştürür. Örneğin, `numbers.iter().map(|x| x * 2)` her sayıyı ikiye katlayan bir yineleyici oluşturur. Filter` yöntemi yalnızca yüklem kapanışının true döndürdüğü öğeleri tutar: `numbers.iter().filter(|&x| x > 10)` yalnızca ondan büyük sayıları tutar.


Tüketici metotları aslında veri üzerinde yineleme yapar ve nihai bir sonuç üretir. Collect` yöntemi bir yineleyiciyi tüketir ve ondan bir koleksiyon oluşturur. Genellikle koleksiyon türünü belirtmeniz gerekir: `let vec: Vec<_> = iterator.collect()`. Diğer tüketiciler arasında sayısal öğeleri toplamak için `sum`, özel bir işlemle değerleri toplamak için `fold` ve her öğe üzerinde yan etkileri çalıştırmak için `for_each` bulunur.


### Gelişmiş Yineleyici Kalıpları


Ek yineleyici işlemleri arasında iki yineleyiciyi eleman bazında birleştirmek için `zip`, yineleyicileri birleştirmek için `chain` ve filtreleme ile eşlemeyi tek bir işlemde birleştirmek için `filter_map` bulunur. Zip` yöntemi, iki yineleyicinin karşılık gelen öğelerinden çiftler oluşturur: a.iter().zip(b.iter())` yöntemi `(a[0], b[0]), (a[1], b[1]), ...` çiftlerini üretir.


Fold` yöntemi değerleri toplamak için kullanışlıdır. Bir başlangıç değeri ve akümülatörü her bir elemanla birleştiren bir kapanış alır: `numbers.iter().fold(0, |acc, x| acc + x)` tüm sayıları toplar. Bu kalıp, maksimum değerleri bulmak, dizeler oluşturmak veya karmaşık veri yapıları oluşturmak gibi diğer birçok işlemi uygulayabilir.


Yineleyici zincirleri karmaşık veri dönüşümlerini kısa ve öz bir şekilde ifade edebilir. Örneğin, ses verilerinin işlenmesi şunları içerebilir: `coefficients.iter().zip(buffer.iter()).map(|(c, b)| c * b).sum::<i32>() >> 12`. Bu, karşılık gelen katsayıları ve tampon değerlerini çarpar, sonuçları toplar ve son değeri tek bir okunabilir ifade içinde kaydırır.


```rust
fn main() {
// Sample UTXOs: (txid_suffix, amount_sats)
let utxos = vec![
("a1b2", 50_000u64),
("c3d4", 15_000),
("e5f6", 100_000),
("g7h8", 3_000),
("i9j0", 75_000),
];

// Using closures and iterators to process UTXOs

// 1. Filter UTXOs above dust threshold (10,000 sats)
let spendable: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000)
.collect();
println!("Spendable UTXOs: {:?}", spendable);

// 2. Calculate total balance with fold
let total_balance: u64 = utxos
.iter()
.map(|(_, amount)| amount)
.fold(0, |acc, amount| acc + amount);
println!("Total balance: {} sats", total_balance);

// 3. Find UTXOs needed to cover a 120,000 sat payment
let target = 120_000u64;
let mut accumulated = 0u64;
let selected: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000) // Skip dust
.take_while(|(_, amount)| {
if accumulated >= target {
false
} else {
accumulated += amount;
true
}
})
.collect();
println!("Selected for payment: {:?}", selected);

// 4. Transform to display format using map and collect
let display_strings: Vec<String> = utxos
.iter()
.map(|(txid, amount)| format!("{}...:{} sats", txid, amount))
.collect();
println!("Display: {:?}", display_strings);
}
```


### Akıllı İşaretçilere Giriş


Akıllı işaretçiler, geleneksel işaretçiler gibi davranan ancak ek yetenekler ve otomatik bellek yönetimi sağlayan veri yapılarıdır. Basit referansların aksine, akıllı işaretçiler işaret ettikleri verilerin sahibidir ve bellek ayırma, ayırma ve erişim modelleri için özel davranışlar uygulayabilirler. Yığın olarak ayrılmış verileri yönetmek ve Rust'ün temel sahiplik sisteminin ötesine geçen karmaşık sahiplik modellerini uygulamak için temel araçlardır.


"Akıllı" yönü, aksi takdirde manuel müdahale gerektirecek bellek yönetimi görevlerini otomatik olarak ele alma yeteneklerinden gelir. Bir akıllı işaretçi kapsam dışına çıktığında, ilişkili belleği otomatik olarak boşaltabilir, referans sayılarını azaltabilir veya diğer temizleme işlemlerini gerçekleştirebilir. Bu otomasyon, bellek sızıntılarını ve use-after-free hatalarını önlemeye yardımcı olurken, yalnızca yığın ayırmaya göre daha fazla esneklik sağlar.


Akıllı işaretçiler tipik olarak iki temel özelliği uygular: `Deref` ve `Drop`. Deref` özelliği, akıllı işaretçinin içerdiği verilere bir referansmış gibi kullanılmasını sağlar. Drop` özelliği, akıllı işaretçi yok edildiğinde özel temizleme mantığını etkinleştirir. Bu özellikler birlikte, akıllı işaretçilerin belleği otomatik olarak yönetmesini sağlar.


### Kutu Akıllı İşaretçi


box<T>` en basit akıllı işaretçidir ve herhangi bir `T` tipi için heap tahsisi sağlar. Bir `Box` oluşturduğunuzda, içerdiği değer yığın yerine heap üzerinde saklanır ve `Box`ın kendisi (sadece bir işaretçidir) yığın üzerinde saklanır. Bu dolaylama, büyük miktarda veriyi hareket ettirmeden saklamanız gerektiğinde, derleme zamanı boyutu bilinmeyen bir türe ihtiyaç duyduğunuzda veya heap verisinin sahipliğini verimli bir şekilde aktarmak istediğinizde kullanışlıdır.


Bir `Box` oluşturmak basittir: `let boxed_value = Box::new(42);` heap üzerinde bir tamsayı ayırır. Box` bu belleği otomatik olarak yönetir - Box` kapsam dışına çıktığında, heap belleğini otomatik olarak deallocate eder. Bu otomatik temizleme, manuel bellek yönetimi gerektirmeden bellek sızıntılarını önler.


Box`ın en önemli kullanım alanlarından biri özyinelemeli veri yapılarını etkinleştirmektir. Her düğümün bir değer ve bir sonraki düğüme bir işaretçi içerdiği bağlantılı bir liste düşünün. Box` olmadan böyle bir yapı tanımlayamazsınız çünkü derleyici kendini içeren bir türün boyutunu belirleyemez. Bir sonraki işaretçi için `Box<Node>` kullanarak özyinelemeli boyutlandırma sorununu ortadan kaldırırsınız, çünkü `Box` ne içerdiğinden bağımsız olarak bilinen, sabit bir boyuta sahiptir.


### Deref Özelliğinin Uygulanması


Deref` özelliği, bir türün `*` operatörü kullanılarak referansının kaldırılmasına olanak tanıyarak akıllı işaretçilerin içerdikleri verilere referans gibi davranmasını sağlar. Bir akıllı işaretçi için `Deref` özelliğini uyguladığınızda, akıllı işaretçinin kullanımını şeffaf hale getiren otomatik dereferencing özelliğini etkinleştirmiş olursunuz. Bu, içerilen türdeki yöntemleri doğrudan akıllı işaretçi aracılığıyla açık dereferanslama olmadan çağırabileceğiniz anlamına gelir.


Deref` özelliği, dereferans işleminin ne tür bir referans üretmesi gerektiğini belirten ilişkili bir `Target` türü tanımlar. Bu özellik, hedef tipe bir referans döndüren bir `deref` yönteminin uygulanmasını gerektirir. Box<T>` için, uygulama, içerilen `T` değerine bir referans döndürür.


Rust otomatik deref zorlaması gerçekleştirir, bu da derleyicinin türleri uyumlu hale getirmek için gerektiğinde otomatik olarak `deref` çağrılarını ekleyebileceği anlamına gelir. Bu nedenle bir `&str` bekleyen bir fonksiyona bir `String` aktarabilirsiniz - derleyici bir string dilimi elde etmek için `String`i otomatik olarak dereferanslar. Bu zorlama birden fazla seviyede zincirleme olabilir, böylece bir `Box<String>` birden fazla deref işlemi ile otomatik olarak bir `&str`ye dönüştürülebilir.


### Özel Damla Uygulaması


Drop` özelliği, bir değer kapsam dışına çıktığında çalışacak özel temizleme kodunu belirlemenize olanak tanır. Bu özellikle dosya tutamaçları, ağ bağlantıları veya referans sayıları gibi basit belleğin ötesinde kaynakları yöneten akıllı işaretçiler için önemlidir. Drop` özelliği, `self` için değiştirilebilir bir referans alan ve temizleme işlemini gerçekleştiren tek bir metoda, `drop` sahiptir.


Çoğu türün özel `Drop` uygulamalarına ihtiyacı yoktur, çünkü Rust alanlarını bırakma işlemini otomatik olarak gerçekleştirir. Ancak, akıllı işaretçiler yönettikleri kaynakları düzgün bir şekilde temizlemek için genellikle özel mantığa ihtiyaç duyarlar. Örneğin, referans sayımlı bir akıllı işaretçinin, son referans düşürüldüğünde referans sayısını azaltması ve potansiyel olarak paylaşılan verileri ayırması gerekir.


Ayrıca `std::mem::drop()` kullanarak bir değeri kapsam dışına çıkmadan önce açıkça düşürebilirsiniz. Bu fonksiyon bir değerin sahipliğini alır ve onu hemen bırakır, bu da kaynakları erken serbest bırakmak veya temizlemenin programınızın belirli bir noktasında gerçekleşmesini sağlamak için yararlı olabilir. Açık drop fonksiyonu sadece sahiplik alan bir kimlik fonksiyonudur - asıl iş fonksiyonun sonunda değer bırakıldığında gerçekleşir.


Kapanışlar, yineleyiciler ve akıllı işaretçilerden oluşan bu temel, Rust geliştiricilerine etkileyici, güvenli ve verimli kod yazmaları için araçlar sunar. Bu özellikler, Rust'nın temel bellek güvenliği ve performans garantilerini korurken ortak programlama modellerini etkinleştirmek için birlikte çalışır.



## Referans Sayma ve İç Değişebilirlik

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

### RC ile Referans Sayma


Referans sayma, Rust'de özellikle çoklu sahiplik senaryolarını etkinleştirmek için tasarlanmış bir başka temel akıllı işaretçi türünü temsil eder. Tek bir varlığın veriye sahip olduğu geleneksel tek sahiplik kurallarını izleyen Box'ın aksine, RC (Referans Sayacı) kodunuzun birden fazla bölümünün aynı verinin sahipliğini aynı anda paylaşmasına olanak tanır. Bu paylaşılan sahiplik modeli, belirli bir veri parçasına kaç referans olduğunu izleyen bir sayma mekanizması aracılığıyla çalışır.


Referans sayma sistemi, bir RC'yi her klonladığınızda artan ve bir RC düşürüldüğünde azalan dahili bir sayaç tutarak çalışır. Bellek yalnızca bu sayaç sıfıra ulaştığında serbest bırakılır ve verilerin herhangi bir referans var olduğu sürece geçerli kalmasını sağlar. Bu yaklaşım, basit Kutu sahipliği ile imkansız olabilecek esnek veri paylaşım modellerini mümkün kılarken erken bellekten çıkarmayı önler.


RC'nin yararlı olduğu pratik bir örnek, birden fazla listenin aynı kuyruk kısmına başvurabileceği bağlantılı listeler gibi paylaşılan veri yapılarının oluşturulmasıdır. Her ikisi de ortak bir alt diziye referans veren iki ayrı liste oluşturmaya çalıştığınızı düşünün. Kutu sahipliği ile bu imkansız hale gelir, çünkü paylaşılan kısmı ilk listeye taşımak sahipliği aktarır ve ikinci listede kullanılmasını engeller. RC bu sorunu, altta yatan veri yerine referansı klonlamanıza izin vererek çözer ve bellek güvenliğini korurken paylaşılan yapıyı mümkün kılar.


Bir RC'yi klonladığınızda, boyutu veya karmaşıklığı ne olursa olsun dahili verileri çoğaltmazsınız. Bunun yerine, aynı bellek konumuna başka bir referans oluşturur ve referans sayacını artırırsınız. Bu, RC örneklerini klonlamayı büyük veri yapıları için bile verimli hale getirir, çünkü temel veriler yerinde kalırken yalnızca referansın kendisi kopyalanır.


### RefCell ile İç Mekan Değişebilirliği


RefCell, yalnızca değişmez bir referansa sahip olduğunuzda bile verileri değiştirmenize olanak tanıyan iç değişebilirliği sunar. Bu özellik, kontrolleri derleme zamanından çalışma zamanına taşıyarak Rust'in ödünç alma kurallarının uygulanma şeklini temelden değiştirir. Normal referanslar ödünç alma güvenliğini doğrulamak için derleyiciye güvenirken, RefCell bu kontrolleri program yürütme sırasında gerçekleştirerek potansiyel çalışma zamanı panikleri pahasına daha fazla esneklik sağlar.


RefCell'in arkasındaki temel ilke, Rust'un normalde derleme zamanında uyguladığı aynı ödünç alma kurallarını sürdürmeyi, ancak bunları dinamik olarak kontrol etmeyi içerir. Herhangi bir anda, bir RefCell içindeki verilere yönelik bir adet değiştirilebilir referansa ya da herhangi bir sayıda değiştirilemez referansa sahip olabilirsiniz. Kodunuz aynı anda çakışan ödünçler oluşturarak bu kuralları ihlal etmeye çalışırsa, program tanımlanmamış davranış üretmek yerine panikleyecektir.


Bu çalışma zamanı denetimi, aslında güvenli olsalar bile derleyicinin reddedebileceği belirli programlama modellerini mümkün kılar. Derleyicinin statik analizi, karmaşık ödünç alma modellerinin doğru olduğunu her zaman kanıtlayamaz, bu da onu ihtiyatlı davranmaya yönlendirir. RefCell, kodunuzun doğruluğundan emin olduğunuzda bu muhafazakar kısıtlamaları geçersiz kılmanıza olanak tanır, ancak bu güven, çalışma zamanı çökmelerini önlemek için doğru kullanımı sağlama sorumluluğunu da beraberinde getirir.


RefCell için yaygın bir kullanım durumu, test senaryolarında sahte nesneleri içerir. Yalnızca kendine değişmez erişim sağlayan bir özellik uygularken, ancak sahte uygulamanızın durum değişikliklerini dahili olarak izlemesi gerekiyorsa, RefCell bu modeli etkinleştirir. Dahili durumu bir RefCell'e sararak mock'un değişmez bir arayüz aracılığıyla bile izleme verilerini değiştirmesine izin verebilirsiniz.


### Paylaşılan Değişken Durum için RC ve RefCell'in Birleştirilmesi


RC ve RefCell'in birleşimi, birden fazla sahibin aynı verileri potansiyel olarak değiştirebildiği paylaşılan değiştirilebilir durum için bir model oluşturur. RC paylaşılan sahiplik özelliğini sağlarken, RefCell değişmez referanslar aracılığıyla mutasyonu mümkün kılar. Bu kombinasyon, grafik yapıları, önbellekler veya programınızın birden fazla bölümünün paylaşılan verilere hem okuma hem de yazma erişimine ihtiyaç duyduğu herhangi bir durum gibi senaryolarda kullanışlıdır.


Bir RefCell'i bir RC'nin içine sardığınızda, programınız boyunca klonlanıp dağıtılabilen ve her klonun aynı temel değiştirilebilir verilere erişim sağladığı bir yapı oluşturursunuz. Tüm sahipler RefCell'in borrow_mut yöntemini kullanarak verileri potansiyel olarak değiştirebilir, ancak yine de çalışma zamanında ödünç alma kurallarına uymaları gerekir. Bu model, çalışma zamanı kontrolleri aracılığıyla Rust'un güvenlik garantilerini korurken karmaşık veri paylaşım senaryolarına olanak tanır.


Ancak bu esneklik, bellek sızıntıları ve referans döngüleri ile ilgili önemli uyarıları da beraberinde getirir. RefCell ile RC kullanıldığında, veri yapılarının doğrudan ya da bir referans zinciri aracılığıyla kendilerine referans verdiği döngüsel referansların yanlışlıkla oluşturulması mümkün hale gelir. Bu döngüler, referans sayısının sıfıra ulaşmasını engelleyerek bellek sızıntılarına neden olur, çünkü veriler programın geri kalanından artık erişilebilir olmasa bile her zaman aktif referanslara sahip gibi görünür.


Referans döngülerinin çözümü, bellek yönetimi kararları için kullanılan referans sayısına katkıda bulunmayan zayıf referansların kullanılmasını içerir. Zayıf referanslar, veri yapıları arasındaki bağlantıları canlı tutmadan sürdürmenize olanak tanıyarak potansiyel döngüleri kırarken ilgili veriler hala mevcutken bunlara erişme yeteneğini korur.


```rust
use std::rc::Rc;
use std::cell::RefCell;

// Simulating a channel state that multiple components need to access and modify
#[derive(Debug)]
struct ChannelState {
channel_id: String,
local_balance_msat: u64,
remote_balance_msat: u64,
is_active: bool,
}

fn main() {
// Rc<RefCell<T>> allows multiple owners with interior mutability
let channel = Rc::new(RefCell::new(ChannelState {
channel_id: "abc123".to_string(),
local_balance_msat: 1_000_000_000,  // 1M sats in msats
remote_balance_msat: 500_000_000,
is_active: true,
}));

// Clone Rc to share ownership (cheap - only increments counter)
let channel_for_ui = Rc::clone(&channel);
let channel_for_router = Rc::clone(&channel);

// Reference count is now 3
println!("Reference count: {}", Rc::strong_count(&channel));

// UI component reads the state (immutable borrow)
{
let state = channel_for_ui.borrow();
println!("UI shows balance: {} msats", state.local_balance_msat);
} // borrow ends here

// Router updates the state after a payment (mutable borrow)
{
let mut state = channel_for_router.borrow_mut();
state.local_balance_msat -= 100_000_000; // Sent 100k sats
state.remote_balance_msat += 100_000_000;
println!("Router updated balances");
} // mutable borrow ends here

// Original reference can still read the updated state
let state = channel.borrow();
println!("New local balance: {} msats", state.local_balance_msat);

// WARNING: This would panic at runtime!
// let borrow1 = channel.borrow();
// let borrow2 = channel.borrow_mut(); // PANIC: already borrowed
}
```


### İş Parçacığı Güvenliği ve Eşzamanlılık Temelleri


Rust'in eşzamanlılık yaklaşımı, derleme zamanında veri yarışlarını ve bellek güvenliği sorunlarını önlemeye odaklanır. Tip sistemi, tipleri sırasıyla iş parçacıkları arasında aktarım için güvenli veya eşzamanlı erişim için güvenli olarak işaretleyen `Send` ve `Sync` gibi özellikler aracılığıyla iş parçacığı güvenliğini sağlar. Bu derleme zamanı doğrulaması, diğer sistem programlama dillerinde yalnızca çalışma zamanında ortaya çıkabilecek birçok eşzamanlılık hatasını yakalar.


Rust'de iş parçacığı oluşturmak, yeni iş parçacığında yürütülecek bir kapanış alan ve iş parçacığının yaşam döngüsünü yönetmek için bir tanıtıcı döndüren thread::spawn kullanılarak basit bir model izler. Oluşturulan iş parçacığı ana iş parçacığı ile eşzamanlı olarak çalışır ve tamamlanmasını beklemek için tanıtıcı üzerindeki join yöntemini kullanabilirsiniz. Açıkça birleştirme yapılmazsa, ana iş parçacığı çıktığında yeni iş parçacığı sonlandırılabilir ve bu da tamamlanmamış işlerin kesilmesine neden olabilir.


İş parçacıklarıyla çalışırken move anahtar sözcüğü çok önemli hale gelir çünkü doğan iş parçacıklarına aktarılan kapanışların genellikle verileri ödünç almak yerine kendilerine ait olması gerekir. Ortaya çıkan iş parçacıkları kendilerini oluşturan kapsamdan daha uzun ömürlü olabileceğinden, ana kapsamdan ödünç almak potansiyel yaşam süresi ihlallerine neden olur. Verileri iş parçacığı kapanışına taşımak, sahipliği aktarır ve verilerin iş parçacığının tüm yaşam süresi boyunca geçerli kalmasını sağlarken orijinal kapsamdan erişimi engeller.


Mesaj geçişi, iş parçacıklarının belleği paylaşmak yerine veri göndererek iletişim kurmasına olanak tanıyan kanallar aracılığıyla paylaşılan durum eşzamanlılığına bir alternatif sunar. Rust'ün standart kütüphanesi, birden fazla iş parçacığının tek bir alıcı iş parçacığına mesaj gönderebildiği Çoklu Üretici Tek Tüketici (MPSC) kanalları sağlar. Bu model, paylaşılan değiştirilebilir durumdan tamamen kaçınarak, bunun yerine koordinasyon için mesaj alışverişine güvenerek birçok senkronizasyon sorununu ortadan kaldırır.


### Mutex ve Arc ile Paylaşılan Durum Eşzamanlılığı


Mesaj geçişi uygun olmadığında, Rust, Arc (Atomik Referans Sayacı) ile birleştirilmiş Mutex (karşılıklı dışlama) aracılığıyla geleneksel paylaşılan durum eşzamanlılığı sağlar. Mutex, iş parçacıklarının verilere erişmeden önce bir kilit edinmesini gerektirerek aynı anda yalnızca bir iş parçacığının korunan verilere erişebilmesini sağlar. Kilit işlemi tarafından döndürülen koruma nesnesi kapsam dışına çıktığında kilit otomatik olarak serbest bırakılır ve unutulan kilitlerin neden olduğu yaygın kilitlenme senaryoları önlenir.


Arc, birden fazla iş parçacığında referans sayısını güvenli bir şekilde yönetmek için atomik işlemleri kullanarak RC'nin iş parçacığı güvenli eşdeğeri olarak hizmet eder. RC tek iş parçacıklı senaryolar için mükemmel çalışırken, atomik olmayan referans sayımı birden fazla iş parçacığından erişildiğinde yarış koşulları yaratır. Arc'ın atomik sayaçları, referans sayımı değişikliklerinin eşzamanlı erişim altında bile güvenli bir şekilde gerçekleşmesini sağlar ve bu da onu iş parçacığı sınırları boyunca veri paylaşımı için uygun hale getirir.


Arc ve Mutex kombinasyonu, eş zamanlı programlarda paylaşılan değiştirilebilir durum için bir model oluşturur. Bir Mutex'i bir Arc'a sararak, aynı mutex'e erişimi birden fazla iş parçacığına dağıtmak için Arc'ı klonlayabilirsiniz; her iş parçacığı kilidi alabilir ve korunan verileri güvenli bir şekilde değiştirebilir. Bu model, derleme zamanı doğrulama ve çalışma zamanı kilitleme yoluyla Rust'in güvenlik garantilerini korurken paylaşılan durumun esnekliğini sağlar.


Send ve Sync özellikleri, derleme zamanında iş parçacığı güvenliğini sağlamak için perde arkasında çalışır. Send bir türün başka bir iş parçacığına güvenli bir şekilde aktarılabileceğini gösterirken, Sync bir türe yapılan referansların iş parçacıkları arasında güvenli bir şekilde paylaşılabileceğini gösterir. Çoğu tür, bileşenleri iş parçacığı güvenli olduğunda bu özellikleri otomatik olarak uygular, ancak RC ve RefCell gibi bazı türler, eşzamanlı erişim için tasarlanmadıkları için bunları açıkça uygulamaz. Bu otomatik özellik uygulaması, iş parçacığı güvenliği ihlallerinin kazara ortaya çıkmasını önlerken, güvenli türlerin eşzamanlı bağlamlarda sorunsuz bir şekilde çalışmasına olanak tanır.


## Rust Makrolarını Anlama

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::

### Rust'de Makrolara Giriş


Rust'deki makrolar, geliştiricilerin derleme zamanında başka kodlar üreten kodlar yazmasına olanak tanıyan bir metaprogramlama özelliğidir. Çalışma zamanında çağrılan fonksiyonların aksine, makrolar derleme sürecinin başlarında, tip kontrolü ve sonraki aşamalardan önce genişletilir. Bu temel ayrım, makroları özellikle kod tekrarını azaltmak ve Rust programları içinde alana özgü diller oluşturmak için kullanışlı hale getirir.


Bir makro çağrısının en tanınmış göstergesi, makro adını izleyen ünlem işaretidir (!). Örneğin, `println!("Hello, world!")` komutunu kullandığınızda, bir fonksiyon çağırmıyor, bir makro çağırıyorsunuz demektir. Bu makro, biçimlendirme ve çıktı işlemlerini gerçekleştiren daha karmaşık bir koda genişler. Ünlem işareti, geliştiricilere standart bir işlev çağrısı yerine derleme zamanı kod üretiminin gerçekleştiğine dair görsel bir ipucu görevi görür.


Rust, her biri dil ekosisteminde farklı amaçlara hizmet eden üç farklı makro türü sağlar:



- Fonksiyon benzeri makrolar**: Fonksiyon çağrılarına benzer ancak derleme zamanında çalışır (örneğin, `vec!`, `println!`)
- Türetme makroları**: Türler için özellikleri otomatik olarak uygulayın (örneğin, `#[derive(Debug, Clone)]`)
- Öznitelik benzeri makrolar**: Uygulandıkları kod öğelerinin davranışını değiştirir (örneğin, `#[test]`, `#[tokio::main]`)


Bu farklı makro türlerini anlamak, her biri belirli kullanım durumlarına ve programlama modellerine hitap ettiğinden, etkili Rust programlaması için çok önemlidir.


### Makro Türleri ve Uygulamaları


Fonksiyon benzeri makrolar, Rust programlamasında en sık karşılaşılan makro türünü temsil eder. Bu makrolar fonksiyon çağrılarına benzer sözdizimi kullanır ancak generate uygun koduna girdileri üzerinde desen eşleştirme gerçekleştirir. Bu kategorinin yaygın bir örneği olan `vec!` makrosu, geliştiricilerin kısa bir sözdizimiyle vektörler oluşturmasına ve başlatmasına olanak tanır. Vec![1, 2, 3, 4]` yazdığınızda, makro bunu yeni bir vektör oluşturan, her bir öğeyi ayrı ayrı iten ve tamamlanmış vektörü döndüren koda genişletir.


Türetme makroları, özel tipler için otomatik özellik uygulamaları sağlayarak ayrıntılı kodu önemli ölçüde azaltır. Bir struct veya enum tanımına `#[derive(Debug)]` eklediğinizde, derleyiciye bu tür için Debug özelliğinin eksiksiz bir uygulamasını generate'e talimat vermiş olursunuz. Bu oluşturulan uygulama, türün içeriğini insan tarafından okunabilir bir biçimde görüntülemek için gerekli biçimlendirme mantığını ele alır. Türetme mekanizması, Clone, PartialEq gibi çok sayıda standart kütüphane özelliğini destekler ve bu da onu boilerplate'i azaltmak için yaygın olarak kullanılan bir araç haline getirir.


Öznitelik benzeri makrolar, açıklama ekledikleri kod öğelerinin davranışını değiştirerek meta veri eklemek veya derleme davranışını değiştirmek için bir yol sağlar. Bu makrolar, tip tanımlarının, fonksiyonların veya diğer kod yapılarının üzerine yerleştirilmiş öznitelikler olarak görünür. Örneğin, bir enum üzerindeki `#[non_exhaustive]` özniteliği, gelecek sürümlerde ek varyantların eklenebileceğini belirtir ve eşleşme ifadelerinin varsayılan bir durum içermesini gerektirir. Bu mekanizma, ileriye dönük uyumluluğu sağlarken, türün evrim potansiyelinin açık bir şekilde belgelenmesini sağlar.


### Özel Fonksiyon Benzeri Makrolar Oluşturma


Özel fonksiyon benzeri makrolar yazmak, Rust'in makro tanımları için kalıp eşleştirme sözdizimini anlamayı gerektirir. Makro tanımı, farklı girdi formlarıyla eşleşen kalıpları ve bunlara karşılık gelen kod oluşturma şablonlarını belirttiğiniz bildirimsel bir yaklaşım kullanır. Her makro birden fazla dal içerebilir, bu da çeşitli girdi kalıplarını ve generate her durum için uygun kodu işlemesine olanak tanır.


Makro oluşturmanın temel ilkelerini gösteren özel bir vektör makrosu oluşturmayı düşünün. Makro tanımı `macro_rules!` ile başlar, ardından makro adı ve bir dizi kalıp eşleştirme dalı gelir. Her dal, belirli girdi sözdizimiyle eşleşen bir kalıptan ve karşılık gelen Rust kodunu üreten bir kod şablonundan oluşur. Örneğin, basit bir dal `[]` boş parantezleriyle ve boş bir vektör oluşturmak için generate koduyla eşleşebilirken, başka bir dal tek bir ifadeyle eşleşir ve tek elemanlı bir vektör oluşturmak için kod üretir.


Makrolar, tekrarlama sözdizimini kullanarak değişken argüman kalıplarını uygularken özellikle kullanışlı hale gelir. $($x:expr),*` kalıbı, virgülle ayrılmış sıfır veya daha fazla ifadeyle eşleşerek makronun rastgele sayıda argümanı işlemesine olanak tanır. İlgili kod oluşturma şablonu, eşleşen tüm ifadeler üzerinde yineleme yapmak için `$(vec.push($x);)*` ifadesini ve her biri için generate ayrı push ifadelerini kullanır. Bu tekrarlama mekanizması, makroların manuel olarak yazılması imkansız veya son derece ayrıntılı olabilecek generate koduna olanak tanır.


```rust
// A macro to create a HashMap with Bitcoin-related data
macro_rules! btc_map {
// Empty case
() => {
std::collections::HashMap::new()
};
// Key-value pairs case
($($key:expr => $value:expr),+ $(,)?) => {
{
let mut map = std::collections::HashMap::new();
$(
map.insert($key, $value);
)+
map
}
};
}

// A macro for logging with context (simulating a derive-like pattern)
macro_rules! log_payment {
($level:ident, $($arg:tt)*) => {
println!(
"[{}] [PAYMENT] {}",
stringify!($level).to_uppercase(),
format!($($arg)*)
)
};
}

fn main() {
// Using the btc_map! macro
let fee_rates = btc_map! {
"high_priority" => 50_u64,    // sats/vbyte
"medium" => 25_u64,
"low" => 10_u64,
};

println!("Fee rates: {:?}", fee_rates);

// Using the log_payment! macro
log_payment!(info, "Sending {} sats to {}", 100_000, "bc1q...");
log_payment!(warn, "Fee rate {} sats/vB is above average", 75);
log_payment!(error, "Payment failed: insufficient funds");

// Standard vec! macro usage comparison
let utxos = vec![50_000_u64, 30_000, 20_000];
let total: u64 = utxos.iter().sum();
println!("Total UTXOs: {} sats", total);
}
```


Derleme işlemi, tip denetimi ve optimizasyon gerçekleşmeden önce makro çağrılarını genişletilmiş koda dönüştürür. Derleyici bir makro çağrısıyla karşılaştığında, girdiyi tanımlanan kalıplarla eşleştirir ve makro çağrısını üretilen kodla değiştirir. Bu genişletilmiş kod daha sonra tip denetimi ve optimizasyon dahil olmak üzere normal derleme işlemlerine tabi tutulur. Kargo genişletme gibi araçlar, geliştiricilerin oluşturulan kodu incelemesine olanak tanıyarak karmaşık makrolar geliştirirken değerli hata ayıklama yetenekleri sağlar.


### İleri Makro Kavramları ve Hata Ayıklama


Makro geliştirme, derleme zamanı ve çalışma zamanı yürütme arasındaki ayrımı anlamayı gerektirir. Makrolar derleme sırasında yürütülür ve çalışma zamanında çalışacak kodu üretir. Bu zamansal ayrım, makro mantığının çalışma zamanı değerlerine bağlı olamayacağı anlamına gelir, ancak aynı zamanda karmaşık hesaplamaların yürütme sırasında tekrar tekrar yerine derleme sırasında bir kez gerçekleştirilebileceği optimizasyonlara da olanak tanır.


Makrolardaki kalıp eşleştirme sistemi, ne tür kod öğelerinin eşleştirilebileceğini tanımlayan çeşitli parça belirticilerini destekler. Expr` belirticisi ifadelerle, `ty` tiplerle, `ident` tanımlayıcılarla eşleşir ve diğerleri girdi doğrulama üzerinde ince taneli kontrol sağlar. Bu belirleyiciler makroların sözdizimsel olarak geçerli girdi almasını sağlar ve geçersiz sözdizimiyle karşılaşıldığında açık hata mesajları verir.


Makrolarda hata ayıklama, derleme zamanı yapıları nedeniyle benzersiz zorluklar sunar. Cargo expand' komutu, makro çağrımları tarafından oluşturulan tamamen genişletilmiş kodu görüntülediğinden makro geliştirme için kullanışlıdır. Bu araç, geliştiricilerin makrolarının amaçlanan kodu generate doğrulamalarına ve genişletme mantığındaki sorunları belirlemelerine olanak tanır. Makro tarafından oluşturulan kod hatalar içerdiğinde, genişletilmiş çıktı, sorunun makro tanımında mı yoksa oluşturulan kod yapısında mı olduğunu belirlemeye yardımcı olur.


Karmaşık makrolar, bir makronun iç içe geçmiş veya yinelemeli kod üretimini işlemek için değiştirilmiş argümanlarla kendisini çağırdığı özyinelemeli kalıpları uygulayabilir. Ancak özyinelemeli makrolar, sonsuz genişleme ve derleme performansı sorunlarından kaçınmak için dikkatli bir tasarım gerektirir. Makro genişlemesinin derleme zamanı doğası, verimsiz makro uygulamalarının bile çalışma zamanı performansını değil, yalnızca derleme hızını etkilediği anlamına gelir, ancak aşırı karmaşık makrolar derleme sürecini önemli ölçüde yavaşlatabilir.



# Rust & Bitcoin

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Bitcoin Geliştirme için Neden Rust

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


Bitcoin ve Lightning geliştirme için Rust'in seçilmesi tesadüfi değildir. Bitcoin geliştirme, onu tipik yazılım geliştirmeden ayıran benzersiz sorumluluklar taşır. Bitcoin ile çalışırken, geliştiriciler genellikle hataların geri döndürülemez olabileceği bir ortamda kullanıcı fonlarını kullanmaktadır. Düzenleyici korumalara ve ters ibraz mekanizmalarına sahip geleneksel finansal sistemlerin aksine, Bitcoin'ün merkezi olmayan yapısı, bir [işlem](https://planb.academy/resources/glossary/transaction-tx) yayınlandıktan sonra fonun geri alınması için başvurulacak bir makam olmadığı anlamına gelir. Bu gerçeklik, yazılım geliştirmede daha yüksek düzeyde sorumluluk ve hassasiyet gerektirmektedir.


Birçok teknoloji sektöründe işe yarayan "hızlı hareket et ve bir şeyleri kır" felsefesi Bitcoin geliştirme için geçerli değildir. Bunun yerine, ekosistem, geliştiricilerin hataların önlendiği veya zarif bir şekilde ele alındığı sağlam, güvenli yazılımlar oluşturmasına yardımcı olan diller ve araçlar gerektirir. Bu nedenle Bitcoin Geliştirme Kiti (BDK), Lightning Geliştirme Kiti (LDK) ve BreezSDK dahil olmak üzere önde gelen birçok Bitcoin projesi Rust'ye yönelmiştir.


Rust, onu Bitcoin geliştirme için özellikle uygun kılan üç temel özellik sunar: statik güçlü tip sistemi, zengin modern araçlar ve platformlar arası uyumluluk. Bu özelliklerin her biri, dilin geliştiricilerin [kripto para](https://planb.academy/resources/glossary/cryptocurrency) işlemlerini yürütmek için daha güvenli, daha güvenilir kod yazmalarına yardımcı olma yeteneğine katkıda bulunur.


### Rust'in Statik Güçlü Tip Sistemi


Rust'nin tip sistemi, hataları kullanıcıları etkilemeden önce yakalamak için birlikte çalışan hem statik hem de güçlü tipleme özellikleri sağlar. Statik yapı, tip kontrolünün derleme zamanında gerçekleştiği ve geliştiricilerin tip uyumsuzluklarını program daha oluşturulmadan önce çözmelerini gerektirdiği anlamına gelir. Bu durum, tip hatalarının yalnızca çalışma zamanı sırasında, potansiyel olarak yazılım dağıtıldıktan ve gerçek kullanıcı fonlarını kullandıktan sonra ortaya çıktığı dinamik olarak yazılan dillerle tezat oluşturur.


Rust'ün tip sisteminin gücü, problemleri modellemedeki ifade gücü ve titizliği ile ilgilidir. Geliştiricilerin sayılar ve yapılar gibi temel türlerle sınırlı kaldığı C gibi daha zayıf tür sistemlerine sahip dillerin aksine, Rust karmaşık alan kavramlarını doğru bir şekilde temsil edebilen zengin tür modellemesine izin verir. Örneğin, farklı liste türlerini birbirinden ayıran veya belirli işlemlerin yalnızca belirli nesne türleri üzerinde gerçekleştirilmesini zorunlu kılan türler oluşturabilirsiniz.


Rust'in tip sistemini Bitcoin'ün geliştirilmesiyle ilgili kılan şey, bellek güvenliğine yaklaşımıdır. İş mantığını modelleyen aynı tip sistemi bellek sahipliğini ve paylaşılan erişim kontrolünü de ele alır. Bu ikili sorumluluk, bellek sızıntıları, çift serbest hatalar ve yarış koşulları gibi yaygın güvenlik açığı sınıflarının derleyici tarafından tamamen ortadan kaldırıldığı anlamına gelir. Tip sistemi bu güvenlik garantilerini sahiplik, ödünç alma ve referans sayma gibi kavramlar aracılığıyla uygulayarak güvenlik veya kararlılığı tehlikeye atabilecek bellekle ilgili hataların ortaya çıkmasını son derece zor hale getirir.


```rust
// Example: Type-safe Bitcoin amount handling
// Using newtypes to prevent mixing up satoshis and other values

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Satoshis(u64);

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct FeeRate(u64); // sats per vbyte

impl Satoshis {
fn from_btc(btc: f64) -> Self {
Satoshis((btc * 100_000_000.0) as u64)
}

fn as_btc(&self) -> f64 {
self.0 as f64 / 100_000_000.0
}
}

// Calculate fee given tx size - type system ensures we can't mix up values
fn calculate_fee(tx_size_vbytes: u32, rate: FeeRate) -> Satoshis {
Satoshis(tx_size_vbytes as u64 * rate.0)
}

fn main() {
let payment = Satoshis::from_btc(0.001); // 100,000 sats
let fee_rate = FeeRate(25);              // 25 sats/vbyte
let tx_size = 250_u32;                   // vbytes

let fee = calculate_fee(tx_size, fee_rate);
println!("Payment: {:?} ({} BTC)", payment, payment.as_btc());
println!("Fee: {:?}", fee);

// This would NOT compile - type safety prevents mixing values:
// let bad_fee = calculate_fee(tx_size, payment); // ERROR: expected FeeRate, found Satoshis
}
```


### Modern Araçlar ve Platformlar Arası Destek


Rust'nın araç ekosistemi, geliştiricilere üretkenlik ve kod kalitesine yardımcı olan araçlar sağlar. Rust derleyicisinin kendisi sadece kodu ikili forma çevirmek için değil, aynı zamanda geliştiricilerin öğrenmesine ve gelişmesine yardımcı olan bir eğitim aracı olarak hizmet etmek üzere tasarlanmıştır. Derleme hataları oluştuğunda, derleyici neyin yanlış gittiğine dair ayrıntılı açıklamalar sunar ve genellikle belirli düzeltmeler önerir. Derleyici iyi uygulamaları etkili bir şekilde öğrettiğinden ve yaygın hataları önlemeye yardımcı olduğundan, bu yaklaşım özellikle Rust'ya yeni başlayan geliştiriciler için değerlidir.


Dil, bağımlılık yönetimi, oluşturma, test etme ve dokümantasyon oluşturma işlemlerini gerçekleştiren birleşik bir paket yöneticisi olan Cargo'yu içerir. Bu standardizasyon, birden fazla rakip aracın projeler arasında tutarsızlık yarattığı C++ gibi eski dillerde görülen parçalanmayı ortadan kaldırır. Cargo ayrıca kod biçimlendirme için rustfmt ve statik analiz için Clippy gibi uzantıları destekleyerek kodun tutarlı stil yönergelerini izlemesini ve olası sorunları sorun haline gelmeden önce yakalamasını sağlar.


Rust'un çapraz platform yetenekleri, Android ve iOS gibi mobil platformların yanı sıra tarayıcı tabanlı uygulamalar için WebAssembly'yi de içerecek şekilde geleneksel işletim sistemlerinin ötesine uzanır. Bu çapraz platform desteği, farklı ortamlarda çalışması gereken Bitcoin uygulamaları için kullanışlıdır. Örneğin, Mutiny Wallet gibi projeler, doğrudan web tarayıcılarında çalışan Lightning cüzdanları oluşturmak için Rust'un WebAssembly derlemesinden yararlanır; bu, yalnızca geleneksel web teknolojileriyle pratik olmayacak bir şeydir.


### Hata Türlerini ve Sonuçlarını Anlama


Etkili hata işleme, programın yürütülmesi sırasında oluşabilecek farklı hata kategorilerini anlamakla başlar. Coğrafi noktalar arasındaki yolları hesaplayan basit bir yönlendirme uygulaması düşünün. Bu örnek, geliştiricilerin ele alması gereken üç temel hata türünü göstermektedir: geçersiz girdi hataları, çalışma zamanı kaynak hataları ve mantık hataları.


Geçersiz girdi hataları, bir fonksiyon gereksinimlerini karşılamayan parametreler aldığında ortaya çıkar. Örneğin, bir coğrafi koordinat sistemi boylam için işaretli tam sayılar kullanıyorsa ancak yalnızca pozitif değerlerin geçerli olduğu bir yerde negatif bir değer alırsa, işlev anlamlı bir şekilde ilerleyemez. Bu hatalar, çağıran ile fonksiyon arasında bir sözleşme ihlalini temsil eder ve uygun yanıt genellikle girdiyi reddetmek ve bir hata göstergesi döndürmektir.


Çalışma zamanı kaynak hataları, harici bağımlılıklar kullanılamadığında veya erişilemediğinde ortaya çıkar. Bir eşleme dosyasının okunması, dosya mevcut olmadığından, uygulama uygun izinlere sahip olmadığından veya depolama aygıtı kullanılamadığından başarısız olabilir. Bu hatalar program mantığının dışındadır ve genellikle kod değişiklikleri yerine çevresel düzeltmeler gerektirir. Ancak, sağlam uygulamalar bu senaryoları öngörmeli ve incelikle ele almalıdır.


Mantık hataları, program uygulamasındaki hataları veya bileşenlerin nasıl etkileşime girdiğine ilişkin yanlış anlamaları temsil eder. Bir yönlendirme algoritması geçerli başlangıç ve bitiş noktaları verildiğinde boş bir yol döndürüyorsa bu, kodun kendisinde düzeltilmesi gereken mantıksal bir kusur olduğunu gösterir. Diğer hata türlerinin aksine, mantık hataları genellikle hata ayıklama ve kod değişikliği gerektirir.


### Sağlam Hata Yönetimi için Stratejiler


Güvenilir bir yazılım oluşturmak, hata fırsatlarını en aza indiren ve kaçınılmaz hataları incelikle ele alan proaktif stratejiler gerektirir. İlk strateji, dikkatli tip tasarımı yoluyla olası hataların sınırlandırılmasını içerir. Geliştiriciler, yalnızca geçerli değerleri temsil edebilen türleri seçerek geçersiz girdi hatalarının tüm sınıflarını ortadan kaldırabilir. Örneğin, negatif olamayacak değerler için işaretsiz tamsayıların kullanılması, derleme zamanında negatif değer hatalarını önler.


İtirazlar, programın yürütülmesi sırasında beklenen koşulların doğru olup olmadığını açıkça kontrol ederek başka bir koruma katmanı sağlar. Bu kontroller birden fazla amaca hizmet eder: test sırasında hataları yakalar, sorunlar ortaya çıktığında programların erken başarısız olmasına neden olur (hata ayıklamayı kolaylaştırır) ve programcının varsayımlarını açıklayan çalıştırılabilir belgeler olarak hizmet eder. Bir iddia başarısız olduğunda, programın durumuyla ilgili temel bir varsayımın ihlal edildiğini gösterir ve genellikle araştırılması gereken bir mantık hatasına işaret eder.


Katmanlı soyutlama ilkesi, hataların sistemin uygun seviyelerinde ele alınmasını sağlayarak karmaşıklığın yönetilmesine yardımcı olur. Alt düzey kütüphanelerdeki belirli hata türleri de dahil olmak üzere dahili uygulama ayrıntıları, alt sistem sınırlarının ötesine yayılmamalıdır. Bunun yerine, her katman hataları o soyutlama seviyesinde anlamlı olan terimlere çevirmelidir. Örneğin, Bitcoin kütüphanesi kullanan bir wallet uygulaması, düşük seviyeli tanımlayıcı ayrıştırma hatalarını, kullanıcılara veya çağıran koda işlem yapılabilir bilgiler sağlayan "geçersiz wallet yapılandırması" gibi daha yüksek seviyeli mesajlara çevirmelidir.


Rust'ün tip sistemi ve araçlarıyla birlikte hata işlemeye yönelik bu yaklaşım, potansiyel sorunların kullanıcıları etkilemeden veya Bitcoin uygulamalarının güvenliğini tehlikeye atmadan önce geliştirme sürecinin erken aşamalarında yakalanmasına yardımcı olur.



## Hata modeli

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

Rust, güvenliği pratiklikle dengeleyen kapsamlı bir hata işleme yaklaşımı sağlar. Genel hata modeli kavramları tüm programlama dillerinde geçerli olsa da, Rust hata işlemeyi hem açık hem de yönetilebilir hale getiren özel araçlar ve modeller sunar. Bu mekanizmaları anlamak, performansı ve güvenliği korurken beklenmedik durumları incelikle ele alabilen sağlam Rust uygulamaları yazmak için çok önemlidir.


### Panik ve Uygun Kullanımları


Rust'in panik mekanizması, kurtarılamayan hataları ele almanın en doğrudan yolunu temsil eder. Panic!` makrosunu çağırdığınızda, program yapılandırmanıza bağlı olarak yürütmeyi derhal durdurur, ya iptal eder ya da gevşetir. Panic makrosu, neyin yanlış gittiğini açıklayan ve hata ayıklama için bağlam sağlayan bir dize mesajı kabul eder. Ayrıca, Result ve Option türleri üzerindeki `unwrap()` ve `expect()` gibi yöntemler, bu türler sırasıyla hata değerleri veya None içerdiğinde panik için kısayol görevi görür. Expect()` yöntemi, özel bir mesaj sağlamanıza olanak tanıyarak, hataları ayıklarken `unwrap()` yönteminden biraz daha bilgilendirici olmasını sağlar.


Basitliğine rağmen panik, üretim kodunda mantıklı bir şekilde kullanılmalıdır. Paniğin yalnızca kabul edilebilir değil aynı zamanda tavsiye edildiği birkaç senaryo vardır. Örnekler veya prototipler yazarken panik, kodu kapsamlı hata işleme ile karıştırmadan temel işlevselliğe odaklanmak için temiz bir yol sağlar. Test ortamlarında, panik, beklenmedik bir şeyin meydana geldiğini açıkça gösterdiğinden, onaylamalar başarısız olduğunda genellikle istenen davranıştır. Rust topluluğu, geliştiricilerin derleyiciden daha fazla bilgiye sahip olduğu durumları da kabul etmektedir; örneğin, geçerli olduğu bilinen sabit kodlu IP adreslerinin ayrıştırılması gibi.


Ancak, "derleyici tarafından doğrulanmış" paniklerin görünürdeki güvenliği aldatıcı olabilir. Bir IP adresini sabit kodladığınız ve geçerli olduğunu bildiğiniz için `expect()` kullandığınız bir senaryo düşünün. Zamanla, kod geliştikçe, sabit kodlu değer bir sabite dönüştürülebilir ve daha sonra bu sabit daha iyi kullanıcı deneyimi için "localhost" gibi bir şeye değiştirilebilir. Birdenbire, "güvenli" paniğiniz bir çalışma zamanı hatası haline gelir. Bu evrim, üretim kodunda paniklerden kaçınmanın ve bunun yerine zarif bir şekilde ele alınabilecek uygun hata türlerini döndürmenin neden genellikle daha iyi olduğunu göstermektedir.


"Panikten kaçınma" kuralının dikkate değer bir istisnası muteks işlemleriyle ilgilidir. Bir muteks üzerinde `lock()` işlevini çağırdığınızda bir Sonuç döndürür, çünkü muteksi tutarken başka bir iş parçacığı paniğe kapılırsa kilit başarısız olabilir. Bu, yerel kodunuzun tamamen farklı bir bağlamda gerçekleşen bir şey için hata aldığı kafa karıştırıcı bir durum yaratır. Başka bir iş parçacığının paniğinden kaynaklanan bir hatayı makul bir şekilde ele alamayacağınız için, birçok geliştirici, özellikle başka bir yerde paniksiz bir kod tabanına sahipseniz, muteks kilitlerini açmanın kabul edilebilir olduğunu düşünür.


### Sonuç ve Seçenek Türleriyle Çalışma


Result türü, Rust'nin hata işleme sisteminin bel kemiğini oluşturur. Bir `Ok(değer)` ya da `Err(hata)` tutabilen bir enum olarak Result, sizi işlemlerin başarısız olabileceğini açıkça kabul etmeye zorlar. Option türü, bir değerin basitçe bulunmayabileceği durumlar için benzer bir amaca hizmet eder ve `Some(value)` ya da `None` içerir. Option ayrıntılı hata bilgisi sağlamasa da, bir değerin yokluğunun anlamlı olduğu ve beklendiği durumlar için mükemmeldir.


Hem Result hem de Option, hata işlemeyi daha ergonomik hale getiren çeşitli yardımcı yöntemler sağlar. Unwrap_or()` yöntemi, mevcutsa içerilen değeri veya bir hata varsa ya da None ise varsayılan bir değeri döndürür. Bu kalıp, ayrıştırma başarısız olduğunda kullanıcı girdisini mantıklı bir öntanımlı değerle ayrıştırmak gibi makul bir geri dönüşünüz olduğunda özellikle kullanışlıdır. Unwrap_or_default()` yöntemi de benzer şekilde çalışır, ancak bir değer belirtmenizi gerektirmek yerine türün varsayılan değerini kullanır. Bu yöntemler teknik olarak geleneksel anlamda hataları ele almasa da, sorunlar ortaya çıktığında işlevselliği zarif bir şekilde azaltmanın bir yolunu sağlar.


Soru işareti operatörü (`?`), hata yayılımı için kısa bir sözdizimidir. Bir Sonuç veya Seçeneğe uygulandığında, varsa başarı değerini çıkarır veya bir sorun varsa geçerli işlevden hemen hatayı döndürür. Bu operatör, Go gibi dillerde yaygın olan ve her adımda hataları manuel olarak kontrol etmeniz ve döndürmeniz gereken ayrıntılı hata kontrol modellerini ortadan kaldırır. Soru işareti operatörü aslında erken geri dönüşler için sözdizimsel şeker sağlar ve hata yayılımını otomatik olarak ele alırken mutlu yola odaklanan temiz, doğrusal kod yazmanıza olanak tanır.


### Gelişmiş Hata İşleme Kalıpları


Result ve Option türleri üzerindeki `map()` yöntemi, kodu daha etkileyici ve birleştirilebilir hale getirebilen işlevsel tarzda hata işleme sağlar. Bir Result üzerinde `map()` metodunu çağırdığınızda, sağlanan fonksiyon varsa başarı değerine uygulanır, hatalar ise değişiklik yapılmadan otomatik olarak yayılır. Bu model, hata durumlarını tekrar tekrar ele almadan değerleri dönüştürmeye odaklanabileceğiniz için işlemleri zincirleme yaparken kullanışlıdır. Map_err()` yöntemi ters işlevsellik sağlayarak, başarı değerlerini değiştirmeden bırakırken hata türlerini dönüştürmenize olanak tanır.


Hata dönüşümü, farklı bileşenlerin farklı hata türlerine ihtiyaç duyduğu katmanlı uygulamalar oluştururken çok önemli hale gelir. Kullanıcı girdisini ayrıştıran ve düşük seviyeli ayrıştırma hatalarını alana özgü hatalara dönüştürmesi gereken bir işlev düşünün. Map_err()` kullanarak, genel bir "geçersiz sayı biçimi" hatasını, uygulamanızın etki alanı içinde anlamlı olan daha bağlamsal bir "geçersiz yaş" hatasına kolayca dönüştürebilirsiniz. Bu dönüşüm, hatanın oluştuğu noktada gerçekleşir ve kodu, hata işlemenin başarısız olabilecek işlemlerden ayrıldığı geleneksel try-catch bloklarından daha okunabilir ve sürdürülebilir hale getirir.


Soru işareti operatörünün hata eşleme ile birleşimi, kısa ve öz hata işleme modelleri oluşturur. İşlemleri zincirleyebilir, hataları gerektiği gibi dönüştürebilir ve bunları en az şablonla çağrı yığınına yayabilirsiniz. Bu yaklaşım, hata işlemeyi başarısız olabilecek işlemlere yakın tutarken, başarı ve hata yolları arasında temiz bir ayrım sağlar.


```rust
use std::fmt;

// Layered error types for a wallet application
#[derive(Debug)]
enum NetworkError {
ConnectionFailed(String),
Timeout,
}

#[derive(Debug)]
enum WalletError {
Network(NetworkError),
InvalidAddress(String),
InsufficientFunds { required: u64, available: u64 },
}

// Implement Display for user-friendly messages
impl fmt::Display for WalletError {
fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
match self {
WalletError::Network(e) => write!(f, "Network error: {:?}", e),
WalletError::InvalidAddress(addr) => write!(f, "Invalid address: {}", addr),
WalletError::InsufficientFunds { required, available } =>
write!(f, "Need {} sats but only have {} available", required, available),
}
}
}

// Convert from lower-level error to domain error
impl From<NetworkError> for WalletError {
fn from(err: NetworkError) -> Self {
WalletError::Network(err)
}
}

// Simulated network call
fn fetch_balance(address: &str) -> Result<u64, NetworkError> {
if address.starts_with("bc1") {
Ok(500_000) // 500k sats
} else {
Err(NetworkError::ConnectionFailed("Invalid endpoint".into()))
}
}

// Higher-level function using ? with automatic error conversion
fn send_payment(from: &str, amount: u64) -> Result<String, WalletError> {
let balance = fetch_balance(from)?; // NetworkError auto-converts to WalletError

if balance < amount {
return Err(WalletError::InsufficientFunds {
required: amount,
available: balance,
});
}

Ok(format!("Sent {} sats", amount))
}

fn main() {
match send_payment("bc1qtest...", 100_000) {
Ok(msg) => println!("Success: {}", msg),
Err(e) => println!("Failed: {}", e), // User-friendly message
}
}
```


### Harici Kütüphaneler ve Hata İşleme Ekosistemleri


Rust ekosistemi, standart kütüphanenin hata işleme yeteneklerini genişleten birkaç popüler kütüphane içerir. Anyhow kütüphanesi, standart Error özelliğini uygulayan herhangi bir hata türünden otomatik olarak dönüşebilen evrensel bir hata türü sunarak hata işleme için basitleştirilmiş bir yaklaşım sağlar. Bu otomatik dönüşüm, soru işareti operatörünü manuel dönüşüm olmadan farklı hata türleriyle kullanmanıza olanak tanıyarak, farklı hata türleri arasında programatik olarak ayrım yapmanız gerekmeyen uygulamalar için özellikle yararlı hale getirir.


Anyhow`, hataların öncelikle kullanıcılara gösterildiği uygulamalar için hata işlemeyi basitleştirmede başarılı olsa da, kütüphane geliştirmede sınırlamaları vardır. Anyhow` esasen tüm hataları dize mesajlarına dönüştürdüğünden, kütüphanenizin tüketicileri farklı hata koşullarına programlı olarak kolayca yanıt veremez. Bu sınırlama `anyhow`u, tüketicilerine yapılandırılmış hata bilgisi sağlaması gereken kütüphanelerden ziyade son kullanıcı uygulamaları için daha uygun hale getirir.


Daha gelişmiş hata işleme yaklaşımları, uygulamanızın veya kütüphanenizin belirli hata modlarını modelleyen özel hata türleri oluşturmayı içerir. İyi tasarlanmış bir hata modeli, geçersiz girdi (çağıranın düzeltebileceği), çalışma zamanı hataları (yeniden denenebilir) ve kalıcı hatalar (hataları veya kurtarılamaz koşulları gösteren) arasında ayrım yapabilir. Bu yapılandırılmış yaklaşım, kodunuzun tüketicilerinin farklı hata türlerine nasıl yanıt verecekleri konusunda akıllı kararlar vermelerini sağlar; bu, işlemlerin yeniden denenmesi, kullanıcılardan farklı girdiler istenmesi veya hataların geliştiricilere bildirilmesi anlamına gelir.


## UniFFI, Rust Kütüphanelerini Çoklu Dillere Köprüleme


<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

### UniFFI ve Platformlar Arası Geliştirmeye Giriş


UniFFI, Rust kütüphanelerini birden fazla programlama dili ve platformda erişilebilir hale getirmeye yönelik bir araçtır. Mozilla tarafından geliştirilen bu araç, modern yazılım geliştirmedeki temel bir zorluğu ele almaktadır: farklı geliştirme ekosistemleriyle uyumluluğu korurken Rust'in performans ve güvenlik avantajlarından nasıl yararlanılacağı. Araç, Rust kütüphaneleri için otomatik olarak dil bağları oluşturarak geliştiricilerin her bir hedef dil için manuel olarak arayüz kodu oluşturma ihtiyacını ortadan kaldırır.


UniFFI'nin çözdüğü temel sorun, Rust'nin derlenmiş bir dil olmasından kaynaklanmaktadır. Rust kodu derlendiğinde, Python, Swift veya Kotlin gibi üst düzey dillerden doğrudan kullanılması zor olabilecek düşük seviyeli bir arayüz sunan bir Yabancı İşlev Interface (FFI) ile ikili çıktı üretir. Geleneksel olarak, her kütüphane geliştiricisinin her hedef dil için özel bağlama kodu yazması gerekir ve bu da platformlar arası benimsemenin önünde önemli bir engel oluşturur. UniFFI, bu bağlayıcıları otomatik olarak oluşturmak için standartlaştırılmış bir yaklaşım sağlayarak bu fazlalığı ortadan kaldırır.


Aracın tasarım felsefesi, Rust geliştiricilerinin temel iş mantığına odaklanmalarını sağlarken, kütüphanelerini diğer dillerde çalışan geliştiriciler için erişilebilir hale getirmeye odaklanmaktadır. Örneğin Swift kullanan bir iOS geliştiricisi, temel uygulamanın Rust'te yazıldığına dair hiçbir belirti olmadan, tamamen yerel bir Swift arayüzü sunan UniFFI tarafından oluşturulan bağlamalar aracılığıyla bir Rust kütüphanesini kullanabilir. Bu sorunsuz entegrasyon, ekiplerin tüm ekip üyelerinin Rust öğrenmesini gerektirmeden Rust'ün performans avantajlarından yararlanmasını sağlar.


### UniFFI Mimarisini ve İş Akışını Anlama


UniFFI, Rust kütüphanelerini çoklu dil uyumlu paketlere dönüştüren iyi tanımlanmış bir iş akışı aracılığıyla çalışır. Süreç, Rust kütüphanenizin hangi bölümlerinin diğer dillere açık olması gerektiğini tanımlayan bir arayüz spesifikasyonu olarak hizmet veren bir Birleşik Tanım Dili (UDL) dosyasının oluşturulmasıyla başlar. Bu UDL dosyası, Rust uygulamanız ile oluşturulan dil bağları arasında bir sözleşme görevi görür.


Mimari, endişelerin net bir şekilde ayrılmasını takip eder. Geliştiriciler Rust kütüphanelerini standart Rust deyimleri ve kalıplarıyla korur, ardından genel arayüzü UniFFI'nin tip sistemiyle eşleştiren ayrı bir UDL dosyası oluşturur. UniFFI bağlama üreticisi, istenen hedef platformlar için yerel dil bağlamaları üretmek için hem Rust kütüphanesini hem de UDL spesifikasyonunu işler. Bu üretilen bağlayıcılar, yabancı dil çalışma zamanı ile Rust kodu arasındaki tüm karmaşık veri aktarım ve aktarım kaldırma işlemlerini gerçekleştirir.


Çalışma zamanında, mimari, hedef dilde (Android için Kotlin gibi) yazılmış uygulama kodunun, o dile tamamen özgü görünen oluşturulmuş bağlayıcı kodla etkileşime girdiği katmanlı bir yaklaşım oluşturur. Bu bağlayıcı katman, dile özgü tipler ve Rust tipleri arasındaki çeviriyi gerçekleştirir, belleği dil sınırları arasında güvenli bir şekilde yönetir ve hedef dilin kurallarına uyan hata işleme sağlar. Altta yatan Rust iş mantığı değişmeden kalır ve üzerine inşa edilen çoklu dil arayüzlerinden habersizdir.


### UDL ile Çalışma: Interface Tanım ve Tip Eşleme


UniFFI'nin işlevselliğinin temel taşı olan Birleşik Tanımlama Dili, bir Rust kütüphanesinin hangi bölümlerinin açığa çıkarılması ve hedef dillerde nasıl sunulması gerektiğini belirtmek için bildirimsel bir yol sağlar. UDL dosyaları, nesne örneklemesi gerektirmeden doğrudan çağrılabilen işlevler için bir kapsayıcı görevi gören en az bir ad alanı içermelidir. Bu isim alanı fonksiyonları tipik olarak parametre olarak değer alan ve sonuç döndüren basit işlemleri ele alır.


UDL, karşılık gelen Rust türleriyle doğal olarak eşleşen kapsamlı bir yerleşik tür kümesini destekler. Temel tipler boolean'lar, çeşitli tamsayı boyutları (u8, u32, vb.), kayan noktalı sayılar ve dizeler gibi standart ilkelleri içerir. Daha karmaşık tipler arasında vektörler, hash haritaları ve Option tipleri (soru işareti sözdizimiyle temsil edilir) ve hata işleme için Result tipleri gibi Rust'a özgü kavramlar bulunur. Tip sistemi aynı zamanda hem basit değer tabanlı enumları hem de ilişkili verileri içeren karmaşık enumları destekleyerek dil sınırlarını aşan veri modellemesine olanak tanır.


Rust'deki yapılar, UDL'deki sözlüklere çevrilir ve UDL'nin sözdizimi kurallarına uyum sağlarken neredeyse bire bir yazışmayı korur. Rust yapıları ilişkili yöntemlere sahip olduğunda, Kotlin veya Swift gibi nesne yönelimli hedef dillerde yöntemlere sahip sınıflar olarak generate olan UDL'de arayüzler olarak gösterilebilirler. Bu eşleme, temel Rust uygulamasının yapısını ve davranışını korurken, geliştiricilerin bu dillerde beklediği nesne yönelimli tasarım modellerini korur.


```
// Example UDL file for a Bitcoin wallet library (wallet.udl)
namespace wallet {
// Namespace functions - called directly without object
string generate_mnemonic();
Wallet create_wallet(string mnemonic);
};

// Dictionary (struct) - becomes data class in Kotlin, struct in Swift
dictionary Balance {
u64 confirmed_sats;
u64 pending_sats;
};

// Interface (class with methods) - becomes class with methods
interface Wallet {
// Constructor
constructor(string mnemonic);

// Methods
Balance get_balance();
string get_new_address();
string send_to_address(string address, u64 amount_sats);
};

// Enum with data - maps to sealed class (Kotlin) or enum with associated values (Swift)
[Enum]
interface TransactionStatus {
Pending(u32 confirmations_needed);
Confirmed(u32 block_height);
Failed(string reason);
};

// Error enum for Result types
[Error]
enum WalletError {
"InsufficientFunds",
"InvalidAddress",
"NetworkError",
};

// Function that can fail - throws in target language
interface Wallet {
[Throws=WalletError]
string send_to_address(string address, u64 amount_sats);
};
```


İlgili Rust uygulaması bu türleri tanımlayacak ve Kotlin, Swift, Python ve diğer desteklenen diller için generate bağlamalarına `uniffi::export` niteliğini uygulayacaktır.


### Hata İşleme ve Gelişmiş Özellikler


UniFFI, Rust'ün Sonuç tabanlı hata modelini koruyan ve hedef diller için uygun şekilde çeviren hata işleme sağlar. Rust'te Result türleri döndüren fonksiyonlar, UDL'de "throws" anahtar sözcüğü ile işaretlenerek hangi hata türlerini üretebilecekleri belirtilebilir. Bu hatalar UDL dosyasında hata enumları olarak tanımlanmalı ve temel Rust kodunda Rust'ün standart Error özelliğini uygulamalıdır. Thiserror crate, bu özelliği uygulamak için uygun bir makro sağlayarak boilerplate kodunu önemli ölçüde azaltır.


Hata işleme çevirisi UniFFI'nin dile duyarlı yaklaşımını göstermektedir. Kotlin'de, UDL generate'te fırlatma olarak işaretlenen işlevler, Java/Kotlin kurallarına uygun olarak istisna fırlatan yöntemlerdir. Python bağlamaları da benzer şekilde Python'un istisna modelini kullanır. Bu çeviri, orijinal Rust hata türlerinin semantik anlamını korurken, hata işlemenin her hedef dilde doğal ve deyimsel hissettirmesini sağlar.


Geri arama arayüzleri, Rust kütüphaneleri ve tüketen uygulamalar arasında çift yönlü iletişim sağlayan bir başka gelişmiş özelliği temsil eder. Bir Rust kütüphanesinin uygulama kodunu geri çağırması gerektiğinde, geliştiriciler Rust'de özellikler tanımlayabilir ve bunları UDL'de geri arama arayüzleri olarak işaretleyebilir. Tüketen uygulama bu arayüzleri kendi ana dilinde uygular ve UniFFI, Rust kodundan bu geri çağrıları çağırmak için gereken karmaşık marshaling işlemini gerçekleştirir. Geri aramalar iş parçacığı sınırlarını aşabileceğinden ve Rust tarafında Send ve Sync sınırlarını gerektirdiğinden, bu model iş parçacığı güvenliğinin dikkatli bir şekilde dikkate alınmasını gerektirir.


### Gerçek Dünya Uygulamaları ve Mevcut Sınırlamalar


UniFFI, BDK (Bitcoin Geliştirme Kiti), LDK (Lightning Geliştirme Kiti) gibi büyük projeler ve mobil SDK'lar sağlamak için onu kullanan çeşitli wallet uygulamaları ile kripto para ve blok zinciri geliştirme topluluğunda benimsenmiştir. Bu projeler UniFFI'nin üretim ortamlarında kullanımını göstermektedir.


Bu projelerdeki gerçek dünya UDL dosyalarının incelenmesi, pratik kullanımdan ortaya çıkan kalıpları ve en iyi uygulamaları ortaya koymaktadır. Örneğin BDK'in UDL dosyası, birden fazla enum, struct ve arayüze sahip karmaşık alan modellerinin kapsamlı mobil SDK'lar oluşturmak için nasıl etkili bir şekilde eşleştirilebileceğini göstermektedir. Farklı projeler arasında UDL sözdiziminin tutarlılığı, UniFFI özellikli bir kütüphaneye aşina olan geliştiricilerin diğerlerini hızlı bir şekilde anlayabileceği ve onlarla çalışabileceği anlamına gelir ve tüm ekosisteme fayda sağlayan bir ağ etkisi yaratır.


Bununla birlikte, UniFFI'nin geliştiricilerin dikkate alması gereken önemli sınırlamaları vardır. Bunlardan en önemlisi asenkron arayüzler için destek eksikliğidir. Oluşturulan tüm bağlar senkrondur, bu da geliştiricilerin Rust kodlarında asenkron işlemleri ele almalarını ve tüketen uygulamalara senkron arayüzler sunmalarını gerektirir. Ek olarak, dokümantasyon yerleşimi bir zorluk teşkil etmektedir: Rust kodunda yazılan dokümantasyon oluşturulan bağlamalara aktarılmazken, UDL dosyalarındaki dokümantasyon kütüphanenin doğrudan Rust tüketicileri için mevcut değildir. Otomatik ayrıştırma ve üretim yoluyla bu sınırlamaları ele almak için devam eden çabalar olsa da, mevcut uygulamalar için dikkate alınması gereken hususlar olmaya devam etmektedir. Son olarak, UniFFI dil bağlarını üretir ancak platforma özgü paketleme ve dağıtımı gerçekleştirmez, geliştiricileri her hedef platform için dağıtılabilir paketler oluşturmanın son adımlarını yönetmeye bırakır.


# SDK ile LNP/BP Geliştirme

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## SDK üzerinde LN düğümü

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

### LDK'nın Modüler Mimarisini Anlama


Lightning Geliştirme Kiti (LDK), CLightning veya LND gibi geleneksel [düğüm](https://planb.academy/resources/glossary/node) yazılımlarına kıyasla [Lightning Network](https://planb.academy/resources/glossary/lightning-network) uygulamasına farklı bir yaklaşım getirmektedir. Geleneksel Lightning düğümleri bir makinede sürekli olarak çalışan eksiksiz daemon uygulamaları olarak çalışırken, LDK özel Lightning çözümleri oluşturmak için ilkel bileşenler sağlayan modüler bir Rust kütüphanesi olarak işlev görür. Bu mimari ayrım, LDK'yı esnek hale getirerek geliştiricilerin Lightning işlevselliğini kendi özel proje gereksinimlerine hizmet edecek şekilde bir araya getirmelerine olanak tanır.


LDK'nın arkasındaki temel felsefe modülerlik ve uyarlanabilirlik üzerine odaklanmaktadır. LDK, monolitik bir çözüm sunmak yerine, birleştirilebilen, özelleştirilebilen veya tamamen değiştirilebilen ayrı bileşenler sunar. Her bileşen, kutudan çıktığı gibi çalışan varsayılan uygulamalarla birlikte gelir, ancak geliştiriciler gerektiğinde kendi uygulamalarını değiştirme özgürlüğüne sahiptir. Örneğin, LDK blok zinciri izleme, işlem imzalama ve ağ iletişimi için varsayılan uygulamalar içerir, ancak bunlardan herhangi biri belirli kullanım durumlarına veya ortamlara göre uyarlanmış özel çözümlerle değiştirilebilir.


Bu modüler tasarım, LDK'nın geleneksel Lightning düğümleri için zorlayıcı olabilecek çeşitli platformlarda ve senaryolarda çalışmasını sağlar. Mobil uygulamalar, web tarayıcıları, gömülü cihazlar ve özel donanımların tümü, LDK'nın bileşenlerinden kendi benzersiz kısıtlamalarına ve gereksinimlerine uygun şekillerde yararlanabilir. Kütüphanenin mimarisi, geliştiricilerin önceden belirlenmiş çalışma modellerine veya sistem bağımlılıklarına bağlı kalmadan Lightning özellikli uygulamalar oluşturabilmelerini sağlar.


### LDK Kullanım Alanları ve Platform Esnekliği


LDK'nın mimari esnekliği, geleneksel Lightning node dağıtımlarının çok ötesine uzanan çok sayıda kullanım alanı açmaktadır. Mobil wallet geliştirme, LDK'nın Phoenix wallet'a benzer gözetim dışı Lightning cüzdanlarının oluşturulmasını sağladığı en ilgi çekici uygulamalardan birini temsil etmektedir. Bu mobil uygulamalar, çevrimiçi olduklarında Lightning Hizmet Sağlayıcıları (LSP'ler) ile senkronize olurken [özel anahtarlar](https://planb.academy/resources/glossary/private-key) üzerinde kullanıcı kontrolünü koruyabilir ve kesintili bağlantıda bile sorunsuz ödeme alımı ve [kanal](https://planb.academy/resources/glossary/payment-channel) yönetimi sağlar.


Donanım Güvenlik Modülü (HSM) entegrasyonu, LDK için başka bir güçlü kullanım durumu sergiliyor. Geliştiriciler, sadece işlem imzalama ve doğrulama bileşenlerini çıkararak Lightning işlemlerinin bağlamını ve sonuçlarını anlayan Lightning farkındalı imzalama cihazları oluşturabilirler. Bu yetenek, basit işlem imzalama işleminin ötesine geçerek ödeme yönlendirme, kanal işlemleri ve güvenlik açısından kritik kararların akıllı analizini de içeriyor. HSM, bir işlemin meşru bir ödemeyi mi, bir yönlendirme işlemini mi yoksa potansiyel olarak kötü niyetli bir girişimi mi temsil ettiğini değerlendirerek kullanıcılara anlamlı güvenlik içgörüleri sağlayabilir.


Web tabanlı Lightning uygulamaları, LDK'nın sistem çağrısı içermeyen tasarım felsefesinden önemli ölçüde yararlanır. WebAssembly ortamlarının dosya sistemleri, ağ soketleri veya entropi kaynakları gibi sistem kaynaklarına doğrudan erişimi olmadığından, LDK'nın saf yaklaşımı Lightning işlevselliğinin tarayıcı ortamlarında sorunsuz bir şekilde çalışmasına olanak tanır. Geliştiriciler WebSockets kullanarak özel ağ katmanları uygulayabilir ve tam Lightning protokol uyumluluğunu korurken tarayıcı uyumlu kalıcılık ve rastgelelik kaynakları sağlayabilir.


### Çekirdek Bileşenler ve Olay Güdümlü Mimari


LDK'nın iç mimarisi, olay odaklı bir sistem aracılığıyla birlikte çalışan birkaç temel bileşen etrafında döner. Eş yönetim sistemi, şifreleme için gürültü protokolünü uygulayarak ve Lightning protokolü uyumluluğu için mesaj yapılarını yöneterek diğer Lightning düğümleriyle tüm iletişimi yönetir. Bu bileşen, altta yatan taşıma mekanizmasından bağımsız olarak çalışarak geliştiricilerin TCP soketleri, WebSockets, USB seri bağlantıları veya diğer çift yönlü iletişim kanalları üzerinden ağ oluşturmasına olanak tanır.


Kanal yöneticisi, Lightning kanal işlemleri için merkezi koordinatör olarak hizmet verir ve kanal açma, kapatma ve ödeme işlemlerini yürütmek için eş yöneticiyle yakın bir şekilde çalışır. Bir geliştirici bir kanal açılışı başlattığında, kanal yöneticisi gerekli protokol mesajlarını oluşturur ve çok adımlı müzakere sürecini yürütmek için eş yöneticisi ile koordinasyon sağlar. Endişelerin bu şekilde ayrılması, Lightning protokol mantığı ile ağ iletişim detayları arasında temiz bir soyutlama sağlar.


LDK'nın olay sistemi, tüm önemli işlemler ve durum değişiklikleri için asenkron bildirimler sağlar. Olaylar, eş bağlantıları ve bağlantı kesilmelerinden ödeme başarıları ve başarısızlıklarına, kanal durumu değişikliklerine ve blok zinciri onaylarına kadar Lightning işlemlerinin tüm yelpazesini kapsar. Bu olay odaklı yaklaşım, uygulamaların Lightning ağ etkinliğine uygun şekilde yanıt vermesini sağlarken, LDK'nın temel işlevselliği ile uygulamaya özgü mantık arasında temiz bir ayrım sağlar. Geliştiriciler, Lightning ağ olaylarına dayalı olarak kullanıcı arayüzlerini güncelleyen, bildirimleri tetikleyen veya takip eylemlerini başlatan özel olay işleyicileri uygulayabilir.


### Blockchain Entegrasyon ve Veri Yönetimi


Blockchain veri entegrasyonu, LDK'nın tam Bitcoin düğümlerinden hafif mobil istemcilere kadar her şeyi barındıracak şekilde tasarlanmış soyutlama katmanlarından birini temsil eder. LDK, her biri farklı kaynak kısıtlamaları ve operasyonel gereksinimler için optimize edilmiş iki ana blok zinciri etkileşim modunu destekler. Tam blok modu, eksiksiz blok zinciri verilerine erişimi olan uygulamaların tüm blokları LDK'ya aktarmasına olanak tanıyarak kapsamlı işlem izleme ve ilgili blok zinciri olaylarına anında yanıt verme olanağı sağlar.


Kaynakları kısıtlı ortamlar için LDK, bant genişliği ve depolama gereksinimlerini azaltan filtreleme tabanlı bir yaklaşım sunar. Bu modda LDK, izleme ilgi alanlarını soyut arayüzler aracılığıyla ileterek belirli işlem kimliklerinin, [UTXO](https://planb.academy/resources/glossary/utxo)'ların veya komut dosyası modellerinin gözetimini talep eder. Uygulama katmanı daha sonra bu izlemeyi Electrum sunucuları, blok kaşifleri veya diğer hafif blok zinciri veri kaynaklarını kullanarak gerçekleştirebilir. Bu yaklaşım, mobil cüzdanların ve web uygulamalarının tam blok zinciri senkronizasyonu gerektirmeden Lightning işlevselliğini sürdürmesini sağlar.


LDK'daki kalıcılık katmanı da aynı soyutlama ilkelerini izler ve uygulamalara güvenilir bir şekilde saklanması ve alınması gereken ikili veri blobları sağlar. LDK, Yıldırım kanalı durumlarını, ağ dedikodu verilerini ve diğer kritik bilgileri serileştirme ve seriden çıkarmanın tüm karmaşıklığını ele alır. Uygulamaların yerel dosya sistemleri, bulut depolama hizmetleri veya özel veritabanı sistemleri kullanarak güvenilir depolama mekanizmaları uygulaması yeterlidir. Bu tasarım, Lightning durum yönetiminin sağlam kalmasını sağlarken, uygulamaların operasyonel gereksinimlerine ve güvenlik modellerine uygun depolama çözümlerini seçmelerine olanak tanır.


### Gelişmiş Özellikler ve Entegrasyon Kalıpları


LDK'nın yetenekleri, çok yollu ödemeler, rota optimizasyonu ve ağ dedikodu yönetimi gibi Lightning Network özelliklerine kadar uzanmaktadır. Yönlendirme sistemi, dedikodu protokolü katılımı yoluyla Lightning Network topolojisinin kapsamlı bir görünümünü koruyarak ödemeler için akıllı yol bulmayı sağlar. Uygulamalar, yapılandırma parametreleri aracılığıyla yönlendirme kararlarını etkileyebilir ve hatta özel kullanım durumları için özel yönlendirme mantığı uygulayabilir.


Kütüphanenin dil bağlama sistemi, Java, Kotlin, Swift, TypeScript, JavaScript ve C++'ı destekleyerek birden fazla programlama ortamında LDK entegrasyonunu sağlar. Bu platformlar arası uyumluluk, yerel dillerde yazılmış mobil uygulamaların optimum performans özelliklerini korurken Lightning işlevselliğini dahil etmesine olanak tanır. Bağlama sistemi, LDK'nın olay odaklı mimarisini ve modüler tasarımını desteklenen tüm dillerde koruyarak hedef platformdan bağımsız olarak tutarlı geliştirici deneyimleri sağlar.


Ücret tahmini ve işlem yayını, LDK'nın esneklik sağladığı ek alanları temsil eder. Uygulamalar, kendi özel operasyonel modellerini ve kullanıcı gereksinimlerini hesaba katan özel ücret tahmin stratejileri uygulayabilir. Benzer şekilde, işlem yayını, doğrudan full node bağlantılarından üçüncü taraf yayın hizmetlerine kadar çeşitli Bitcoin ağ arayüzleriyle çalışacak şekilde özelleştirilebilir. Bu esneklik, LDK tabanlı uygulamaların Lightning protokol uyumluluğunu ve güvenlik standartlarını korurken, blok zinciri etkileşimlerini kendi özel kullanım durumları için optimize edebilmelerini sağlar.


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

### Yıldırım Geliştirme Zorluğu


Lightning ödemelerini entegre eden uygulamalar geliştirmek çoğu geliştirici için önemli bir engel teşkil ediyor. Lightning ödeme işlevselliğine sahip bir uygulama oluşturmak için, geliştiricilerin kanal yönetimi, likidite dengeleme ve ağ topolojisi gibi karmaşık kavramları anlayarak Lightning uzmanı olmaları gerekmektedir. Bu uzmanlık gereksinimi, Lightning'in benimsenmesi için temel bir sorun yaratmaktadır: Lightning ağının kendisi çalışır durumda ve ödemeler güvenilir olsa da, teknik karmaşıklık günlük uygulamalara yaygın entegrasyonu engellemektedir.


Temel zorluk, geliştiricilerin ihtiyaç duydukları ile sunmak istedikleri arasındaki uçurumda yatmaktadır. Geliştiriciler genellikle sıkı teslim tarihleri altında çalışır ve ödeme altyapısında uzmanlaşmak yerine uygulamalarının temel işlevlerine odaklanmalarına olanak tanıyan basit çözümleri tercih eder. Lightning entegrasyonu zor olduğunda, geliştiriciler en az dirençli yolu sundukları için doğal olarak gözetim çözümlerine yönelirler. Ancak, saklama hizmetlerine yönelik bu eğilim, Bitcoin'in saklama dışı finansal egemenliğe ilişkin temel değer önerisini zayıflatmaktadır.


### Breez'un Vizyonu, Her Yerde Yıldırım


Breez basit ama iddialı bir vizyonla ortaya çıktı: Lightning ekonomisine yönelik sezgisel arayüzler aracılığıyla herkesin Lightning ağına bağlanmasını sağlamak. Şirketin yaklaşımı, Lightning ağının teknik olarak iyi çalışmasına rağmen, tam potansiyeline ulaşması için umutsuzca kullanıcı benimsemesine ihtiyaç duyduğunu kabul etmektedir. Bu benimseme sorunu, Lightning entegrasyonundan faydalanabilecek tüm uygulama ve hizmet ekosistemini kapsayacak şekilde bireysel kullanıcıların ötesine uzanıyor.


Orijinal Breez uygulaması, kullanıcılara doğrudan cep telefonlarında çalışan, gözetim altında olmayan bir Lightning düğümü sağlayarak bu vizyonu ortaya koydu. Bu uygulama, podcast yayıncılarına mikro ödeme akışı ve satış noktası işlevselliği gibi Lightning yeteneklerini sergiledi. Bununla birlikte, Breez uygulaması kritik bir mimari sınırlamayı da ortaya çıkardı: mobil uygulama ekosistemi uygulamalar arasında kolay iletişimi kolaylaştırmıyor ve geliştiricileri, özel uygulamaların paylaşılan Lightning altyapısından yararlanmasına izin vermek yerine Lightning ile ilgili tüm özellikleri tek bir uygulamada oluşturmaya zorluyor.


Şirketin Breez uygulamasından öğrendikleri çok önemli bir içgörüye yol açtı: Lightning'in benimsenmesinin geleceği geliştiricilerin kazanılmasına bağlı. Gözetim dışı Lightning entegrasyonu geliştiriciler için en kolay seçenek haline gelirse, varsayılan tercih haline gelir. Bu yaklaşım aynı zamanda yasal avantajlar da sunuyor, çünkü gözetim dışı yazılımlar gözetim hizmetlerine kıyasla daha az yasal engelle karşılaşıyor ve bu da geliştiricilerin uygulamalarını küresel olarak göndermelerini kolaylaştırıyor.


### Breez SDK Mimarisi


Breez SDK, Lightning işlevselliğini uygulamalara entegre etmek için alternatif bir yaklaşım sunar. SDK, her uygulamanın kendi Lightning düğümünü çalıştırmasını gerektirmek yerine, geliştirici deneyimini basitleştirirken gözetim dışı ilkeleri koruyan bir mimari sağlar. Özünde SDK, her son kullanıcıya Blockstream'in bulut tabanlı Lightning düğümü barındırma hizmeti olan Greenlight altyapısında çalışan kendi kişisel Lightning düğümünü verir.


Bu mimari birçok kritik sorunu aynı anda çözer. Kullanıcıların veritabanı yönetimi, sunucu çalışma süresi veya altyapı bakımı gibi tipik tüketiciler için çok zorlayıcı olabilecek konular hakkında endişelenmelerine gerek yoktur. Bununla birlikte, geleneksel gözetim çözümlerinin aksine, Greenlight hiçbir zaman kullanıcı anahtarlarına erişemez. Buluttaki Lightning düğümü, işlemleri ve mesajları imzalayabilen aktif olarak bağlı bir uygulama olmadan herhangi bir işlem gerçekleştiremez. Bu tasarım, operasyonel karmaşıklığı ortadan kaldırırken kendi kendine saklama özelliğinin güvenlik avantajlarını korur.


SDK ayrıca birlikte çalışabilirliği de destekler. Birden fazla uygulama, aynı seed ifadesini kullanarak aynı kullanıcının Lightning düğümüne bağlanabilir ve kullanıcıların farklı özel uygulamalar arasında tek bir Lightning bakiyesini korumasına olanak tanır. Örneğin, bir kullanıcı hem genel bir Lightning wallet uygulamasına hem de her ikisi de aynı fonlara ve Lightning kanallarına erişen özel bir podcasting uygulamasına sahip olabilir. Bu mimari, birleşik finansal altyapıyı korurken odaklanmış, özel uygulamaların geliştirilmesini sağlar.


### Yıldırım Hizmet Sağlayıcıları ve Tam Zamanında Likidite


Breez SDK'nın kritik bir bileşeni, İnternet Hizmet Sağlayıcılarına benzer şekilde Lightning ağı için işlev gören Lightning Hizmet Sağlayıcıları (LSP'ler) ile entegrasyonudur. LSP'ler Lightning'in en karmaşık sorunlarından birini çözer: likidite yönetimi. Lightning kanallarında fonlar, abaküs üzerindeki boncukların yalnızca boşluk olan yerlerde hareket edebilmesine benzer şekilde, yalnızca likiditenin bulunduğu yönlere akabilir.


SDK, LSP'ler aracılığıyla "tam zamanında" kanallar uygulayarak kullanıcı müdahalesi olmadan likiditeyi otomatik olarak yönetir. Bir kullanıcının bir ödeme alması gerektiğinde ancak yeterli gelen likiditesi olmadığında, LSP ödeme geldiği anda otomatik olarak yeni bir Lightning kanalı açar. Bu süreç arka planda sorunsuz bir şekilde gerçekleşir ve kullanıcıların temel kanal mekaniğini anlamadan her zaman ödeme alabilmelerini sağlar.


Bu LSP entegrasyonu basit likidite yönetiminin ötesine geçmektedir. SDK, kutudan çıkar çıkmaz kapsamlı Lightning işlevselliği içerir: güvenlik için yerleşik gözetleme kulesi hizmetleri, denizaltı takasları yoluyla on-chain birlikte çalışabilirliği, MoonPay gibi hizmetler aracılığıyla fiat rampaları ve LNURL protokolleri desteği. Sistem ayrıca sorunsuz yedekleme ve kurtarma sağlayarak, altyapı sağlayıcıları değişse veya kullanılamaz hale gelse bile kullanıcıların fonlarına erişimlerini asla kaybetmemelerini sağlar.


### Uygulama ve Geliştirici Deneyimi


Breez SDK, kapsamlı, batarya dahil yaklaşımı sayesinde geliştirici deneyimine öncelik verir. SDK, Rust, Swift, Kotlin, Python, Go, React Native, Flutter ve C# dahil olmak üzere çok sayıda programlama dili için bağlayıcılar sağlayarak geliştiricilerin tercih ettikleri geliştirme araçlarını kullanarak Lightning ödemelerini entegre etmelerine olanak tanır. Mimari, Lightning ağının güvenliğini korurken API'ler aracılığıyla Lightning karmaşıklığını ortadan kaldırır.


Bu basitleştirilmiş deneyimi sağlamak için temel bileşenler birlikte çalışır. Girdi ayrıştırıcı, farklı ödeme formatlarını otomatik olarak işler, bir dizenin fatura, LNURL veya başka bir ödeme yöntemini temsil edip etmediğini belirler ve uygun işleme işlevine yönlendirir. Entegre imzalayıcı tüm kriptografik işlemleri arka planda yönetirken, takasçı on-chain etkileşimlerini şeffaf bir şekilde ele alır. Bu tasarım, geliştiricilerin Lightning altyapısı uzmanı olmak yerine uygulamalarının benzersiz değer önerisine odaklanmalarını sağlar.


SDK'nın güvensiz mimarisi, Greenlight'ın kanal durumlarını ve yönlendirme bilgilerini gözlemleyebilmesine rağmen, kullanıcı fonlarına erişememesini veya yetkisiz işlemler gerçekleştirememesini sağlar. Kullanıcılar, cihazlarını asla terk etmeyen özel anahtarları üzerinde tam kontrole sahiptir. Bu yaklaşım, operasyonel basitlik ve gizlilik arasında dikkatlice düşünülmüş bir ödünleşmeyi temsil eder ve Bitcoin'nin temel finansal egemenlik ilkelerini korurken ana akım Lightning'in benimsenmesi için pratik bir yol sağlar.


## LDK vs Breez SDK

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

### Lightning Development Kit'in (LDK) Sınırlamalarını Anlama


Lightning Geliştirme Kiti, geliştiricilere Lightning Network uygulamaları oluştururken esneklik sağlamak üzere tasarlanmış bir Rust kütüphaneleri koleksiyonudur. Ancak bu esneklik, Lipa'daki gerçek dünya geliştirme sırasında ortaya çıkan önemli uygulama zorluklarını da beraberinde getirmektedir. LDK'nın düşük seviyeli yapısı, geliştiricilerin ağ grafiği senkronizasyonundan ödeme yönlendirme optimizasyonuna kadar çok sayıda karmaşık görevi bağımsız olarak ele almaları gerektiği anlamına gelir. Bu yaklaşım Lightning uygulaması üzerinde tam kontrol sunarken, üretime hazır güvenilirlik elde etmek için önemli geliştirme kaynakları ve derin teknik uzmanlık gerektirir.


LDK'daki en kritik eksik özelliklerden biri, son kullanıcılar için Lightning Network etkileşimlerini basitleştiren ve yaygın olarak benimsenen bir standart olan LNURL desteğiydi. Ayrıca, çapa çıkışlarının olmaması, özellikle yüksek ücretli ortamlarda ciddi operasyonel zorluklar ortaya çıkarıyordu. Anchor çıktıları, Lightning kanalının zorla kapatılmasıyla ilgili temel bir sorunu çözmektedir: ağ ücretleri önemli ölçüde arttığında, önceden belirlenmiş ücretlere sahip kanalların tek taraflı olarak kapatılması imkansız hale gelebilir çünkü önceden belirlenmiş ücret işlem onayı için yetersiz kalır. Bu sınırlama özellikle mobil wallet uygulamaları için sorun teşkil etmekte olup, kullanıcılar işbirliğine dayalı kanal kapatma işlemlerini koordine etmeden wallet'u terk edebilir ve ücret artışları sırasında fonları potansiyel olarak mahsur bırakabilir.


LDK'nın göreceli olgunlaşmamışlığı, herhangi bir Lightning uygulaması için kritik bir sorun olan güvenilir olmayan ödeme yönlendirmesinde de kendini gösterdi. Teknik olarak sağlam bir uygulama olmasına rağmen, LDK'nın genel bir çözüm olarak geniş kapsamı, belirli sorunların hızlı bir şekilde ele alınmasını zorlaştırdı. Geliştirme ekibi, yönlendirme sorunlarını gidermek ve ideal olarak kütüphane düzeyinde ele alınması gereken özellikleri uygulamak için önemli ölçüde zaman harcarken buldu ve sonuçta geliştirme hızını ve kullanıcı deneyimi kalitesini etkiledi.


### Breez SDK ve Greenlight'ın Avantajlarını Keşfetme


Breez SDK'ya geçiş, kendi kendini yöneten bir Lightning düğümünden Blockstream'in Greenlight hizmeti tarafından desteklenen bulut tabanlı bir çözüme geçerek mimari yaklaşımda bir değişimi temsil etti. Bu değişiklik, LDK uygulamasında yaşanan birkaç kritik sorun noktasını hemen ele aldı. En önemli gelişme, öncelikle Greenlight'ın her zaman güncel bir ağ grafiğini sürdürme yeteneği nedeniyle ödeme güvenilirliğinde gerçekleşti. Uygulama başladığında ağ bilgilerini senkronize etmesi gereken geleneksel mobil Lightning uygulamalarının aksine, Greenlight düğümleri bulutta sürekli olarak çalışır, gerçek zamanlı ağ farkındalığını korur ve kullanıcılar bağlandığında anında eksiksiz grafik verileri sağlar.


Bu mimari, orijinal Lightning Network uygulamalarından biri olarak yıllardır ödemeleri başarıyla yönlendiren ve savaşta test edilmiş Core Lightning (CLN) uygulamasından yararlanmaktadır. CLN'nin birikmiş deneyimi ve kanıtlanmış güvenilirliği, daha genç LDK projesine göre anında istikrar iyileştirmeleri sağladı. Kullanıcılar Greenlight destekli wallet'lerini etkinleştirdiklerinde, sürekli çalışan bir Lightning düğümünün tüm ağ bilgisini ve yönlendirme yeteneklerini anında devralırlar ve önceki uygulamayı rahatsız eden senkronizasyon gecikmelerini ve yönlendirme belirsizliklerini ortadan kaldırırlar.


Breez SDK'nın görüşe dayalı tasarım felsefesi, wallet'ün geliştirilmesi için faydalı olmuştur. Genel bir Lightning araç seti sağlamak yerine, Breez özellikle son kullanıcı wallet uygulamalarına odaklanarak geliştirme ekibinin çabalarını bu özel kullanım durumu için kapsamlı çözümler oluşturmaya yoğunlaştırmasına olanak tanır. Bu hedefli yaklaşım, Breez'in, kullanıcıların manuel kanal açma prosedürleri gerektirmeden wallet kurulumundan hemen sonra ödeme almalarını sağlayan Lightning Hizmet Sağlayıcısı (LSP) işlevi de dahil olmak üzere temel hizmetleri doğrudan SDK'ya entegre etmesini sağladı.


### Kapsamlı Özellikler ve Kullanıcı Deneyimi Geliştirmeleri


Breez SDK'nın entegre yaklaşımı, temel Lightning işlevselliğinin ötesine geçerek kullanıcı deneyimini geliştiren özellikler içerir. Yerleşik LSP entegrasyonu, kullanıcıların kanal yönetimini anlamasını gerektiren geleneksel engeli ortadan kaldırarak yeni wallet kurulumları için anında ödeme alımını mümkün kılar. Kullanıcılar herhangi bir teknik bilgi veya kurulum prosedürü olmadan Lightning ödemelerini almaya başlayabildiğinden, bu ilk katılım süreci ana akım benimsemeye yardımcı olur.


Zincir içi takas işlevi, kullanıcılara birleşik bir bakiye sunulmasını sağlayarak kullanıcı deneyimi optimizasyonunun başka bir katmanını sağlar. Kullanıcıları Lightning ve on-chain Bitcoin arasındaki ayrımı anlamaya zorlamak yerine, takas hizmeti gerektiğinde bu katmanlar arasında otomatik dönüşüm sağlar. Kullanıcıların on-chain ödemeleri yapmaları gerektiğinde, sistem Lightning fonlarını on-chain Bitcoin ile perde arkasında sorunsuz bir şekilde değiştirebilir ve teknik karmaşıklığı dahili olarak ele alırken tek, likit bir bakiye yanılsamasını koruyabilir.


SDK'nın sıfır kanal rezervi desteği, geleneksel Lightning uygulamalarındaki önemli bir kullanıcı deneyimi sorununu ele almaktadır. Kanal rezervleri genellikle kullanıcıların görüntülenen bakiyelerinin tamamını harcamasını engeller ve görünüşte yeterli fon olmasına rağmen ödemeler başarısız olduğunda kafa karışıklığı yaratır. Breez, bu rezervleri ortadan kaldırarak kullanıcıların görüntülenen bakiyelerinin tamamını harcamalarını sağlar, ancak bu LSP'nin ek riski kabul etmesini gerektirir. Bu değiş tokuş, sezgisel kullanıcı deneyimleri yaratmak için teknik karmaşıklığın ve riskin hizmet sağlayıcılar tarafından üstlenildiği Breez'nin kullanıcı merkezli yaklaşımını örneklemektedir.


LNURL desteği, döviz kuru hizmetleri ve çoklu cihaz senkronizasyonu gibi ek özellikler, SDK'nın wallet geliştirmeye yönelik kapsamlı yaklaşımını daha da ortaya koymaktadır. Bulut tabanlı mimari, kullanıcıların Lightning düğümlerine birden fazla cihazdan veya uygulamadan erişebilmelerini sağlar ve Breez bu farklı erişim noktaları arasında durum senkronizasyonunu yönetir. Gelecekteki yol haritası öğeleri arasında tam wallet drenajı için tüm harcama işlevselliği, dinamik kanal yönetimi için ekleme ve hizmet sunumunda sağlıklı rekabet sağlamak için rakip LSP'lerden oluşan bir pazar yer almaktadır.


### Ödünleşimlerin ve Merkezileştirme Endişelerinin Değerlendirilmesi


Breez SDK ve Greenlight'a geçiş, Bitcoin'ün ademi merkeziyetçilik ilkeleri bağlamında dikkatle değerlendirilmesi gereken önemli merkezileşme ödünleşimlerini beraberinde getirmektedir. Bulut tabanlı mimari, kullanıcıların Lightning düğümlerinin Blockstream'in altyapısı üzerinde çalıştığı anlamına gelir ve hem Greenlight'ın sürekli çalışmasına hem de Breez'ün devam eden gelişimine bağımlılık yaratır. Bu merkezileşme, yalnızca kolaylık sağlamanın ötesine geçerek, hizmetlerin kullanılamaz hale gelmesi veya sansür uygulanması durumunda kullanıcıların fonlarını geri alma becerilerini potansiyel olarak etkilemektedir.


Kurtarma senaryoları bu mimaride özel zorluklar ortaya çıkarmaktadır. Kullanıcılar özel anahtarlarının kontrolünü ellerinde tutarken, Greenlight'ın altyapısı olmadan fonlara erişmek, bağımsız Core Lightning düğümlerini döndürmek ve kanal durumlarını geri yüklemek için teknik uzmanlık gerektirecektir. Bireysel kullanıcılar için bu kurtarma süreci muhtemelen son derece karmaşık olacaktır ve Greenlight hizmetlerinin durdurulması halinde wallet sağlayıcıları bile tüm kullanıcı tabanlarını alternatif altyapıya geçirmekte önemli zorluklarla karşılaşacaktır.


Gizlilikle ilgili hususlar da bu mimari değişiklikle birlikte değişiyor. Bulut tabanlı yönlendirme, Greenlight'ın potansiyel olarak ödeme hedeflerine görünürlük kazandığı anlamına gelirken, önceki yalnızca LSP mimarileri bilgi sızıntısını ödeme tutarları ve zamanlamasıyla sınırladı. Bulutta Invoice üretimi, daha önce kullanıcı cihazlarında gizli kalan kullanılmayan faturalar artık Blockstream'in altyapısından geçtiğinden, potansiyel bilgi maruziyetini daha da genişletir.


Bu merkezileştirme endişelerine rağmen, pratik faydalar birçok kullanım durumu için teorik risklerden daha ağır basmaktadır. Geliştirilmiş güvenilirlik, kapsamlı özellik seti ve üstün kullanıcı deneyimi, wallet geliştiricilerinin Lightning altyapı yönetimi yerine uygulama katmanı yeniliklerine odaklanmalarını sağlar. Bu iş bölümü, uzman hizmet sağlayıcıların karmaşık teknik zorlukların üstesinden geldiği ve uygulama geliştiricilerin kullanıcı deneyimi ve iş mantığına odaklanmasına olanak tanıyan olgunlaşan bir ekosistemi yansıtmaktadır. Önemli olan, bu ödünleşimleri net bir şekilde anlamak ve belirli kullanım durumu gereksinimlerine ve risk tolerans düzeylerine dayalı bilinçli kararlar vermektir.




# Son Bölüm

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Yorumlar & Derecelendirmeler

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Sonuç

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>